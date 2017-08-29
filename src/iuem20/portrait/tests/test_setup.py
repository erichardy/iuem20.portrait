# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from iuem20.portrait.testing import IUEM20_PORTRAIT_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that iuem20.portrait is properly installed."""

    layer = IUEM20_PORTRAIT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if iuem20.portrait is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'iuem20.portrait'))

    def test_browserlayer(self):
        """Test that IIuem20PortraitLayer is registered."""
        from iuem20.portrait.interfaces import (
            IIuem20PortraitLayer)
        from plone.browserlayer import utils
        self.assertIn(IIuem20PortraitLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = IUEM20_PORTRAIT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['iuem20.portrait'])

    def test_product_uninstalled(self):
        """Test if iuem20.portrait is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'iuem20.portrait'))

    def test_browserlayer_removed(self):
        """Test that IIuem20PortraitLayer is removed."""
        from iuem20.portrait.interfaces import \
            IIuem20PortraitLayer
        from plone.browserlayer import utils
        self.assertNotIn(IIuem20PortraitLayer, utils.registered_layers())
