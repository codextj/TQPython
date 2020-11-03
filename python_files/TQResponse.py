# TreasuryQuants.com Ltd.
# email: contact@treasuryquants.com
# Note: this software is provided "as-is" under the agreed terms of your account.
#       For more information see https://treasuryquants.com/terms-of-services/
from xml.etree import ElementTree as ET


class Response:
    def __init__(self):
        self.focus=""
        self.id=""
        self.cost=""
        self.balance=""
        self.expiry_minutes=""
        self.results={}
        self.errors={}
        self.logs={} #curenctly not used
        self.notes=[]#curenctly not used

    def fromXml(self, string_xml):
        store_element = ET.fromstring(string_xml)
        response_element=store_element[0]
        self.cost=float(response_element.attrib['cost'])
        self.balance=float(response_element.attrib['balance'])
        self.focus=response_element.attrib['focus']
        self.id=response_element.attrib['id']
        self.expiry_minutes=float(response_element.attrib['expiry_minutes'])
        result_elements=store_element.findall('./Response/Results/Item')
        if result_elements is not None:
            for node in result_elements:
                tokens=node.text.split('=')
                self.results[tokens[0]]=tokens[1]

        error_elements=store_element.findall('./Response/Errors/Item')
        if error_elements is not None:
            for node in error_elements:
                tokens=node.text.split('=')
                self.errors[tokens[0]]=tokens[1]

        log_elements=store_element.findall('./Response/Logs/Item')
        if log_elements is not None:
            for node in log_elements:
                tokens=node.text.split('=')
                self.logs[tokens[0]]=tokens[1]

        error_elements=store_element.findall('./Response/Note/Item')
        if error_elements is not None:
            for node in error_elements:
                self.notes.append(node.text)
        return


class Store:
    def __init__(self):
        self.client_id = ""
        self.session_id = ""
        self.id = ""
        self.version = ""
        self.note = ""
        self.source_id = ""
        self.response=Response()
    def fromXml(self, string_xml):
        store_element = ET.fromstring(string_xml)
        self.client_id=store_element.attrib["client_id"]
        self.session_id=store_element.attrib["session_id"]
        self.id=store_element.attrib["id"]
        self.version=store_element.attrib["version"]
        self.note=store_element.attrib["note"]
        self.source_id=store_element.attrib["source_id"]
        self.response.fromXml(string_xml)