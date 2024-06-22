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
        with open('appartment_analysis\\non_spons_links.json', 'w') as json_file:
            json.dump(self.non_spons_links, json_file, indent=4)
    
    def load_non_spons_links(self):
        # loading the non_spons_links from a json file
        with open('appartment_analysis\\non_spons_links.json', 'r') as json_file:
            self.non_spons_links = json.load(json_file)

    def get_app_info(self):
        scraper = Scraper()
        for page, links in self.non_spons_links.items():
            if int(page) > 2: # first 2 pages
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
                        print(f"Failed get the data: {new_link}")
                else:
                    self.skipped_links.append(new_link)
                    print(f"Failed to get the page: {new_link}")
                    print(f"Status code: {response.status_code}")
                    break
    

        # link_1 = 'https://www.wg-gesucht.de' + self.non_spons_links["0"][0]
        # response_1 =scraper.get_page(link_1)
        # soup_1 = BeautifulSoup(response_1.text, 'html.parser')
        # appart_scraper = AppartScraper(soup_1, link_1)
        # appart_scraper.get_icons()
        # dict_1 = appart_scraper.result_dict
        # # print(dict_1)

        # link_2 = 'https://www.wg-gesucht.de' + self.non_spons_links["0"][1]
        # response_2 =scraper.get_page(link_2)
        # soup_2 = BeautifulSoup(response_2.text, 'html.parser')
        # appart_scraper = AppartScraper(soup_2, link_2)
        # appart_scraper.get_icons()
        # dict_2 = appart_scraper.result_dict
        # # print(dict_2)

        # ges.update({link_1: dict_1})
        # print(ges)
        self.save_appart_info()
        
    
    def save_appart_info(self):
        # saving the non_spons_links to a json file
        with open('appartment_analysis\\appart_info.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.appart_dict, json_file, ensure_ascii=False, indent=4)



                
    
        
    



# Testing the Wg_Controller()
# controller = Wg_Controller()
# scraper = Scraper()
# link = "https://www.wg-gesucht.de/wg-zimmer-in-Koeln.73.0.1.0.html"
# response = scraper.get_page_direct(link)
# soup = BeautifulSoup(response.text, 'html.parser')
# link_scr = LinkScraper()
# link_scr.get_non_spons_links(soup)
# controller.non_spons_links = controller.non_spons_links + link_scr.non_spons_links_pp
# print(controller.non_spons_links)

#Testing get_non_spons_links
# controller = Wg_Controller()
# controller.get_non_spons_links("https://www.wg-gesucht.de/wg-zimmer-in-Koeln.73.0.1.0.html", 0, 40)
# print(controller.non_spons_links)
# print(len(controller.non_spons_links))

# Testing get_app_info
controller = Wg_Controller()
controller.load_non_spons_links()
# print(controller.non_spons_links)
controller.get_app_info()
