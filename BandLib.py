# gene8192@live.com
# BandAPI Module - https://developers.band.us/

import json
from urllib import request
from urllib import parse

class Band:
    def __init__(self, token):
        self.token = token
        self.__bandkey = 0
    
    @property
    def bandkey(self):
        return self.__bandkey
    
    @bandkey.setter
    def bandkey(self, value):
        self.__bandkey = value
     
      
    def get_bands(self):    
        url = f'https://openapi.band.us/v2.1/bands?access_token={self.token}'
        req = request.Request(url)
        res = request.urlopen(req)
        decoded = res.read().decode('UTF-8')
        json_dict = json.loads(decoded)
        return json_dict


    def get_posts(self, paging_post_dict):
        url = f'https://openapi.band.us/v2/band/posts'
        req = request.Request(url)

        if paging_post_dict == None:
            data = {'access_token': self.token, 'band_key': self.bandkey, 'locale': 'ko_KR'}
        else:
            data = paging_post_dict

        post_data = parse.urlencode(data).encode('UTF-8')
        res = request.urlopen(req, post_data)
        decoded = res.read().decode('UTF-8')
        json_dict = json.loads(decoded)
        return json_dict


    def get_comments(self, content_post_key, paging_comment_dict):
        url = f'https://openapi.band.us/v2/band/post/comments'
        req = request.Request(url)

        if paging_comment_dict == None:
            data = {'access_token': self.token, 'band_key': self.bandkey, 'post_key': content_post_key}
        else:
            data = paging_comment_dict

        post_data = parse.urlencode(data).encode('UTF-8')
        res = request.urlopen(req, post_data)
        decoded = res.read().decode('UTF-8')
        json_dict = json.loads(decoded)
        return json_dict


    def create_post(self, band_Key, content, do_push=True):
        url = f'https://openapi.band.us/v2.2/band/post/create'
        req = request.Request(url)
        data = {'access_token': self.token, 'band_key': band_Key, 'content':content, 'do_push':do_push}
        post_data = parse.urlencode(data).encode('UTF-8')
        res = request.urlopen(req, post_data)
        decoded = res.read().decode('UTF-8')
        json_dict = json.loads(decoded)
        return json_dict
