import stubout
import mox
import sys
import unittest

from cloudbaseinit.metadata.services import base as services_base
from cloudbaseinit.osutils import windows
from cloudbaseinit.openstack.commom import cfg
from cloudbaseinit.osutils import factory
from cloudbaseinit.plugins import base
from cloudbaseinit.utils import crypt
from cloudbaseinit.plugins.windows import setuserpassword
from cloudbaseinit.metadata.services import httpservice
from cloudbaseinit.test.metadata import fake


CONF = cfg.CONF


class SetUserPasswordPluginTest(unittest.TestCase):

    def __init__(self, test_case_name):
        self._mox = mox.Mox()

    def setUp(self):

        self.password = None
        self.flags(username='username')

        self._mox.StubOutWithMock(crypt.RSAWrapper, 'public_encrypt')
        self._mox.StubOutWithMock(setuserpassword.SetUserPasswordPlugin,
                                    '_get_password')
        self._mox.StubOutWithMock(windows.WindowsUtils, 'get_meta_data')
        self._mox.StubOutWithMock(windows.WindowsUtils,
                                    'generate_random_password')
        self._mox.StubOutWithMock(windows.SetUserPasswordPlugin,
                                    '_get_ssh_public_key')
        self._mox.StubOutWithMock(httpservice.HttpService, 'can_post_password')
        self._mox.StubOutWithMock(services_base.BaseMetadataService,
                                    'is_password_set')
        self._mox.StubOutWithMock(windows.WindowsUtils, 'user_exists')
        self._mox.StubOutWithMock(setuserpassword.SetUserPasswordPlugin,
                                    '_set_metadata_password')

    def tearDown(self):
        self._mox.UnsetStubs()

    def _test_get_ssh_public_key():
        test = setuserpassword.SetUserPasswordPlugin._get_ssh_public_key()
        self.assertEquals(test, )

    def _test_get_password(self, integer):
        passwrd = osutils.generate_random_password(integer)
        self.assertEquals(len(passwrd), integer)

    def _test_user_password_set(self, integer, ):
        fake_data = fake.get_fake_data()
        self.cloudbaseinit.utils.crypt.RSAWrapper.public_encrypt(mox.IsA(str))

        self.osutils.generate_random_password(mox.IsA(int))

        m = windows.WindowsUtils.get_meta_data(mox.IsA(str), mox.IsA(str))
        m.AndReturn(fake_data)

        m = httpservice.HttpService.can_post_password()
        m.AndReturn(True)

        m = services_base.BaseMetadataService.is_password_set(mox.IsA(str))
        m.AndReturn(len(password))

        m = windows.WindowsUtils.user_exists(mox.IsA(str))

        password = setuserpassword.SetUserPasswordPlugin._get_password(osutils)

        self.setuserpassword.SetUserPasswordPlugin._set_metadata_password(
            password, httpservice)

        self._mox.ReplayAll

        self._mox.VerifyAll

    def test_user_password_set(self):
        self._test_user_password_set()


'''

'''
