import os
import httpx

PROPERTY_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/properties/'


def is_property_present(property_id: int):
    url = os.environ.get('PROPERTY_SERVICE_HOST_URL') or PROPERTY_SERVICE_HOST_URL
    r = httpx.get(f'{url}{property_id}')
    return True if r.status_code == 200 else False