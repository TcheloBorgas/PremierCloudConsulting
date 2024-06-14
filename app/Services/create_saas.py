import boto3

def create_s3_bucket(bucket_name):
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)
    return f"S3 bucket {bucket_name} created"

def deploy_lambda_function(function_name, role, handler, zip_file):
    lambda_client = boto3.client('lambda')
    with open(zip_file, 'rb') as f:
        code = f.read()
    lambda_client.create_function(
        FunctionName=function_name,
        Runtime='python3.8',
        Role=role,
        Handler=handler,
        Code={'ZipFile': code}
    )
    return f"Lambda function {function_name} deployed"
