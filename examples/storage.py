#!/usr/bin/env python


import ttnc
import json


def d(j):
    print (json.dumps(j, sort_keys=True, indent=4, separators=(',', ': ')))

def main():
    app_id = ''
    app_access_key = ''
    device_id = ''
    api = ttnc.Storage(app_id)
    api.set_credential(app_access_key)
    d(api.devices())
#    d(api.query(last='1h'))
#    d(api.query_device(device_id, last='1h'))

if __name__ == '__main__':
    main()

