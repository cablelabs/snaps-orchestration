Quick Start
===========

Use openstack-launch.py to deploy and clean up OpenStack objects that
are described in YAML files.

1.  Clone the repo and install into Python runtime

    >     git clone https://github.com/cablelabs/snaps-orchestration
    >     pip install -e snaps-orchestration

1.  Go to the repo directory

    >     cd snaps-orchestraion

1.  Create your YAML environment file from the examples/openstack/envs/lab-n.yaml.tmplt

1.  Deploy your virtual environment

    >     python openstack-launch.py -t examples/openstack/simple/deploy-simple.yaml -e {env filepath} -d

1.  Verify

    >     ssh ubuntu@{VM's floating IP}
    >     password: password

    > The output should begin with 'Greetings' along with the OpenStack credentials and networking information

1.  Clean the deployment.

    >     python openstack-launch.py -t examples/openstack/simple/deploy-simple.yaml -e {env filepath} -c
