# Copyright 2018 ARICENT HOLDINGS LUXEMBOURG SARL and Cable Television
# Laboratories, Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
import unittest

import pkg_resources
from mock import patch
from snaps_common.file import file_utils

from snaps_orch.openstack import launch_utils

logging.basicConfig(level=logging.DEBUG)


class LaunchUtilsTests(unittest.TestCase):
    """
    Mocked unit tests for snaps_orch.openstack.launch_utils.py#launch_config()
    """
    def setUp(self):
        self.pb_loc = pkg_resources.resource_filename(
            'tests.openstack.conf', 'snaps-orch-tmplt.yaml')
        self.pb_dict = file_utils.read_yaml(self.pb_loc)

    @patch('snaps.openstack.create_project.OpenStackProject.create')
    @patch('snaps.openstack.create_project.OpenStackProject.assoc_user')
    @patch('snaps.openstack.create_user.OpenStackUser.create')
    @patch('snaps.openstack.create_flavor.OpenStackFlavor.create')
    @patch('snaps.openstack.create_image.OpenStackImage.create')
    @patch('snaps.openstack.create_network.OpenStackNetwork.create')
    @patch('snaps.openstack.create_router.OpenStackRouter.create')
    @patch('snaps.openstack.create_keypairs.OpenStackKeypair.create')
    @patch('snaps.openstack.create_security_group.OpenStackSecurityGroup.'
           'create')
    @patch('snaps.openstack.create_instance.OpenStackVmInstance.create')
    @patch('snaps.openstack.create_instance.OpenStackVmInstance.vm_ssh_active',
           return_value=True)
    def test_launch_config(self, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11):
        """
        Initial test to ensure main code path does not have any syntax or
        import errors when calling with parameters that are mostly used
        :return:
        """
        # self.assertIsNotNone(m1)
        # self.assertIsNotNone(m2)
        launch_utils.launch_config(
            self.pb_dict, self.pb_loc, True, False, False)
