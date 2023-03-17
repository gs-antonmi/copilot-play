from .deployment_type import DeploymentType

schema = {
    
}

def main():
    deployment_type = DeploymentType('SME', 'Single Model Endpoint', schema)

if __name__ == '__main__':
    main()