from config import run_oc_command

def create_project(project_name):
    command = f"oc new-project {project_name}"
    output = run_oc_command(command)
    return f"Project {project_name} created with output: {output}"

def create_service(service_name, namespace, image):
    command = f"oc new-app {image} --name={service_name} -n {namespace}"
    output = run_oc_command(command)
    return f"Service {service_name} deployed in namespace {namespace} with output: {output}"
