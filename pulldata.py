# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 12:18:41 2016

@author: ryan
"""

import requests
import json

appid =  10

def get_app_price(appid):
    '''
    Return price_dict, a dictionary of prices, which will have the keys:
    'discount_percent' (value: int between 0 and 100)
    'currency' (value: string such as 'USD')
    'final' (value: int where the value is a price times 10**2)
    'initial' (value: int, with the same convetion as 'final')
    '''
    
    request_url = "http://store.steampowered.com/api/appdetails/?appids=%d" % appid    
    r = requests.get(request_url)
    if r.status_code == 200:
        page_info = r.text
        page_dict = json.loads(page_info)
        price_dict = page_dict[str(appid)]['data']['price_overview']
    else:
        print('status code %d' % r.status_code)
        #institute a logger here
        
    return price_dict
    #log the status code here
    

