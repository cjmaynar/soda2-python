import json
import requests
from urllib import urlencode
from urlparse import urljoin

class Socrata(object):
    '''A wrapper for the SODA 2.0 API by Socrata'''
    def __init__(self, host, username, password, token):
        self.host = host
        self.username = username
        self.password = password
        self.token = token
        self.resource = None

    def _request(self, params = {}, type = 'GET'):
        '''Private function, handles the guts of sending requests'''
        if self.resource == None:
            raise Exception("Must provide a resource")

        client = getattr(requests, type.lower())
        uri = urljoin(self.host, self.resource)
        uri += "?"

        for param, value in params.iteritems():
            uri += "$%s=%s&" % (param, value)
        uri = uri[:-1]

        headers = {'Content-type': 'application/json', 'X-App-Token': self.token }
        response = client(uri, headers = headers, auth = (self.username, self.password))
        content = response.text

        if content != None and len(content) > 0:
            response_parased = json.loads(content)
            return response_parased

        return None

    def setDataset(self, resource):
        '''Generates the resource string to identify which dataset will be queried against.
        Required to be set before calling any requests, otherwise an exception will be
        thrown.'''
        self.resource = 'resource/%s.json' % resource

    def get(self, params = {}):
        '''Perform a GET request against the data source. Example of parameters are
        limit and offset'''
        return self._request(params)
