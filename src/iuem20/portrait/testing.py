# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import iuem20.portrait


class Iuem20PortraitLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=iuem20.portrait)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'iuem20.portrait:default')


IUEM20_PORTRAIT_FIXTURE = Iuem20PortraitLayer()


IUEM20_PORTRAIT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(IUEM20_PORTRAIT_FIXTURE,),
    name='Iuem20PortraitLayer:IntegrationTesting'
)


IUEM20_PORTRAIT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(IUEM20_PORTRAIT_FIXTURE,),
    name='Iuem20PortraitLayer:FunctionalTesting'
)


IUEM20_PORTRAIT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        IUEM20_PORTRAIT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='Iuem20PortraitLayer:AcceptanceTesting'
)
