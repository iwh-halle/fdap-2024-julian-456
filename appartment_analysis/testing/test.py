import pandas as pd
import json

# JSON data (for demonstration purposes, the same JSON structure is used here)
json_data = open('appartment_analysis\\non_spons_links.json').read()

"""
{
    "https://www.wg-gesucht.de/wg-zimmer-in-Koeln-Neustadt-Sued.11026016.html": {
        "WG_Size": 2,
        "Total_People": 1,
        "w": 0,
        "m": 1,
        "d": 0,
        "Title": "Zimmer in der Nähe der Zülpicherstr",
        "Size": "18m²",
        "Rent": "450€",
        "Extra_Costs": "50€",
        "Other_Costs": "n.a.",
        "Deposit": "400€",
        "Redemption_Agreement": "n.a.",
        "Address": "Beethovenstraße 50674 Köln Neustadt-Süd",
        "Available_From": "01.08.2024",
        "Available_Till": "30.11.2024",
        "Online_Since": "18 Stunden",
        "Search_Info": "Geschlecht egal",
        "3 Minuten zu Fuß entfernt": 1,
        "teilmöbliert": 1,
        "Mehrfamilienhaus": 1,
        "Wohnungsgröße": "Wohnungsgröße: 60m²",
        "Berufstätigen-WG": 1,
        "gemischte-WG": 1,
        "Studenten-WG": 1
    },
    "https://www.wg-gesucht.de/wg-zimmer-in-Koeln-Humboldt-Gremberg.11042480.html": {
        "WG_Size": 2,
        "Total_People": 1,
        "w": 0,
        "m": 1,
        "d": 0,
        "Title": "Looking for a part time flatmate ;)",
        "Size": "13m²",
        "Rent": "300€",
        "Extra_Costs": "150€",
        "Other_Costs": "n.a.",
        "Deposit": "500€",
        "Redemption_Agreement": "n.a.",
        "Address": "Roddergasse 122 51105 Köln Humboldt/Gremberg",
        "Available_From": "01.07.2024",
        "Available_Till": "01.11.2024",
        "Online_Since": "18 Stunden",
        "Search_Info": "Geschlecht egal",
        "möbliert": 1,
        "Laminat": 1,
        "gute Parkmöglichkeiten": 1,
        "WLAN schneller als 100 Mbit/s": 1,
        "2 Minuten zu Fuß entfernt": 1,
        "Keller": 1,
        "Altbau": 1,
        "Badewanne": 1,
        "Waschmaschine": 1,
        "1. OG": 1,
        "DSL": 1,
        "Bewerbermappe": 1,
        "itsmydata": 1,
        "SCHUFA": 1,
        "Ausweis/ID": 1,
        "Einkommensnachweis": 1,
        "Wohnungsgröße": "Wohnungsgröße: 70m²",
        "Rauchen": "Rauchen nicht erwünscht",
        "Berufstätigen-WG": 1,
        "Studenten-WG": 1,
        "LGBTQ": 1,
        "Sprache/n": "Sprache/n: Deutsch, Englisch"
    }
}
"""

# Load JSON data
data = json.loads(json_data)

# Create DataFrame from the JSON data
df = pd.DataFrame.from_dict(data, orient='index')

# Display the DataFrame
print(df.head(5))
