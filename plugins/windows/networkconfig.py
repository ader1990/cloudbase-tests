import stubout
import mox
import unittest

from cloudbaseinit.metadata.services import httpservice
from cloudbaseinit.openstack.common import cfg

CONF = cfg.CONF


class NetworkConfigPluginTest(unittest.TestCase):

    def __init__(self):
        self._mox = mox.Mox()

    def setUp(self):
        self.flags(network_adapter=None)

    def tearDown(self):
        self._mox.UnsetStubs()

    def _test_network_config(self):

        m = httpservice.HttpService('openstack')
        m.AndReturn(fake_data)