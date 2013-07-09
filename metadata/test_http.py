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

#from cloudbaseinit.metadata.services import base
from cloudbaseinit.openstack.common import cfg
#from cloudbaseinit.test.metadata import fake
from cloudbaseinit.metadata.services import httpservice
#from cloudbaseinit.osutils import windows

CONF = cfg.CONF


class HttpServiceTest(unittest.TestCase):
    ''' testing http requests Class '''

    def setUp(self):

        self._mox = mox.Mox()
        self._setup_stubs()

    def _setup_stubs(self):
        self._mox.StubOutWithMock(urllib2, 'Request')
        self._mox.StubOutWithMock(urllib2, 'urlopen')
        #self._mox.StubOutWithMock(windows.WindowsUtils, 'get_os_version')
        #not yet self._mox.StubOutWithMock(posixpath, 'join')

    def tearDown(self):
        self._mox.UnsetStubs()
        self._mox.ResetAll()

    def test_get_meta_data(self):
        svc = httpservice.HttpService()

        fake_request = 'fake_request'
        fake_meta_data = '{"fake_meta_data": "fake_value"}'
        version = 'latest'
        data_type = 'openstack'

        m = urllib2.Request(mox.IsA(str))
        m.AndReturn(fake_request)

        m = urllib2.urlopen(fake_request)
        response_mock = mox.Mox().CreateMockAnything()
        m1 = response_mock.read()
        m1.AndReturn(fake_meta_data)
        m.AndReturn(response_mock)

        self._mox.ReplayAll()
        meta_data = svc.get_meta_data(data_type, version)
        self._mox.VerifyAll()

        meta_data_compare = json.loads(fake_meta_data)
        self.assertEquals(meta_data, meta_data_compare)





'''
    def test_post_password(self):
        svc = httpservice.HttpService()

        fake_request = 'fake_request'
        fake_meta_data = '{"fake_meta_data": "fake_value"}'
        version = 'latest'
        data_type = 'openstack'
        fake_data = 'fake_data'

        m = urllib2.Request(mox.IsA(str))
        m.AndReturn(fake_request)

        m = urllib2.urlopen(fake_request, fake_data)
        response_mock = mox.Mox().CreateMockAnything()
        m1 = response_mock.read()
        m1.AndReturn(fake_meta_data)
        m.AndReturn(response_mock)

        self._mox.ReplayAll()
        meta_data = svc.get_meta_data(data_type, version)
        self._mox.VerifyAll()

        meta_data_compare = json.loads(fake_meta_data)
        self.assertEquals(meta_data, meta_data_compare)

        test_check_metadata_ip_route(self):
            version = windows.WindowsUtils.get_os_version()
            m.AndReturn(version)

            self._mox.ReplayAll()
            meta_data = svc._check_metadata_ip_route()
            self._mox.VerifyAll()

'''
