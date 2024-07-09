import numpy as np
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

# class for scraping a specific appartment
class AppartScraper():
    def __init__(self, soup, url):
        self.result_dict = {} # self.result_dict = {url: url}
        self.soup = soup
    
    def get_flatmates(self):
        flatmate_span = self.soup.find('span', class_='mr5')
        # print(flatmate_span)
        flatmate_title = flatmate_span['title']

        # Regular expression to find the size of the WG (e.g., "3er WG")
        wg_size_pattern = re.compile(r'(\d+)er WG')
        wg_size_match = wg_size_pattern.search(flatmate_title)
        
        # If a match is found, extract the number of flatmates
        if wg_size_match:
            wg_size = int(wg_size_match.group(1))
        else:
            wg_size = np.nan
        
        # Regular expression to find all groups (number and gender)
        pattern = re.compile(r'(\d+)([wmd])')
        # Find all matches in the input string
        matches = pattern.findall(flatmate_title)
        
        total_people = 0
        gender_counts = {'w': 0, 'm': 0, 'd': 0}
        
        # Iterate over all matches and count the total number of people and the number
        for count, gender in matches:
            count = int(count)
            total_people += count
            if gender in gender_counts:
                gender_counts[gender] += count
        
        # Add the results to the DataFrame
        self.result_dict.update({'WG_Size': wg_size, 'Total_People': total_people})
        self.result_dict.update(gender_counts)
         
    
    def get_base_info(self):
        title = self.soup.find('h1', class_='headline headline-detailed-view-title').text
        title = title.replace('\n', '').strip()
        self.result_dict.update({'Title': title})

        size = self.soup.find('b', class_='key_fact_value').text
        size = size.replace('\n', '').strip()
        self.result_dict.update({'Size': size})
        
    
    def get_price(self):
        cost_panel = self.soup.find_all('div', class_='panel section_panel')[1]

        rent = cost_panel.find_all('span', class_='section_panel_value')[0].text
        rent = rent.replace('\n', '').strip()
        self.result_dict.update({'Rent': rent})

        extra_costs = cost_panel.find_all('span', class_='section_panel_value')[1].text
        extra_costs = extra_costs.replace('\n', '').strip()
        self.result_dict.update({'Extra_Costs': extra_costs})

        other_costs = cost_panel.find_all('span', class_='section_panel_value')[2].text
        other_costs = other_costs.replace('\n', '').strip()
        self.result_dict.update({'Other_Costs': other_costs})

        deposit = cost_panel.find_all('span', class_='section_panel_value')[3].text
        deposit = deposit.replace('\n', '').strip()
        self.result_dict.update({'Deposit': deposit})

        redemption_agreement = cost_panel.find_all('span', class_='section_panel_value')[4].text
        redemption_agreement = redemption_agreement.replace('\n', '').strip()
        self.result_dict.update({'Redemption_Agreement': redemption_agreement})
        
    
    def get_address(self):
        address_panel = self.soup.find_all('div', class_='panel section_panel')[2]

        address = address_panel.find_all('span', class_='section_panel_detail')[0].text
        address = ' '.join(address.split())
        self.result_dict.update({'Address': address})
        
    
    def get_availability(self):
        address_panel = self.soup.find_all('div', class_='panel section_panel')[2]
        available_from = address_panel.find_all('span', class_='section_panel_value')[0].text
        available_from = available_from.replace('\n', '').strip()
        self.result_dict.update({'Available_From': available_from})

        # Sometimes the available till is not available, so we need to check if the second span is 'frei bis:' --> if not we need to set it to n.a.
        if address_panel.find_all('span', class_='section_panel_detail')[2].text.strip() == 'frei bis:':
            available_till = address_panel.find_all('span', class_='section_panel_value')[1].text
            available_till = available_till.replace('\n', '').strip()
            online_since = address_panel.find_all('b', class_='noprint')[0].text
            online_since = online_since.replace('\n', '').strip()

        else:
            available_till = "n.a."
            online_since = address_panel.find_all('b', class_='noprint')[0].text
            online_since = online_since.replace('\n', '').strip()
        
        self.result_dict.update({'Available_Till': available_till, 'Online_Since': online_since})
    
    def get_search_info(self):
        headline = self.soup.find('h4', class_='headline pb0', string = re.compile(r'Gesucht wird:'))
        # Finde das nächste span-Element mit der Klasse "section_panel_detail" nach der Überschrift
        if headline:
            section_detail = headline.find_next('span', class_='section_panel_detail')
            if section_detail:
                # Extrahiere den Text und entferne unnötige Leerzeichen
                search_text = section_detail.get_text().replace('\n', '').strip()
                search_text = ' '.join(search_text.split())
                self.result_dict.update({'Search_Info': search_text})
            else:
                self.result_dict.update({'Search_Info': np.nan})
        else:
            self.result_dict.update({'Search_Info': np.nan})
    
    def get_icons(self):
        headline = self.soup.find('div', class_='utility_icons')
        if headline:
            feature_set = set()
            features = headline.find_all('div', class_='text-center')

            for feature in features:
                text = feature.get_text(strip=True)
                split_text = [t.strip() for t in text.split(',')]
                feature_set.update(split_text)
                
            self.result_dict.update({feature: 1 for feature in feature_set})
        else:
            print("Es wurden keine Features gefunden.")
    
    def get_docs(self):
        headline = self.soup.find('h3', class_='headline section_panel_title', string = re.compile(r'Benötigte Unterlagen'))

        # Finde das nächste span-Element mit der Klasse "section_panel_detail" nach der Überschrift
        if headline:
            test = True
            while test:
                ben_Unt = headline.find_next('b', class_='font-12px text-decoration-underline')
                if ben_Unt:
                    # Extrahiere den Text und entferne unnötige Leerzeichen
                    text = ben_Unt.get_text(strip=True)
                    self.result_dict.update({text: 1})
                    headline = ben_Unt
                else:
                    test = False
            
        else:
            print("No documents needed.")
    
    def get_wg_details(self):
        detail_list = []
        detail_dic = {}
        details = self.soup.find_all('ul', class_='pl15 mb15')
        for detail in details:
            spans = detail.find_all('span')
            detail_list.extend(spans)
        details

        for span in detail_list:
            span = span.text.replace('\n', '').strip()
            span = re.sub(r'\s+', ' ', span)
            
            if 'rauchen' in span.lower():
                detail_dic.update({'Rauchen': span}) 
            
            if 'alter' in span.lower():
                detail_dic.update({'Alter': span})
            
            if 'wohnungsgröße' in span.lower():
                detail_dic.update({'Wohnungsgröße': span})
            
            if 'sprache/n' in span.lower():
                detail_dic.update({'Sprache/n': span})
            
            if ('zweck-wg'  in span.lower()) or ('zweck wg' in span.lower()) or ('zweckgemeinschaft' in span.lower()):
                detail_dic.update({'Zweck-WG': 1})

            if ('frauen-wg' in span.lower()) or ('frauen wg' in span.lower()) or ('mädels wg' in span.lower()) or ('mädels-wg' in span.lower()):
                detail_dic.update({'Frauen-WG': 1})
            
            if ('männer-wg' in span.lower()) or ('männer wg' in span.lower()) or ('jungs wg' in span.lower()) or ('jungs-wg' in span.lower()):
                detail_dic.update({'Männer-WG': 1})
            
            if ('berufstätigen-wg' in span.lower()) or ('berufstätigen wg' in span.lower()) or ('berufstätige wg' in span.lower()) or ('berufstätige-wg' in span.lower()):
                detail_dic.update({'Berufstätigen-WG': 1})
            
            if ('gemischte wg' in span.lower()) or ('gemischte-wg' in span.lower()):
                detail_dic.update({'gemischte-WG': 1})

            if ('studenten-wg' in span.lower()) or ('studenten wg' in span.lower()) or ('studentinnen wg' in span.lower()) or ('studentinnen-wg' in span.lower()):
                detail_dic.update({'Studenten-WG': 1})
            
            if ('keine zweck-wg' in span.lower()) or ('keine zweck wg' in span.lower()) or ('keine zweckgemeinschaft' in span.lower()):
                detail_dic.update({'Zweck-WG': 0})
            
            if ('verbindung' in span.lower()):
                detail_dic.update({'Verbindung': 1})

            if('azubi-wg' in span.lower()) or ('azubi wg' in span.lower()) or ('azubis wg' in span.lower()) or ('azubis-wg' in span.lower()):
                detail_dic.update({'Azubi-WG': 1})
            
            if ('lgbtq' in span.lower()) or ('queer' in span.lower()):
                detail_dic.update({'LGBTQ': 1})

        self.result_dict.update(detail_dic)
    
    def get_freitext(self):
        freitext_names = []
        # Not all appartments have the same number of descriptions, so we need to find out how many descriptions (Freitext) are available
        freitext_names_soup = self.soup.find_all('div', class_ = "section_panel_tab")
        for freitext_name in freitext_names_soup:
            freitext_names.append(freitext_name.text.strip())
        
        print(freitext_names)

        freitext_desc = []
        # First description is always available and has a different class
        desc_1 = self.soup.find('div', class_ = "wordWrap section_freetext")
        freitext_desc.append(desc_1.text.strip())

        # other descriptions have the same class
        freitext_desc_soup = self.soup.find_all('div', class_ = "wordWrap section_freetext display-none")
        for desc in freitext_desc_soup:
            freitext_desc.append(desc.text.replace('\n', '').replace('\r', '').strip())
        
        if len(freitext_names) != len(freitext_desc):
            print("The number of descriptions does not match the number of names.")
            freitext_dict = {}
        else:
            freitext_dict = dict(zip(freitext_names, freitext_desc))
        
        self.result_dict.update(freitext_dict)
        
        # freitext_0 = soup.find_all('div', class_ = "section_panel_tab")[0].text.strip()
        # print(freitext_0)
        # freitext_1 = soup.find_all('div', class_ = "section_panel_tab")[1].text.strip()
        # print(freitext_1)
        # freitext_2 = soup.find_all('div', class_ = "section_panel_tab")[2].text.strip()
        # print(freitext_2)
        # freitext_3 = soup.find_all('div', class_ = "section_panel_tab")[3].text.strip()
        # print(freitext_3)
        # text_2
        # zimmer = soup.find('div', id='freitext_0', class_="wordWrap section_freetext").text.strip()
    
    def get_all(self):
        self.get_flatmates()
        self.get_base_info()
        self.get_price()
        self.get_address()
        self.get_availability()
        self.get_search_info()
        self.get_icons()
        self.get_docs()
        self.get_wg_details()
        self.get_freitext()

    
    
    

    
    

# url_shared_app = "https://www.wg-gesucht.de/wg-zimmer-in-Koeln-Nippes.11098319.html"
# url_shared_app = "https://www.wg-gesucht.de/wg-zimmer-in-Koeln-Lindenthal.6260524.html"
# response = requests.get(url_shared_app, allow_redirects=False)
# soup = BeautifulSoup(response.text, 'html.parser')

# test = AppartScraper(soup, url_shared_app)
# test.get_freitext()

# test.get_flatmates()
# test.get_base_info()
# test.get_price()
# test.get_address()
# test.get_availability()
# test.get_search_info()
# test.get_icons()
# test.get_docs()

# print(test.result_dict)