import json
import re

def extract_graphql_types(schema_content):
    # Regular expression to match type definitions
    type_pattern = re.compile(
        r'type\s+(?P<name>\w+)\s*(?:implements\s+[^\{]+)?\s*\{(?P<content>[^\}]+)\}'
    )
    
    # Find all type definitions
    types = {}
    for match in type_pattern.finditer(schema_content):
        type_name = match.group('name')
        type_content = match.group('content').strip()
        
        # Parse fields
        fields = {}
        for line in type_content.split('\n'):
            line = line.strip()
            
            # Skip empty lines and comments
            if not line or line.startswith('"""'):
                continue
                
            # Extract field name and type
            field_match = re.match(r'(?P<name>\w+):\s*(?P<type>[^\s!]+)', line)
            if field_match:
                field_name = field_match.group('name')
                field_type = field_match.group('type')
                fields[field_name] = field_type
        
        types[type_name] = fields
    
    return types

def save_types(types):
    with open('types.json', 'w') as f:
        json.dump(types, f)
    
    
if __name__ == "__main__":
    with open('nc.graphql', 'r') as f:
        schema_content = f.read()
    types = extract_graphql_types(schema_content)
    save_types(types)