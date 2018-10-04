Quick Start
===========

Use openstack-launch.py to deploy and clean up OpenStack objects that
are described in YAML files.

1.  Clone the repo and install into Python runtime

```Bash
git clone https://github.com/cablelabs/snaps-orchestration.git

# Cleanup Python runtime
pip uninstall -y snaps-orchestration; pip freeze | xargs pip uninstall -y
pip install -r snaps-orchestration/requirements.txt
pip install -e snaps-orchestration/
```

1.  Go to the repo directory

```Bash
cd snaps-orchestraion
```

1.  Create your YAML environment file from the examples/openstack/envs/lab-n.yaml.tmplt

1.  Deploy your virtual environment

```Bash
python openstack-launch.py -t examples/openstack/simple/deploy-simple.yaml -e {env filepath} -d
```

1.  Verify

```Bash
ssh ubuntu@{VM's floating IP}
password: password
```
The output should begin with 'Greetings' and continue with OpenStack credentials and networking information

1.  Clean the deployment.

```Bash
python openstack-launch.py -t examples/openstack/simple/deploy-simple.yaml -e {env filepath} -c
```
