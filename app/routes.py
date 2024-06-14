from flask import request, jsonify
from app import app
from Services.provision_ec2 import provision_ec2
from Services.create_vm import create_vm
from Services.manage_containers import deploy_container, delete_container
from Services.create_saas import create_s3_bucket, deploy_lambda_function
from Services.create_mysql_db import create_mysql_db
from Services.create_postgresql_db import create_postgresql_db
from Services.create_mongodb_db import create_mongodb_db
from Services.manage_security import create_user_and_role
from Services.manage_openshift import create_project, create_service

@app.route('/provision/ec2', methods=['POST'])
def provision_ec2_route():
    data = request.get_json()
    instance_id = provision_ec2(data['image_id'], data['instance_type'], data['key_name'])
    return jsonify({'instance_id': instance_id})

@app.route('/create/vm', methods=['POST'])
def create_vm_route():
    data = request.get_json()
    instance_id = create_vm(data['image_id'], data['instance_type'], data['key_name'])
    return jsonify({'instance_id': instance_id})

@app.route('/deploy/container', methods=['POST'])
def deploy_container_route():
    data = request.get_json()
    message = deploy_container(data['image'], data['name'], data['namespace'])
    return jsonify({'message': message})

@app.route('/delete/container', methods=['POST'])
def delete_container_route():
    data = request.get_json()
    message = delete_container(data['name'], data['namespace'])
    return jsonify({'message': message})

@app.route('/create/saas/s3', methods=['POST'])
def create_s3_bucket_route():
    data = request.get_json()
    message = create_s3_bucket(data['bucket_name'])
    return jsonify({'message': message})

@app.route('/deploy/lambda', methods=['POST'])
def deploy_lambda_function_route():
    data = request.get_json()
    message = deploy_lambda_function(data['function_name'], data['role'], data['handler'], data['zip_file'])
    return jsonify({'message': message})

@app.route('/create/db/mysql', methods=['POST'])
def create_mysql_db_route():
    data = request.get_json()
    db_identifier = create_mysql_db(data['db_identifier'], data['master_username'], data['master_password'])
    return jsonify({'db_identifier': db_identifier})

@app.route('/create/db/postgresql', methods=['POST'])
def create_postgresql_db_route():
    data = request.get_json()
    db_identifier = create_postgresql_db(data['db_identifier'], data['master_username'], data['master_password'])
    return jsonify({'db_identifier': db_identifier})

@app.route('/create/db/mongodb', methods=['POST'])
def create_mongodb_db_route():
    data = request.get_json()
    cluster_identifier = create_mongodb_db(data['cluster_identifier'], data['master_username'], data['master_password'])
    return jsonify({'cluster_identifier': cluster_identifier})

@app.route('/manage/security', methods=['POST'])
def manage_security_route():
    data = request.get_json()
    user, role = create_user_and_role(data['user_name'], data['policy_arn'])
    return jsonify({'user': user, 'role': role})

@app.route('/create/project', methods=['POST'])
def create_project_route():
    data = request.get_json()
    message = create_project(data['project_name'])
    return jsonify({'message': message})

@app.route('/create/service', methods=['POST'])
def create_service_route():
    data = request.get_json()
    message = create_service(data['service_name'], data['namespace'], data['image'])
    return jsonify({'message': message})
