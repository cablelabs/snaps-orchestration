# snaps-orchestration

snaps-orchestration contains Python clients for provisioning cloud
services. Currently OpenStack is supported.

## Getting started

```Bash
git clone https://github.com/cablelabs/snaps-orchestration.git
pip install -e snaps-orchestration/
```

If you're new to git and GitHub, be sure to check out the [Pro
Git](https://git-scm.com/book/en/v2) book. [GitHub
Help](https://help.github.com/) is also outstanding.

## Executing Orchestration for OpenStack

```Bash
python {repo_dir}/openstack-launch.py -t {path to snaps template} -e {path to optional environment file for J2} [-d (for deploy)| -c (for cleanup)
```

Please see the docs/examples/openstack directory for example SNAPS OpenStack orchestration templates

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
