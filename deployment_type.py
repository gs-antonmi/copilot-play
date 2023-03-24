from typing import Optional, Dict, Any

class DeploymentType:
    def __init__(self, spec: Dict[str, Any]):
        self.validate_spec(spec)
        self._name = spec['template']
        self._description = spec['description']
        self._parameters = spec['parameters']

    def validate_spec(self, spec) -> bool:
        """Validates the schema of the deployment type."""
        if spec is None:
            raise RuntimeError('Deployment type spec is None')
        if 'template' not in spec:
            raise RuntimeError('Deployment type spec does not contain a template name')
        if 'description' not in spec:
            raise RuntimeError('Deployment type spec does not contain a description')
        if 'parameters' not in spec:
            raise RuntimeError('Deployment type spec does not contain parameters')
        for parameter in spec['parameters']:
            if 'name' not in parameter:
                raise RuntimeError('Deployment type spec contains a parameter without a name')
            if 'required' not in parameter:
                raise RuntimeError('Deployment type spec contains a parameter without a required flag')
            if 'schema' not in parameter:
                raise RuntimeError('Deployment type spec contains a parameter without a schema')
