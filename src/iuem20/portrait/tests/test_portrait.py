# -*- coding: utf-8 -*-
from iuem20.portrait.interfaces import Iportrait
from iuem20.portrait.testing import IUEM20_PORTRAIT_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


class portraitIntegrationTest(unittest.TestCase):

    layer = IUEM20_PORTRAIT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='portrait')
        schema = fti.lookupSchema()
        self.assertEqual(Iportrait, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='portrait')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='portrait')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(Iportrait.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type='portrait',
            id='portrait',
        )
        self.assertTrue(Iportrait.providedBy(obj))
