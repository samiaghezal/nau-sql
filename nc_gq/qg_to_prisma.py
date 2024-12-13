def convert_gql_type_to_prisma(gql_type: str) -> str:
    """Convert GraphQL types to Prisma types."""
    type_mapping = {
        'String': 'String',
        'Int': 'Int',
        'Float': 'Float',
        'Boolean': 'Boolean',
        'ID': 'String @id',
        'DateTime': 'DateTime',
        'JSONString': 'Json',
        'Decimal': 'Decimal',
        'Upload': 'String',  # Simplified mapping for file uploads
    }
    return type_mapping.get(gql_type, 'String')  # Default to String if type not found

def parse_gql_schema(schema_content: str) -> str:
    """Parse GraphQL schema and convert to Prisma schema."""
    prisma_schema = []
    current_type = None
    lines = schema_content.split('\n')
    
    # Add Prisma schema header
    prisma_schema.append('generator client {\n  provider = "prisma-client-js"\n}\n')
    prisma_schema.append('datasource db {\n  provider = "postgresql"\n  url = env("DATABASE_URL")\n}\n')
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines and comments
        if not line or line.startswith('"""'):
            continue
            
        # Handle type definitions
        if line.startswith('type ') and ' implements ' in line:
            type_name = line.split(' implements ')[0].replace('type ', '').strip()
            current_type = f'model {type_name} {{'
            prisma_schema.append(current_type)
            
        elif line.startswith('type '):
            type_name = line.replace('type ', '').replace(' {', '').strip()
            current_type = f'model {type_name} {{'
            prisma_schema.append(current_type)
            
        # Handle enum definitions
        elif line.startswith('enum '):
            enum_name = line.replace('enum ', '').replace(' {', '').strip()
            current_type = f'enum {enum_name} {{'
            prisma_schema.append(current_type)
            
        # Handle fields
        elif current_type and line.strip() and not line.startswith('}'):
            # Remove descriptions and directives
            if '"""' in line or '@' in line:
                continue
                
            field_parts = line.split(':')
            if len(field_parts) == 2:
                field_name = field_parts[0].strip()
                field_type = field_parts[1].strip().rstrip('!')
                
                # Handle list types
                if field_type.startswith('[') and field_type.endswith(']'):
                    inner_type = field_type[1:-1].rstrip('!')
                    prisma_type = convert_gql_type_to_prisma(inner_type)
                    prisma_field = f'  {field_name} {prisma_type}[]'
                else:
                    prisma_type = convert_gql_type_to_prisma(field_type)
                    required = '!' in field_parts[1]
                    prisma_field = f'  {field_name} {prisma_type}'
                    if not required:
                        prisma_field += '?'
                
                prisma_schema.append(prisma_field)
                
        # Handle closing braces
        elif line.startswith('}'):
            prisma_schema.append('}')
            current_type = None
            prisma_schema.append('')  # Add empty line between models
    
    return '\n'.join(prisma_schema)

def convert_schema(input_file: str, output_file: str):
    """Convert GraphQL schema file to Prisma schema file."""
    try:
        with open(input_file, 'r') as f:
            gql_schema = f.read()
            
        prisma_schema = parse_gql_schema(gql_schema)
        
        with open(output_file, 'w') as f:
            f.write(prisma_schema)
            
        print(f"Successfully converted schema to {output_file}")
        
    except Exception as e:
        print(f"Error converting schema: {str(e)}")

# Example usage
if __name__ == "__main__":
    convert_schema('nc.graphql', 'schema.prisma')
