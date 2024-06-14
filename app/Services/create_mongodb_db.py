import boto3

def create_mongodb_db(cluster_identifier, master_username, master_password):
    docdb = boto3.client('docdb')
    response = docdb.create_db_cluster(
        DBClusterIdentifier=cluster_identifier,
        MasterUsername=master_username,
        MasterUserPassword=master_password,
        Engine='docdb'
    )
    return response['DBClusterIdentifier']
