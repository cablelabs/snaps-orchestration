# snaps-orchestration

This is a lightweight orchestrator for OpenStack that allows one to
create objects, create complex virtual environments, and execute Ansible
Playbooks against virtual machines.

## Getting started

```Bash
git clone https://github.com/cablelabs/snaps-orchestration.git

# Cleanup Python runtime
pip uninstall -y snaps-orchestration; pip freeze | xargs pip uninstall -y
pip install -r snaps-orchestration/requirements.txt
pip install -e snaps-orchestration/
```

If you're new to git and GitHub, be sure to check out the [Pro
Git](https://git-scm.com/book/en/v2) book. [GitHub
Help](https://help.github.com/) is also outstanding.

## Executing Orchestration for OpenStack

```Bash
python {repo_dir}/snaps-orchestration/openstack-launch.py -t {path to snaps template} -e {path to optional environment file for J2} [-d (for deploy)| -c (for cleanup)
```

**Please see the [Quickstart](docs/quickstart.md) to get you started with a concrete example on deploying a simple scenario**
**Also see the [Configuration Guide](docs/orchestrator-config.md) for assistance on creating your own deployment**

## Contributing

snaps-orchestration was originally built by [CableLabs](http://cablelabs.com/),
but we could use your help! Check out our
[contributing guidelines](CONTRIBUTING.md) to get started.

## Other important stuff

We use an [Apache 2.0 License](LICENSE) for snaps-orchestration.

Questions? Just send us an email at
[snaps@cablelabs.com](mailto:snaps@cablelabs.com) or join the conversation:
[![IRC](https://www.irccloud.com/invite-svg?channel=%23cablelabs-snaps&amp;hostname=irc.freenode.net&amp;port=6697&amp;ssl=1)](http://webchat.freenode.net/?channels=cablelabs-snaps)[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fcablelabs%2Fsnaps-boot.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fcablelabs%2Fsnaps-boot?ref=badge_shield)
.

## License

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fcablelabs%2Fsnaps-boot.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fcablelabs%2Fsnaps-boot?ref=badge_large)
