

import requests


class Storage(object):

    def __init__(self, app_id):
        self.__url = 'https://%s.data.thethingsnetwork.org/api/v2/' % app_id

    def set_credential(self, app_access_key):
        self.__app_access_key = 'key %s' % app_access_key

    def __get_credential(self):
        headers = {
                'Accept': 'application/json',
                'Authorization': self.__app_access_key
                }
        return headers

    def __request(self, endpoint, params):
        full_url = '%s%s' % (self.__url, endpoint)
        headers = self.__get_credential()
        r = requests.get(full_url, headers=headers, params=params)
        response_code = r.status_code
        if response_code != 200:
            raise Exception('Exception response code: %d' % response_code)
        return r.json()

    def devices(self):
        params = {}
        return self.__request('devices', params)

    def query(self, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('query', params)

    def query_device(self, device_id, **kwargs):
        params = {}
        params.update(kwargs)
        return self.__request('query/%s' % device_id, params)

