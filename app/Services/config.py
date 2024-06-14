import boto3
import subprocess

def get_boto3_client(service):
    return boto3.client(service)

def get_boto3_resource(service):
    return boto3.resource(service)

def run_oc_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(e.stderr.decode('utf-8'))
        raise e
