import json
from typing import Dict, Any

def convert_graphql_type(gql_type: str) -> str:
    """Convert GraphQL types to Python/Pydantic types"""
    type_mapping = {
        "String": "str",
        "Int": "int",
        "Float": "float",
        "Boolean": "bool",
        "ID": "str",
        "DateTime": "datetime",
        "Date": "date",
        "BigInt": "int",
        "Decimal": "Decimal",
        "JSONString": "Dict[str, Any]",
        "UUID": "UUID",
        "NauticalUUID": "UUID"
    }
    
    # Handle non-null (!) and list types ([])
    is_required = gql_type.endswith("!")
    is_list = gql_type.startswith("[") and gql_type.endswith("]")
    
    # Clean up the type
    clean_type = gql_type.replace("!", "").replace("[", "").replace("]", "")
    
    # Get the Python type
    python_type = type_mapping.get(clean_type, clean_type)
    
    # Add List wrapper if needed
    if is_list:
        python_type = f"List[{python_type}]"
    
    # Add Optional wrapper if not required
    if not is_required and not is_list:
        python_type = f"Optional[{python_type}]"
        
    return python_type

def generate_pydantic_model(name: str, fields: Dict[str, str]) -> str:
    """Generate a Pydantic model class from GraphQL type definition"""
    imports = set()
    field_definitions = []
    
    for field_name, field_type in fields.items():
        python_type = convert_graphql_type(field_type)
        
        # Track needed imports
        if "datetime" in python_type:
            imports.add("from datetime import datetime, date")
        if "Decimal" in python_type:
            imports.add("from decimal import Decimal")
        if "UUID" in python_type:
            imports.add("from uuid import UUID")
        if "List" in python_type:
            imports.add("from typing import List, Optional, Dict, Any")
        elif "Optional" in python_type:
            imports.add("from typing import Optional, Dict, Any")
            
        # Handle camelCase to snake_case conversion
        snake_case_name = ''.join(['_' + c.lower() if c.isupper() else c for c in field_name]).lstrip('_')
        
        # Add Field if name needs to be aliased
        if snake_case_name != field_name:
            field_definitions.append(f'    {snake_case_name}: {python_type} = Field(..., alias="{field_name}")')
        else:
            field_definitions.append(f'    {snake_case_name}: {python_type}')
    
    # Combine everything into a class definition
    imports.add("from pydantic import BaseModel, Field")
    
    return f"""{''.join(f'{imp}\n' for imp in sorted(imports))}

class {name}(BaseModel):
{chr(10).join(field_definitions)}
"""

def generate_all_models(schema_dict: Dict[str, Any]) -> Dict[str, str]:
    """Generate all Pydantic models from GraphQL schema"""
    models = {}
    
    for type_name, type_def in schema_dict["types"].items():
        # Skip certain types if needed
        # if type_name in ["Query", "Mutation"]:
        #     continue
            
        models[type_name] = generate_pydantic_model(type_name, type_def)
    
    return models

# Load your GraphQL schema
with open("extracted_models.json") as f:
    schema = json.load(f)

# Generate all models
models = generate_all_models(schema)

# Write to separate files or one large file
with open("generated_models.py", "w") as f:
    f.write("# Generated Pydantic models from GraphQL schema\n\n")
    for model_code in models.values():
        f.write(f"{model_code}\n")