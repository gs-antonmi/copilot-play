from typing import Optional

from .enforce import enforce

class DeploymentType:
    def __init__(self, name: str, description: Optional(str)=None, schema: Optional(Dict)=None):
        assert(name is not None, 'name cannot be None')
        self._name = name
        self._description = description
        assert(self.is_valid_schema(), 'Invalid schema for deployment type {name}.')
        self._schema = schema

    def is_valid_schema():
        return true