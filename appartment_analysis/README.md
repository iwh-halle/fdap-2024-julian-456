# Financial Data Analytics with Python: A Case Study on Rental Prices

This part of the repository is a case study that was processed as part of the master module "Financial Data Analytics with Python" at the Martin-Luther-University Halle-Wittenberg. The case study examines factors influencing the rental prices of shared flats. It also examines the factors that affect how long advertisements stay online without finding a suitable flatmate.

## Overview

The case study focuse ads from Cologne provided on [WG-GESUCHT.de](https://www.wg-gesucht.de/).  Web scraping was used to compile ads and various parameters into a data set that was retrieved on 09.07.2024.  Utilizing Python, Jupyter notebooks and some librarys, we've processed this data to uncover insights into the shared appartment market and compare these with the results on the housing market.


### Literature Review

Prior to the web scraping, a literature review was carried out to investigate factors influencing the housing market and the associated prices. The findings from this review are summarized in a dedicated chapter. Relevant literature is briefly described and initial points of reference for the subsequent analysis are derived.

For the duration that an ad remains online, we check the suggestions on the WG-GESUCHT page to improve the ad. According to the website, ads with the characteristics described here are placed particularly quickly. We therefore use these as possible indicators for relevant influencing factors. 

The results of the literature research are presented in the Read.me of the "[data_analysis](/appartment_analysis/data_analysis/)" folder.

### Web Scraping

The web scraping process is described in the corresponding folder. The structure described here can be used for various other projects. In addition, an outlook is given on how one should adapt the code to retrieve the data over a longer period of time. In addition, the ethical aspects of web scraping are briefly discussed.
The contents described are in the READNE.md of the "scraping" folder

### Data Analysis

The data analysis and preparation is explained directly in the code in the respective Jupyter notebook. 
The preparation of the data can be traced in the "restructuring_data.ipynb" notebook. The data analysis in "data_analysis.ipynb". Both files are located in the "data_analysis" folder.

### Results and Discussion

The results are also presented in the "data_analysis" folder. First, the literature research is summarized before the own results are presented. The results are then placed in the economic context and an outlook for future projects is presented.

### Data Repository

All data generated from our scripts are stored in the Data folder, ensuring easy access for further analysis or replication.

## Getting Started
Interested in conducting your own analysis? Feel free to clone this repository. Begin by installing the necessary dependencies. These are listed in a requirements.txt

Installing Dependencies:

`pip install -r requirements.txt`

APIs are also used for some scripts. This concerns the ScraperApi for scraping and the GoogleMapsApi for data preparation. To have access to these as well, you must create a separate account for each. You can then create an ini.loc file with the following content: 

```
[scraperapi]
key = 1234

[googlemaps]
key = 5678
```

You must replace the api keys with your own. Add the local.ini file to your Git Ignore file to keep your access code private.