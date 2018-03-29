# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.saml2.testing import PLONE_APP_SAML2_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that plone.app.saml2 is properly installed."""

    layer = PLONE_APP_SAML2_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plone.app.saml2 is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plone.app.saml2'))

    def test_browserlayer(self):
        """Test that IPloneAppSaml2Layer is registered."""
        from plone.app.saml2.interfaces import (
            IPloneAppSaml2Layer)
        from plone.browserlayer import utils
        self.assertIn(
            IPloneAppSaml2Layer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONE_APP_SAML2_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['plone.app.saml2'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if plone.app.saml2 is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plone.app.saml2'))

    def test_browserlayer_removed(self):
        """Test that IPloneAppSaml2Layer is removed."""
        from plone.app.saml2.interfaces import \
            IPloneAppSaml2Layer
        from plone.browserlayer import utils
        self.assertNotIn(
           IPloneAppSaml2Layer,
           utils.registered_layers())
