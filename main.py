from deployment_type import DeploymentType
from validator import validate_params

# spec = {
#     'template': 'SME',
#     'description': 'Single Model Endpoint',
#     'parameters': [
#         {'name': 'endpoint_name', 'required': True, 'schema': {'type': 'string'}},
#         {'name': 'InputLocation', 'required': True, 'schema': {'type': 'string'}},
#     ]
# }

def main():
    # deployment_type = DeploymentType(spec)
    spec_file = 'specs/single_model_endpoint.yaml'
    params = {
        'projectName': 'dsmltests',
        # 'deploymentName': 'antonmi-test',
    }
    validate_params(spec_file, params)
    print('Done!')

if __name__ == '__main__':
    main()
