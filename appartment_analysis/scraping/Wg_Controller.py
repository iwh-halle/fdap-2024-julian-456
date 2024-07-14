import json
from bs4 import BeautifulSoup
from scraper import Scraper
from AppartScraper import AppartScraper
from LinkScraper import LinkScraper

# Main class 
class Wg_Controller():
    def __init__(self):
        self.non_spons_links = {}
        self.appart_dict = {}
        self.skipped_links = []
        self.failed_links = []
    
    def get_non_spons_links(self, url, start, stop):
        """
        Retrieves non-sponsored links from a given WG-gesucht-URL.

        Args:
            url (str): The base URL.
            start (int): The starting page number.
            stop (int): The ending page number.

        Returns:
            None

        Raises:
            None
        """
        scraper = Scraper()
        link_scr = LinkScraper()

        # Splitting the url to put in the pages
        segments = url.rsplit('.', 2)

        for page in range(start, stop):
            # Creating the new url
            new_url = f"{segments[0]}.{page}" + '.html'

            # Getting the response and the soup
            response = scraper.get_page(new_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Getting the non sponsored links
            link_scr.get_non_spons_links(soup)
            self.non_spons_links.update({page: link_scr.non_spons_links_pp}) 
        self.save_appart_links()
    
    def save_appart_links(self):
        # saving the non_spons_links to a json file
        with open('appartment_analysis\\data\\scraped\\non_spons_links.json', 'w') as json_file:
            json.dump(self.non_spons_links, json_file, indent=4)
    
    def load_non_spons_links(self):
        # loading the non_spons_links from a json file
        with open('appartment_analysis\\data\\scraped\\non_spons_links.json', 'r') as json_file:
            self.non_spons_links = json.load(json_file)

    def get_app_info(self):
        try:
            scraper = Scraper()
            for page, links in self.non_spons_links.items():
                if int(page) > 54: # first 55 pages
                    break
    
                for link in links:
                    new_link = 'https://www.wg-gesucht.de' + link
                    response = scraper.get_page(new_link)
                    if response.status_code == 200:
                        try: 
                            soup = BeautifulSoup(response.text, 'html.parser')
                            appart_scraper = AppartScraper(soup, new_link)
                            appart_scraper.get_all()
                            self.appart_dict.update({new_link: appart_scraper.result_dict})
                            print(f"Got the page: {new_link}")
                        except Exception as e:
                            self.failed_links.append(new_link)
                            print(f"Failed to get the data: {new_link}")
                    else:
                        self.skipped_links.append(new_link)
                        print(f"Failed to get the page: {new_link}")
                        print(f"Status code: {response.status_code}")
                        break
        except Exception as e:
            print(f"Error: {e}")
            print(page, link)
        finally:
            self.save_appart_info()
        
    
    def save_appart_info(self):
        # saving the non_spons_links to a json file
        with open('appartment_analysis\\data\\scraped\\appart_info.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.appart_dict, json_file, ensure_ascii=False, indent=4)

        with open('appartment_analysis\\data\\scraped\\skipped_links.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.skipped_links, json_file, ensure_ascii=False, indent=4)
        
        with open('appartment_analysis\\data\\scraped\\failed_links.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.failed_links, json_file, ensure_ascii=False, indent=4)



# Usage:

# Collecting the links
controller = Wg_Controller()
controller.get_non_spons_links("https://www.wg-gesucht.de/wg-zimmer-in-Koeln.73.0.1.0.html", 0, 55)


# Collecting the appartment info
controller = Wg_Controller()
controller.load_non_spons_links()
controller.get_app_info()
