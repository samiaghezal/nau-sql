import re
import json

def extract_types(schema_text):
    # Regular expressions for matching type definitions
    type_pattern = r'type\s+(\w+)\s*(?:{|\s+implements\s+[\w\s&]+{)([\s\S]*?})'
    input_pattern = r'input\s+(\w+)\s*{([\s\S]*?})'
    enum_pattern = r'enum\s+(\w+)\s*{([\s\S]*?})'
    
    # Dictionary to store all models
    models = {
        'types': {},
        'inputs': {},
        'enums': {}
    }
    
    def parse_fields(fields_text):
        # Remove comments
        fields_text = re.sub(r'"""[\s\S]*?"""', '', fields_text)
        fields_text = re.sub(r'#.*$', '', fields_text, flags=re.MULTILINE)
        
        # Extract field definitions
        field_pattern = r'(\w+):\s*([\w\[\]!]+)(?:\s*$|\s*#.*$)'
        fields = {}
        
        for line in fields_text.strip().split('\n'):
            line = line.strip()
            if line and not line.startswith('"'):
                match = re.search(field_pattern, line)
                if match:
                    field_name, field_type = match.groups()
                    fields[field_name] = field_type
        
        return fields

    # Extract types
    for match in re.finditer(type_pattern, schema_text):
        type_name, fields_text = match.groups()
        if not type_name.startswith('__'):  # Skip internal types
            models['types'][type_name] = parse_fields(fields_text)

    # Extract inputs
    for match in re.finditer(input_pattern, schema_text):
        input_name, fields_text = match.groups()
        models['inputs'][input_name] = parse_fields(fields_text)

    # Extract enums
    for match in re.finditer(enum_pattern, schema_text):
        enum_name, values_text = match.groups()
        # Clean up enum values
        values = [v.strip() for v in values_text.split('\n') 
                 if v.strip() and not v.strip().startswith('"')]
        models['enums'][enum_name] = values

    return models

def save_models_as_json(models, filename):
    with open(filename, 'w') as f:
        json.dump(models, f, indent=2)

def main():
    # Read the schema file
    with open('nc.graphql', 'r') as f:
        schema_text = f.read()

    # Extract models
    models = extract_types(schema_text)

    # Save to JSON file
    save_models_as_json(models, 'extracted_models.json')
    print("Models have been extracted and saved to 'extracted_models.json'")

if __name__ == "__main__":
    main()
