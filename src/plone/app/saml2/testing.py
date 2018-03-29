# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plone.app.saml2


class PloneAppSaml2Layer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plone.app.saml2)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plone.app.saml2:default')


PLONE_APP_SAML2_FIXTURE = PloneAppSaml2Layer()


PLONE_APP_SAML2_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONE_APP_SAML2_FIXTURE,),
    name='PloneAppSaml2Layer:IntegrationTesting',
)


PLONE_APP_SAML2_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONE_APP_SAML2_FIXTURE,),
    name='PloneAppSaml2Layer:FunctionalTesting',
)


PLONE_APP_SAML2_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONE_APP_SAML2_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PloneAppSaml2Layer:AcceptanceTesting',
)
