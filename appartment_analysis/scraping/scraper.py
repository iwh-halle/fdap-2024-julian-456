import configparser
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import os




class Scraper():
    def __init__(self):
        self.scraper_api_key = self.set_api_param()
        self.fail_counter = 0
        
    def set_api_param(self):
        config = configparser.ConfigParser()
        ini_path = os.path.join(os.getcwd(), 'appartment_analysis\\','local.ini')
        config.read(ini_path)
        return config['scraperapi']['key'].strip()

    def get_page_via_api(self, url):
        payload = {'api_key': self.scraper_api_key, 'url': url}
        response = requests.get('http://api.scraperapi.com', params=payload)
        return response
    
    def get_page_via_direct_call(self, url):
        response = requests.get(url, allow_redirects=False)
        return response
    
    def get_page(self, url):
        if self.fail_counter < 5:
            response = self.get_page_via_direct_call(url)
            if response.status_code == 200:
                return response
            else:
                print('Failed to get the page')
                self.fail_counter += 1
                response = self.get_page_via_api(url)
                return response
        else:
            response = self.get_page_via_api(url)
            return response
    
    

    

# Testing the Scraper()
# test = Scraper()
# test_response = test.get_page_direct("https://www.wg-gesucht.de/wg-zimmer-in-Koeln.73.0.1.0.html")
# print(test_response.status_code)
# test.collect_non_spons_links_from_response(test_response)
# print(test.non_spons_links)
# print(len(test.non_spons_links))