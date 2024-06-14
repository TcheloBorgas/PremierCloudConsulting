import boto3
import json

def create_user_and_role(user_name, policy_arn):
    iam = boto3.client('iam')
    user = iam.create_user(UserName=user_name)
    role = iam.create_role(
        RoleName=user_name + '_role',
        AssumeRolePolicyDocument=json.dumps({
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Effect': 'Allow',
                    'Principal': {'Service': 'ec2.amazonaws.com'},
                    'Action': 'sts:AssumeRole'
                }
            ]
        })
    )
    iam.attach_user_policy(UserName=user_name, PolicyArn=policy_arn)
    return user, role
