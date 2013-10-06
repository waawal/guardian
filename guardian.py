import requests

class Guardian(object):
    ITEM = 'http://content.guardianapis.com/'
    SEARCH = 'http://content.guardianapis.com/search'
    TAGS = 'http://content.guardianapis.com/tags'
    def __init__(self, key=None):
        self.key = key

    def item(self, id, **kw):
        payload = {}
        for k, v in kw.items():
            payload[k.replace('_','-')] = v
        return requests.get(self.ITEM+id, params=payload).json()['response'].get('content')

    def search(self, q=None, **kw):
        if  q is None:
            payload = {}   
        else:
            payload = {'q': q}
        for k, v in kw.items():
            payload[k.replace('_','-')] = v
        return requests.get(self.SEARCH, params=payload).json()['response'].get('results')

    def tags(self, **kw):
        payload = {}
        for k, v in kw.items():
            payload[k.replace('_','-')] = v
        return requests.get(self.TAGS, params=payload).json()['response'].get('results')

    def __call__(self, q, **kw):
        return self.search(q=q, **kw)

