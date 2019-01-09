# Copyright (c) 2018 Cable Television Laboratories, Inc. ("CableLabs")
#                    and others.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This script is responsible for deploying virtual environments
import argparse
import logging

from jinja2 import Environment, FileSystemLoader
import os
import yaml

from snaps_orch.openstack import launch_utils

__author__ = 'spisarski'

logger = logging.getLogger('openstack-launch')

ARG_NOT_SET = "argument not set"


def __run(arguments):
    """
    :return: To the OS
    """
    log_level = logging.INFO
    if arguments.log_level != 'INFO':
        log_level = logging.DEBUG
    logging.basicConfig(level=log_level)

    logger.info('Starting to Deploy')

    # Setup J2 Template variables
    extra_vars = __parse_ev(arguments.extra_vars)
    ev_env = Environment(loader=FileSystemLoader(
        searchpath=os.path.dirname(arguments.env_file)))
    ev_tmplt = ev_env.get_template(os.path.basename(arguments.env_file))
    env_str = ev_tmplt.render(**extra_vars)
    env_dict = yaml.load(env_str)
    env_dict.update(extra_vars)

    logger.info('Starting deployment of file [%s] with environment %s',
                arguments.tmplt_file, env_dict)

    # Apply env_file and extra_vars file to template
    env = Environment(loader=FileSystemLoader(
        searchpath=os.path.dirname(arguments.tmplt_file)))
    template = env.get_template(os.path.basename(arguments.tmplt_file))
    output = template.render(**env_dict)

    config = yaml.load(output)

    if config:
        clean = arguments.clean is not ARG_NOT_SET
        clean_image = arguments.clean_image is not ARG_NOT_SET
        deploy = arguments.deploy is not ARG_NOT_SET
        launch_utils.launch_config(config, deploy, clean, clean_image)
    else:
        logger.error(
            'Unable to read configuration file - ' + arguments.tmplt_file)
        exit(1)

    exit(0)


def __parse_ev(extra_vars):
    out = dict()
    if extra_vars and isinstance(extra_vars, list):
        for extra_var in extra_vars:
            var_toks = extra_var.split('=')
            if len(var_toks) == 2:
                out[var_toks[0]] = var_toks[1]
    return out


if __name__ == '__main__':
    # To ensure any files referenced via a relative path will begin from the
    # directory in which this file resides
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--deploy', dest='deploy', nargs='?', default=ARG_NOT_SET,
        help='When used, environment will be deployed and provisioned')
    parser.add_argument(
        '-c', '--clean', dest='clean', nargs='?', default=ARG_NOT_SET,
        help='When used, the environment will be removed')
    parser.add_argument(
        '-i', '--clean-image', dest='clean_image', nargs='?',
        default=ARG_NOT_SET,
        help='When cleaning, if this is set, the image will be cleaned too')
    parser.add_argument(
        '-t', '--tmplt', dest='tmplt_file', required=True,
        help='The SNAPS deployment template YAML file - REQUIRED')
    parser.add_argument(
        '-e', '--env-file', dest='env_file',
        help='Yaml file containing substitution values to the env file')
    parser.add_argument(
        '-v', '--extra-vars', dest='extra_vars', nargs='*',
        help='List of k/v pairs separated by =')
    parser.add_argument(
        '-l', '--log-level', dest='log_level', default='INFO',
        help='Logging Level (INFO|DEBUG)')
    args = parser.parse_args()

    if args.deploy is ARG_NOT_SET and args.clean is ARG_NOT_SET:
        print(
            'Must enter either -d for deploy or -c for cleaning up and '
            'environment')
        exit(1)
    if args.deploy is not ARG_NOT_SET and args.clean is not ARG_NOT_SET:
        print('Cannot enter both options -d/--deploy and -c/--clean')
        exit(1)
    __run(args)
