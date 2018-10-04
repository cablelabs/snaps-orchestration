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

from snaps_orch.openstack import launch_utils

logging.basicConfig(level=logging.DEBUG)


class LaunchUtilsTests(unittest.TestCase):
    """
    Mocked unit tests for snaps_orch.openstack.launch_utils.py#launch_config()
    """
    def setUp(self):
        self.pb_loc = pkg_resources.resource_filename(
            'tests.openstack.conf', 'simple_snaps_tmplt.yaml')

    # @patch('ansible.executor.playbook_executor.PlaybookExecutor.run',
    #        return_value=0)
    # @patch('os.path.expanduser', return_value='/foo/bar')
    def test_launch_config(self):
        """
        Initial test to ensure main code path does not have any syntax or
        import errors when calling with parameters that are mostly used
        :return:
        """
        # self.assertIsNotNone(m1)
        # self.assertIsNotNone(m2)
        launch_utils.launch_config(
            self.pb_loc, hosts_inv=['foo', 'bar'], host_user='user',
            password='password', variables={'foo': 'bar'})
