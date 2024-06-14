import boto3

def create_mysql_db(db_identifier, master_username, master_password):
    rds = boto3.client('rds')
    response = rds.create_db_instance(
        DBInstanceIdentifier=db_identifier,
        MasterUsername=master_username,
        MasterUserPassword=master_password,
        DBInstanceClass='db.t2.micro',
        Engine='mysql',
        AllocatedStorage=20
    )
    return response['DBInstanceIdentifier']
