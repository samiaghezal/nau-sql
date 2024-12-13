from pathlib import Path
import re
from typing import Dict, List

def generate_ninja_api(models_json: Dict) -> str:
    """Generate Django Ninja API endpoints from models"""
    output = [
        "from django.shortcuts import get_object_or_404",
        "from ninja import Router, Query",
        "from ninja.pagination import paginate",
        "from typing import List",
        "from .models import *  # Your Django models",
        "from .schemas import *  # Your Pydantic models",
        "\n",
        "router = Router()",
        "\n"
    ]

    # Generate CRUD endpoints for each type
    for type_name in models_json['types'].keys():
        # Skip utility types and types that start with underscore
        if type_name.startswith('_') or type_name in ['Query', 'Mutation', 'PageInfo']:
            continue

        # Generate endpoints
        endpoints = generate_crud_endpoints(type_name)
        output.extend(endpoints)
        output.append("\n")

    return "\n".join(output)

def generate_crud_endpoints(type_name: str) -> List[str]:
    """Generate CRUD endpoints for a specific type"""
    snake_case_name = camel_to_snake(type_name)
    plural_name = snake_case_name + 's'  # Simple pluralization
    
    endpoints = [
        f"# {type_name} endpoints",
        f"@router.get('/{plural_name}', response=List[{type_name}])",
        f"@paginate",
        f"def list_{plural_name}(request):",
        f"    return {type_name}.objects.all()",
        "\n",
        f"@router.get('/{plural_name}/{{id}}', response={type_name})",
        f"def get_{snake_case_name}(request, id: int):",
        f"    return get_object_or_404({type_name}, id=id)",
        "\n",
        f"@router.post('/{plural_name}', response={type_name})",
        f"def create_{snake_case_name}(request, payload: {type_name}Create):",
        f"    data = payload.dict()",
        f"    {snake_case_name} = {type_name}.objects.create(**data)",
        f"    return {snake_case_name}",
        "\n",
        f"@router.put('/{plural_name}/{{id}}', response={type_name})",
        f"def update_{snake_case_name}(request, id: int, payload: {type_name}Update):",
        f"    {snake_case_name} = get_object_or_404({type_name}, id=id)",
        f"    for attr, value in payload.dict(exclude_unset=True).items():",
        f"        setattr({snake_case_name}, attr, value)",
        f"    {snake_case_name}.save()",
        f"    return {snake_case_name}",
        "\n",
        f"@router.delete('/{plural_name}/{{id}}')",
        f"def delete_{snake_case_name}(request, id: int):",
        f"    {snake_case_name} = get_object_or_404({type_name}, id=id)",
        f"    {snake_case_name}.delete()",
        f"    return {{'success': True}}",
    ]
    
    return endpoints

def camel_to_snake(name: str) -> str:
    """Convert CamelCase to snake_case"""
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

def main():
    # Read the JSON file
    with open('extracted_models.json', 'r') as f:
        import json
        models = json.load(f)
    
    # Generate the API
    api_code = generate_ninja_api(models)
    
    # Save to file
    output_file = Path('api.py')
    output_file.write_text(api_code)
    print(f"Django Ninja API has been generated in {output_file}")

    # Generate URLs file
    urls_code = [
        "from django.urls import path",
        "from ninja import NinjaAPI",
        "from .api import router",
        "\n",
        "api = NinjaAPI()",
        "api.add_router('', router)",
        "\n",
        "urlpatterns = [",
        "    path('api/', api.urls),",
        "]"
    ]
    
    urls_file = Path('urls.py')
    urls_file.write_text('\n'.join(urls_code))
    print(f"URLs configuration has been generated in {urls_file}")

if __name__ == "__main__":
    main()
