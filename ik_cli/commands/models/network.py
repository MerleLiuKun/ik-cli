"""
    response models
"""
import json


class IpInfo:
    # info fields
    __attrs__ = [
        'asn', 'city', 'continent_code', 'country', 'country_code',
        'ip', 'latitude', 'longitude', 'organization', 'postal_code',
        'region', 'region_code', 'timezone'
    ]

    def __init__(self, **kwargs):
        for attr in self.__attrs__:
            setattr(self, attr, kwargs.get(attr, ''))

    def __repr__(self) -> str:
        return f"IpInfo(ip={self.ip})"

    @classmethod
    def build_info(cls, json_data: dict):
        """
        data example:
        {
            "asn": 16509,
            "city": "Singapore",
            "continent_code": "AS",
            "country": "Singapore",
            "country_code": "SG",
            "ip": "52.74.223.119",
            "latitude": 1.2929,
            "longitude": 103.8547,
            "offset": 28800,
            "organization": "Amazon.com, Inc.",
            "timezone": "Asia/Singapore"
        }
        from response data to build data model
        :param json_data: response data from ip.sb api.
        """
        c = cls(**json_data)
        return c

    def as_dict(self):
        data = {}
        for key in self.__attrs__:
            attr = getattr(self, key, '')
            data[key] = attr
        return data

    def as_json(self):
        return json.dumps(self.as_dict(), sort_keys=True)


if __name__ == '__main__':
    d = {
        "asn": 15169,
        "continent_code": "NA",
        "country": "United States",
        "country_code": "US",
        "ip": "8.8.8.8",
        "latitude": 37.751,
        "longitude": -97.822,
        "offset": -21600,
        "organization": "Google LLC",
        "timezone": "America/Chicago"
    }

    ip_info = IpInfo.build_info(d)
    print(ip_info.as_json())
