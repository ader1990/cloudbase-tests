import stubout
import mox
import unittest

from cloudbaseinit.openstack.common import cfg
from cloudbaseinit.metadata.services import base
from cloudbaseinit.osutils import windows
from cloudbaseinit.test import fake
from cloudbaseinit.metadata.services import httpservice
from cloudbaseinit.metadata.services import base
# ? from cloudbaseinit.utils import crypt

CONF = cfg.CONF


class HttpServiceTest(unittest.TestCase):

    def __init__(self):
        self._mox = mox.Mox()

    def setUp(self):

        self._os_version = 6
        self.path = 'fake\path'
        self.password = 'Passw0rd'

        self.flags(metadata_base_url='http://169.254.169.254/')

        self._mox.StubOutWithMock(windows.WindowsUtils,
                                    'check_static_route_exists')
        self._mox.StubOutWithMock(httpservice.HttpService,
                                    '_check_metadata_ip_route')
        self._mox.StubOutWithMock(httpservice.HttpService, '_get_response')
        self._mox.StubOutWithMock(httpservice.HttpService, '_get_data')
        self._mox.StubOutWithMock(httpservice.HttpService, '_post_data')
        self._mox.StubOutWithMock(base.BaseMetadataService, 'get_meta_data')
        self._mox.StubOutWithMock(base.BaseMetadataService, 'post_password')

    def tearDown(self):
        self._mox.UnsetStubs()

    def _test_load(self):

        self.httpservice.HttpService._check_metadata_ip_route()

        m = base.BaseMetadataService.get_meta_data(mox.IsA(str))
        m.AndReturn(data)

        self._mox.ReplayAll()
        self.base.BaseMetadataService.get_meta_data('str')
        self._mox.VerifyAll()

    def _test_post_password(self,):
        m = base.BaseMetadataService.post_password(mox.IsA(str))
        m.AndReturn(True)

        self._mox.ReplayAll
        self.base.BaseMetadataService.post_password(password)
        self._mox.VerifyAll

    def _test_get_response():
        req = httpservice.HttpService._get_response()
        assertRaise(req,)

    def _test_get_data(self):
        req = httpservice.HttpService._get_data(path)
        self.assertEquals(req, )

    def _test_post_data(self):
        req = httpservice.HttpService._post_data(metadata_base_url, path)
        self.assertTrue(req)

    def test_http(self):
        self._test_get_response()
        self._test_get_data()
        self._test_post_data()
        self._test_load()
        self._test_post_password()

'''
de definit instance_data #######
'''
