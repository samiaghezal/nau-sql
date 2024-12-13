import json
from typing import Dict, Any

def get_pg_type(gq_type: str) -> str:
    """Convert GraphQL types to PostgreSQL types."""
    type_mapping = {
        'String': 'TEXT',
        'Int': 'INTEGER',
        'Float': 'DECIMAL',
        'Boolean': 'BOOLEAN',
        'ID': 'UUID',
        'DateTime': 'TIMESTAMP',
        'Date': 'DATE',
        'BigInt': 'BIGINT',
        'Decimal': 'DECIMAL',
        'UUID': 'UUID',
        'JSONString': 'JSONB',
        'Upload': 'TEXT',  # Store file path/URL
        'Money': 'DECIMAL',
    }
    
    # Handle array types (marked with "[" prefix)
    if gq_type.startswith('['):
        base_type = gq_type[1:]  # Remove the "["
        pg_base_type = get_pg_type(base_type)
        return f'{pg_base_type}[]'
    
    return type_mapping.get(gq_type, 'TEXT')  # Default to TEXT for unknown types

def generate_table_sql(type_name: str, fields: Dict[str, Any]) -> str:
    """Generate PostgreSQL table creation SQL for a given GraphQL type."""
    columns = []
    
    # Add id column if not present
    if 'id' not in fields:
        columns.append('    id UUID PRIMARY KEY DEFAULT gen_random_uuid()')
    
    for field_name, field_type in fields.items():
        # Skip complex nested types for now
        if isinstance(field_type, dict):
            continue
            
        pg_type = get_pg_type(field_type)
        column_def = f'    {field_name} {pg_type}'
        
        # Make id fields primary key
        if field_name == 'id':
            column_def += ' PRIMARY KEY'
            
        columns.append(column_def)
    
    sql = f'CREATE TABLE IF NOT EXISTS {type_name.lower()} (\n'
    sql += ',\n'.join(columns)
    sql += '\n);\n'
    
    return sql

def convert_schema(types_json: Dict[str, Any]) -> str:
    """Convert entire GraphQL schema to PostgreSQL."""
    sql_statements = []
    
    # Add UUID extension
    sql_statements.append('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";\n')
    
    for type_name, fields in types_json.items():
        # Skip connection/edge types and other special types
        if (type_name.endswith('Connection') or 
            type_name.endswith('Edge') or 
            type_name.startswith('_') or
            type_name in ['Query', 'Mutation']):
            continue
            
        sql = generate_table_sql(type_name, fields)
        sql_statements.append(sql)
    
    return '\n'.join(sql_statements)

def main():
    with open('types.json', 'r') as f:
        types = json.load(f)
    
    sql = convert_schema(types)
    
    with open('schema.sql', 'w') as f:
        f.write(sql)

if __name__ == '__main__':
    main()
