"""
    test for models
"""
import json
import unittest

from ik_cli.commands.models import IpInfo


class IpInfoTest(unittest.TestCase):
    RESPONSE_DATA = (
        '{"asn": 15169, "city": "", "continent_code": "NA", "country": '
        '"United States", "country_code": "US", "ip": "8.8.8.8", '
        '"latitude": 37.751, "longitude": -97.822, "organization": "Google LLC", '
        '"postal_code": "", "region": "", "region_code": "", "timezone": "America/Chicago"}'
    )

    def setUp(self) -> None:
        self.ip_info = self._load_data()

    def _load_data(self) -> type(IpInfo):
        return IpInfo.build_info(
            json_data=json.loads(self.RESPONSE_DATA)
        )

    def testProperties(self):
        self.assertEqual(15169, self.ip_info.asn)

    def testAsDict(self):
        ip_info = self.ip_info.as_dict()
        self.assertEqual('8.8.8.8', ip_info['ip'])

    def testAsJson(self):
        json_data = self.ip_info.as_json()
        self.assertEqual(self.RESPONSE_DATA, json_data)
