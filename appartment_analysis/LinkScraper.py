from bs4 import BeautifulSoup

# Class for Scraping the links from the wg-gesucht website
class LinkScraper():
    def __init__(self):
        self.non_spons_links_pp = [] # non sponsored links per page
        self.spons_links_pp = [] # sponsored links per page
    
    def get_non_spons_links(self, soup):
        elements = soup.find_all('h3', class_ = "truncate_title noprint")
        non_spons_links = []
        for element in elements:
            # Filtering for the non sponsored appartments
            for appartment in element.find_all('a', class_=''):
                non_spons_links.append(element.find('a').get('href'))
        self.non_spons_links_pp = non_spons_links
    
    def get_spons_links(self, soup):
        elements = soup.find_all('h3', class_ = "truncate_title noprint")
        spons_links = []
        for element in elements:
            # Filtering for the sponsored appartments
            for appartment in element.find_all('a', class_="campaign_click"):
                spons_links.append(element.find('a').get('href'))
        self.spons_links_pp = spons_links

