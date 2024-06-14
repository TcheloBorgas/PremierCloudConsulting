from config import run_oc_command

def deploy_container(image, name, namespace):
    command = f"oc new-app {image} --name={name} -n {namespace}"
    output = run_oc_command(command)
    return f"Container {name} deployed in namespace {namespace} with output: {output}"

def delete_container(name, namespace):
    command = f"oc delete all -l app={name} -n {namespace}"
    output = run_oc_command(command)
    return f"Container {name} in namespace {namespace} deleted with output: {output}"
