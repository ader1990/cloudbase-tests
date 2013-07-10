# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 Cloudbase Solutions Srl
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import json
import mox
import unittest
import urllib2

from cloudbaseinit.metadata.services import httpservice


class HttpServiceTest(unittest.TestCase):
    ''' testing http requests Class '''

    def setUp(self):
        self.mox = mox.Mox()
        self._setup_stubs()

    def _setup_stubs(self):
        self.mox.StubOutClassWithMocks(urllib2, 'Request')
        self.mox.StubOutWithMock(urllib2, 'urlopen')

    def tearDown(self):
        self.mox.UnsetStubs()

    def test_get_meta_data(self):
        svc = httpservice.HttpService()
        response_mock = self.mox.CreateMockAnything()

        data_type = 'openstack'
        fake_meta_data = '{"fake_meta_data": "fake_value"}'
        version = 'latest'

        fake_request = urllib2.Request(mox.IsA(str))

        m = urllib2.urlopen(fake_request)
        m.AndReturn(response_mock)
        m1 = response_mock.read()
        m1.AndReturn(fake_meta_data)

        self.mox.ReplayAll()
        meta_data = svc.get_meta_data(data_type, version)
        self.mox.VerifyAll()

        meta_data_compare = json.loads(fake_meta_data)
        self.assertEqual(meta_data, meta_data_compare)
