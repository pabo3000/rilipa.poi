from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import rilipa.poi


RILIPA_POI = PloneWithPackageLayer(
    zcml_package=rilipa.poi,
    zcml_filename='testing.zcml',
    gs_profile_id='rilipa.poi:testing',
    name="RILIPA_POI")

RILIPA_POI_INTEGRATION = IntegrationTesting(
    bases=(RILIPA_POI, ),
    name="RILIPA_POI_INTEGRATION")

RILIPA_POI_FUNCTIONAL = FunctionalTesting(
    bases=(RILIPA_POI, ),
    name="RILIPA_POI_FUNCTIONAL")
