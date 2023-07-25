# ./cmslib/dom.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:b3cb8219570db465abb290189831c54c61a08fa9
# Generated 2022-03-18 15:57:03.239893 by PyXB version 1.2.7-DEV using Python 3.10.2.final.0
# Namespace http://xml.homeinfo.de/schema/dscms4

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier(
    "urn:uuid:aba4aa0e-a6cb-11ec-b8a1-7427eaa9df7d"
)

# Version of PyXB used to generate the bindings
_PyXBVersion = "1.2.7-DEV"
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(
    "http://xml.homeinfo.de/schema/dscms4", create_if_missing=True
)
Namespace.configureCategories(["typeBinding", "elementBinding"])


def CreateFromDocument(
    xml_text, fallback_namespace=None, location_base=None, default_namespace=None
):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword fallback_namespace An absent L{pyxb.Namespace} instance
    to use for unqualified names when there is no default namespace in
    scope.  If unspecified or C{None}, the namespace of the module
    containing this function will be used, if it is an absent
    namespace.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.

    @keyword default_namespace An alias for @c fallback_namespace used
    in PyXB 1.1.4 through 1.2.6.  It behaved like a default namespace
    only for absent namespaces.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(
        fallback_namespace=fallback_namespace, location_base=location_base
    )
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance


def CreateFromDOM(node, fallback_namespace=None, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}.
    """
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, fallback_namespace)


# Complex type {http://xml.homeinfo.de/schema/dscms4}Address with content type ELEMENT_ONLY
class Address(pyxb.binding.basis.complexTypeDefinition):
    """
    Eine Adresse.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Address")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/address.xsd", 12, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element street uses Python identifier street
    __street = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "street"),
        "street",
        "__httpxml_homeinfo_deschemadscms4_Address_street",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/address.xsd", 19, 12
        ),
    )

    street = property(
        __street.value,
        __street.set,
        None,
        "\n                        Der Straßenname.\n                    ",
    )

    # Element house_number uses Python identifier house_number
    __house_number = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "house_number"),
        "house_number",
        "__httpxml_homeinfo_deschemadscms4_Address_house_number",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/address.xsd", 26, 12
        ),
    )

    house_number = property(
        __house_number.value,
        __house_number.set,
        None,
        "\n                        Die Hausnummer.\n                    ",
    )

    # Element zip_code uses Python identifier zip_code
    __zip_code = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "zip_code"),
        "zip_code",
        "__httpxml_homeinfo_deschemadscms4_Address_zip_code",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/address.xsd", 33, 12
        ),
    )

    zip_code = property(
        __zip_code.value,
        __zip_code.set,
        None,
        "\n                        Die Postleitzahl (PLZ).\n                    ",
    )

    # Element city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "city"),
        "city",
        "__httpxml_homeinfo_deschemadscms4_Address_city",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/address.xsd", 40, 12
        ),
    )

    city = property(
        __city.value,
        __city.set,
        None,
        "\n                        Der Ortsname.\n                    ",
    )

    _ElementMap.update(
        {
            __street.name(): __street,
            __house_number.name(): __house_number,
            __zip_code.name(): __zip_code,
            __city.name(): __city,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Address = Address
Namespace.addCategoryObject("typeBinding", "Address", Address)


# Complex type {http://xml.homeinfo.de/schema/dscms4}Attachment with content type ELEMENT_ONLY
class Attachment(pyxb.binding.basis.complexTypeDefinition):
    """
    Ein Dateianhang.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Attachment")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/attachments.xsd", 12, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element mimetype uses Python identifier mimetype
    __mimetype = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "mimetype"),
        "mimetype",
        "__httpxml_homeinfo_deschemadscms4_Attachment_mimetype",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/attachments.xsd", 19, 12
        ),
    )

    mimetype = property(
        __mimetype.value,
        __mimetype.set,
        None,
        "\n                        MIME Typ.\n                    ",
    )

    # Element filename uses Python identifier filename
    __filename = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "filename"),
        "filename",
        "__httpxml_homeinfo_deschemadscms4_Attachment_filename",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/attachments.xsd", 26, 12
        ),
    )

    filename = property(
        __filename.value,
        __filename.set,
        None,
        "\n                        Dateiname.\n                    ",
    )

    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "id"),
        "id",
        "__httpxml_homeinfo_deschemadscms4_Attachment_id",
        pyxb.binding.datatypes.positiveInteger,
        required=True,
    )
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/attachments.xsd", 34, 8
    )
    __id._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/attachments.xsd", 34, 8
    )

    id = property(
        __id.value,
        __id.set,
        None,
        "\n                    Datei-ID des hisfs.\n                ",
    )

    # Attribute sha256sum uses Python identifier sha256sum
    __sha256sum = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "sha256sum"),
        "sha256sum",
        "__httpxml_homeinfo_deschemadscms4_Attachment_sha256sum",
        pyxb.binding.datatypes.string,
    )
    __sha256sum._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/attachments.xsd", 41, 8
    )
    __sha256sum._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/attachments.xsd", 41, 8
    )

    sha256sum = property(
        __sha256sum.value,
        __sha256sum.set,
        None,
        "\n                    SHA-256 Prüfsumme.\n                ",
    )

    # Attribute size uses Python identifier size
    __size = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "size"),
        "size",
        "__httpxml_homeinfo_deschemadscms4_Attachment_size",
        pyxb.binding.datatypes.positiveInteger,
    )
    __size._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/attachments.xsd", 48, 8
    )
    __size._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/attachments.xsd", 48, 8
    )

    size = property(
        __size.value,
        __size.set,
        None,
        "\n                    Dateigröße in Bytes.\n                ",
    )

    # Attribute format uses Python identifier format
    __format = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "format"),
        "format",
        "__httpxml_homeinfo_deschemadscms4_Attachment_format",
        pyxb.binding.datatypes.string,
    )
    __format._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/attachments.xsd", 55, 8
    )
    __format._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/attachments.xsd", 55, 8
    )

    format = property(
        __format.value,
        __format.set,
        None,
        "\n                    Darstellungsformat.\n                ",
    )

    # Attribute index uses Python identifier index
    __index = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "index"),
        "index",
        "__httpxml_homeinfo_deschemadscms4_Attachment_index",
        pyxb.binding.datatypes.integer,
    )
    __index._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/attachments.xsd", 62, 8
    )
    __index._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/attachments.xsd", 62, 8
    )

    index = property(
        __index.value,
        __index.set,
        None,
        "\n                    Sortierungs Index.\n                ",
    )

    _ElementMap.update({__mimetype.name(): __mimetype, __filename.name(): __filename})
    _AttributeMap.update(
        {
            __id.name(): __id,
            __sha256sum.name(): __sha256sum,
            __size.name(): __size,
            __format.name(): __format,
            __index.name(): __index,
        }
    )


_module_typeBindings.Attachment = Attachment
Namespace.addCategoryObject("typeBinding", "Attachment", Attachment)


# Complex type {http://xml.homeinfo.de/schema/dscms4}BaseChart with content type ELEMENT_ONLY
class BaseChart(pyxb.binding.basis.complexTypeDefinition):
    """
    Basis Chart.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "BaseChart")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 18, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "title"),
        "title",
        "__httpxml_homeinfo_deschemadscms4_BaseChart_title",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 25, 12
        ),
    )

    title = property(
        __title.value,
        __title.set,
        None,
        "\n                        Der Titel des Charts.\n                    ",
    )

    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "description"),
        "description",
        "__httpxml_homeinfo_deschemadscms4_BaseChart_description",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 32, 12
        ),
    )

    description = property(
        __description.value,
        __description.set,
        None,
        "\n                        Die Beschreibung des Charts.\n                    ",
    )

    # Element duration uses Python identifier duration
    __duration = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "duration"),
        "duration",
        "__httpxml_homeinfo_deschemadscms4_BaseChart_duration",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 39, 12
        ),
    )

    duration = property(
        __duration.value,
        __duration.set,
        None,
        "\n                        Die Anzeigedauer des Charts.\n                    ",
    )

    # Element position uses Python identifier position
    __position = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "position"),
        "position",
        "__httpxml_homeinfo_deschemadscms4_BaseChart_position",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 46, 12
        ),
    )

    position = property(
        __position.value,
        __position.set,
        None,
        "\n                        Die Anzeigedauer des Charts.\n                    ",
    )

    # Element transition uses Python identifier transition
    __transition = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "transition"),
        "transition",
        "__httpxml_homeinfo_deschemadscms4_BaseChart_transition",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 53, 12
        ),
    )

    transition = property(
        __transition.value,
        __transition.set,
        None,
        "\n                        Übergangseffekt.\n                    ",
    )

    # Element created uses Python identifier created
    __created = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "created"),
        "created",
        "__httpxml_homeinfo_deschemadscms4_BaseChart_created",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 60, 12
        ),
    )

    created = property(
        __created.value,
        __created.set,
        None,
        "\n                        Datum der Erstellung.\n                    ",
    )

    # Element schedule uses Python identifier schedule
    __schedule = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "schedule"),
        "schedule",
        "__httpxml_homeinfo_deschemadscms4_BaseChart_schedule",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 67, 12
        ),
    )

    schedule = property(
        __schedule.value,
        __schedule.set,
        None,
        "\n                        Optionaler Zeitplan.\n                    ",
    )

    # Element pin uses Python identifier pin
    __pin = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "pin"),
        "pin",
        "__httpxml_homeinfo_deschemadscms4_BaseChart_pin",
        True,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 74, 12
        ),
    )

    pin = property(
        __pin.value,
        __pin.set,
        None,
        "\n                        Liste von PINs zur Zugriffssteuerung.\n                    ",
    )

    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "id"),
        "id",
        "__httpxml_homeinfo_deschemadscms4_BaseChart_id",
        pyxb.binding.datatypes.positiveInteger,
        required=True,
    )
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 82, 8
    )
    __id._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 82, 8
    )

    id = property(
        __id.value,
        __id.set,
        None,
        "\n                    Die Base Chart ID.\n                ",
    )

    # Attribute uuid uses Python identifier uuid
    __uuid = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "uuid"),
        "uuid",
        "__httpxml_homeinfo_deschemadscms4_BaseChart_uuid",
        pyxb.binding.datatypes.string,
        required=True,
    )
    __uuid._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 89, 8
    )
    __uuid._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 89, 8
    )

    uuid = property(
        __uuid.value,
        __uuid.set,
        None,
        "\n                    Eideutige Entitäts-ID.\n                ",
    )

    # Attribute display_from uses Python identifier display_from
    __display_from = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "display_from"),
        "display_from",
        "__httpxml_homeinfo_deschemadscms4_BaseChart_display_from",
        pyxb.binding.datatypes.dateTime,
    )
    __display_from._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 96, 8
    )
    __display_from._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 96, 8
    )

    display_from = property(
        __display_from.value,
        __display_from.set,
        None,
        "\n                    Anzeigedatum Beginn.\n                ",
    )

    # Attribute display_until uses Python identifier display_until
    __display_until = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "display_until"),
        "display_until",
        "__httpxml_homeinfo_deschemadscms4_BaseChart_display_until",
        pyxb.binding.datatypes.dateTime,
    )
    __display_until._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 103, 8
    )
    __display_until._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 103, 8
    )

    display_until = property(
        __display_until.value,
        __display_until.set,
        None,
        "\n                    Anzeigedatum Ende.\n                ",
    )

    # Attribute trashed uses Python identifier trashed
    __trashed = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "trashed"),
        "trashed",
        "__httpxml_homeinfo_deschemadscms4_BaseChart_trashed",
        pyxb.binding.datatypes.boolean,
        required=True,
    )
    __trashed._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 110, 8
    )
    __trashed._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 110, 8
    )

    trashed = property(
        __trashed.value,
        __trashed.set,
        None,
        "\n                    Ist der Chart gelöscht?\n                ",
    )

    # Attribute log uses Python identifier log
    __log = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "log"),
        "log",
        "__httpxml_homeinfo_deschemadscms4_BaseChart_log",
        pyxb.binding.datatypes.boolean,
        required=True,
    )
    __log._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 117, 8
    )
    __log._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 117, 8
    )

    log = property(
        __log.value,
        __log.set,
        None,
        "\n                    Sollen Änderungen am Chart geloggt werden?\n                ",
    )

    _ElementMap.update(
        {
            __title.name(): __title,
            __description.name(): __description,
            __duration.name(): __duration,
            __position.name(): __position,
            __transition.name(): __transition,
            __created.name(): __created,
            __schedule.name(): __schedule,
            __pin.name(): __pin,
        }
    )
    _AttributeMap.update(
        {
            __id.name(): __id,
            __uuid.name(): __uuid,
            __display_from.name(): __display_from,
            __display_until.name(): __display_until,
            __trashed.name(): __trashed,
            __log.name(): __log,
        }
    )


_module_typeBindings.BaseChart = BaseChart
Namespace.addCategoryObject("typeBinding", "BaseChart", BaseChart)


# Complex type {http://xml.homeinfo.de/schema/dscms4}Chart with content type ELEMENT_ONLY
class Chart(pyxb.binding.basis.complexTypeDefinition):
    """
    Abstrakter Chart.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Chart")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 127, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element base uses Python identifier base
    __base = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "base"),
        "base",
        "__httpxml_homeinfo_deschemadscms4_Chart_base",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 134, 12
        ),
    )

    base = property(
        __base.value,
        __base.set,
        None,
        "\n                        Der zugehörige Basis-Chart.\n                    ",
    )

    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "id"),
        "id",
        "__httpxml_homeinfo_deschemadscms4_Chart_id",
        pyxb.binding.datatypes.positiveInteger,
        required=True,
    )
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 142, 8
    )
    __id._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 142, 8
    )

    id = property(
        __id.value,
        __id.set,
        None,
        "\n                    Die Chart ID.\n                ",
    )

    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "type"),
        "type",
        "__httpxml_homeinfo_deschemadscms4_Chart_type",
        pyxb.binding.datatypes.string,
        required=True,
    )
    __type._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 149, 8
    )
    __type._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 149, 8
    )

    type = property(
        __type.value,
        __type.set,
        None,
        "\n                    Der Charttyp.\n                ",
    )

    _ElementMap.update({__base.name(): __base})
    _AttributeMap.update({__id.name(): __id, __type.name(): __type})


_module_typeBindings.Chart = Chart
Namespace.addCategoryObject("typeBinding", "Chart", Chart)


# Complex type {http://xml.homeinfo.de/schema/dscms4}BriefChart with content type ELEMENT_ONLY
class BriefChart(pyxb.binding.basis.complexTypeDefinition):
    """
    Kurzinformation über einen Chart.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "BriefChart")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 159, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "id"),
        "id",
        "__httpxml_homeinfo_deschemadscms4_BriefChart_id",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 166, 12
        ),
    )

    id = property(
        __id.value,
        __id.set,
        None,
        "\n                        ID des Charts.\n                    ",
    )

    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "type"),
        "type",
        "__httpxml_homeinfo_deschemadscms4_BriefChart_type",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 173, 12
        ),
    )

    type = property(
        __type.value,
        __type.set,
        None,
        "\n                        Der Typ des Charts.\n                    ",
    )

    _ElementMap.update({__id.name(): __id, __type.name(): __type})
    _AttributeMap.update({})


_module_typeBindings.BriefChart = BriefChart
Namespace.addCategoryObject("typeBinding", "BriefChart", BriefChart)


# Complex type {http://xml.homeinfo.de/schema/dscms4}Configuration with content type ELEMENT_ONLY
class Configuration(pyxb.binding.basis.complexTypeDefinition):
    """
    Eine Konfiguration.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Configuration")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 13, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "name"),
        "name",
        "__httpxml_homeinfo_deschemadscms4_Configuration_name",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 20, 12
        ),
    )

    name = property(
        __name.value,
        __name.set,
        None,
        "\n                        Name der Konfiguration.\n                    ",
    )

    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "description"),
        "description",
        "__httpxml_homeinfo_deschemadscms4_Configuration_description",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 27, 12
        ),
    )

    description = property(
        __description.value,
        __description.set,
        None,
        "\n                        Beschreibung der Konfiguration.\n                    ",
    )

    # Element font uses Python identifier font
    __font = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "font"),
        "font",
        "__httpxml_homeinfo_deschemadscms4_Configuration_font",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 34, 12
        ),
    )

    font = property(
        __font.value,
        __font.set,
        None,
        "\n                        Schriftart.\n                    ",
    )

    # Element portrait uses Python identifier portrait
    __portrait = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "portrait"),
        "portrait",
        "__httpxml_homeinfo_deschemadscms4_Configuration_portrait",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 41, 12
        ),
    )

    portrait = property(
        __portrait.value,
        __portrait.set,
        None,
        "\n                        Soll Portrait Darstellung verwendet werden?\n                    ",
    )

    # Element touch uses Python identifier touch
    __touch = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "touch"),
        "touch",
        "__httpxml_homeinfo_deschemadscms4_Configuration_touch",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 48, 12
        ),
    )

    touch = property(
        __touch.value,
        __touch.set,
        None,
        "\n                        Handelt es sich um ein Touch System?\n                    ",
    )

    # Element design uses Python identifier design
    __design = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "design"),
        "design",
        "__httpxml_homeinfo_deschemadscms4_Configuration_design",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 55, 12
        ),
    )

    design = property(
        __design.value,
        __design.set,
        None,
        "\n                        Das verwendete Design.\n                    ",
    )

    # Element effects uses Python identifier effects
    __effects = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "effects"),
        "effects",
        "__httpxml_homeinfo_deschemadscms4_Configuration_effects",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 62, 12
        ),
    )

    effects = property(
        __effects.value,
        __effects.set,
        None,
        "\n                        Sollen Effekte verwendet werden?\n                    ",
    )

    # Element ticker_speed uses Python identifier ticker_speed
    __ticker_speed = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "ticker_speed"),
        "ticker_speed",
        "__httpxml_homeinfo_deschemadscms4_Configuration_ticker_speed",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 69, 12
        ),
    )

    ticker_speed = property(
        __ticker_speed.value,
        __ticker_speed.set,
        None,
        "\n                        Geschwindigkeit des Tickers.\n                    ",
    )

    # Element colors uses Python identifier colors
    __colors = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "colors"),
        "colors",
        "__httpxml_homeinfo_deschemadscms4_Configuration_colors",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 76, 12
        ),
    )

    colors = property(
        __colors.value,
        __colors.set,
        None,
        "\n                        Die verwendeten Farben.\n                    ",
    )

    # Element title_size uses Python identifier title_size
    __title_size = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "title_size"),
        "title_size",
        "__httpxml_homeinfo_deschemadscms4_Configuration_title_size",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 83, 12
        ),
    )

    title_size = property(
        __title_size.value,
        __title_size.set,
        None,
        "\n                        Größe des Titels.\n                    ",
    )

    # Element text_size uses Python identifier text_size
    __text_size = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "text_size"),
        "text_size",
        "__httpxml_homeinfo_deschemadscms4_Configuration_text_size",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 90, 12
        ),
    )

    text_size = property(
        __text_size.value,
        __text_size.set,
        None,
        "\n                        Größe des Texts.\n                    ",
    )

    # Element logo uses Python identifier logo
    __logo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "logo"),
        "logo",
        "__httpxml_homeinfo_deschemadscms4_Configuration_logo",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 97, 12
        ),
    )

    logo = property(
        __logo.value,
        __logo.set,
        None,
        "\n                        Firmenlogo.\n                    ",
    )

    # Element dummy_picture uses Python identifier dummy_picture
    __dummy_picture = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "dummy_picture"),
        "dummy_picture",
        "__httpxml_homeinfo_deschemadscms4_Configuration_dummy_picture",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 104, 12
        ),
    )

    dummy_picture = property(
        __dummy_picture.value,
        __dummy_picture.set,
        None,
        "\n                        Platzhalterbild.\n                    ",
    )

    # Element hide_cursor uses Python identifier hide_cursor
    __hide_cursor = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "hide_cursor"),
        "hide_cursor",
        "__httpxml_homeinfo_deschemadscms4_Configuration_hide_cursor",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 111, 12
        ),
    )

    hide_cursor = property(
        __hide_cursor.value,
        __hide_cursor.set,
        None,
        "\n                        Soll der Cursor ausgeblendet werden?\n                    ",
    )

    # Element rotation uses Python identifier rotation
    __rotation = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "rotation"),
        "rotation",
        "__httpxml_homeinfo_deschemadscms4_Configuration_rotation",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 118, 12
        ),
    )

    rotation = property(
        __rotation.value,
        __rotation.set,
        None,
        "\n                        Rotation in Grad.\n                    ",
    )

    # Element email_form uses Python identifier email_form
    __email_form = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "email_form"),
        "email_form",
        "__httpxml_homeinfo_deschemadscms4_Configuration_email_form",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 125, 12
        ),
    )

    email_form = property(
        __email_form.value,
        __email_form.set,
        None,
        "\n                        Soll ein E-Mail Formular angezeigt werden?\n                    ",
    )

    # Element volume uses Python identifier volume
    __volume = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "volume"),
        "volume",
        "__httpxml_homeinfo_deschemadscms4_Configuration_volume",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 132, 12
        ),
    )

    volume = property(
        __volume.value,
        __volume.set,
        None,
        "\n                        Lautstärke als Faktor von 0-1.\n                    ",
    )

    # Element text_bg_transparent uses Python identifier text_bg_transparent
    __text_bg_transparent = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "text_bg_transparent"),
        "text_bg_transparent",
        "__httpxml_homeinfo_deschemadscms4_Configuration_text_bg_transparent",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 139, 12
        ),
    )

    text_bg_transparent = property(
        __text_bg_transparent.value,
        __text_bg_transparent.set,
        None,
        "\n                        Soll die Hintergrundmaske der Textfelder im HD-Design transparent sein?\n                    ",
    )

    # Element background uses Python identifier background
    __background = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "background"),
        "background",
        "__httpxml_homeinfo_deschemadscms4_Configuration_background",
        True,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 146, 12
        ),
    )

    background = property(
        __background.value,
        __background.set,
        None,
        "\n                        Hintergrundbilder.\n                    ",
    )

    # Element ticker uses Python identifier ticker
    __ticker = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "ticker"),
        "ticker",
        "__httpxml_homeinfo_deschemadscms4_Configuration_ticker",
        True,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 153, 12
        ),
    )

    ticker = property(
        __ticker.value,
        __ticker.set,
        None,
        "\n                        Ticker.\n                    ",
    )

    # Element backlight uses Python identifier backlight
    __backlight = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "backlight"),
        "backlight",
        "__httpxml_homeinfo_deschemadscms4_Configuration_backlight",
        True,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 160, 12
        ),
    )

    backlight = property(
        __backlight.value,
        __backlight.set,
        None,
        "\n                        Hintergrundbeleuchtung.\n                    ",
    )

    _ElementMap.update(
        {
            __name.name(): __name,
            __description.name(): __description,
            __font.name(): __font,
            __portrait.name(): __portrait,
            __touch.name(): __touch,
            __design.name(): __design,
            __effects.name(): __effects,
            __ticker_speed.name(): __ticker_speed,
            __colors.name(): __colors,
            __title_size.name(): __title_size,
            __text_size.name(): __text_size,
            __logo.name(): __logo,
            __dummy_picture.name(): __dummy_picture,
            __hide_cursor.name(): __hide_cursor,
            __rotation.name(): __rotation,
            __email_form.name(): __email_form,
            __volume.name(): __volume,
            __text_bg_transparent.name(): __text_bg_transparent,
            __background.name(): __background,
            __ticker.name(): __ticker,
            __backlight.name(): __backlight,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Configuration = Configuration
Namespace.addCategoryObject("typeBinding", "Configuration", Configuration)


# Complex type {http://xml.homeinfo.de/schema/dscms4}Colors with content type ELEMENT_ONLY
class Colors(pyxb.binding.basis.complexTypeDefinition):
    """
    Farben der Konfiguration.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Colors")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 171, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element header uses Python identifier header
    __header = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "header"),
        "header",
        "__httpxml_homeinfo_deschemadscms4_Colors_header",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 178, 12
        ),
    )

    header = property(
        __header.value,
        __header.set,
        None,
        "\n                        Farbe der Kopfzeile.\n                    ",
    )

    # Element header_background uses Python identifier header_background
    __header_background = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "header_background"),
        "header_background",
        "__httpxml_homeinfo_deschemadscms4_Colors_header_background",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 185, 12
        ),
    )

    header_background = property(
        __header_background.value,
        __header_background.set,
        None,
        "\n                        Hintergrundfarbe der Kopfzeile.\n                    ",
    )

    # Element background_left uses Python identifier background_left
    __background_left = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "background_left"),
        "background_left",
        "__httpxml_homeinfo_deschemadscms4_Colors_background_left",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 192, 12
        ),
    )

    background_left = property(
        __background_left.value,
        __background_left.set,
        None,
        "\n                        Hintergrundfarbe links.\n                    ",
    )

    # Element background_right uses Python identifier background_right
    __background_right = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "background_right"),
        "background_right",
        "__httpxml_homeinfo_deschemadscms4_Colors_background_right",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 199, 12
        ),
    )

    background_right = property(
        __background_right.value,
        __background_right.set,
        None,
        "\n                        Hintergrundfarbe rechts.\n                    ",
    )

    # Element ticker uses Python identifier ticker
    __ticker = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "ticker"),
        "ticker",
        "__httpxml_homeinfo_deschemadscms4_Colors_ticker",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 206, 12
        ),
    )

    ticker = property(
        __ticker.value,
        __ticker.set,
        None,
        "\n                        Farbe des Tickers.\n                    ",
    )

    # Element ticker_background uses Python identifier ticker_background
    __ticker_background = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "ticker_background"),
        "ticker_background",
        "__httpxml_homeinfo_deschemadscms4_Colors_ticker_background",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 213, 12
        ),
    )

    ticker_background = property(
        __ticker_background.value,
        __ticker_background.set,
        None,
        "\n                        Hintergrundfarbe des Tickers.\n                    ",
    )

    # Element clock uses Python identifier clock
    __clock = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "clock"),
        "clock",
        "__httpxml_homeinfo_deschemadscms4_Colors_clock",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 220, 12
        ),
    )

    clock = property(
        __clock.value,
        __clock.set,
        None,
        "\n                        Farbe der Uhr.\n                    ",
    )

    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "title"),
        "title",
        "__httpxml_homeinfo_deschemadscms4_Colors_title",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 227, 12
        ),
    )

    title = property(
        __title.value,
        __title.set,
        None,
        "\n                        Farbe des Titels.\n                    ",
    )

    # Element text uses Python identifier text
    __text = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "text"),
        "text",
        "__httpxml_homeinfo_deschemadscms4_Colors_text",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 234, 12
        ),
    )

    text = property(
        __text.value,
        __text.set,
        None,
        "\n                        Textfarbe.\n                    ",
    )

    # Element text_background uses Python identifier text_background
    __text_background = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "text_background"),
        "text_background",
        "__httpxml_homeinfo_deschemadscms4_Colors_text_background",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 241, 12
        ),
    )

    text_background = property(
        __text_background.value,
        __text_background.set,
        None,
        "\n                        Hintergrundfarbe des Texts.\n                    ",
    )

    _ElementMap.update(
        {
            __header.name(): __header,
            __header_background.name(): __header_background,
            __background_left.name(): __background_left,
            __background_right.name(): __background_right,
            __ticker.name(): __ticker,
            __ticker_background.name(): __ticker_background,
            __clock.name(): __clock,
            __title.name(): __title,
            __text.name(): __text,
            __text_background.name(): __text_background,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Colors = Colors
Namespace.addCategoryObject("typeBinding", "Colors", Colors)


# Complex type {http://xml.homeinfo.de/schema/dscms4}Ticker with content type ELEMENT_ONLY
class Ticker(pyxb.binding.basis.complexTypeDefinition):
    """
    Ein Ticker.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Ticker")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 252, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "type"),
        "type",
        "__httpxml_homeinfo_deschemadscms4_Ticker_type",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 259, 12
        ),
    )

    type = property(
        __type.value,
        __type.set,
        None,
        "\n                        Typ des Tickers.\n                    ",
    )

    # Element content uses Python identifier content_
    __content = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "content"),
        "content_",
        "__httpxml_homeinfo_deschemadscms4_Ticker_content",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 266, 12
        ),
    )

    content_ = property(
        __content.value,
        __content.set,
        None,
        "\n                        Inhalt des Tickers (Text / URL).\n                    ",
    )

    _ElementMap.update({__type.name(): __type, __content.name(): __content})
    _AttributeMap.update({})


_module_typeBindings.Ticker = Ticker
Namespace.addCategoryObject("typeBinding", "Ticker", Ticker)


# Complex type {http://xml.homeinfo.de/schema/dscms4}Backlight with content type ELEMENT_ONLY
class Backlight(pyxb.binding.basis.complexTypeDefinition):
    """
    Einstellung zur Hintergrundbeleuchtung.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Backlight")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 277, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element time uses Python identifier time
    __time = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "time"),
        "time",
        "__httpxml_homeinfo_deschemadscms4_Backlight_time",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 284, 12
        ),
    )

    time = property(
        __time.value,
        __time.set,
        None,
        "\n                        Zeitstempel.\n                    ",
    )

    # Element brightness uses Python identifier brightness
    __brightness = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "brightness"),
        "brightness",
        "__httpxml_homeinfo_deschemadscms4_Backlight_brightness",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 291, 12
        ),
    )

    brightness = property(
        __brightness.value,
        __brightness.set,
        None,
        "\n                        Helligkeit in Prozent.\n                    ",
    )

    _ElementMap.update({__time.name(): __time, __brightness.name(): __brightness})
    _AttributeMap.update({})


_module_typeBindings.Backlight = Backlight
Namespace.addCategoryObject("typeBinding", "Backlight", Backlight)


# Complex type {http://xml.homeinfo.de/schema/dscms4}Deployment with content type ELEMENT_ONLY
class Deployment(pyxb.binding.basis.complexTypeDefinition):
    """
    Ein Standort.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Deployment")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/deployment.xsd", 14, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element address uses Python identifier address
    __address = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "address"),
        "address",
        "__httpxml_homeinfo_deschemadscms4_Deployment_address",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/deployment.xsd", 21, 12
        ),
    )

    address = property(
        __address.value,
        __address.set,
        None,
        "\n                        Die Adresse.\n                    ",
    )

    # Element lpt_address uses Python identifier lpt_address
    __lpt_address = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "lpt_address"),
        "lpt_address",
        "__httpxml_homeinfo_deschemadscms4_Deployment_lpt_address",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/deployment.xsd", 28, 12
        ),
    )

    lpt_address = property(
        __lpt_address.value,
        __lpt_address.set,
        None,
        "\n                        Abweichende Adresse für ÖPNV Daten.\n                    ",
    )

    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "id"),
        "id",
        "__httpxml_homeinfo_deschemadscms4_Deployment_id",
        pyxb.binding.datatypes.positiveInteger,
        required=True,
    )
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/deployment.xsd", 36, 8
    )
    __id._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/deployment.xsd", 36, 8
    )

    id = property(
        __id.value,
        __id.set,
        None,
        "\n                    Die Deployment-ID.\n                ",
    )

    # Attribute customer uses Python identifier customer
    __customer = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "customer"),
        "customer",
        "__httpxml_homeinfo_deschemadscms4_Deployment_customer",
        pyxb.binding.datatypes.positiveInteger,
        required=True,
    )
    __customer._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/deployment.xsd", 43, 8
    )
    __customer._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/deployment.xsd", 43, 8
    )

    customer = property(
        __customer.value,
        __customer.set,
        None,
        "\n                    Die Kundennummer.\n                ",
    )

    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "type"),
        "type",
        "__httpxml_homeinfo_deschemadscms4_Deployment_type",
        pyxb.binding.datatypes.string,
        required=True,
    )
    __type._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/deployment.xsd", 50, 8
    )
    __type._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/deployment.xsd", 50, 8
    )

    type = property(
        __type.value,
        __type.set,
        None,
        "\n                    Der Deployment-Typ.\n                ",
    )

    # Attribute connection uses Python identifier connection
    __connection = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "connection"),
        "connection",
        "__httpxml_homeinfo_deschemadscms4_Deployment_connection",
        pyxb.binding.datatypes.string,
        required=True,
    )
    __connection._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/deployment.xsd", 57, 8
    )
    __connection._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/deployment.xsd", 57, 8
    )

    connection = property(
        __connection.value,
        __connection.set,
        None,
        "\n                    Der Typ der Internetanbindung.\n                ",
    )

    # Attribute testing uses Python identifier testing
    __testing = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "testing"),
        "testing",
        "__httpxml_homeinfo_deschemadscms4_Deployment_testing",
        pyxb.binding.datatypes.boolean,
        required=True,
    )
    __testing._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/deployment.xsd", 64, 8
    )
    __testing._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/deployment.xsd", 64, 8
    )

    testing = property(
        __testing.value,
        __testing.set,
        None,
        "\n                    Flag für Teststellungen.\n                ",
    )

    # Attribute scheduled uses Python identifier scheduled
    __scheduled = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "scheduled"),
        "scheduled",
        "__httpxml_homeinfo_deschemadscms4_Deployment_scheduled",
        pyxb.binding.datatypes.date,
    )
    __scheduled._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/deployment.xsd", 71, 8
    )
    __scheduled._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/deployment.xsd", 71, 8
    )

    scheduled = property(
        __scheduled.value,
        __scheduled.set,
        None,
        "\n                    Das geplante Einbaudatum.\n                ",
    )

    _ElementMap.update(
        {__address.name(): __address, __lpt_address.name(): __lpt_address}
    )
    _AttributeMap.update(
        {
            __id.name(): __id,
            __customer.name(): __customer,
            __type.name(): __type,
            __connection.name(): __connection,
            __testing.name(): __testing,
            __scheduled.name(): __scheduled,
        }
    )


_module_typeBindings.Deployment = Deployment
Namespace.addCategoryObject("typeBinding", "Deployment", Deployment)


# Complex type {http://xml.homeinfo.de/schema/dscms4}Choice with content type SIMPLE
class Choice(pyxb.binding.basis.complexTypeDefinition):
    """
    Auswahloption für Formulare.
    """

    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Choice")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/form.xsd", 12, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string

    # Attribute index uses Python identifier index
    __index = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "index"),
        "index",
        "__httpxml_homeinfo_deschemadscms4_Choice_index",
        pyxb.binding.datatypes.nonNegativeInteger,
    )
    __index._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/form.xsd", 20, 16
    )
    __index._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/form.xsd", 20, 16
    )

    index = property(
        __index.value,
        __index.set,
        None,
        "\n                            Sortierindex.\n                        ",
    )

    _ElementMap.update({})
    _AttributeMap.update({__index.name(): __index})


_module_typeBindings.Choice = Choice
Namespace.addCategoryObject("typeBinding", "Choice", Choice)


# Complex type {http://xml.homeinfo.de/schema/dscms4}MenuItem with content type ELEMENT_ONLY
class MenuItem(pyxb.binding.basis.complexTypeDefinition):
    """
    Menüelemente.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "MenuItem")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 14, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "name"),
        "name",
        "__httpxml_homeinfo_deschemadscms4_MenuItem_name",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 21, 12
        ),
    )

    name = property(
        __name.value,
        __name.set,
        None,
        "\n                        Name des Menüelements.\n                    ",
    )

    # Element icon uses Python identifier icon
    __icon = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "icon"),
        "icon",
        "__httpxml_homeinfo_deschemadscms4_MenuItem_icon",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 28, 12
        ),
    )

    icon = property(
        __icon.value,
        __icon.set,
        None,
        "\n                        Symbol des Menüelements.\n                    ",
    )

    # Element icon_image uses Python identifier icon_image
    __icon_image = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "icon_image"),
        "icon_image",
        "__httpxml_homeinfo_deschemadscms4_MenuItem_icon_image",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 35, 12
        ),
    )

    icon_image = property(
        __icon_image.value,
        __icon_image.set,
        None,
        "\n                        Bildsymbol des Menüelements.\n                    ",
    )

    # Element text_color uses Python identifier text_color
    __text_color = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "text_color"),
        "text_color",
        "__httpxml_homeinfo_deschemadscms4_MenuItem_text_color",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 42, 12
        ),
    )

    text_color = property(
        __text_color.value,
        __text_color.set,
        None,
        "\n                        Schriftfarbe des Menüelements.\n                    ",
    )

    # Element background_color uses Python identifier background_color
    __background_color = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "background_color"),
        "background_color",
        "__httpxml_homeinfo_deschemadscms4_MenuItem_background_color",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 49, 12
        ),
    )

    background_color = property(
        __background_color.value,
        __background_color.set,
        None,
        "\n                        Hintergrundfarbe des Menüelements.\n                    ",
    )

    # Element index uses Python identifier index
    __index = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "index"),
        "index",
        "__httpxml_homeinfo_deschemadscms4_MenuItem_index",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 56, 12
        ),
    )

    index = property(
        __index.value,
        __index.set,
        None,
        "\n                        Position des Menüelements.\n                    ",
    )

    # Element menu_item uses Python identifier menu_item
    __menu_item = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "menu_item"),
        "menu_item",
        "__httpxml_homeinfo_deschemadscms4_MenuItem_menu_item",
        True,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 63, 12
        ),
    )

    menu_item = property(
        __menu_item.value,
        __menu_item.set,
        None,
        "\n                        Untermenüelemente.\n                    ",
    )

    # Element chart uses Python identifier chart
    __chart = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "chart"),
        "chart",
        "__httpxml_homeinfo_deschemadscms4_MenuItem_chart",
        True,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 70, 12
        ),
    )

    chart = property(
        __chart.value,
        __chart.set,
        None,
        "\n                        Charts, welche diesem Menüelement zugeordnet sind.\n                    ",
    )

    _ElementMap.update(
        {
            __name.name(): __name,
            __icon.name(): __icon,
            __icon_image.name(): __icon_image,
            __text_color.name(): __text_color,
            __background_color.name(): __background_color,
            __index.name(): __index,
            __menu_item.name(): __menu_item,
            __chart.name(): __chart,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.MenuItem = MenuItem
Namespace.addCategoryObject("typeBinding", "MenuItem", MenuItem)


# Complex type {http://xml.homeinfo.de/schema/dscms4}PollOption with content type SIMPLE
class PollOption(pyxb.binding.basis.complexTypeDefinition):
    """
    Auswahloption für Umfragen.
    """

    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "PollOption")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/poll.xsd", 12, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string

    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "id"),
        "id",
        "__httpxml_homeinfo_deschemadscms4_PollOption_id",
        pyxb.binding.datatypes.positiveInteger,
        required=True,
    )
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/poll.xsd", 20, 16
    )
    __id._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/poll.xsd", 20, 16
    )

    id = property(
        __id.value,
        __id.set,
        None,
        "\n                            ID des Datenbakeintrags.\n                        ",
    )

    # Attribute votes uses Python identifier votes
    __votes = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "votes"),
        "votes",
        "__httpxml_homeinfo_deschemadscms4_PollOption_votes",
        pyxb.binding.datatypes.nonNegativeInteger,
    )
    __votes._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/poll.xsd", 27, 16
    )
    __votes._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/poll.xsd", 27, 16
    )

    votes = property(
        __votes.value,
        __votes.set,
        None,
        "\n                            Anzahl der Stimmen.\n                        ",
    )

    _ElementMap.update({})
    _AttributeMap.update({__id.name(): __id, __votes.name(): __votes})


_module_typeBindings.PollOption = PollOption
Namespace.addCategoryObject("typeBinding", "PollOption", PollOption)


# Complex type {http://xml.homeinfo.de/schema/dscms4}Presentation with content type ELEMENT_ONLY
class Presentation(pyxb.binding.basis.complexTypeDefinition):
    """
    Hauptobjekt für Präsentationsdaten.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Presentation")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 27, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element deployment uses Python identifier deployment
    __deployment = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "deployment"),
        "deployment",
        "__httpxml_homeinfo_deschemadscms4_Presentation_deployment",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 34, 12
        ),
    )

    deployment = property(
        __deployment.value,
        __deployment.set,
        None,
        "\n                        Der Standort.\n                    ",
    )

    # Element configuration uses Python identifier configuration
    __configuration = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "configuration"),
        "configuration",
        "__httpxml_homeinfo_deschemadscms4_Presentation_configuration",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 41, 12
        ),
    )

    configuration = property(
        __configuration.value,
        __configuration.set,
        None,
        "\n                        Konfigurationen.\n                    ",
    )

    # Element menu_item uses Python identifier menu_item
    __menu_item = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "menu_item"),
        "menu_item",
        "__httpxml_homeinfo_deschemadscms4_Presentation_menu_item",
        True,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 48, 12
        ),
    )

    menu_item = property(
        __menu_item.value,
        __menu_item.set,
        None,
        "\n                        Menüelemente.\n                    ",
    )

    # Element playlist uses Python identifier playlist
    __playlist = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "playlist"),
        "playlist",
        "__httpxml_homeinfo_deschemadscms4_Presentation_playlist",
        True,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 55, 12
        ),
    )

    playlist = property(
        __playlist.value,
        __playlist.set,
        None,
        "\n                        Playlist von Chart-Kurzinformationen in Reihenfolge.\n                    ",
    )

    # Element chart uses Python identifier chart
    __chart = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "chart"),
        "chart",
        "__httpxml_homeinfo_deschemadscms4_Presentation_chart",
        True,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 62, 12
        ),
    )

    chart = property(
        __chart.value,
        __chart.set,
        None,
        "\n                        Vollständige Chart-Informationen.\n                    ",
    )

    # Attribute customer uses Python identifier customer
    __customer = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "customer"),
        "customer",
        "__httpxml_homeinfo_deschemadscms4_Presentation_customer",
        pyxb.binding.datatypes.positiveInteger,
    )
    __customer._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 70, 8
    )
    __customer._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 70, 8
    )

    customer = property(
        __customer.value,
        __customer.set,
        None,
        "\n                    Die Kundennummer.\n                ",
    )

    # Attribute user uses Python identifier user
    __user = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "user"),
        "user",
        "__httpxml_homeinfo_deschemadscms4_Presentation_user",
        pyxb.binding.datatypes.positiveInteger,
    )
    __user._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 77, 8
    )
    __user._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 77, 8
    )

    user = property(
        __user.value,
        __user.set,
        None,
        "\n                    ID eines ComCat Accounts.\n                ",
    )

    # Attribute group uses Python identifier group
    __group = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "group"),
        "group",
        "__httpxml_homeinfo_deschemadscms4_Presentation_group",
        pyxb.binding.datatypes.integer,
    )
    __group._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 84, 8
    )
    __group._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 84, 8
    )

    group = property(
        __group.value,
        __group.set,
        None,
        "\n                    Die ID der entsprechenden Gruppe.\n                ",
    )

    # Attribute file_preview_token uses Python identifier file_preview_token
    __file_preview_token = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "file_preview_token"),
        "file_preview_token",
        "__httpxml_homeinfo_deschemadscms4_Presentation_file_preview_token",
        pyxb.binding.datatypes.string,
    )
    __file_preview_token._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 91, 8
    )
    __file_preview_token._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 91, 8
    )

    file_preview_token = property(
        __file_preview_token.value,
        __file_preview_token.set,
        None,
        "\n                    Temporäres Vorschau Token für Dateianhänge.\n                ",
    )

    _ElementMap.update(
        {
            __deployment.name(): __deployment,
            __configuration.name(): __configuration,
            __menu_item.name(): __menu_item,
            __playlist.name(): __playlist,
            __chart.name(): __chart,
        }
    )
    _AttributeMap.update(
        {
            __customer.name(): __customer,
            __user.name(): __user,
            __group.name(): __group,
            __file_preview_token.name(): __file_preview_token,
        }
    )


_module_typeBindings.Presentation = Presentation
Namespace.addCategoryObject("typeBinding", "Presentation", Presentation)


# Complex type {http://xml.homeinfo.de/schema/dscms4}Filter with content type EMPTY
class Filter(pyxb.binding.basis.complexTypeDefinition):
    """
    Ein Immobilien Filter.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Filter")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 12, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({})
    _AttributeMap.update({})


_module_typeBindings.Filter = Filter
Namespace.addCategoryObject("typeBinding", "Filter", Filter)


# Complex type {http://xml.homeinfo.de/schema/dscms4}RealEstateContact with content type ELEMENT_ONLY
class RealEstateContact(pyxb.binding.basis.complexTypeDefinition):
    """
    Kontaktperson einer Immobilie.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "RealEstateContact")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 79, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "name"),
        "name",
        "__httpxml_homeinfo_deschemadscms4_RealEstateContact_name",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 86, 12
        ),
    )

    name = property(
        __name.value,
        __name.set,
        None,
        '\n                        Der Name der Kontaktperson. Dieser muss mit dem Feld "name" aus OpenImmo übereinstimmen.\n                    ',
    )

    # Element image uses Python identifier image
    __image = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "image"),
        "image",
        "__httpxml_homeinfo_deschemadscms4_RealEstateContact_image",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 93, 12
        ),
    )

    image = property(
        __image.value,
        __image.set,
        None,
        "\n                        Das zugehörige Bild.\n                    ",
    )

    _ElementMap.update({__name.name(): __name, __image.name(): __image})
    _AttributeMap.update({})


_module_typeBindings.RealEstateContact = RealEstateContact
Namespace.addCategoryObject("typeBinding", "RealEstateContact", RealEstateContact)


# Complex type {http://xml.homeinfo.de/schema/dscms4}TimeInterval with content type ELEMENT_ONLY
class TimeInterval(pyxb.binding.basis.complexTypeDefinition):
    """
    Ein Zeitintervall.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "TimeInterval")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 12, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "value"),
        "value_",
        "__httpxml_homeinfo_deschemadscms4_TimeInterval_value",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 19, 12
        ),
    )

    value_ = property(
        __value.value,
        __value.set,
        None,
        "\n                        Wert des Intervalls.\n                    ",
    )

    # Element unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "unit"),
        "unit",
        "__httpxml_homeinfo_deschemadscms4_TimeInterval_unit",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 26, 12
        ),
    )

    unit = property(
        __unit.value,
        __unit.set,
        None,
        "\n                        Zeiteinheit des Intervalls.\n                    ",
    )

    _ElementMap.update({__value.name(): __value, __unit.name(): __unit})
    _AttributeMap.update({})


_module_typeBindings.TimeInterval = TimeInterval
Namespace.addCategoryObject("typeBinding", "TimeInterval", TimeInterval)


# Complex type {http://xml.homeinfo.de/schema/dscms4}Schedule with content type ELEMENT_ONLY
class Schedule(pyxb.binding.basis.complexTypeDefinition):
    """
    Ein Zeitplan.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Schedule")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 37, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "description"),
        "description",
        "__httpxml_homeinfo_deschemadscms4_Schedule_description",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 44, 12
        ),
    )

    description = property(
        __description.value,
        __description.set,
        None,
        "\n                        Eine Beschreibung.\n                    ",
    )

    # Element start uses Python identifier start
    __start = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "start"),
        "start",
        "__httpxml_homeinfo_deschemadscms4_Schedule_start",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 51, 12
        ),
    )

    start = property(
        __start.value,
        __start.set,
        None,
        "\n                        Startzeitpunkt.\n                    ",
    )

    # Element end uses Python identifier end
    __end = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "end"),
        "end",
        "__httpxml_homeinfo_deschemadscms4_Schedule_end",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 58, 12
        ),
    )

    end = property(
        __end.value,
        __end.set,
        None,
        "\n                        Endzeitpunkt.\n                    ",
    )

    # Element duration uses Python identifier duration
    __duration = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "duration"),
        "duration",
        "__httpxml_homeinfo_deschemadscms4_Schedule_duration",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 65, 12
        ),
    )

    duration = property(
        __duration.value,
        __duration.set,
        None,
        "\n                        Anzeigedauer.\n                    ",
    )

    # Element interval uses Python identifier interval
    __interval = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "interval"),
        "interval",
        "__httpxml_homeinfo_deschemadscms4_Schedule_interval",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 72, 12
        ),
    )

    interval = property(
        __interval.value,
        __interval.set,
        None,
        "\n                        Anzeigeintervall.\n                    ",
    )

    _ElementMap.update(
        {
            __description.name(): __description,
            __start.name(): __start,
            __end.name(): __end,
            __duration.name(): __duration,
            __interval.name(): __interval,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Schedule = Schedule
Namespace.addCategoryObject("typeBinding", "Schedule", Schedule)


# Complex type {http://xml.homeinfo.de/schema/dscms4}Blackboard with content type ELEMENT_ONLY
class Blackboard(Chart):
    """
    Schwarzes Brett / Pin Chart.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Blackboard")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 184, 4
    )
    _ElementMap = Chart._ElementMap.copy()
    _AttributeMap = Chart._AttributeMap.copy()
    # Base type is Chart

    # Element base (base) inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Element image uses Python identifier image
    __image = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "image"),
        "image",
        "__httpxml_homeinfo_deschemadscms4_Blackboard_image",
        True,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 193, 20
        ),
    )

    image = property(
        __image.value,
        __image.set,
        None,
        "\n                                Bilder.\n                            ",
    )

    # Attribute id inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Attribute type inherited from {http://xml.homeinfo.de/schema/dscms4}Chart
    _ElementMap.update({__image.name(): __image})
    _AttributeMap.update({})


_module_typeBindings.Blackboard = Blackboard
Namespace.addCategoryObject("typeBinding", "Blackboard", Blackboard)


# Complex type {http://xml.homeinfo.de/schema/dscms4}Cleaning with content type ELEMENT_ONLY
class Cleaning(Chart):
    """
    Reinigungs Chart.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Cleaning")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 206, 4
    )
    _ElementMap = Chart._ElementMap.copy()
    _AttributeMap = Chart._AttributeMap.copy()
    # Base type is Chart

    # Element base (base) inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "title"),
        "title",
        "__httpxml_homeinfo_deschemadscms4_Cleaning_title",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 215, 20
        ),
    )

    title = property(
        __title.value,
        __title.set,
        None,
        "\n                                Überschrift.\n                            ",
    )

    # Element mode uses Python identifier mode
    __mode = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "mode"),
        "mode",
        "__httpxml_homeinfo_deschemadscms4_Cleaning_mode",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 222, 20
        ),
    )

    mode = property(
        __mode.value,
        __mode.set,
        None,
        "\n                                Modus des Charts.\n                            ",
    )

    # Element text uses Python identifier text
    __text = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "text"),
        "text",
        "__httpxml_homeinfo_deschemadscms4_Cleaning_text",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 229, 20
        ),
    )

    text = property(
        __text.value,
        __text.set,
        None,
        "\n                                Textinhalt.\n                            ",
    )

    # Element font_size uses Python identifier font_size
    __font_size = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "font_size"),
        "font_size",
        "__httpxml_homeinfo_deschemadscms4_Cleaning_font_size",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 236, 20
        ),
    )

    font_size = property(
        __font_size.value,
        __font_size.set,
        None,
        "\n                                Schriftgröße.\n                            ",
    )

    # Element text_color uses Python identifier text_color
    __text_color = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "text_color"),
        "text_color",
        "__httpxml_homeinfo_deschemadscms4_Cleaning_text_color",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 243, 20
        ),
    )

    text_color = property(
        __text_color.value,
        __text_color.set,
        None,
        "\n                                Textfarbe.\n                            ",
    )

    # Attribute id inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Attribute type inherited from {http://xml.homeinfo.de/schema/dscms4}Chart
    _ElementMap.update(
        {
            __title.name(): __title,
            __mode.name(): __mode,
            __text.name(): __text,
            __font_size.name(): __font_size,
            __text_color.name(): __text_color,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Cleaning = Cleaning
Namespace.addCategoryObject("typeBinding", "Cleaning", Cleaning)


# Complex type {http://xml.homeinfo.de/schema/dscms4}Form with content type ELEMENT_ONLY
class Form(Chart):
    """
    Formular Chart.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Form")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 256, 4
    )
    _ElementMap = Chart._ElementMap.copy()
    _AttributeMap = Chart._AttributeMap.copy()
    # Base type is Chart

    # Element base (base) inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Element mode uses Python identifier mode
    __mode = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "mode"),
        "mode",
        "__httpxml_homeinfo_deschemadscms4_Form_mode",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 265, 20
        ),
    )

    mode = property(
        __mode.value,
        __mode.set,
        None,
        "\n                                Typ (Modus) des Formulars.\n                            ",
    )

    # Element text uses Python identifier text
    __text = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "text"),
        "text",
        "__httpxml_homeinfo_deschemadscms4_Form_text",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 272, 20
        ),
    )

    text = property(
        __text.value,
        __text.set,
        None,
        "\n                                Optionaler Text.\n                            ",
    )

    # Element choice uses Python identifier choice
    __choice = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "choice"),
        "choice",
        "__httpxml_homeinfo_deschemadscms4_Form_choice",
        True,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 279, 20
        ),
    )

    choice = property(
        __choice.value,
        __choice.set,
        None,
        "\n                                Auswahloptionen.\n                            ",
    )

    # Attribute id inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Attribute type inherited from {http://xml.homeinfo.de/schema/dscms4}Chart
    _ElementMap.update(
        {__mode.name(): __mode, __text.name(): __text, __choice.name(): __choice}
    )
    _AttributeMap.update({})


_module_typeBindings.Form = Form
Namespace.addCategoryObject("typeBinding", "Form", Form)


# Complex type {http://xml.homeinfo.de/schema/dscms4}GarbageCollection with content type ELEMENT_ONLY
class GarbageCollection(Chart):
    """
    Müllabfuhr Chart.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "GarbageCollection")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 292, 4
    )
    _ElementMap = Chart._ElementMap.copy()
    _AttributeMap = Chart._AttributeMap.copy()
    # Base type is Chart

    # Element base (base) inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Attribute id inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Attribute type inherited from {http://xml.homeinfo.de/schema/dscms4}Chart
    _ElementMap.update({})
    _AttributeMap.update({})


_module_typeBindings.GarbageCollection = GarbageCollection
Namespace.addCategoryObject("typeBinding", "GarbageCollection", GarbageCollection)


# Complex type {http://xml.homeinfo.de/schema/dscms4}GuessPicture with content type ELEMENT_ONLY
class GuessPicture(Chart):
    """
    Bilderraten Chart.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "GuessPicture")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 304, 4
    )
    _ElementMap = Chart._ElementMap.copy()
    _AttributeMap = Chart._AttributeMap.copy()
    # Base type is Chart

    # Element base (base) inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Attribute id inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Attribute type inherited from {http://xml.homeinfo.de/schema/dscms4}Chart
    _ElementMap.update({})
    _AttributeMap.update({})


_module_typeBindings.GuessPicture = GuessPicture
Namespace.addCategoryObject("typeBinding", "GuessPicture", GuessPicture)


# Complex type {http://xml.homeinfo.de/schema/dscms4}ImageText with content type ELEMENT_ONLY
class ImageText(Chart):
    """
    Bild / Text Chart.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "ImageText")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 316, 4
    )
    _ElementMap = Chart._ElementMap.copy()
    _AttributeMap = Chart._AttributeMap.copy()
    # Base type is Chart

    # Element base (base) inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "title"),
        "title",
        "__httpxml_homeinfo_deschemadscms4_ImageText_title",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 325, 20
        ),
    )

    title = property(
        __title.value,
        __title.set,
        None,
        "\n                                Titel des Charts.\n                            ",
    )

    # Element font_size uses Python identifier font_size
    __font_size = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "font_size"),
        "font_size",
        "__httpxml_homeinfo_deschemadscms4_ImageText_font_size",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 332, 20
        ),
    )

    font_size = property(
        __font_size.value,
        __font_size.set,
        None,
        "\n                                Schriftgröße.\n                            ",
    )

    # Element title_color uses Python identifier title_color
    __title_color = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "title_color"),
        "title_color",
        "__httpxml_homeinfo_deschemadscms4_ImageText_title_color",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 339, 20
        ),
    )

    title_color = property(
        __title_color.value,
        __title_color.set,
        None,
        "\n                                Titelfarbe.\n                            ",
    )

    # Element ken_burns uses Python identifier ken_burns
    __ken_burns = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "ken_burns"),
        "ken_burns",
        "__httpxml_homeinfo_deschemadscms4_ImageText_ken_burns",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 346, 20
        ),
    )

    ken_burns = property(
        __ken_burns.value,
        __ken_burns.set,
        None,
        "\n                                Ken Burns Effekt.\n                            ",
    )

    # Element random_image uses Python identifier random_image
    __random_image = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "random_image"),
        "random_image",
        "__httpxml_homeinfo_deschemadscms4_ImageText_random_image",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 353, 20
        ),
    )

    random_image = property(
        __random_image.value,
        __random_image.set,
        None,
        "\n                                Flag zur Anzeige von zufälligen Bildern.\n                            ",
    )

    # Element image uses Python identifier image
    __image = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "image"),
        "image",
        "__httpxml_homeinfo_deschemadscms4_ImageText_image",
        True,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 360, 20
        ),
    )

    image = property(
        __image.value,
        __image.set,
        None,
        "\n                                Bilder.\n                            ",
    )

    # Element text uses Python identifier text
    __text = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "text"),
        "text",
        "__httpxml_homeinfo_deschemadscms4_ImageText_text",
        True,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 367, 20
        ),
    )

    text = property(
        __text.value,
        __text.set,
        None,
        "\n                                Texte.\n                            ",
    )

    # Attribute id inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Attribute type inherited from {http://xml.homeinfo.de/schema/dscms4}Chart
    _ElementMap.update(
        {
            __title.name(): __title,
            __font_size.name(): __font_size,
            __title_color.name(): __title_color,
            __ken_burns.name(): __ken_burns,
            __random_image.name(): __random_image,
            __image.name(): __image,
            __text.name(): __text,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.ImageText = ImageText
Namespace.addCategoryObject("typeBinding", "ImageText", ImageText)


# Complex type {http://xml.homeinfo.de/schema/dscms4}News with content type ELEMENT_ONLY
class News(Chart):
    """
    Nachrichten Chart.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "News")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 380, 4
    )
    _ElementMap = Chart._ElementMap.copy()
    _AttributeMap = Chart._AttributeMap.copy()
    # Base type is Chart

    # Element base (base) inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Element font_size_title uses Python identifier font_size_title
    __font_size_title = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "font_size_title"),
        "font_size_title",
        "__httpxml_homeinfo_deschemadscms4_News_font_size_title",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 389, 20
        ),
    )

    font_size_title = property(
        __font_size_title.value,
        __font_size_title.set,
        None,
        "\n                                Schriftgröße des Titles.\n                            ",
    )

    # Element title_color uses Python identifier title_color
    __title_color = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "title_color"),
        "title_color",
        "__httpxml_homeinfo_deschemadscms4_News_title_color",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 396, 20
        ),
    )

    title_color = property(
        __title_color.value,
        __title_color.set,
        None,
        "\n                                Titelfarbe.\n                            ",
    )

    # Element font_size_text uses Python identifier font_size_text
    __font_size_text = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "font_size_text"),
        "font_size_text",
        "__httpxml_homeinfo_deschemadscms4_News_font_size_text",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 403, 20
        ),
    )

    font_size_text = property(
        __font_size_text.value,
        __font_size_text.set,
        None,
        "\n                                Schriftgröße des Texts.\n                            ",
    )

    # Element text_color uses Python identifier text_color
    __text_color = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "text_color"),
        "text_color",
        "__httpxml_homeinfo_deschemadscms4_News_text_color",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 410, 20
        ),
    )

    text_color = property(
        __text_color.value,
        __text_color.set,
        None,
        "\n                                Textfarbe.\n                            ",
    )

    # Element ken_burns uses Python identifier ken_burns
    __ken_burns = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "ken_burns"),
        "ken_burns",
        "__httpxml_homeinfo_deschemadscms4_News_ken_burns",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 417, 20
        ),
    )

    ken_burns = property(
        __ken_burns.value,
        __ken_burns.set,
        None,
        "\n                                Ken Burns Effekt.\n                            ",
    )

    # Element provider uses Python identifier provider
    __provider = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "provider"),
        "provider",
        "__httpxml_homeinfo_deschemadscms4_News_provider",
        True,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 424, 20
        ),
    )

    provider = property(
        __provider.value,
        __provider.set,
        None,
        "\n                                Provider für diesen news chart.\n                            ",
    )

    # Attribute id inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Attribute type inherited from {http://xml.homeinfo.de/schema/dscms4}Chart
    _ElementMap.update(
        {
            __font_size_title.name(): __font_size_title,
            __title_color.name(): __title_color,
            __font_size_text.name(): __font_size_text,
            __text_color.name(): __text_color,
            __ken_burns.name(): __ken_burns,
            __provider.name(): __provider,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.News = News
Namespace.addCategoryObject("typeBinding", "News", News)


# Complex type {http://xml.homeinfo.de/schema/dscms4}Poll with content type ELEMENT_ONLY
class Poll(Chart):
    """
    Umfrage Chart.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Poll")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 437, 4
    )
    _ElementMap = Chart._ElementMap.copy()
    _AttributeMap = Chart._AttributeMap.copy()
    # Base type is Chart

    # Element base (base) inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Element text uses Python identifier text
    __text = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "text"),
        "text",
        "__httpxml_homeinfo_deschemadscms4_Poll_text",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 446, 20
        ),
    )

    text = property(
        __text.value,
        __text.set,
        None,
        "\n                                Fragetext.\n                            ",
    )

    # Element mode uses Python identifier mode
    __mode = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "mode"),
        "mode",
        "__httpxml_homeinfo_deschemadscms4_Poll_mode",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 453, 20
        ),
    )

    mode = property(
        __mode.value,
        __mode.set,
        None,
        "\n                                Umfragemodus (Single- oder Multiple-Choice).\n                            ",
    )

    # Element option uses Python identifier option
    __option = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "option"),
        "option",
        "__httpxml_homeinfo_deschemadscms4_Poll_option",
        True,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 460, 20
        ),
    )

    option = property(
        __option.value,
        __option.set,
        None,
        "\n                                Antwortoptionen.\n                            ",
    )

    # Attribute id inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Attribute type inherited from {http://xml.homeinfo.de/schema/dscms4}Chart
    _ElementMap.update(
        {__text.name(): __text, __mode.name(): __mode, __option.name(): __option}
    )
    _AttributeMap.update({})


_module_typeBindings.Poll = Poll
Namespace.addCategoryObject("typeBinding", "Poll", Poll)


# Complex type {http://xml.homeinfo.de/schema/dscms4}PublicTransport with content type ELEMENT_ONLY
class PublicTransport(Chart):
    """
    ÖPNV Chart.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "PublicTransport")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 473, 4
    )
    _ElementMap = Chart._ElementMap.copy()
    _AttributeMap = Chart._AttributeMap.copy()
    # Base type is Chart

    # Element base (base) inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Attribute id inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Attribute type inherited from {http://xml.homeinfo.de/schema/dscms4}Chart
    _ElementMap.update({})
    _AttributeMap.update({})


_module_typeBindings.PublicTransport = PublicTransport
Namespace.addCategoryObject("typeBinding", "PublicTransport", PublicTransport)


# Complex type {http://xml.homeinfo.de/schema/dscms4}Quotes with content type ELEMENT_ONLY
class Quotes(Chart):
    """
    Zitate Chart.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Quotes")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 485, 4
    )
    _ElementMap = Chart._ElementMap.copy()
    _AttributeMap = Chart._AttributeMap.copy()
    # Base type is Chart

    # Element base (base) inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Element font_color uses Python identifier font_color
    __font_color = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "font_color"),
        "font_color",
        "__httpxml_homeinfo_deschemadscms4_Quotes_font_color",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 494, 20
        ),
    )

    font_color = property(
        __font_color.value,
        __font_color.set,
        None,
        "\n                                Schriftfarbe.\n                            ",
    )

    # Element background_color uses Python identifier background_color
    __background_color = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "background_color"),
        "background_color",
        "__httpxml_homeinfo_deschemadscms4_Quotes_background_color",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 501, 20
        ),
    )

    background_color = property(
        __background_color.value,
        __background_color.set,
        None,
        "\n                                Hintergrundfarbe.\n                            ",
    )

    # Element font_size_quote uses Python identifier font_size_quote
    __font_size_quote = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "font_size_quote"),
        "font_size_quote",
        "__httpxml_homeinfo_deschemadscms4_Quotes_font_size_quote",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 508, 20
        ),
    )

    font_size_quote = property(
        __font_size_quote.value,
        __font_size_quote.set,
        None,
        "\n                                Textfarbe des Zitats.\n                            ",
    )

    # Element font_size_author uses Python identifier font_size_author
    __font_size_author = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "font_size_author"),
        "font_size_author",
        "__httpxml_homeinfo_deschemadscms4_Quotes_font_size_author",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 515, 20
        ),
    )

    font_size_author = property(
        __font_size_author.value,
        __font_size_author.set,
        None,
        "\n                                Textfarbe des Autors.\n                            ",
    )

    # Attribute id inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Attribute type inherited from {http://xml.homeinfo.de/schema/dscms4}Chart
    _ElementMap.update(
        {
            __font_color.name(): __font_color,
            __background_color.name(): __background_color,
            __font_size_quote.name(): __font_size_quote,
            __font_size_author.name(): __font_size_author,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Quotes = Quotes
Namespace.addCategoryObject("typeBinding", "Quotes", Quotes)


# Complex type {http://xml.homeinfo.de/schema/dscms4}RealEstates with content type ELEMENT_ONLY
class RealEstates(Chart):
    """
    Immobilien Chart.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "RealEstates")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 528, 4
    )
    _ElementMap = Chart._ElementMap.copy()
    _AttributeMap = Chart._AttributeMap.copy()
    # Base type is Chart

    # Element base (base) inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Element display_format uses Python identifier display_format
    __display_format = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "display_format"),
        "display_format",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_display_format",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 537, 20
        ),
    )

    display_format = property(
        __display_format.value,
        __display_format.set,
        None,
        "\n                                Anzeigeformat.\n                            ",
    )

    # Element ken_burns uses Python identifier ken_burns
    __ken_burns = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "ken_burns"),
        "ken_burns",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_ken_burns",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 544, 20
        ),
    )

    ken_burns = property(
        __ken_burns.value,
        __ken_burns.set,
        None,
        "\n                                Ken Burns Effekt.\n                            ",
    )

    # Element scaling uses Python identifier scaling
    __scaling = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "scaling"),
        "scaling",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_scaling",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 551, 20
        ),
    )

    scaling = property(
        __scaling.value,
        __scaling.set,
        None,
        "\n                                Soll die Application skalieren?\n                            ",
    )

    # Element slideshow uses Python identifier slideshow
    __slideshow = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "slideshow"),
        "slideshow",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_slideshow",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 558, 20
        ),
    )

    slideshow = property(
        __slideshow.value,
        __slideshow.set,
        None,
        "\n                                Soll die Application eine Slideshow anzeigen?\n                            ",
    )

    # Element qr_codes uses Python identifier qr_codes
    __qr_codes = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "qr_codes"),
        "qr_codes",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_qr_codes",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 565, 20
        ),
    )

    qr_codes = property(
        __qr_codes.value,
        __qr_codes.set,
        None,
        "\n                                Sollen QR Codes angezeigt werden?\n                            ",
    )

    # Element show_contact uses Python identifier show_contact
    __show_contact = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "show_contact"),
        "show_contact",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_show_contact",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 572, 20
        ),
    )

    show_contact = property(
        __show_contact.value,
        __show_contact.set,
        None,
        "\n                                Sollen Kontaktpersonen angezeigt werden?\n                            ",
    )

    # Element contact_picture uses Python identifier contact_picture
    __contact_picture = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "contact_picture"),
        "contact_picture",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_contact_picture",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 579, 20
        ),
    )

    contact_picture = property(
        __contact_picture.value,
        __contact_picture.set,
        None,
        "\n                                Sollen Bilder von Kontaktpersonen angezeigt werden?\n                            ",
    )

    # Element font_size uses Python identifier font_size
    __font_size = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "font_size"),
        "font_size",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_font_size",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 586, 20
        ),
    )

    font_size = property(
        __font_size.value,
        __font_size.set,
        None,
        "\n                                Schriftgröße.\n                            ",
    )

    # Element font_color uses Python identifier font_color
    __font_color = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "font_color"),
        "font_color",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_font_color",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 593, 20
        ),
    )

    font_color = property(
        __font_color.value,
        __font_color.set,
        None,
        "\n                                Schriftfarbe.\n                            ",
    )

    # Element data uses Python identifier data
    __data = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "data"),
        "data",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_data",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 601, 20
        ),
    )

    data = property(
        __data.value,
        __data.set,
        None,
        "\n                                Schriftfarbe.\n                            ",
    )

    # Element background_data uses Python identifier background_data
    __background_data = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "background_data"),
        "background_data",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_background_data",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 608, 20
        ),
    )

    background_data = property(
        __background_data.value,
        __background_data.set,
        None,
        "\n                                Farbe Hintergrund Daten.\n                            ",
    )

    # Element values uses Python identifier values
    __values = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "values"),
        "values",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_values",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 615, 20
        ),
    )

    values = property(
        __values.value,
        __values.set,
        None,
        "\n                                Farbe Werte.\n                            ",
    )

    # Element background_values uses Python identifier background_values
    __background_values = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "background_values"),
        "background_values",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_background_values",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 622, 20
        ),
    )

    background_values = property(
        __background_values.value,
        __background_values.set,
        None,
        "\n                                Farbe Hintergrund Werte.\n                            ",
    )

    # Element amenities_background_even uses Python identifier amenities_background_even
    __amenities_background_even = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "amenities_background_even"),
        "amenities_background_even",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_amenities_background_even",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 629, 20
        ),
    )

    amenities_background_even = property(
        __amenities_background_even.value,
        __amenities_background_even.set,
        None,
        "\n                                Farbe Ausstattungen Hintergrund gerade.\n                            ",
    )

    # Element amenities_text_even uses Python identifier amenities_text_even
    __amenities_text_even = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "amenities_text_even"),
        "amenities_text_even",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_amenities_text_even",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 636, 20
        ),
    )

    amenities_text_even = property(
        __amenities_text_even.value,
        __amenities_text_even.set,
        None,
        "\n                                Farbe Ausstattungen Text gerade.\n                            ",
    )

    # Element amenities_background_uneven uses Python identifier amenities_background_uneven
    __amenities_background_uneven = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "amenities_background_uneven"),
        "amenities_background_uneven",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_amenities_background_uneven",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 643, 20
        ),
    )

    amenities_background_uneven = property(
        __amenities_background_uneven.value,
        __amenities_background_uneven.set,
        None,
        "\n                                Farbe Ausstattungen Hintergrund ungerade.\n                            ",
    )

    # Element amenities_text_uneven uses Python identifier amenities_text_uneven
    __amenities_text_uneven = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "amenities_text_uneven"),
        "amenities_text_uneven",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_amenities_text_uneven",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 650, 20
        ),
    )

    amenities_text_uneven = property(
        __amenities_text_uneven.value,
        __amenities_text_uneven.set,
        None,
        "\n                                Farbe Ausstattungen Text ungerade.\n                            ",
    )

    # Element amenities uses Python identifier amenities
    __amenities = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "amenities"),
        "amenities",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_amenities",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 658, 20
        ),
    )

    amenities = property(__amenities.value, __amenities.set, None, None)

    # Element construction uses Python identifier construction
    __construction = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "construction"),
        "construction",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_construction",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 659, 20
        ),
    )

    construction = property(__construction.value, __construction.set, None, None)

    # Element courtage uses Python identifier courtage
    __courtage = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "courtage"),
        "courtage",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_courtage",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 660, 20
        ),
    )

    courtage = property(__courtage.value, __courtage.set, None, None)

    # Element floor uses Python identifier floor
    __floor = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "floor"),
        "floor",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_floor",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 661, 20
        ),
    )

    floor = property(__floor.value, __floor.set, None, None)

    # Element area uses Python identifier area
    __area = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "area"),
        "area",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_area",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 662, 20
        ),
    )

    area = property(__area.value, __area.set, None, None)

    # Element free_from uses Python identifier free_from
    __free_from = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "free_from"),
        "free_from",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_free_from",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 663, 20
        ),
    )

    free_from = property(__free_from.value, __free_from.set, None, None)

    # Element coop_share uses Python identifier coop_share
    __coop_share = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "coop_share"),
        "coop_share",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_coop_share",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 664, 20
        ),
    )

    coop_share = property(__coop_share.value, __coop_share.set, None, None)

    # Element total_area uses Python identifier total_area
    __total_area = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "total_area"),
        "total_area",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_total_area",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 665, 20
        ),
    )

    total_area = property(__total_area.value, __total_area.set, None, None)

    # Element plot_area uses Python identifier plot_area
    __plot_area = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "plot_area"),
        "plot_area",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_plot_area",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 666, 20
        ),
    )

    plot_area = property(__plot_area.value, __plot_area.set, None, None)

    # Element cold_rent uses Python identifier cold_rent
    __cold_rent = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "cold_rent"),
        "cold_rent",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_cold_rent",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 667, 20
        ),
    )

    cold_rent = property(__cold_rent.value, __cold_rent.set, None, None)

    # Element purchase_price uses Python identifier purchase_price
    __purchase_price = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "purchase_price"),
        "purchase_price",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_purchase_price",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 668, 20
        ),
    )

    purchase_price = property(__purchase_price.value, __purchase_price.set, None, None)

    # Element security_deposit uses Python identifier security_deposit
    __security_deposit = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "security_deposit"),
        "security_deposit",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_security_deposit",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 669, 20
        ),
    )

    security_deposit = property(
        __security_deposit.value, __security_deposit.set, None, None
    )

    # Element service_charge uses Python identifier service_charge
    __service_charge = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "service_charge"),
        "service_charge",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_service_charge",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 670, 20
        ),
    )

    service_charge = property(__service_charge.value, __service_charge.set, None, None)

    # Element object_id uses Python identifier object_id
    __object_id = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "object_id"),
        "object_id",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_object_id",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 671, 20
        ),
    )

    object_id = property(__object_id.value, __object_id.set, None, None)

    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "description"),
        "description",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_description",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 672, 20
        ),
    )

    description = property(__description.value, __description.set, None, None)

    # Element warm_rent uses Python identifier warm_rent
    __warm_rent = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "warm_rent"),
        "warm_rent",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_warm_rent",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 673, 20
        ),
    )

    warm_rent = property(__warm_rent.value, __warm_rent.set, None, None)

    # Element rooms uses Python identifier rooms
    __rooms = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "rooms"),
        "rooms",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_rooms",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 674, 20
        ),
    )

    rooms = property(__rooms.value, __rooms.set, None, None)

    # Element lift uses Python identifier lift
    __lift = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "lift"),
        "lift",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_lift",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 676, 20
        ),
    )

    lift = property(__lift.value, __lift.set, None, None)

    # Element bathtub uses Python identifier bathtub
    __bathtub = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "bathtub"),
        "bathtub",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_bathtub",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 677, 20
        ),
    )

    bathtub = property(__bathtub.value, __bathtub.set, None, None)

    # Element balcony uses Python identifier balcony
    __balcony = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "balcony"),
        "balcony",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_balcony",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 678, 20
        ),
    )

    balcony = property(__balcony.value, __balcony.set, None, None)

    # Element accessibility uses Python identifier accessibility
    __accessibility = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "accessibility"),
        "accessibility",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_accessibility",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 679, 20
        ),
    )

    accessibility = property(__accessibility.value, __accessibility.set, None, None)

    # Element assited_living uses Python identifier assited_living
    __assited_living = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "assited_living"),
        "assited_living",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_assited_living",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 680, 20
        ),
    )

    assited_living = property(__assited_living.value, __assited_living.set, None, None)

    # Element carport uses Python identifier carport
    __carport = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "carport"),
        "carport",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_carport",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 681, 20
        ),
    )

    carport = property(__carport.value, __carport.set, None, None)

    # Element floorboards uses Python identifier floorboards
    __floorboards = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "floorboards"),
        "floorboards",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_floorboards",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 682, 20
        ),
    )

    floorboards = property(__floorboards.value, __floorboards.set, None, None)

    # Element duplex uses Python identifier duplex
    __duplex = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "duplex"),
        "duplex",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_duplex",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 683, 20
        ),
    )

    duplex = property(__duplex.value, __duplex.set, None, None)

    # Element shower uses Python identifier shower
    __shower = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "shower"),
        "shower",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_shower",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 684, 20
        ),
    )

    shower = property(__shower.value, __shower.set, None, None)

    # Element builtin_kitchen uses Python identifier builtin_kitchen
    __builtin_kitchen = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "builtin_kitchen"),
        "builtin_kitchen",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_builtin_kitchen",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 685, 20
        ),
    )

    builtin_kitchen = property(
        __builtin_kitchen.value, __builtin_kitchen.set, None, None
    )

    # Element screed uses Python identifier screed
    __screed = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "screed"),
        "screed",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_screed",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 686, 20
        ),
    )

    screed = property(__screed.value, __screed.set, None, None)

    # Element tiles uses Python identifier tiles
    __tiles = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "tiles"),
        "tiles",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_tiles",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 687, 20
        ),
    )

    tiles = property(__tiles.value, __tiles.set, None, None)

    # Element outdoor_parking uses Python identifier outdoor_parking
    __outdoor_parking = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "outdoor_parking"),
        "outdoor_parking",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_outdoor_parking",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 688, 20
        ),
    )

    outdoor_parking = property(
        __outdoor_parking.value, __outdoor_parking.set, None, None
    )

    # Element garage uses Python identifier garage
    __garage = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "garage"),
        "garage",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_garage",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 689, 20
        ),
    )

    garage = property(__garage.value, __garage.set, None, None)

    # Element cable_sat_tv uses Python identifier cable_sat_tv
    __cable_sat_tv = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "cable_sat_tv"),
        "cable_sat_tv",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_cable_sat_tv",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 690, 20
        ),
    )

    cable_sat_tv = property(__cable_sat_tv.value, __cable_sat_tv.set, None, None)

    # Element fireplace uses Python identifier fireplace
    __fireplace = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "fireplace"),
        "fireplace",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_fireplace",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 691, 20
        ),
    )

    fireplace = property(__fireplace.value, __fireplace.set, None, None)

    # Element basement uses Python identifier basement
    __basement = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "basement"),
        "basement",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_basement",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 692, 20
        ),
    )

    basement = property(__basement.value, __basement.set, None, None)

    # Element plastic uses Python identifier plastic
    __plastic = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "plastic"),
        "plastic",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_plastic",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 693, 20
        ),
    )

    plastic = property(__plastic.value, __plastic.set, None, None)

    # Element furnished uses Python identifier furnished
    __furnished = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "furnished"),
        "furnished",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_furnished",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 694, 20
        ),
    )

    furnished = property(__furnished.value, __furnished.set, None, None)

    # Element parquet uses Python identifier parquet
    __parquet = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "parquet"),
        "parquet",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_parquet",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 695, 20
        ),
    )

    parquet = property(__parquet.value, __parquet.set, None, None)

    # Element car_park uses Python identifier car_park
    __car_park = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "car_park"),
        "car_park",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_car_park",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 696, 20
        ),
    )

    car_park = property(__car_park.value, __car_park.set, None, None)

    # Element wheelchair_accessible uses Python identifier wheelchair_accessible
    __wheelchair_accessible = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "wheelchair_accessible"),
        "wheelchair_accessible",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_wheelchair_accessible",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 697, 20
        ),
    )

    wheelchair_accessible = property(
        __wheelchair_accessible.value, __wheelchair_accessible.set, None, None
    )

    # Element sauna uses Python identifier sauna
    __sauna = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "sauna"),
        "sauna",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_sauna",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 698, 20
        ),
    )

    sauna = property(__sauna.value, __sauna.set, None, None)

    # Element stone uses Python identifier stone
    __stone = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "stone"),
        "stone",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_stone",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 699, 20
        ),
    )

    stone = property(__stone.value, __stone.set, None, None)

    # Element swimming_pool uses Python identifier swimming_pool
    __swimming_pool = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "swimming_pool"),
        "swimming_pool",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_swimming_pool",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 700, 20
        ),
    )

    swimming_pool = property(__swimming_pool.value, __swimming_pool.set, None, None)

    # Element carpet uses Python identifier carpet
    __carpet = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "carpet"),
        "carpet",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_carpet",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 701, 20
        ),
    )

    carpet = property(__carpet.value, __carpet.set, None, None)

    # Element underground_carpark uses Python identifier underground_carpark
    __underground_carpark = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "underground_carpark"),
        "underground_carpark",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_underground_carpark",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 702, 20
        ),
    )

    underground_carpark = property(
        __underground_carpark.value, __underground_carpark.set, None, None
    )

    # Element lavatory uses Python identifier lavatory
    __lavatory = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "lavatory"),
        "lavatory",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_lavatory",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 703, 20
        ),
    )

    lavatory = property(__lavatory.value, __lavatory.set, None, None)

    # Element rooms_1 uses Python identifier rooms_1
    __rooms_1 = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "rooms_1"),
        "rooms_1",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_rooms_1",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 705, 20
        ),
    )

    rooms_1 = property(__rooms_1.value, __rooms_1.set, None, None)

    # Element rooms_2 uses Python identifier rooms_2
    __rooms_2 = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "rooms_2"),
        "rooms_2",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_rooms_2",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 706, 20
        ),
    )

    rooms_2 = property(__rooms_2.value, __rooms_2.set, None, None)

    # Element rooms_3 uses Python identifier rooms_3
    __rooms_3 = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "rooms_3"),
        "rooms_3",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_rooms_3",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 707, 20
        ),
    )

    rooms_3 = property(__rooms_3.value, __rooms_3.set, None, None)

    # Element rooms_4 uses Python identifier rooms_4
    __rooms_4 = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "rooms_4"),
        "rooms_4",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_rooms_4",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 708, 20
        ),
    )

    rooms_4 = property(__rooms_4.value, __rooms_4.set, None, None)

    # Element rooms_5 uses Python identifier rooms_5
    __rooms_5 = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "rooms_5"),
        "rooms_5",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_rooms_5",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 709, 20
        ),
    )

    rooms_5 = property(__rooms_5.value, __rooms_5.set, None, None)

    # Element rooms_5_or_more uses Python identifier rooms_5_or_more
    __rooms_5_or_more = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "rooms_5_or_more"),
        "rooms_5_or_more",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_rooms_5_or_more",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 710, 20
        ),
    )

    rooms_5_or_more = property(
        __rooms_5_or_more.value, __rooms_5_or_more.set, None, None
    )

    # Element finance_project uses Python identifier finance_project
    __finance_project = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "finance_project"),
        "finance_project",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_finance_project",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 712, 20
        ),
    )

    finance_project = property(
        __finance_project.value, __finance_project.set, None, None
    )

    # Element business_realty uses Python identifier business_realty
    __business_realty = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "business_realty"),
        "business_realty",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_business_realty",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 713, 20
        ),
    )

    business_realty = property(
        __business_realty.value, __business_realty.set, None, None
    )

    # Element short_term_accommodation uses Python identifier short_term_accommodation
    __short_term_accommodation = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "short_term_accommodation"),
        "short_term_accommodation",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_short_term_accommodation",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 714, 20
        ),
    )

    short_term_accommodation = property(
        __short_term_accommodation.value, __short_term_accommodation.set, None, None
    )

    # Element living_realty uses Python identifier living_realty
    __living_realty = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "living_realty"),
        "living_realty",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_living_realty",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 715, 20
        ),
    )

    living_realty = property(__living_realty.value, __living_realty.set, None, None)

    # Element office uses Python identifier office
    __office = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "office"),
        "office",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_office",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 717, 20
        ),
    )

    office = property(__office.value, __office.set, None, None)

    # Element retail uses Python identifier retail
    __retail = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "retail"),
        "retail",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_retail",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 718, 20
        ),
    )

    retail = property(__retail.value, __retail.set, None, None)

    # Element recreational uses Python identifier recreational
    __recreational = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "recreational"),
        "recreational",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_recreational",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 719, 20
        ),
    )

    recreational = property(__recreational.value, __recreational.set, None, None)

    # Element hospitality_industry uses Python identifier hospitality_industry
    __hospitality_industry = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "hospitality_industry"),
        "hospitality_industry",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_hospitality_industry",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 720, 20
        ),
    )

    hospitality_industry = property(
        __hospitality_industry.value, __hospitality_industry.set, None, None
    )

    # Element plot uses Python identifier plot
    __plot = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "plot"),
        "plot",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_plot",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 721, 20
        ),
    )

    plot = property(__plot.value, __plot.set, None, None)

    # Element hall_warehouse_production uses Python identifier hall_warehouse_production
    __hall_warehouse_production = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "hall_warehouse_production"),
        "hall_warehouse_production",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_hall_warehouse_production",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 722, 20
        ),
    )

    hall_warehouse_production = property(
        __hall_warehouse_production.value, __hall_warehouse_production.set, None, None
    )

    # Element house uses Python identifier house
    __house = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "house"),
        "house",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_house",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 723, 20
        ),
    )

    house = property(__house.value, __house.set, None, None)

    # Element agriculture_forestry uses Python identifier agriculture_forestry
    __agriculture_forestry = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "agriculture_forestry"),
        "agriculture_forestry",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_agriculture_forestry",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 724, 20
        ),
    )

    agriculture_forestry = property(
        __agriculture_forestry.value, __agriculture_forestry.set, None, None
    )

    # Element miscellaneous uses Python identifier miscellaneous
    __miscellaneous = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "miscellaneous"),
        "miscellaneous",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_miscellaneous",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 725, 20
        ),
    )

    miscellaneous = property(__miscellaneous.value, __miscellaneous.set, None, None)

    # Element flat uses Python identifier flat
    __flat = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "flat"),
        "flat",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_flat",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 726, 20
        ),
    )

    flat = property(__flat.value, __flat.set, None, None)

    # Element room uses Python identifier room
    __room = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "room"),
        "room",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_room",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 727, 20
        ),
    )

    room = property(__room.value, __room.set, None, None)

    # Element income_property uses Python identifier income_property
    __income_property = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "income_property"),
        "income_property",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_income_property",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 728, 20
        ),
    )

    income_property = property(
        __income_property.value, __income_property.set, None, None
    )

    # Element emphyteusis uses Python identifier emphyteusis
    __emphyteusis = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "emphyteusis"),
        "emphyteusis",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_emphyteusis",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 730, 20
        ),
    )

    emphyteusis = property(__emphyteusis.value, __emphyteusis.set, None, None)

    # Element leasing uses Python identifier leasing
    __leasing = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "leasing"),
        "leasing",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_leasing",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 731, 20
        ),
    )

    leasing = property(__leasing.value, __leasing.set, None, None)

    # Element rent uses Python identifier rent
    __rent = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "rent"),
        "rent",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_rent",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 732, 20
        ),
    )

    rent = property(__rent.value, __rent.set, None, None)

    # Element sale uses Python identifier sale
    __sale = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "sale"),
        "sale",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_sale",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 733, 20
        ),
    )

    sale = property(__sale.value, __sale.set, None, None)

    # Element filter uses Python identifier filter
    __filter = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "filter"),
        "filter",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_filter",
        True,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 735, 20
        ),
    )

    filter = property(__filter.value, __filter.set, None, None)

    # Element contact uses Python identifier contact
    __contact = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "contact"),
        "contact",
        "__httpxml_homeinfo_deschemadscms4_RealEstates_contact",
        True,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 737, 20
        ),
    )

    contact = property(__contact.value, __contact.set, None, None)

    # Attribute id inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Attribute type inherited from {http://xml.homeinfo.de/schema/dscms4}Chart
    _ElementMap.update(
        {
            __display_format.name(): __display_format,
            __ken_burns.name(): __ken_burns,
            __scaling.name(): __scaling,
            __slideshow.name(): __slideshow,
            __qr_codes.name(): __qr_codes,
            __show_contact.name(): __show_contact,
            __contact_picture.name(): __contact_picture,
            __font_size.name(): __font_size,
            __font_color.name(): __font_color,
            __data.name(): __data,
            __background_data.name(): __background_data,
            __values.name(): __values,
            __background_values.name(): __background_values,
            __amenities_background_even.name(): __amenities_background_even,
            __amenities_text_even.name(): __amenities_text_even,
            __amenities_background_uneven.name(): __amenities_background_uneven,
            __amenities_text_uneven.name(): __amenities_text_uneven,
            __amenities.name(): __amenities,
            __construction.name(): __construction,
            __courtage.name(): __courtage,
            __floor.name(): __floor,
            __area.name(): __area,
            __free_from.name(): __free_from,
            __coop_share.name(): __coop_share,
            __total_area.name(): __total_area,
            __plot_area.name(): __plot_area,
            __cold_rent.name(): __cold_rent,
            __purchase_price.name(): __purchase_price,
            __security_deposit.name(): __security_deposit,
            __service_charge.name(): __service_charge,
            __object_id.name(): __object_id,
            __description.name(): __description,
            __warm_rent.name(): __warm_rent,
            __rooms.name(): __rooms,
            __lift.name(): __lift,
            __bathtub.name(): __bathtub,
            __balcony.name(): __balcony,
            __accessibility.name(): __accessibility,
            __assited_living.name(): __assited_living,
            __carport.name(): __carport,
            __floorboards.name(): __floorboards,
            __duplex.name(): __duplex,
            __shower.name(): __shower,
            __builtin_kitchen.name(): __builtin_kitchen,
            __screed.name(): __screed,
            __tiles.name(): __tiles,
            __outdoor_parking.name(): __outdoor_parking,
            __garage.name(): __garage,
            __cable_sat_tv.name(): __cable_sat_tv,
            __fireplace.name(): __fireplace,
            __basement.name(): __basement,
            __plastic.name(): __plastic,
            __furnished.name(): __furnished,
            __parquet.name(): __parquet,
            __car_park.name(): __car_park,
            __wheelchair_accessible.name(): __wheelchair_accessible,
            __sauna.name(): __sauna,
            __stone.name(): __stone,
            __swimming_pool.name(): __swimming_pool,
            __carpet.name(): __carpet,
            __underground_carpark.name(): __underground_carpark,
            __lavatory.name(): __lavatory,
            __rooms_1.name(): __rooms_1,
            __rooms_2.name(): __rooms_2,
            __rooms_3.name(): __rooms_3,
            __rooms_4.name(): __rooms_4,
            __rooms_5.name(): __rooms_5,
            __rooms_5_or_more.name(): __rooms_5_or_more,
            __finance_project.name(): __finance_project,
            __business_realty.name(): __business_realty,
            __short_term_accommodation.name(): __short_term_accommodation,
            __living_realty.name(): __living_realty,
            __office.name(): __office,
            __retail.name(): __retail,
            __recreational.name(): __recreational,
            __hospitality_industry.name(): __hospitality_industry,
            __plot.name(): __plot,
            __hall_warehouse_production.name(): __hall_warehouse_production,
            __house.name(): __house,
            __agriculture_forestry.name(): __agriculture_forestry,
            __miscellaneous.name(): __miscellaneous,
            __flat.name(): __flat,
            __room.name(): __room,
            __income_property.name(): __income_property,
            __emphyteusis.name(): __emphyteusis,
            __leasing.name(): __leasing,
            __rent.name(): __rent,
            __sale.name(): __sale,
            __filter.name(): __filter,
            __contact.name(): __contact,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.RealEstates = RealEstates
Namespace.addCategoryObject("typeBinding", "RealEstates", RealEstates)


# Complex type {http://xml.homeinfo.de/schema/dscms4}Booking with content type ELEMENT_ONLY
class Booking(Chart):
    """
    Vermietungs-Chart.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Booking")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 744, 4
    )
    _ElementMap = Chart._ElementMap.copy()
    _AttributeMap = Chart._AttributeMap.copy()
    # Base type is Chart

    # Element base (base) inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Element bookable uses Python identifier bookable
    __bookable = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "bookable"),
        "bookable",
        "__httpxml_homeinfo_deschemadscms4_Booking_bookable",
        True,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 753, 20
        ),
    )

    bookable = property(
        __bookable.value,
        __bookable.set,
        None,
        "\n                                Datenbank-IDs der Mietobjekte.\n                            ",
    )

    # Element rentee uses Python identifier rentee
    __rentee = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "rentee"),
        "rentee",
        "__httpxml_homeinfo_deschemadscms4_Booking_rentee",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 760, 20
        ),
    )

    rentee = property(
        __rentee.value,
        __rentee.set,
        None,
        "\n                                Schalter für Mieterangabe.\n                            ",
    )

    # Element purpose uses Python identifier purpose
    __purpose = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "purpose"),
        "purpose",
        "__httpxml_homeinfo_deschemadscms4_Booking_purpose",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 767, 20
        ),
    )

    purpose = property(
        __purpose.value,
        __purpose.set,
        None,
        "\n                                Schalter für Verwendungszweck.\n                            ",
    )

    # Element text uses Python identifier text
    __text = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "text"),
        "text",
        "__httpxml_homeinfo_deschemadscms4_Booking_text",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 774, 20
        ),
    )

    text = property(
        __text.value,
        __text.set,
        None,
        "\n                                Textinhalt.\n                            ",
    )

    # Attribute id inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Attribute type inherited from {http://xml.homeinfo.de/schema/dscms4}Chart
    _ElementMap.update(
        {
            __bookable.name(): __bookable,
            __rentee.name(): __rentee,
            __purpose.name(): __purpose,
            __text.name(): __text,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Booking = Booking
Namespace.addCategoryObject("typeBinding", "Booking", Booking)


# Complex type {http://xml.homeinfo.de/schema/dscms4}SoccerTable with content type ELEMENT_ONLY
class SoccerTable(Chart):
    """
    Bundesligatabelle.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "SoccerTable")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 787, 4
    )
    _ElementMap = Chart._ElementMap.copy()
    _AttributeMap = Chart._AttributeMap.copy()
    # Base type is Chart

    # Element base (base) inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Element font_size_title uses Python identifier font_size_title
    __font_size_title = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "font_size_title"),
        "font_size_title",
        "__httpxml_homeinfo_deschemadscms4_SoccerTable_font_size_title",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 796, 20
        ),
    )

    font_size_title = property(
        __font_size_title.value,
        __font_size_title.set,
        None,
        "\n                                Schriftgröße des Titles.\n                            ",
    )

    # Element title_color uses Python identifier title_color
    __title_color = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "title_color"),
        "title_color",
        "__httpxml_homeinfo_deschemadscms4_SoccerTable_title_color",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 803, 20
        ),
    )

    title_color = property(
        __title_color.value,
        __title_color.set,
        None,
        "\n                                Titelfarbe.\n                            ",
    )

    # Element font_size_text uses Python identifier font_size_text
    __font_size_text = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "font_size_text"),
        "font_size_text",
        "__httpxml_homeinfo_deschemadscms4_SoccerTable_font_size_text",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 810, 20
        ),
    )

    font_size_text = property(
        __font_size_text.value,
        __font_size_text.set,
        None,
        "\n                                Schriftgröße des Texts.\n                            ",
    )

    # Element text_color uses Python identifier text_color
    __text_color = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "text_color"),
        "text_color",
        "__httpxml_homeinfo_deschemadscms4_SoccerTable_text_color",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 817, 20
        ),
    )

    text_color = property(
        __text_color.value,
        __text_color.set,
        None,
        "\n                                Textfarbe.\n                            ",
    )

    # Attribute id inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Attribute type inherited from {http://xml.homeinfo.de/schema/dscms4}Chart
    _ElementMap.update(
        {
            __font_size_title.name(): __font_size_title,
            __title_color.name(): __title_color,
            __font_size_text.name(): __font_size_text,
            __text_color.name(): __text_color,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.SoccerTable = SoccerTable
Namespace.addCategoryObject("typeBinding", "SoccerTable", SoccerTable)


# Complex type {http://xml.homeinfo.de/schema/dscms4}URL with content type ELEMENT_ONLY
class URL(Chart):
    """
    URL Chart.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "URL")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 830, 4
    )
    _ElementMap = Chart._ElementMap.copy()
    _AttributeMap = Chart._AttributeMap.copy()
    # Base type is Chart

    # Element base (base) inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Element url uses Python identifier url
    __url = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "url"),
        "url",
        "__httpxml_homeinfo_deschemadscms4_URL_url",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 839, 20
        ),
    )

    url = property(
        __url.value,
        __url.set,
        None,
        "\n                                RSS Feed URL.\n                            ",
    )

    # Element mode uses Python identifier mode
    __mode = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "mode"),
        "mode",
        "__httpxml_homeinfo_deschemadscms4_URL_mode",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 846, 20
        ),
    )

    mode = property(
        __mode.value,
        __mode.set,
        None,
        "\n                                Modus des Charts.\n                            ",
    )

    # Element title_color uses Python identifier title_color
    __title_color = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "title_color"),
        "title_color",
        "__httpxml_homeinfo_deschemadscms4_URL_title_color",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 853, 20
        ),
    )

    title_color = property(
        __title_color.value,
        __title_color.set,
        None,
        "\n                                Titelfarbe.\n                            ",
    )

    # Element font_size_title uses Python identifier font_size_title
    __font_size_title = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "font_size_title"),
        "font_size_title",
        "__httpxml_homeinfo_deschemadscms4_URL_font_size_title",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 860, 20
        ),
    )

    font_size_title = property(
        __font_size_title.value,
        __font_size_title.set,
        None,
        "\n                                Schriftgröße des Titels.\n                            ",
    )

    # Element text_color uses Python identifier text_color
    __text_color = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "text_color"),
        "text_color",
        "__httpxml_homeinfo_deschemadscms4_URL_text_color",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 867, 20
        ),
    )

    text_color = property(
        __text_color.value,
        __text_color.set,
        None,
        "\n                                Schriftfarbe des Texts.\n                            ",
    )

    # Element font_size_text uses Python identifier font_size_text
    __font_size_text = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "font_size_text"),
        "font_size_text",
        "__httpxml_homeinfo_deschemadscms4_URL_font_size_text",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 874, 20
        ),
    )

    font_size_text = property(
        __font_size_text.value,
        __font_size_text.set,
        None,
        "\n                                Schriftgröße des Texts.\n                            ",
    )

    # Attribute id inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Attribute type inherited from {http://xml.homeinfo.de/schema/dscms4}Chart
    _ElementMap.update(
        {
            __url.name(): __url,
            __mode.name(): __mode,
            __title_color.name(): __title_color,
            __font_size_title.name(): __font_size_title,
            __text_color.name(): __text_color,
            __font_size_text.name(): __font_size_text,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.URL = URL
Namespace.addCategoryObject("typeBinding", "URL", URL)


# Complex type {http://xml.homeinfo.de/schema/dscms4}Video with content type ELEMENT_ONLY
class Video(Chart):
    """
    Video Chart.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Video")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 887, 4
    )
    _ElementMap = Chart._ElementMap.copy()
    _AttributeMap = Chart._AttributeMap.copy()
    # Base type is Chart

    # Element base (base) inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Element video uses Python identifier video
    __video = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "video"),
        "video",
        "__httpxml_homeinfo_deschemadscms4_Video_video",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 896, 20
        ),
    )

    video = property(
        __video.value,
        __video.set,
        None,
        "\n                                Das entsprechende Video.\n                            ",
    )

    # Attribute id inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Attribute type inherited from {http://xml.homeinfo.de/schema/dscms4}Chart
    _ElementMap.update({__video.name(): __video})
    _AttributeMap.update({})


_module_typeBindings.Video = Video
Namespace.addCategoryObject("typeBinding", "Video", Video)


# Complex type {http://xml.homeinfo.de/schema/dscms4}Weather with content type ELEMENT_ONLY
class Weather(Chart):
    """
    Wetter Chart.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Weather")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 909, 4
    )
    _ElementMap = Chart._ElementMap.copy()
    _AttributeMap = Chart._AttributeMap.copy()
    # Base type is Chart

    # Element base (base) inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "location"),
        "location",
        "__httpxml_homeinfo_deschemadscms4_Weather_location",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 918, 20
        ),
    )

    location = property(
        __location.value,
        __location.set,
        None,
        "\n                                Ort des Wetters.\n                            ",
    )

    # Element font_color uses Python identifier font_color
    __font_color = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "font_color"),
        "font_color",
        "__httpxml_homeinfo_deschemadscms4_Weather_font_color",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 925, 20
        ),
    )

    font_color = property(
        __font_color.value,
        __font_color.set,
        None,
        "\n                                Schriftfarbe.\n                            ",
    )

    # Element icon_color uses Python identifier icon_color
    __icon_color = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "icon_color"),
        "icon_color",
        "__httpxml_homeinfo_deschemadscms4_Weather_icon_color",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 932, 20
        ),
    )

    icon_color = property(
        __icon_color.value,
        __icon_color.set,
        None,
        "\n                                Icon Farbe.\n                            ",
    )

    # Element box_color_top uses Python identifier box_color_top
    __box_color_top = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "box_color_top"),
        "box_color_top",
        "__httpxml_homeinfo_deschemadscms4_Weather_box_color_top",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 939, 20
        ),
    )

    box_color_top = property(
        __box_color_top.value,
        __box_color_top.set,
        None,
        "\n                                Obere Farbe der Box.\n                            ",
    )

    # Element box_color_middle uses Python identifier box_color_middle
    __box_color_middle = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "box_color_middle"),
        "box_color_middle",
        "__httpxml_homeinfo_deschemadscms4_Weather_box_color_middle",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 946, 20
        ),
    )

    box_color_middle = property(
        __box_color_middle.value,
        __box_color_middle.set,
        None,
        "\n                                Mittlere Farbe der Box.\n                            ",
    )

    # Element box_color_bottom uses Python identifier box_color_bottom
    __box_color_bottom = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "box_color_bottom"),
        "box_color_bottom",
        "__httpxml_homeinfo_deschemadscms4_Weather_box_color_bottom",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 953, 20
        ),
    )

    box_color_bottom = property(
        __box_color_bottom.value,
        __box_color_bottom.set,
        None,
        "\n                                Untere Farbe der Box.\n                            ",
    )

    # Element transparency uses Python identifier transparency
    __transparency = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "transparency"),
        "transparency",
        "__httpxml_homeinfo_deschemadscms4_Weather_transparency",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 960, 20
        ),
    )

    transparency = property(
        __transparency.value,
        __transparency.set,
        None,
        "\n                                Transparenz.\n                            ",
    )

    # Element image uses Python identifier image
    __image = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "image"),
        "image",
        "__httpxml_homeinfo_deschemadscms4_Weather_image",
        True,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 967, 20
        ),
    )

    image = property(
        __image.value,
        __image.set,
        None,
        "\n                                Bilder.\n                            ",
    )

    # Attribute id inherited from {http://xml.homeinfo.de/schema/dscms4}Chart

    # Attribute type inherited from {http://xml.homeinfo.de/schema/dscms4}Chart
    _ElementMap.update(
        {
            __location.name(): __location,
            __font_color.name(): __font_color,
            __icon_color.name(): __icon_color,
            __box_color_top.name(): __box_color_top,
            __box_color_middle.name(): __box_color_middle,
            __box_color_bottom.name(): __box_color_bottom,
            __transparency.name(): __transparency,
            __image.name(): __image,
        }
    )
    _AttributeMap.update({})


_module_typeBindings.Weather = Weather
Namespace.addCategoryObject("typeBinding", "Weather", Weather)


# Complex type {http://xml.homeinfo.de/schema/dscms4}MenuItemChart with content type ELEMENT_ONLY
class MenuItemChart(BriefChart):
    """
    Chart eines Menüelements.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "MenuItemChart")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 81, 4
    )
    _ElementMap = BriefChart._ElementMap.copy()
    _AttributeMap = BriefChart._AttributeMap.copy()
    # Base type is BriefChart

    # Element id (id) inherited from {http://xml.homeinfo.de/schema/dscms4}BriefChart

    # Element type (type) inherited from {http://xml.homeinfo.de/schema/dscms4}BriefChart

    # Element index uses Python identifier index
    __index = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "index"),
        "index",
        "__httpxml_homeinfo_deschemadscms4_MenuItemChart_index",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 90, 20
        ),
    )

    index = property(
        __index.value,
        __index.set,
        None,
        "\n                                Position des Charts.\n                            ",
    )

    _ElementMap.update({__index.name(): __index})
    _AttributeMap.update({})


_module_typeBindings.MenuItemChart = MenuItemChart
Namespace.addCategoryObject("typeBinding", "MenuItemChart", MenuItemChart)


# Complex type {http://xml.homeinfo.de/schema/dscms4}IdFilter with content type ELEMENT_ONLY
class IdFilter(Filter):
    """
    Ein Immobilien Filter zur Filterung nach IDs.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "IdFilter")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 21, 4
    )
    _ElementMap = Filter._ElementMap.copy()
    _AttributeMap = Filter._AttributeMap.copy()
    # Base type is Filter

    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "value"),
        "value_",
        "__httpxml_homeinfo_deschemadscms4_IdFilter_value",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 30, 20
        ),
    )

    value_ = property(
        __value.value,
        __value.set,
        None,
        "\n                                Wert der ID.\n                            ",
    )

    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "type"),
        "type",
        "__httpxml_homeinfo_deschemadscms4_IdFilter_type",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 37, 20
        ),
    )

    type = property(
        __type.value,
        __type.set,
        None,
        "\n                                Typ der ID.\n                            ",
    )

    _ElementMap.update({__value.name(): __value, __type.name(): __type})
    _AttributeMap.update({})


_module_typeBindings.IdFilter = IdFilter
Namespace.addCategoryObject("typeBinding", "IdFilter", IdFilter)


# Complex type {http://xml.homeinfo.de/schema/dscms4}ZipCodeFilter with content type ELEMENT_ONLY
class ZipCodeFilter(Filter):
    """
    Ein Immobilien Filter zur Filterung nach IDs.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "ZipCodeFilter")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 50, 4
    )
    _ElementMap = Filter._ElementMap.copy()
    _AttributeMap = Filter._AttributeMap.copy()
    # Base type is Filter

    # Element zip_code uses Python identifier zip_code
    __zip_code = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "zip_code"),
        "zip_code",
        "__httpxml_homeinfo_deschemadscms4_ZipCodeFilter_zip_code",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 59, 20
        ),
    )

    zip_code = property(
        __zip_code.value,
        __zip_code.set,
        None,
        "\n                                Postleitzahl.\n                            ",
    )

    # Element blacklist uses Python identifier blacklist
    __blacklist = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "blacklist"),
        "blacklist",
        "__httpxml_homeinfo_deschemadscms4_ZipCodeFilter_blacklist",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 66, 20
        ),
    )

    blacklist = property(
        __blacklist.value,
        __blacklist.set,
        None,
        "\n                                Handelt es sich um eine Blacklist (true) oder Whitelist(false)?\n                            ",
    )

    _ElementMap.update({__zip_code.name(): __zip_code, __blacklist.name(): __blacklist})
    _AttributeMap.update({})


_module_typeBindings.ZipCodeFilter = ZipCodeFilter
Namespace.addCategoryObject("typeBinding", "ZipCodeFilter", ZipCodeFilter)


presentation = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "presentation"),
    Presentation,
    documentation="\n                Wurzelelement.\n            ",
    location=pyxb.utils.utility.Location(
        "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 18, 4
    ),
)
Namespace.addCategoryObject(
    "elementBinding", presentation.name().localName(), presentation
)


Address._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "street"),
        pyxb.binding.datatypes.string,
        scope=Address,
        documentation="\n                        Der Straßenname.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/address.xsd", 19, 12
        ),
    )
)

Address._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "house_number"),
        pyxb.binding.datatypes.string,
        scope=Address,
        documentation="\n                        Die Hausnummer.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/address.xsd", 26, 12
        ),
    )
)

Address._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "zip_code"),
        pyxb.binding.datatypes.string,
        scope=Address,
        documentation="\n                        Die Postleitzahl (PLZ).\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/address.xsd", 33, 12
        ),
    )
)

Address._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "city"),
        pyxb.binding.datatypes.string,
        scope=Address,
        documentation="\n                        Der Ortsname.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/address.xsd", 40, 12
        ),
    )
)


def _BuildAutomaton():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Address._UseForTag(pyxb.namespace.ExpandedName(None, "street")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/address.xsd", 19, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Address._UseForTag(pyxb.namespace.ExpandedName(None, "house_number")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/address.xsd", 26, 12
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Address._UseForTag(pyxb.namespace.ExpandedName(None, "zip_code")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/address.xsd", 33, 12
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Address._UseForTag(pyxb.namespace.ExpandedName(None, "city")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/address.xsd", 40, 12
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Address._Automaton = _BuildAutomaton()


Attachment._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "mimetype"),
        pyxb.binding.datatypes.string,
        scope=Attachment,
        documentation="\n                        MIME Typ.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/attachments.xsd", 19, 12
        ),
    )
)

Attachment._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "filename"),
        pyxb.binding.datatypes.string,
        scope=Attachment,
        documentation="\n                        Dateiname.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/attachments.xsd", 26, 12
        ),
    )
)


def _BuildAutomaton_():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Attachment._UseForTag(pyxb.namespace.ExpandedName(None, "mimetype")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/attachments.xsd", 19, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Attachment._UseForTag(pyxb.namespace.ExpandedName(None, "filename")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/attachments.xsd", 26, 12
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Attachment._Automaton = _BuildAutomaton_()


BaseChart._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "title"),
        pyxb.binding.datatypes.string,
        scope=BaseChart,
        documentation="\n                        Der Titel des Charts.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 25, 12
        ),
    )
)

BaseChart._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "description"),
        pyxb.binding.datatypes.string,
        scope=BaseChart,
        documentation="\n                        Die Beschreibung des Charts.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 32, 12
        ),
    )
)

BaseChart._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "duration"),
        pyxb.binding.datatypes.unsignedShort,
        scope=BaseChart,
        documentation="\n                        Die Anzeigedauer des Charts.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 39, 12
        ),
    )
)

BaseChart._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "position"),
        pyxb.binding.datatypes.unsignedShort,
        scope=BaseChart,
        documentation="\n                        Die Anzeigedauer des Charts.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 46, 12
        ),
    )
)

BaseChart._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "transition"),
        pyxb.binding.datatypes.string,
        scope=BaseChart,
        documentation="\n                        Übergangseffekt.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 53, 12
        ),
    )
)

BaseChart._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "created"),
        pyxb.binding.datatypes.dateTime,
        scope=BaseChart,
        documentation="\n                        Datum der Erstellung.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 60, 12
        ),
    )
)

BaseChart._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "schedule"),
        Schedule,
        scope=BaseChart,
        documentation="\n                        Optionaler Zeitplan.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 67, 12
        ),
    )
)

BaseChart._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "pin"),
        pyxb.binding.datatypes.string,
        scope=BaseChart,
        documentation="\n                        Liste von PINs zur Zugriffssteuerung.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 74, 12
        ),
    )
)


def _BuildAutomaton_2():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 32, 12
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 46, 12
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 53, 12
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 67, 12
        ),
    )
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 74, 12
        ),
    )
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        BaseChart._UseForTag(pyxb.namespace.ExpandedName(None, "title")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 25, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        BaseChart._UseForTag(pyxb.namespace.ExpandedName(None, "description")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 32, 12
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        BaseChart._UseForTag(pyxb.namespace.ExpandedName(None, "duration")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 39, 12
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        BaseChart._UseForTag(pyxb.namespace.ExpandedName(None, "position")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 46, 12
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        BaseChart._UseForTag(pyxb.namespace.ExpandedName(None, "transition")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 53, 12
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        BaseChart._UseForTag(pyxb.namespace.ExpandedName(None, "created")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 60, 12
        ),
    )
    st_5 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(
        BaseChart._UseForTag(pyxb.namespace.ExpandedName(None, "schedule")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 67, 12
        ),
    )
    st_6 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(
        BaseChart._UseForTag(pyxb.namespace.ExpandedName(None, "pin")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 74, 12
        ),
    )
    st_7 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    transitions.append(fac.Transition(st_2, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    transitions.append(fac.Transition(st_4, []))
    transitions.append(fac.Transition(st_5, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_1, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_2, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, []))
    transitions.append(fac.Transition(st_7, []))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_3, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_4, True)]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


BaseChart._Automaton = _BuildAutomaton_2()


Chart._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "base"),
        BaseChart,
        scope=Chart,
        documentation="\n                        Der zugehörige Basis-Chart.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 134, 12
        ),
    )
)


def _BuildAutomaton_3():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Chart._UseForTag(pyxb.namespace.ExpandedName(None, "base")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 134, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Chart._Automaton = _BuildAutomaton_3()


BriefChart._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "id"),
        pyxb.binding.datatypes.positiveInteger,
        scope=BriefChart,
        documentation="\n                        ID des Charts.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 166, 12
        ),
    )
)

BriefChart._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "type"),
        pyxb.binding.datatypes.string,
        scope=BriefChart,
        documentation="\n                        Der Typ des Charts.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 173, 12
        ),
    )
)


def _BuildAutomaton_4():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        BriefChart._UseForTag(pyxb.namespace.ExpandedName(None, "id")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 166, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        BriefChart._UseForTag(pyxb.namespace.ExpandedName(None, "type")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 173, 12
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


BriefChart._Automaton = _BuildAutomaton_4()


Configuration._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "name"),
        pyxb.binding.datatypes.string,
        scope=Configuration,
        documentation="\n                        Name der Konfiguration.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 20, 12
        ),
    )
)

Configuration._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "description"),
        pyxb.binding.datatypes.string,
        scope=Configuration,
        documentation="\n                        Beschreibung der Konfiguration.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 27, 12
        ),
    )
)

Configuration._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "font"),
        pyxb.binding.datatypes.string,
        scope=Configuration,
        documentation="\n                        Schriftart.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 34, 12
        ),
    )
)

Configuration._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "portrait"),
        pyxb.binding.datatypes.boolean,
        scope=Configuration,
        documentation="\n                        Soll Portrait Darstellung verwendet werden?\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 41, 12
        ),
    )
)

Configuration._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "touch"),
        pyxb.binding.datatypes.boolean,
        scope=Configuration,
        documentation="\n                        Handelt es sich um ein Touch System?\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 48, 12
        ),
    )
)

Configuration._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "design"),
        pyxb.binding.datatypes.string,
        scope=Configuration,
        documentation="\n                        Das verwendete Design.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 55, 12
        ),
    )
)

Configuration._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "effects"),
        pyxb.binding.datatypes.boolean,
        scope=Configuration,
        documentation="\n                        Sollen Effekte verwendet werden?\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 62, 12
        ),
    )
)

Configuration._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "ticker_speed"),
        pyxb.binding.datatypes.unsignedShort,
        scope=Configuration,
        documentation="\n                        Geschwindigkeit des Tickers.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 69, 12
        ),
    )
)

Configuration._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "colors"),
        Colors,
        scope=Configuration,
        documentation="\n                        Die verwendeten Farben.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 76, 12
        ),
    )
)

Configuration._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "title_size"),
        pyxb.binding.datatypes.unsignedShort,
        scope=Configuration,
        documentation="\n                        Größe des Titels.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 83, 12
        ),
    )
)

Configuration._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "text_size"),
        pyxb.binding.datatypes.unsignedShort,
        scope=Configuration,
        documentation="\n                        Größe des Texts.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 90, 12
        ),
    )
)

Configuration._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "logo"),
        Attachment,
        scope=Configuration,
        documentation="\n                        Firmenlogo.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 97, 12
        ),
    )
)

Configuration._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "dummy_picture"),
        Attachment,
        scope=Configuration,
        documentation="\n                        Platzhalterbild.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 104, 12
        ),
    )
)

Configuration._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "hide_cursor"),
        pyxb.binding.datatypes.boolean,
        scope=Configuration,
        documentation="\n                        Soll der Cursor ausgeblendet werden?\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 111, 12
        ),
    )
)

Configuration._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "rotation"),
        pyxb.binding.datatypes.unsignedShort,
        scope=Configuration,
        documentation="\n                        Rotation in Grad.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 118, 12
        ),
    )
)

Configuration._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "email_form"),
        pyxb.binding.datatypes.boolean,
        scope=Configuration,
        documentation="\n                        Soll ein E-Mail Formular angezeigt werden?\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 125, 12
        ),
    )
)

Configuration._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "volume"),
        pyxb.binding.datatypes.float,
        scope=Configuration,
        documentation="\n                        Lautstärke als Faktor von 0-1.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 132, 12
        ),
    )
)

Configuration._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "text_bg_transparent"),
        pyxb.binding.datatypes.boolean,
        scope=Configuration,
        documentation="\n                        Soll die Hintergrundmaske der Textfelder im HD-Design transparent sein?\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 139, 12
        ),
    )
)

Configuration._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "background"),
        Attachment,
        scope=Configuration,
        documentation="\n                        Hintergrundbilder.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 146, 12
        ),
    )
)

Configuration._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "ticker"),
        Ticker,
        scope=Configuration,
        documentation="\n                        Ticker.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 153, 12
        ),
    )
)

Configuration._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "backlight"),
        Backlight,
        scope=Configuration,
        documentation="\n                        Hintergrundbeleuchtung.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 160, 12
        ),
    )
)


def _BuildAutomaton_5():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 27, 12
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 97, 12
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 104, 12
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 146, 12
        ),
    )
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 153, 12
        ),
    )
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 160, 12
        ),
    )
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Configuration._UseForTag(pyxb.namespace.ExpandedName(None, "name")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 20, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Configuration._UseForTag(pyxb.namespace.ExpandedName(None, "description")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 27, 12
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Configuration._UseForTag(pyxb.namespace.ExpandedName(None, "font")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 34, 12
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Configuration._UseForTag(pyxb.namespace.ExpandedName(None, "portrait")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 41, 12
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Configuration._UseForTag(pyxb.namespace.ExpandedName(None, "touch")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 48, 12
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Configuration._UseForTag(pyxb.namespace.ExpandedName(None, "design")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 55, 12
        ),
    )
    st_5 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Configuration._UseForTag(pyxb.namespace.ExpandedName(None, "effects")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 62, 12
        ),
    )
    st_6 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Configuration._UseForTag(pyxb.namespace.ExpandedName(None, "ticker_speed")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 69, 12
        ),
    )
    st_7 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Configuration._UseForTag(pyxb.namespace.ExpandedName(None, "colors")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 76, 12
        ),
    )
    st_8 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Configuration._UseForTag(pyxb.namespace.ExpandedName(None, "title_size")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 83, 12
        ),
    )
    st_9 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Configuration._UseForTag(pyxb.namespace.ExpandedName(None, "text_size")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 90, 12
        ),
    )
    st_10 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Configuration._UseForTag(pyxb.namespace.ExpandedName(None, "logo")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 97, 12
        ),
    )
    st_11 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Configuration._UseForTag(pyxb.namespace.ExpandedName(None, "dummy_picture")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 104, 12
        ),
    )
    st_12 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Configuration._UseForTag(pyxb.namespace.ExpandedName(None, "hide_cursor")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 111, 12
        ),
    )
    st_13 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Configuration._UseForTag(pyxb.namespace.ExpandedName(None, "rotation")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 118, 12
        ),
    )
    st_14 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Configuration._UseForTag(pyxb.namespace.ExpandedName(None, "email_form")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 125, 12
        ),
    )
    st_15 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Configuration._UseForTag(pyxb.namespace.ExpandedName(None, "volume")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 132, 12
        ),
    )
    st_16 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_16)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Configuration._UseForTag(
            pyxb.namespace.ExpandedName(None, "text_bg_transparent")
        ),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 139, 12
        ),
    )
    st_17 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(
        Configuration._UseForTag(pyxb.namespace.ExpandedName(None, "background")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 146, 12
        ),
    )
    st_18 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(
        Configuration._UseForTag(pyxb.namespace.ExpandedName(None, "ticker")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 153, 12
        ),
    )
    st_19 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(
        Configuration._UseForTag(pyxb.namespace.ExpandedName(None, "backlight")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 160, 12
        ),
    )
    st_20 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_20)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    transitions.append(fac.Transition(st_2, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, []))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, []))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, []))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, []))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, []))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, []))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, []))
    transitions.append(fac.Transition(st_12, []))
    transitions.append(fac.Transition(st_13, []))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_13, [fac.UpdateInstruction(cc_1, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_13, [fac.UpdateInstruction(cc_2, False)]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, []))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, []))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, []))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, []))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, []))
    transitions.append(fac.Transition(st_19, []))
    transitions.append(fac.Transition(st_20, []))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_19, [fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_20, [fac.UpdateInstruction(cc_3, False)]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_20, [fac.UpdateInstruction(cc_4, False)]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [fac.UpdateInstruction(cc_5, True)]))
    st_20._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Configuration._Automaton = _BuildAutomaton_5()


Colors._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "header"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=Colors,
        documentation="\n                        Farbe der Kopfzeile.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 178, 12
        ),
    )
)

Colors._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "header_background"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=Colors,
        documentation="\n                        Hintergrundfarbe der Kopfzeile.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 185, 12
        ),
    )
)

Colors._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "background_left"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=Colors,
        documentation="\n                        Hintergrundfarbe links.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 192, 12
        ),
    )
)

Colors._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "background_right"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=Colors,
        documentation="\n                        Hintergrundfarbe rechts.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 199, 12
        ),
    )
)

Colors._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "ticker"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=Colors,
        documentation="\n                        Farbe des Tickers.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 206, 12
        ),
    )
)

Colors._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "ticker_background"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=Colors,
        documentation="\n                        Hintergrundfarbe des Tickers.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 213, 12
        ),
    )
)

Colors._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "clock"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=Colors,
        documentation="\n                        Farbe der Uhr.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 220, 12
        ),
    )
)

Colors._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "title"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=Colors,
        documentation="\n                        Farbe des Titels.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 227, 12
        ),
    )
)

Colors._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "text"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=Colors,
        documentation="\n                        Textfarbe.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 234, 12
        ),
    )
)

Colors._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "text_background"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=Colors,
        documentation="\n                        Hintergrundfarbe des Texts.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 241, 12
        ),
    )
)


def _BuildAutomaton_6():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Colors._UseForTag(pyxb.namespace.ExpandedName(None, "header")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 178, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Colors._UseForTag(pyxb.namespace.ExpandedName(None, "header_background")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 185, 12
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Colors._UseForTag(pyxb.namespace.ExpandedName(None, "background_left")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 192, 12
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Colors._UseForTag(pyxb.namespace.ExpandedName(None, "background_right")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 199, 12
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Colors._UseForTag(pyxb.namespace.ExpandedName(None, "ticker")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 206, 12
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Colors._UseForTag(pyxb.namespace.ExpandedName(None, "ticker_background")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 213, 12
        ),
    )
    st_5 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Colors._UseForTag(pyxb.namespace.ExpandedName(None, "clock")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 220, 12
        ),
    )
    st_6 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Colors._UseForTag(pyxb.namespace.ExpandedName(None, "title")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 227, 12
        ),
    )
    st_7 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Colors._UseForTag(pyxb.namespace.ExpandedName(None, "text")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 234, 12
        ),
    )
    st_8 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Colors._UseForTag(pyxb.namespace.ExpandedName(None, "text_background")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 241, 12
        ),
    )
    st_9 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, []))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, []))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, []))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, []))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, []))
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Colors._Automaton = _BuildAutomaton_6()


Ticker._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "type"),
        pyxb.binding.datatypes.string,
        scope=Ticker,
        documentation="\n                        Typ des Tickers.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 259, 12
        ),
    )
)

Ticker._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "content"),
        pyxb.binding.datatypes.string,
        scope=Ticker,
        documentation="\n                        Inhalt des Tickers (Text / URL).\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 266, 12
        ),
    )
)


def _BuildAutomaton_7():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Ticker._UseForTag(pyxb.namespace.ExpandedName(None, "type")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 259, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Ticker._UseForTag(pyxb.namespace.ExpandedName(None, "content")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 266, 12
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Ticker._Automaton = _BuildAutomaton_7()


Backlight._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "time"),
        pyxb.binding.datatypes.time,
        scope=Backlight,
        documentation="\n                        Zeitstempel.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 284, 12
        ),
    )
)

Backlight._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "brightness"),
        pyxb.binding.datatypes.unsignedShort,
        scope=Backlight,
        documentation="\n                        Helligkeit in Prozent.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 291, 12
        ),
    )
)


def _BuildAutomaton_8():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Backlight._UseForTag(pyxb.namespace.ExpandedName(None, "time")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 284, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Backlight._UseForTag(pyxb.namespace.ExpandedName(None, "brightness")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/configuration.xsd", 291, 12
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Backlight._Automaton = _BuildAutomaton_8()


Deployment._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "address"),
        Address,
        scope=Deployment,
        documentation="\n                        Die Adresse.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/deployment.xsd", 21, 12
        ),
    )
)

Deployment._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "lpt_address"),
        Address,
        scope=Deployment,
        documentation="\n                        Abweichende Adresse für ÖPNV Daten.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/deployment.xsd", 28, 12
        ),
    )
)


def _BuildAutomaton_9():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/deployment.xsd", 28, 12
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Deployment._UseForTag(pyxb.namespace.ExpandedName(None, "address")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/deployment.xsd", 21, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        Deployment._UseForTag(pyxb.namespace.ExpandedName(None, "lpt_address")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/deployment.xsd", 28, 12
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Deployment._Automaton = _BuildAutomaton_9()


MenuItem._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "name"),
        pyxb.binding.datatypes.string,
        scope=MenuItem,
        documentation="\n                        Name des Menüelements.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 21, 12
        ),
    )
)

MenuItem._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "icon"),
        pyxb.binding.datatypes.string,
        scope=MenuItem,
        documentation="\n                        Symbol des Menüelements.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 28, 12
        ),
    )
)

MenuItem._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "icon_image"),
        Attachment,
        scope=MenuItem,
        documentation="\n                        Bildsymbol des Menüelements.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 35, 12
        ),
    )
)

MenuItem._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "text_color"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=MenuItem,
        documentation="\n                        Schriftfarbe des Menüelements.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 42, 12
        ),
    )
)

MenuItem._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "background_color"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=MenuItem,
        documentation="\n                        Hintergrundfarbe des Menüelements.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 49, 12
        ),
    )
)

MenuItem._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "index"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=MenuItem,
        documentation="\n                        Position des Menüelements.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 56, 12
        ),
    )
)

MenuItem._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "menu_item"),
        MenuItem,
        scope=MenuItem,
        documentation="\n                        Untermenüelemente.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 63, 12
        ),
    )
)

MenuItem._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "chart"),
        MenuItemChart,
        scope=MenuItem,
        documentation="\n                        Charts, welche diesem Menüelement zugeordnet sind.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 70, 12
        ),
    )
)


def _BuildAutomaton_10():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 28, 12
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 35, 12
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 63, 12
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 70, 12
        ),
    )
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        MenuItem._UseForTag(pyxb.namespace.ExpandedName(None, "name")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 21, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        MenuItem._UseForTag(pyxb.namespace.ExpandedName(None, "icon")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 28, 12
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        MenuItem._UseForTag(pyxb.namespace.ExpandedName(None, "icon_image")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 35, 12
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        MenuItem._UseForTag(pyxb.namespace.ExpandedName(None, "text_color")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 42, 12
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        MenuItem._UseForTag(pyxb.namespace.ExpandedName(None, "background_color")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 49, 12
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        MenuItem._UseForTag(pyxb.namespace.ExpandedName(None, "index")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 56, 12
        ),
    )
    st_5 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        MenuItem._UseForTag(pyxb.namespace.ExpandedName(None, "menu_item")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 63, 12
        ),
    )
    st_6 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(
        MenuItem._UseForTag(pyxb.namespace.ExpandedName(None, "chart")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 70, 12
        ),
    )
    st_7 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, []))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, []))
    transitions.append(fac.Transition(st_7, []))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_2, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_3, True)]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


MenuItem._Automaton = _BuildAutomaton_10()


Presentation._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "deployment"),
        Deployment,
        scope=Presentation,
        documentation="\n                        Der Standort.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 34, 12
        ),
    )
)

Presentation._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "configuration"),
        Configuration,
        scope=Presentation,
        documentation="\n                        Konfigurationen.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 41, 12
        ),
    )
)

Presentation._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "menu_item"),
        MenuItem,
        scope=Presentation,
        documentation="\n                        Menüelemente.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 48, 12
        ),
    )
)

Presentation._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "playlist"),
        BriefChart,
        scope=Presentation,
        documentation="\n                        Playlist von Chart-Kurzinformationen in Reihenfolge.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 55, 12
        ),
    )
)

Presentation._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "chart"),
        Chart,
        scope=Presentation,
        documentation="\n                        Vollständige Chart-Informationen.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 62, 12
        ),
    )
)


def _BuildAutomaton_11():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 34, 12
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 48, 12
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 55, 12
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 62, 12
        ),
    )
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Presentation._UseForTag(pyxb.namespace.ExpandedName(None, "deployment")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 34, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Presentation._UseForTag(pyxb.namespace.ExpandedName(None, "configuration")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 41, 12
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        Presentation._UseForTag(pyxb.namespace.ExpandedName(None, "menu_item")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 48, 12
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        Presentation._UseForTag(pyxb.namespace.ExpandedName(None, "playlist")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 55, 12
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(
        Presentation._UseForTag(pyxb.namespace.ExpandedName(None, "chart")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/presentation.xsd", 62, 12
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    transitions.append(fac.Transition(st_4, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_2, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_3, True)]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Presentation._Automaton = _BuildAutomaton_11()


RealEstateContact._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "name"),
        pyxb.binding.datatypes.string,
        scope=RealEstateContact,
        documentation='\n                        Der Name der Kontaktperson. Dieser muss mit dem Feld "name" aus OpenImmo übereinstimmen.\n                    ',
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 86, 12
        ),
    )
)

RealEstateContact._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "image"),
        Attachment,
        scope=RealEstateContact,
        documentation="\n                        Das zugehörige Bild.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 93, 12
        ),
    )
)


def _BuildAutomaton_12():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 93, 12
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        RealEstateContact._UseForTag(pyxb.namespace.ExpandedName(None, "name")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 86, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        RealEstateContact._UseForTag(pyxb.namespace.ExpandedName(None, "image")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 93, 12
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


RealEstateContact._Automaton = _BuildAutomaton_12()


TimeInterval._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "value"),
        pyxb.binding.datatypes.integer,
        scope=TimeInterval,
        documentation="\n                        Wert des Intervalls.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 19, 12
        ),
    )
)

TimeInterval._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "unit"),
        pyxb.binding.datatypes.string,
        scope=TimeInterval,
        documentation="\n                        Zeiteinheit des Intervalls.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 26, 12
        ),
    )
)


def _BuildAutomaton_13():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        TimeInterval._UseForTag(pyxb.namespace.ExpandedName(None, "value")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 19, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        TimeInterval._UseForTag(pyxb.namespace.ExpandedName(None, "unit")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 26, 12
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


TimeInterval._Automaton = _BuildAutomaton_13()


Schedule._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "description"),
        pyxb.binding.datatypes.string,
        scope=Schedule,
        documentation="\n                        Eine Beschreibung.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 44, 12
        ),
    )
)

Schedule._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "start"),
        pyxb.binding.datatypes.dateTime,
        scope=Schedule,
        documentation="\n                        Startzeitpunkt.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 51, 12
        ),
    )
)

Schedule._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "end"),
        pyxb.binding.datatypes.dateTime,
        scope=Schedule,
        documentation="\n                        Endzeitpunkt.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 58, 12
        ),
    )
)

Schedule._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "duration"),
        TimeInterval,
        scope=Schedule,
        documentation="\n                        Anzeigedauer.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 65, 12
        ),
    )
)

Schedule._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "interval"),
        TimeInterval,
        scope=Schedule,
        documentation="\n                        Anzeigeintervall.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 72, 12
        ),
    )
)


def _BuildAutomaton_14():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 44, 12
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 58, 12
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Schedule._UseForTag(pyxb.namespace.ExpandedName(None, "description")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 44, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Schedule._UseForTag(pyxb.namespace.ExpandedName(None, "start")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 51, 12
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Schedule._UseForTag(pyxb.namespace.ExpandedName(None, "end")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 58, 12
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Schedule._UseForTag(pyxb.namespace.ExpandedName(None, "duration")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 65, 12
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Schedule._UseForTag(pyxb.namespace.ExpandedName(None, "interval")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/schedule.xsd", 72, 12
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Schedule._Automaton = _BuildAutomaton_14()


Blackboard._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "image"),
        Attachment,
        scope=Blackboard,
        documentation="\n                                Bilder.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 193, 20
        ),
    )
)


def _BuildAutomaton_15():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 193, 20
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Blackboard._UseForTag(pyxb.namespace.ExpandedName(None, "base")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 134, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        Blackboard._UseForTag(pyxb.namespace.ExpandedName(None, "image")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 193, 20
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Blackboard._Automaton = _BuildAutomaton_15()


Cleaning._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "title"),
        pyxb.binding.datatypes.string,
        scope=Cleaning,
        documentation="\n                                Überschrift.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 215, 20
        ),
    )
)

Cleaning._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "mode"),
        pyxb.binding.datatypes.string,
        scope=Cleaning,
        documentation="\n                                Modus des Charts.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 222, 20
        ),
    )
)

Cleaning._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "text"),
        pyxb.binding.datatypes.string,
        scope=Cleaning,
        documentation="\n                                Textinhalt.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 229, 20
        ),
    )
)

Cleaning._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "font_size"),
        pyxb.binding.datatypes.unsignedShort,
        scope=Cleaning,
        documentation="\n                                Schriftgröße.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 236, 20
        ),
    )
)

Cleaning._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "text_color"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=Cleaning,
        documentation="\n                                Textfarbe.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 243, 20
        ),
    )
)


def _BuildAutomaton_16():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 215, 20
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 229, 20
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Cleaning._UseForTag(pyxb.namespace.ExpandedName(None, "base")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 134, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Cleaning._UseForTag(pyxb.namespace.ExpandedName(None, "title")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 215, 20
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Cleaning._UseForTag(pyxb.namespace.ExpandedName(None, "mode")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 222, 20
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Cleaning._UseForTag(pyxb.namespace.ExpandedName(None, "text")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 229, 20
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Cleaning._UseForTag(pyxb.namespace.ExpandedName(None, "font_size")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 236, 20
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Cleaning._UseForTag(pyxb.namespace.ExpandedName(None, "text_color")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 243, 20
        ),
    )
    st_5 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    transitions.append(fac.Transition(st_2, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    transitions.append(fac.Transition(st_4, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, []))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Cleaning._Automaton = _BuildAutomaton_16()


Form._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "mode"),
        pyxb.binding.datatypes.string,
        scope=Form,
        documentation="\n                                Typ (Modus) des Formulars.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 265, 20
        ),
    )
)

Form._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "text"),
        pyxb.binding.datatypes.string,
        scope=Form,
        documentation="\n                                Optionaler Text.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 272, 20
        ),
    )
)

Form._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "choice"),
        Choice,
        scope=Form,
        documentation="\n                                Auswahloptionen.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 279, 20
        ),
    )
)


def _BuildAutomaton_17():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 272, 20
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 279, 20
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Form._UseForTag(pyxb.namespace.ExpandedName(None, "base")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 134, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Form._UseForTag(pyxb.namespace.ExpandedName(None, "mode")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 265, 20
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        Form._UseForTag(pyxb.namespace.ExpandedName(None, "text")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 272, 20
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        Form._UseForTag(pyxb.namespace.ExpandedName(None, "choice")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 279, 20
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, True)]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Form._Automaton = _BuildAutomaton_17()


def _BuildAutomaton_18():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        GarbageCollection._UseForTag(pyxb.namespace.ExpandedName(None, "base")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 134, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


GarbageCollection._Automaton = _BuildAutomaton_18()


def _BuildAutomaton_19():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        GuessPicture._UseForTag(pyxb.namespace.ExpandedName(None, "base")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 134, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


GuessPicture._Automaton = _BuildAutomaton_19()


ImageText._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "title"),
        pyxb.binding.datatypes.string,
        scope=ImageText,
        documentation="\n                                Titel des Charts.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 325, 20
        ),
    )
)

ImageText._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "font_size"),
        pyxb.binding.datatypes.unsignedShort,
        scope=ImageText,
        documentation="\n                                Schriftgröße.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 332, 20
        ),
    )
)

ImageText._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "title_color"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=ImageText,
        documentation="\n                                Titelfarbe.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 339, 20
        ),
    )
)

ImageText._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "ken_burns"),
        pyxb.binding.datatypes.boolean,
        scope=ImageText,
        documentation="\n                                Ken Burns Effekt.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 346, 20
        ),
    )
)

ImageText._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "random_image"),
        pyxb.binding.datatypes.boolean,
        scope=ImageText,
        documentation="\n                                Flag zur Anzeige von zufälligen Bildern.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 353, 20
        ),
    )
)

ImageText._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "image"),
        Attachment,
        scope=ImageText,
        documentation="\n                                Bilder.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 360, 20
        ),
    )
)

ImageText._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "text"),
        pyxb.binding.datatypes.string,
        scope=ImageText,
        documentation="\n                                Texte.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 367, 20
        ),
    )
)


def _BuildAutomaton_20():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 360, 20
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 367, 20
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        ImageText._UseForTag(pyxb.namespace.ExpandedName(None, "base")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 134, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        ImageText._UseForTag(pyxb.namespace.ExpandedName(None, "title")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 325, 20
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        ImageText._UseForTag(pyxb.namespace.ExpandedName(None, "font_size")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 332, 20
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        ImageText._UseForTag(pyxb.namespace.ExpandedName(None, "title_color")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 339, 20
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        ImageText._UseForTag(pyxb.namespace.ExpandedName(None, "ken_burns")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 346, 20
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        ImageText._UseForTag(pyxb.namespace.ExpandedName(None, "random_image")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 353, 20
        ),
    )
    st_5 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        ImageText._UseForTag(pyxb.namespace.ExpandedName(None, "image")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 360, 20
        ),
    )
    st_6 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        ImageText._UseForTag(pyxb.namespace.ExpandedName(None, "text")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 367, 20
        ),
    )
    st_7 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, []))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, []))
    transitions.append(fac.Transition(st_7, []))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_0, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [fac.UpdateInstruction(cc_1, True)]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


ImageText._Automaton = _BuildAutomaton_20()


News._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "font_size_title"),
        pyxb.binding.datatypes.unsignedShort,
        scope=News,
        documentation="\n                                Schriftgröße des Titles.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 389, 20
        ),
    )
)

News._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "title_color"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=News,
        documentation="\n                                Titelfarbe.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 396, 20
        ),
    )
)

News._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "font_size_text"),
        pyxb.binding.datatypes.unsignedShort,
        scope=News,
        documentation="\n                                Schriftgröße des Texts.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 403, 20
        ),
    )
)

News._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "text_color"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=News,
        documentation="\n                                Textfarbe.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 410, 20
        ),
    )
)

News._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "ken_burns"),
        pyxb.binding.datatypes.boolean,
        scope=News,
        documentation="\n                                Ken Burns Effekt.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 417, 20
        ),
    )
)

News._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "provider"),
        pyxb.binding.datatypes.string,
        scope=News,
        documentation="\n                                Provider für diesen news chart.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 424, 20
        ),
    )
)


def _BuildAutomaton_21():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 417, 20
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 424, 20
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        News._UseForTag(pyxb.namespace.ExpandedName(None, "base")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 134, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        News._UseForTag(pyxb.namespace.ExpandedName(None, "font_size_title")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 389, 20
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        News._UseForTag(pyxb.namespace.ExpandedName(None, "title_color")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 396, 20
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        News._UseForTag(pyxb.namespace.ExpandedName(None, "font_size_text")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 403, 20
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        News._UseForTag(pyxb.namespace.ExpandedName(None, "text_color")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 410, 20
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        News._UseForTag(pyxb.namespace.ExpandedName(None, "ken_burns")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 417, 20
        ),
    )
    st_5 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        News._UseForTag(pyxb.namespace.ExpandedName(None, "provider")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 424, 20
        ),
    )
    st_6 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, []))
    transitions.append(fac.Transition(st_6, []))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_0, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [fac.UpdateInstruction(cc_1, True)]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


News._Automaton = _BuildAutomaton_21()


Poll._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "text"),
        pyxb.binding.datatypes.string,
        scope=Poll,
        documentation="\n                                Fragetext.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 446, 20
        ),
    )
)

Poll._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "mode"),
        pyxb.binding.datatypes.string,
        scope=Poll,
        documentation="\n                                Umfragemodus (Single- oder Multiple-Choice).\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 453, 20
        ),
    )
)

Poll._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "option"),
        PollOption,
        scope=Poll,
        documentation="\n                                Antwortoptionen.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 460, 20
        ),
    )
)


def _BuildAutomaton_22():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 460, 20
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Poll._UseForTag(pyxb.namespace.ExpandedName(None, "base")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 134, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Poll._UseForTag(pyxb.namespace.ExpandedName(None, "text")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 446, 20
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Poll._UseForTag(pyxb.namespace.ExpandedName(None, "mode")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 453, 20
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        Poll._UseForTag(pyxb.namespace.ExpandedName(None, "option")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 460, 20
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, True)]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Poll._Automaton = _BuildAutomaton_22()


def _BuildAutomaton_23():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        PublicTransport._UseForTag(pyxb.namespace.ExpandedName(None, "base")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 134, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


PublicTransport._Automaton = _BuildAutomaton_23()


Quotes._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "font_color"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=Quotes,
        documentation="\n                                Schriftfarbe.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 494, 20
        ),
    )
)

Quotes._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "background_color"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=Quotes,
        documentation="\n                                Hintergrundfarbe.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 501, 20
        ),
    )
)

Quotes._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "font_size_quote"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=Quotes,
        documentation="\n                                Textfarbe des Zitats.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 508, 20
        ),
    )
)

Quotes._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "font_size_author"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=Quotes,
        documentation="\n                                Textfarbe des Autors.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 515, 20
        ),
    )
)


def _BuildAutomaton_24():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Quotes._UseForTag(pyxb.namespace.ExpandedName(None, "base")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 134, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Quotes._UseForTag(pyxb.namespace.ExpandedName(None, "font_color")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 494, 20
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Quotes._UseForTag(pyxb.namespace.ExpandedName(None, "background_color")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 501, 20
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Quotes._UseForTag(pyxb.namespace.ExpandedName(None, "font_size_quote")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 508, 20
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Quotes._UseForTag(pyxb.namespace.ExpandedName(None, "font_size_author")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 515, 20
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Quotes._Automaton = _BuildAutomaton_24()


RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "display_format"),
        pyxb.binding.datatypes.string,
        scope=RealEstates,
        documentation="\n                                Anzeigeformat.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 537, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "ken_burns"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        documentation="\n                                Ken Burns Effekt.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 544, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "scaling"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        documentation="\n                                Soll die Application skalieren?\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 551, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "slideshow"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        documentation="\n                                Soll die Application eine Slideshow anzeigen?\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 558, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "qr_codes"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        documentation="\n                                Sollen QR Codes angezeigt werden?\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 565, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "show_contact"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        documentation="\n                                Sollen Kontaktpersonen angezeigt werden?\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 572, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "contact_picture"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        documentation="\n                                Sollen Bilder von Kontaktpersonen angezeigt werden?\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 579, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "font_size"),
        pyxb.binding.datatypes.unsignedShort,
        scope=RealEstates,
        documentation="\n                                Schriftgröße.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 586, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "font_color"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=RealEstates,
        documentation="\n                                Schriftfarbe.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 593, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "data"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=RealEstates,
        documentation="\n                                Schriftfarbe.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 601, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "background_data"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=RealEstates,
        documentation="\n                                Farbe Hintergrund Daten.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 608, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "values"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=RealEstates,
        documentation="\n                                Farbe Werte.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 615, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "background_values"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=RealEstates,
        documentation="\n                                Farbe Hintergrund Werte.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 622, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "amenities_background_even"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=RealEstates,
        documentation="\n                                Farbe Ausstattungen Hintergrund gerade.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 629, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "amenities_text_even"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=RealEstates,
        documentation="\n                                Farbe Ausstattungen Text gerade.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 636, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "amenities_background_uneven"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=RealEstates,
        documentation="\n                                Farbe Ausstattungen Hintergrund ungerade.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 643, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "amenities_text_uneven"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=RealEstates,
        documentation="\n                                Farbe Ausstattungen Text ungerade.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 650, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "amenities"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 658, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "construction"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 659, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "courtage"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 660, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "floor"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 661, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "area"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 662, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "free_from"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 663, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "coop_share"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 664, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "total_area"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 665, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "plot_area"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 666, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "cold_rent"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 667, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "purchase_price"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 668, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "security_deposit"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 669, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "service_charge"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 670, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "object_id"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 671, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "description"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 672, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "warm_rent"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 673, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "rooms"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 674, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "lift"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 676, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "bathtub"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 677, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "balcony"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 678, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "accessibility"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 679, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "assited_living"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 680, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "carport"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 681, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "floorboards"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 682, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "duplex"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 683, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "shower"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 684, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "builtin_kitchen"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 685, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "screed"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 686, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "tiles"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 687, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "outdoor_parking"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 688, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "garage"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 689, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "cable_sat_tv"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 690, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "fireplace"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 691, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "basement"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 692, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "plastic"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 693, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "furnished"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 694, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "parquet"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 695, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "car_park"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 696, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "wheelchair_accessible"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 697, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "sauna"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 698, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "stone"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 699, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "swimming_pool"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 700, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "carpet"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 701, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "underground_carpark"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 702, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "lavatory"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 703, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "rooms_1"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 705, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "rooms_2"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 706, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "rooms_3"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 707, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "rooms_4"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 708, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "rooms_5"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 709, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "rooms_5_or_more"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 710, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "finance_project"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 712, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "business_realty"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 713, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "short_term_accommodation"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 714, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "living_realty"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 715, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "office"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 717, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "retail"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 718, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "recreational"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 719, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "hospitality_industry"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 720, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "plot"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 721, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "hall_warehouse_production"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 722, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "house"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 723, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "agriculture_forestry"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 724, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "miscellaneous"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 725, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "flat"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 726, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "room"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 727, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "income_property"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 728, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "emphyteusis"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 730, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "leasing"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 731, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "rent"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 732, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "sale"),
        pyxb.binding.datatypes.boolean,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 733, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "filter"),
        Filter,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 735, 20
        ),
    )
)

RealEstates._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "contact"),
        RealEstateContact,
        scope=RealEstates,
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 737, 20
        ),
    )
)


def _BuildAutomaton_25():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 735, 20
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 737, 20
        ),
    )
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "base")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 134, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "display_format")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 537, 20
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "ken_burns")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 544, 20
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "scaling")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 551, 20
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "slideshow")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 558, 20
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "qr_codes")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 565, 20
        ),
    )
    st_5 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "show_contact")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 572, 20
        ),
    )
    st_6 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "contact_picture")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 579, 20
        ),
    )
    st_7 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "font_size")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 586, 20
        ),
    )
    st_8 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "font_color")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 593, 20
        ),
    )
    st_9 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "data")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 601, 20
        ),
    )
    st_10 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "background_data")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 608, 20
        ),
    )
    st_11 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "values")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 615, 20
        ),
    )
    st_12 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "background_values")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 622, 20
        ),
    )
    st_13 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(
            pyxb.namespace.ExpandedName(None, "amenities_background_even")
        ),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 629, 20
        ),
    )
    st_14 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(
            pyxb.namespace.ExpandedName(None, "amenities_text_even")
        ),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 636, 20
        ),
    )
    st_15 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(
            pyxb.namespace.ExpandedName(None, "amenities_background_uneven")
        ),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 643, 20
        ),
    )
    st_16 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(
            pyxb.namespace.ExpandedName(None, "amenities_text_uneven")
        ),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 650, 20
        ),
    )
    st_17 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "amenities")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 658, 20
        ),
    )
    st_18 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "construction")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 659, 20
        ),
    )
    st_19 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "courtage")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 660, 20
        ),
    )
    st_20 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_20)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "floor")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 661, 20
        ),
    )
    st_21 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_21)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "area")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 662, 20
        ),
    )
    st_22 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_22)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "free_from")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 663, 20
        ),
    )
    st_23 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_23)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "coop_share")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 664, 20
        ),
    )
    st_24 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_24)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "total_area")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 665, 20
        ),
    )
    st_25 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_25)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "plot_area")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 666, 20
        ),
    )
    st_26 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_26)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "cold_rent")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 667, 20
        ),
    )
    st_27 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_27)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "purchase_price")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 668, 20
        ),
    )
    st_28 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_28)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "security_deposit")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 669, 20
        ),
    )
    st_29 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_29)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "service_charge")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 670, 20
        ),
    )
    st_30 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_30)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "object_id")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 671, 20
        ),
    )
    st_31 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_31)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "description")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 672, 20
        ),
    )
    st_32 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_32)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "warm_rent")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 673, 20
        ),
    )
    st_33 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_33)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "rooms")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 674, 20
        ),
    )
    st_34 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_34)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "lift")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 676, 20
        ),
    )
    st_35 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_35)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "bathtub")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 677, 20
        ),
    )
    st_36 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_36)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "balcony")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 678, 20
        ),
    )
    st_37 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_37)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "accessibility")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 679, 20
        ),
    )
    st_38 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_38)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "assited_living")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 680, 20
        ),
    )
    st_39 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_39)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "carport")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 681, 20
        ),
    )
    st_40 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_40)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "floorboards")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 682, 20
        ),
    )
    st_41 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_41)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "duplex")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 683, 20
        ),
    )
    st_42 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_42)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "shower")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 684, 20
        ),
    )
    st_43 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_43)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "builtin_kitchen")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 685, 20
        ),
    )
    st_44 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_44)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "screed")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 686, 20
        ),
    )
    st_45 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_45)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "tiles")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 687, 20
        ),
    )
    st_46 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_46)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "outdoor_parking")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 688, 20
        ),
    )
    st_47 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_47)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "garage")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 689, 20
        ),
    )
    st_48 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_48)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "cable_sat_tv")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 690, 20
        ),
    )
    st_49 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_49)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "fireplace")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 691, 20
        ),
    )
    st_50 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_50)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "basement")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 692, 20
        ),
    )
    st_51 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_51)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "plastic")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 693, 20
        ),
    )
    st_52 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_52)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "furnished")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 694, 20
        ),
    )
    st_53 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_53)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "parquet")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 695, 20
        ),
    )
    st_54 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_54)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "car_park")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 696, 20
        ),
    )
    st_55 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_55)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(
            pyxb.namespace.ExpandedName(None, "wheelchair_accessible")
        ),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 697, 20
        ),
    )
    st_56 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_56)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "sauna")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 698, 20
        ),
    )
    st_57 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_57)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "stone")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 699, 20
        ),
    )
    st_58 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_58)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "swimming_pool")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 700, 20
        ),
    )
    st_59 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_59)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "carpet")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 701, 20
        ),
    )
    st_60 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_60)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(
            pyxb.namespace.ExpandedName(None, "underground_carpark")
        ),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 702, 20
        ),
    )
    st_61 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_61)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "lavatory")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 703, 20
        ),
    )
    st_62 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_62)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "rooms_1")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 705, 20
        ),
    )
    st_63 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_63)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "rooms_2")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 706, 20
        ),
    )
    st_64 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_64)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "rooms_3")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 707, 20
        ),
    )
    st_65 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_65)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "rooms_4")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 708, 20
        ),
    )
    st_66 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_66)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "rooms_5")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 709, 20
        ),
    )
    st_67 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_67)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "rooms_5_or_more")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 710, 20
        ),
    )
    st_68 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_68)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "finance_project")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 712, 20
        ),
    )
    st_69 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_69)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "business_realty")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 713, 20
        ),
    )
    st_70 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_70)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(
            pyxb.namespace.ExpandedName(None, "short_term_accommodation")
        ),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 714, 20
        ),
    )
    st_71 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_71)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "living_realty")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 715, 20
        ),
    )
    st_72 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_72)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "office")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 717, 20
        ),
    )
    st_73 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_73)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "retail")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 718, 20
        ),
    )
    st_74 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_74)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "recreational")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 719, 20
        ),
    )
    st_75 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_75)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(
            pyxb.namespace.ExpandedName(None, "hospitality_industry")
        ),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 720, 20
        ),
    )
    st_76 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_76)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "plot")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 721, 20
        ),
    )
    st_77 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_77)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(
            pyxb.namespace.ExpandedName(None, "hall_warehouse_production")
        ),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 722, 20
        ),
    )
    st_78 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_78)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "house")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 723, 20
        ),
    )
    st_79 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_79)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(
            pyxb.namespace.ExpandedName(None, "agriculture_forestry")
        ),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 724, 20
        ),
    )
    st_80 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_80)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "miscellaneous")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 725, 20
        ),
    )
    st_81 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_81)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "flat")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 726, 20
        ),
    )
    st_82 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_82)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "room")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 727, 20
        ),
    )
    st_83 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_83)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "income_property")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 728, 20
        ),
    )
    st_84 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_84)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "emphyteusis")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 730, 20
        ),
    )
    st_85 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_85)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "leasing")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 731, 20
        ),
    )
    st_86 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_86)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "rent")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 732, 20
        ),
    )
    st_87 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_87)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "sale")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 733, 20
        ),
    )
    st_88 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_88)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "filter")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 735, 20
        ),
    )
    st_89 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_89)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        RealEstates._UseForTag(pyxb.namespace.ExpandedName(None, "contact")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 737, 20
        ),
    )
    st_90 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_90)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, []))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, []))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, []))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, []))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, []))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, []))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, []))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, []))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, []))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, []))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, []))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, []))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, []))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, []))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, []))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, []))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, []))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, []))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, []))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, []))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, []))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, []))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, []))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, []))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, []))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, []))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_31, []))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, []))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_33, []))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_34, []))
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_35, []))
    st_34._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_36, []))
    st_35._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_37, []))
    st_36._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_38, []))
    st_37._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_39, []))
    st_38._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_40, []))
    st_39._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_41, []))
    st_40._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_42, []))
    st_41._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_43, []))
    st_42._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_44, []))
    st_43._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_45, []))
    st_44._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_46, []))
    st_45._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_47, []))
    st_46._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_48, []))
    st_47._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_49, []))
    st_48._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_50, []))
    st_49._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_51, []))
    st_50._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_52, []))
    st_51._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_53, []))
    st_52._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_54, []))
    st_53._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_55, []))
    st_54._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_56, []))
    st_55._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_57, []))
    st_56._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_58, []))
    st_57._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_59, []))
    st_58._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_60, []))
    st_59._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_61, []))
    st_60._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_62, []))
    st_61._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_63, []))
    st_62._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_64, []))
    st_63._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_65, []))
    st_64._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_66, []))
    st_65._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_67, []))
    st_66._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_68, []))
    st_67._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_69, []))
    st_68._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_70, []))
    st_69._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_71, []))
    st_70._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_72, []))
    st_71._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_73, []))
    st_72._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_74, []))
    st_73._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_75, []))
    st_74._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_76, []))
    st_75._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_77, []))
    st_76._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_78, []))
    st_77._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_79, []))
    st_78._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_80, []))
    st_79._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_81, []))
    st_80._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_82, []))
    st_81._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_83, []))
    st_82._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_84, []))
    st_83._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_85, []))
    st_84._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_86, []))
    st_85._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_87, []))
    st_86._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_88, []))
    st_87._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_89, []))
    transitions.append(fac.Transition(st_90, []))
    st_88._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_89, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_90, [fac.UpdateInstruction(cc_0, False)]))
    st_89._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_90, [fac.UpdateInstruction(cc_1, True)]))
    st_90._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


RealEstates._Automaton = _BuildAutomaton_25()


Booking._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "bookable"),
        pyxb.binding.datatypes.positiveInteger,
        scope=Booking,
        documentation="\n                                Datenbank-IDs der Mietobjekte.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 753, 20
        ),
    )
)

Booking._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "rentee"),
        pyxb.binding.datatypes.boolean,
        scope=Booking,
        documentation="\n                                Schalter für Mieterangabe.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 760, 20
        ),
    )
)

Booking._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "purpose"),
        pyxb.binding.datatypes.boolean,
        scope=Booking,
        documentation="\n                                Schalter für Verwendungszweck.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 767, 20
        ),
    )
)

Booking._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "text"),
        pyxb.binding.datatypes.string,
        scope=Booking,
        documentation="\n                                Textinhalt.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 774, 20
        ),
    )
)


def _BuildAutomaton_26():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 753, 20
        ),
    )
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 760, 20
        ),
    )
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 767, 20
        ),
    )
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 774, 20
        ),
    )
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Booking._UseForTag(pyxb.namespace.ExpandedName(None, "base")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 134, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        Booking._UseForTag(pyxb.namespace.ExpandedName(None, "bookable")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 753, 20
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        Booking._UseForTag(pyxb.namespace.ExpandedName(None, "rentee")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 760, 20
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        Booking._UseForTag(pyxb.namespace.ExpandedName(None, "purpose")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 767, 20
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(
        Booking._UseForTag(pyxb.namespace.ExpandedName(None, "text")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 774, 20
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    transitions.append(fac.Transition(st_2, []))
    transitions.append(fac.Transition(st_3, []))
    transitions.append(fac.Transition(st_4, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_2, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [fac.UpdateInstruction(cc_3, True)]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Booking._Automaton = _BuildAutomaton_26()


SoccerTable._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "font_size_title"),
        pyxb.binding.datatypes.unsignedShort,
        scope=SoccerTable,
        documentation="\n                                Schriftgröße des Titles.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 796, 20
        ),
    )
)

SoccerTable._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "title_color"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=SoccerTable,
        documentation="\n                                Titelfarbe.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 803, 20
        ),
    )
)

SoccerTable._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "font_size_text"),
        pyxb.binding.datatypes.unsignedShort,
        scope=SoccerTable,
        documentation="\n                                Schriftgröße des Texts.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 810, 20
        ),
    )
)

SoccerTable._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "text_color"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=SoccerTable,
        documentation="\n                                Textfarbe.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 817, 20
        ),
    )
)


def _BuildAutomaton_27():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        SoccerTable._UseForTag(pyxb.namespace.ExpandedName(None, "base")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 134, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        SoccerTable._UseForTag(pyxb.namespace.ExpandedName(None, "font_size_title")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 796, 20
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        SoccerTable._UseForTag(pyxb.namespace.ExpandedName(None, "title_color")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 803, 20
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        SoccerTable._UseForTag(pyxb.namespace.ExpandedName(None, "font_size_text")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 810, 20
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        SoccerTable._UseForTag(pyxb.namespace.ExpandedName(None, "text_color")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 817, 20
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


SoccerTable._Automaton = _BuildAutomaton_27()


URL._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "url"),
        pyxb.binding.datatypes.string,
        scope=URL,
        documentation="\n                                RSS Feed URL.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 839, 20
        ),
    )
)

URL._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "mode"),
        pyxb.binding.datatypes.string,
        scope=URL,
        documentation="\n                                Modus des Charts.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 846, 20
        ),
    )
)

URL._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "title_color"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=URL,
        documentation="\n                                Titelfarbe.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 853, 20
        ),
    )
)

URL._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "font_size_title"),
        pyxb.binding.datatypes.unsignedShort,
        scope=URL,
        documentation="\n                                Schriftgröße des Titels.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 860, 20
        ),
    )
)

URL._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "text_color"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=URL,
        documentation="\n                                Schriftfarbe des Texts.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 867, 20
        ),
    )
)

URL._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "font_size_text"),
        pyxb.binding.datatypes.unsignedShort,
        scope=URL,
        documentation="\n                                Schriftgröße des Texts.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 874, 20
        ),
    )
)


def _BuildAutomaton_28():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        URL._UseForTag(pyxb.namespace.ExpandedName(None, "base")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 134, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        URL._UseForTag(pyxb.namespace.ExpandedName(None, "url")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 839, 20
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        URL._UseForTag(pyxb.namespace.ExpandedName(None, "mode")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 846, 20
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        URL._UseForTag(pyxb.namespace.ExpandedName(None, "title_color")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 853, 20
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        URL._UseForTag(pyxb.namespace.ExpandedName(None, "font_size_title")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 860, 20
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        URL._UseForTag(pyxb.namespace.ExpandedName(None, "text_color")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 867, 20
        ),
    )
    st_5 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        URL._UseForTag(pyxb.namespace.ExpandedName(None, "font_size_text")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 874, 20
        ),
    )
    st_6 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, []))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, []))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


URL._Automaton = _BuildAutomaton_28()


Video._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "video"),
        Attachment,
        scope=Video,
        documentation="\n                                Das entsprechende Video.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 896, 20
        ),
    )
)


def _BuildAutomaton_29():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=1,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 896, 20
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Video._UseForTag(pyxb.namespace.ExpandedName(None, "base")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 134, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        Video._UseForTag(pyxb.namespace.ExpandedName(None, "video")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 896, 20
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Video._Automaton = _BuildAutomaton_29()


Weather._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "location"),
        pyxb.binding.datatypes.string,
        scope=Weather,
        documentation="\n                                Ort des Wetters.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 918, 20
        ),
    )
)

Weather._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "font_color"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=Weather,
        documentation="\n                                Schriftfarbe.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 925, 20
        ),
    )
)

Weather._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "icon_color"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=Weather,
        documentation="\n                                Icon Farbe.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 932, 20
        ),
    )
)

Weather._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "box_color_top"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=Weather,
        documentation="\n                                Obere Farbe der Box.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 939, 20
        ),
    )
)

Weather._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "box_color_middle"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=Weather,
        documentation="\n                                Mittlere Farbe der Box.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 946, 20
        ),
    )
)

Weather._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "box_color_bottom"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=Weather,
        documentation="\n                                Untere Farbe der Box.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 953, 20
        ),
    )
)

Weather._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "transparency"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=Weather,
        documentation="\n                                Transparenz.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 960, 20
        ),
    )
)

Weather._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "image"),
        Attachment,
        scope=Weather,
        documentation="\n                                Bilder.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 967, 20
        ),
    )
)


def _BuildAutomaton_30():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 967, 20
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Weather._UseForTag(pyxb.namespace.ExpandedName(None, "base")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 134, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Weather._UseForTag(pyxb.namespace.ExpandedName(None, "location")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 918, 20
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Weather._UseForTag(pyxb.namespace.ExpandedName(None, "font_color")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 925, 20
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Weather._UseForTag(pyxb.namespace.ExpandedName(None, "icon_color")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 932, 20
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Weather._UseForTag(pyxb.namespace.ExpandedName(None, "box_color_top")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 939, 20
        ),
    )
    st_4 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Weather._UseForTag(pyxb.namespace.ExpandedName(None, "box_color_middle")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 946, 20
        ),
    )
    st_5 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Weather._UseForTag(pyxb.namespace.ExpandedName(None, "box_color_bottom")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 953, 20
        ),
    )
    st_6 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Weather._UseForTag(pyxb.namespace.ExpandedName(None, "transparency")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 960, 20
        ),
    )
    st_7 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        Weather._UseForTag(pyxb.namespace.ExpandedName(None, "image")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 967, 20
        ),
    )
    st_8 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, []))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, []))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, []))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, []))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, []))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [fac.UpdateInstruction(cc_0, True)]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Weather._Automaton = _BuildAutomaton_30()


MenuItemChart._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "index"),
        pyxb.binding.datatypes.nonNegativeInteger,
        scope=MenuItemChart,
        documentation="\n                                Position des Charts.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 90, 20
        ),
    )
)


def _BuildAutomaton_31():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        MenuItemChart._UseForTag(pyxb.namespace.ExpandedName(None, "id")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 166, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        MenuItemChart._UseForTag(pyxb.namespace.ExpandedName(None, "type")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/charts.xsd", 173, 12
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        MenuItemChart._UseForTag(pyxb.namespace.ExpandedName(None, "index")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/menu.xsd", 90, 20
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


MenuItemChart._Automaton = _BuildAutomaton_31()


IdFilter._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "value"),
        pyxb.binding.datatypes.string,
        scope=IdFilter,
        documentation="\n                                Wert der ID.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 30, 20
        ),
    )
)

IdFilter._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "type"),
        pyxb.binding.datatypes.string,
        scope=IdFilter,
        documentation="\n                                Typ der ID.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 37, 20
        ),
    )
)


def _BuildAutomaton_32():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        IdFilter._UseForTag(pyxb.namespace.ExpandedName(None, "value")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 30, 20
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        IdFilter._UseForTag(pyxb.namespace.ExpandedName(None, "type")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 37, 20
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


IdFilter._Automaton = _BuildAutomaton_32()


ZipCodeFilter._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "zip_code"),
        pyxb.binding.datatypes.string,
        scope=ZipCodeFilter,
        documentation="\n                                Postleitzahl.\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 59, 20
        ),
    )
)

ZipCodeFilter._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "blacklist"),
        pyxb.binding.datatypes.boolean,
        scope=ZipCodeFilter,
        documentation="\n                                Handelt es sich um eine Blacklist (true) oder Whitelist(false)?\n                            ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 66, 20
        ),
    )
)


def _BuildAutomaton_33():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        ZipCodeFilter._UseForTag(pyxb.namespace.ExpandedName(None, "zip_code")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 59, 20
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        ZipCodeFilter._UseForTag(pyxb.namespace.ExpandedName(None, "blacklist")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/cmslib/xsd/realestates.xsd", 66, 20
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


ZipCodeFilter._Automaton = _BuildAutomaton_33()
