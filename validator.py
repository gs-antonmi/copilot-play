import os
import yaml

from typing import Dict, Any
from openapi_schema_validator import validate


def validate_params(spec_file: str, params: Dict[str, Any]) -> bool:
    assert os.path.exists(spec_file), f'Spec file {spec_file} does not exist'
    with open(spec_file, 'r') as f:
        spec_dict = yaml.load(f, Loader=yaml.FullLoader)
    validate(params, spec_dict)
    return True



#     from openapi_schema_validator import validate

# # A sample schema
# schema = {
#     "type": "object",
#     "required": [
#        "name"
#     ],
#     "properties": {
#         "name": {
#             "type": "string"
#         },
#         "age": {
#             "type": ["integer", "null"],
#             "format": "int32",
#             "minimum": 0,
#         },
#         "birth-date": {
#             "type": "string",
#             "format": "date",
#         },
#         "address": {
#              "type": 'array',
#              "prefixItems": [
#                  { "type": "number" },
#                  { "type": "string" },
#                  { "enum": ["Street", "Avenue", "Boulevard"] },
#                  { "enum": ["NW", "NE", "SW", "SE"] }
#              ],
#              "items": False,
#          }
#     },
#     "additionalProperties": False,
# }

# # If no exception is raised by validate(), the instance is valid.
# validate({"name": "John", "age": 23, "address": [1600, "Pennsylvania", "Avenue"]}, schema)

# validate({"name": "John", "city": "London"}, schema)