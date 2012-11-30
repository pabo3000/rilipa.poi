"""
Add a group string field to Products.
http://pypi.python.org/pypi/archetypes.schemaextender Chapter: Layer-aware example

"""

from zope.component import adapts
from zope.interface import implements

from Products.Archetypes.public import BooleanWidget
from Products.ATContentTypes.interface import IATDocument
from Products.Archetypes import public as atapi
from Products.Poi.interfaces import ITracker

from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import ISchemaExtender, IOrderableSchemaExtender, IBrowserLayerAwareExtender

# Your add-on browserlayer
from rilipa.poi.interfaces import IPoiExInstalled

class ExtensionStringField(ExtensionField, atapi.StringField):
    """ Added string field """


class PoiTrackerExtender(object):
    """ Include revisit date on all objects.

    An example extended which will create a new field on Dates tab between effective date and expiration date.
    """

    # This extender will apply only to Products.Poi.interfaces.ITracker
    adapts(ITracker)

    # We use both orderable and browser layer aware sensitive properties
    implements(IOrderableSchemaExtender, IBrowserLayerAwareExtender)

    # Don't do schema extending unless our add-on product is installed on Plone site
    layer = IPoiExInstalled

    fields = [
        ExtensionStringField("group",
            widget = atapi.StringWidget(
                label="Group field",
                description="The main group for this Tracker",
            ),
        )
    ]

    def __init__(self, context):
        self.context = context

    def getOrder(self, schematas):
        """ Manipulate the order in which fields appear.

        @return: Dictionary of reordered field lists per schemata.
        """

        return schematas

    def getFields(self):
        """
        @return: List of new fields we contribute to content.
        """
        return self.fields