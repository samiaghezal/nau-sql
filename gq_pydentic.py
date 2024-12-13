from typing import Dict, List, Optional, Any
import json
import re
from pathlib import Path

def graphql_to_python_type(gql_type: str) -> str:
    """Convert GraphQL types to Python/Pydantic types"""
    # Remove non-null operator
    is_required = gql_type.endswith('!')
    gql_type = gql_type.rstrip('!')
    
    # Handle arrays
    is_list = gql_type.startswith('[') and gql_type.endswith(']')
    if is_list:
        inner_type = gql_type[1:-1].rstrip('!')
        python_type = f"List[{graphql_to_python_type(inner_type)}]"
        return python_type if is_required else f"Optional[{python_type}]"

    # Basic type mapping
    type_mapping = {
        'String': 'str',
        'Int': 'int',
        'Float': 'float',
        'Boolean': 'bool',
        'ID': 'str',  # GraphQL ID is typically a string
        'DateTime': 'datetime',
        'Date': 'date',
        'JSON': 'Dict[str, Any]',
        'JSONString': 'str',
        'Decimal': 'Decimal',
        'BigInt': 'int',
    }
    
    python_type = type_mapping.get(gql_type, gql_type)
    return python_type if is_required else f"Optional[{python_type}]"

def sanitize_field_name(name: str) -> str:
    """Sanitize field names to be valid Python identifiers"""
    # Handle Python keywords
    python_keywords = {'from', 'class', 'import', 'return', 'None', 'True', 'False', 'async', 'await'}
    if name in python_keywords:
        return f"{name}_"
    return name

def generate_pydantic_models(models_json: Dict) -> str:
    """Generate Pydantic models from the GraphQL schema"""
    output = [
        "from datetime import datetime, date",
        "from decimal import Decimal",
        "from typing import List, Optional, Dict, Any",
        "from pydantic import BaseModel, Field",
        "\n\n"
    ]
    
    # First generate enums
    for enum_name, values in models_json['enums'].items():
        output.append(f"class {enum_name}(str):")
        for value in values:
            # Clean up enum values
            clean_value = value.strip().replace(' ', '_').upper()
            output.append(f"    {clean_value} = '{value}'")
        output.append("")
    
    # Then generate type models
    for type_name, fields in models_json['types'].items():
        output.append(f"class {type_name}(BaseModel):")
        if not fields:
            output.append("    pass")
        else:
            for field_name, field_type in fields.items():
                sanitized_name = sanitize_field_name(field_name)
                python_type = graphql_to_python_type(field_type)
                
                # If the field name needed to be sanitized, use Field alias
                if sanitized_name != field_name:
                    output.append(f"    {sanitized_name}: {python_type} = Field(None, alias='{field_name}')")
                else:
                    output.append(f"    {field_name}: {python_type}")
        output.append("")
    
    # Finally generate input models
    for input_name, fields in models_json['inputs'].items():
        output.append(f"class {input_name}(BaseModel):")
        if not fields:
            output.append("    pass")
        else:
            for field_name, field_type in fields.items():
                sanitized_name = sanitize_field_name(field_name)
                python_type = graphql_to_python_type(field_type)
                
                if sanitized_name != field_name:
                    output.append(f"    {sanitized_name}: {python_type} = Field(None, alias='{field_name}')")
                else:
                    output.append(f"    {field_name}: {python_type}")
        output.append("")
    
    return "\n".join(output)

def main():
    # Read the JSON file
    with open('extracted_models.json', 'r') as f:
        models = json.load(f)
    
    # Generate the Pydantic models
    pydantic_models = generate_pydantic_models(models)
    
    # Save to file
    output_file = Path('models.py')
    output_file.write_text(pydantic_models)
    print(f"Pydantic models have been generated in {output_file}")

if __name__ == "__main__":
    main()
