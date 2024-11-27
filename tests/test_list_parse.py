import os
from lxml import etree
from shareplumfreightplusio.list import _List2007

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def test_xml_with_validation():
    with open(os.path.join(__location__, "data", "validation.xml")) as f:
        xml: str = f.read()
    envelope: etree.ElementTree = etree.fromstring(xml.encode("utf-8"), parser=etree.XMLParser(huge_tree=True, recover=True))
    fields, regional_settings, server_settings = _List2007.parse_list_envelope(envelope)
    print(fields)
    assert len(fields) > 0


def test_xml_sharepoint_2010():
    with open(os.path.join(__location__, "data", "2010xml.xml")) as f:
        xml: str = f.read()
    envelope: etree.ElementTree = etree.fromstring(xml.encode("utf-8"), parser=etree.XMLParser(huge_tree=True, recover=True))
    fields, regional_settings, server_settings = _List2007.parse_list_envelope(envelope)
    print(fields)
    assert len(fields) > 0
