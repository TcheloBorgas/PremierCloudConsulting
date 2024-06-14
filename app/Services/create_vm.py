import boto3

def create_vm(image_id, instance_type, key_name):
    ec2 = boto3.resource('ec2')
    instances = ec2.create_instances(
        ImageId=image_id,
        MinCount=1,
        MaxCount=1,
        InstanceType=instance_type,
        KeyName=key_name
    )
    return instances[0].id
