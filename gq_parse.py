from graphql import build_schema
from graphql.language.ast import ObjectTypeDefinitionNode

# Load the GraphQL schema
with open("nc.graphql", "r") as schema_file:
    schema_str = schema_file.read()

schema = build_schema(schema_str)

# Parse types from the schema
for type_name, type_def in schema.type_map.items():
    if type_name.startswith("__"):  # Skip introspection types
        continue
    if isinstance(type_def.ast_node, ObjectTypeDefinitionNode):
        fields = type_def.ast_node.fields
        model_fields = []
        for field in fields:
            field_name = field.name.value
            # Get the inner type by traversing through NonNull and List wrappers
            field_type_node = field.type
            while hasattr(field_type_node, 'type'):
                field_type_node = field_type_node.type
            field_type = field_type_node.name.value if field_type_node else "Unknown"
            model_fields.append((field_name, field_type))

        # Generate Django model
        # save to file
        with open(f"./dj_models/{type_name}.py", "w") as f:
            f.write(f"class {type_name}(models.Model):\n")
            for field_name, field_type in model_fields:
                f.write(f"    {field_name} = models.{field_type}()\n")
            f.write("\n")
