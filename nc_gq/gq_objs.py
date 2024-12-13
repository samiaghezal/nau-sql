import re
import json
import os
from typing import Dict, List


def extract_graphql_objects(schema_text: str) -> Dict[str, Dict]:
    """
    Extracts complete object definitions from GraphQL schema including fields and implementations.

    Args:
        schema_text (str): The GraphQL schema text

    Returns:
        dict: Dictionary of object definitions with their fields and implementations
    """
    # Remove comments to simplify parsing
    schema_text = re.sub(r'""".*?"""', "", schema_text, flags=re.DOTALL)
    schema_text = re.sub(r"#.*?\n", "\n", schema_text)

    # Pattern to match type definitions and their content
    type_pattern = (
        r"type\s+([A-Za-z][A-Za-z0-9_]*)\s*(?:implements\s+([^{]+))?\s*{([^}]+)}"
    )

    objects = {}
    for match in re.finditer(type_pattern, schema_text, re.DOTALL):
        type_name = match.group(1)
        implements = match.group(2)
        fields_text = match.group(3)

        # Clean up implementations
        if implements:
            implements = [i.strip() for i in implements.replace("&", ",").split(",")]
        else:
            implements = []

        # Extract fields
        field_pattern = r"([A-Za-z][A-Za-z0-9_]*)\s*(?:\(.*?\))?\s*:\s*([^!\s]+!?\s*(?:\[[^\]]+\])?!?)"
        fields = {}
        for field_match in re.finditer(field_pattern, fields_text):
            field_name = field_match.group(1)
            field_type = field_match.group(2).strip()
            fields[field_name] = field_type

        objects[type_name] = {"implements": implements, "fields": fields}

    return objects


def save_objects_to_files(objects: Dict[str, Dict]):
    """
    Saves extracted objects to organized folder structure
    """
    # Create base directory
    base_dir = "graphql_objects"
    os.makedirs(base_dir, exist_ok=True)

    # Create subdirectories based on object categories
    categories = {
        "core": ["User", "Product", "Order", "Customer"],
        "commerce": ["Cart", "Checkout", "Payment", "Shipping"],
        "seller": ["Seller", "SellerType", "SellerApplication"],
        "content": ["Page", "Menu", "Content", "Media"],
        "config": ["MarketplaceConfiguration", "NauticalConfiguration"],
        "misc": [],  # For objects that don't fit other categories
    }

    # Create category directories
    for category in categories.keys():
        os.makedirs(os.path.join(base_dir, category), exist_ok=True)

    # Create index file
    index = {"total_objects": len(objects), "categories": {}, "object_listing": {}}

    # Save each object to appropriate directory
    for type_name, type_info in objects.items():
        # Determine category
        category = "misc"
        for cat, types in categories.items():
            if any(type_name.startswith(t) or type_name == t for t in types):
                category = cat
                break

        # Add to index
        if category not in index["categories"]:
            index["categories"][category] = []
        index["categories"][category].append(type_name)
        index["object_listing"][type_name] = f"{category}/{type_name}.json"

        # Save object definition
        file_path = os.path.join(base_dir, category, f"{type_name}.json")
        with open(file_path, "w") as f:
            json.dump(
                {
                    "name": type_name,
                    "implements": type_info["implements"],
                    "fields": type_info["fields"],
                },
                f,
                indent=2,
            )

    # Save index file
    with open(os.path.join(base_dir, "index.json"), "w") as f:
        json.dump(index, f, indent=2)

    # Create README
    readme_content = f"""# GraphQL Objects Documentation

Total Objects: {len(objects)}

## Categories
{generate_readme_categories(index['categories'])}

## Directory Structure
```
graphql_objects/
├── index.json
├── core/
├── commerce/
├── seller/
├── content/
├── config/
└── misc/
```"""
    with open(os.path.join(base_dir, "README.md"), "w") as f:
        f.write(readme_content)


def generate_readme_categories(categories: Dict[str, List[str]]) -> str:
    """Generates the categories section of the README"""
    result = []
    for category, types in categories.items():
        result.append(f"\n### {category.title()}")
        for type_name in sorted(types):
            result.append(f"- {type_name}")
    return "\n".join(result)


def main():
    # Read the schema file
    try:
        with open("nc.graphql", "r") as f:
            schema = f.read()
    except FileNotFoundError:
        print("Error: Could not find nc.graphql file")
        return

    # Extract objects
    objects = extract_graphql_objects(schema)

    # Save to files
    save_objects_to_files(objects)

    print(f"\nSuccessfully extracted and saved {len(objects)} GraphQL objects")
    print("Check the 'graphql_objects' directory for the organized files")


if __name__ == "__main__":
    main()
