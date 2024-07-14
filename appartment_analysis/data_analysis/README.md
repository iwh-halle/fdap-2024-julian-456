# Appartment Analysis Results

## Overview
This folder contains the data preprocessing and data analysis. The scripts can be found in the following files, with the result of the case study shown below. 

- `restructuring_data.ipynb`: This file contains the steps for data preparation and selection. The data set resulting from the web scraping is restructured and relevant data is selected for the regression.
- `data_analysis.ipynb`: After some minor filtering. In this file, the data is analyzed using a regression.


## Results
Before the results of the regression are presented. A brief literature review of relevant influencing factors is presented. The two regression models are then introduced and the findings presented.

### Literature Review
Apartment prices, house prices and shared apartment prices influence each other and are not only a key issue in real estate and urban planning.[(J. Gallin; 2004)](../literature/The_Long-Run_Relationship_between_House_Prices_and_Rents.pdf) There are therefore a large number of studies that attempt to determine the factors influencing house prices. There are various approaches to categorizing the influencing factors.
In various studies, these are divided into factors on the demand side and factors on the supply side. [(A. Belke, J. Keil; 2017)](../literature/Fundamental_determinants_of_real_estate_prices_A_panel_study_of_German_regions.pdf)
Another possibility is to divide them into hedonic factors and fundamental factors. Fundamental factors are, for example, income structures, the unemployment rate, population density or the availability of credit. These are general characteristics and do not only apply to just one apartment.
Hedonic factors, on the other hand, are facts that are directly linked to the apartment itself, such as the surroundings, the number of rooms, the age of the apartment or other structural characteristics such as the presence of a balcony. 
For further analysis, we focus on the hedonic factors. As these are included in our scrapped data set.
This approach is based on the hedonic hypothesis of Brachinger [(H. W. Brachinger; 2003)](../literature/Statistical_Theory_of_Hedonic_Price_Indices.pdf). This states that the price of a rental apartment is dependent on its specific properties and characteristics.[(Dr. P. Deschermeier, B. Seipelt; 2016)](../literature/IW-Institute_Expertise_2016_A-Hedonic-Rent-Index-for-Student-Housing-in-Germany.pdf)
Such a study has already been carried out for apartments in Berlin, for example. A hedonic regression was carried out in which various influencing variables such as the number of rooms, the type of apartment or the zip code were used. [(A. Kholodilin, A. Mense; 2012)](../literature/Internet-Based_Hedonic_Indices_of_Rents_and_Prices_for_flats.pdf) 
In addition to European studies, this approach is also used on other continents. A hedonic regression was also carried out in a study from Vietnam. It was found that size, the presence of a balcony and proximity to the city center can have an influence on prices. [(T. N. Bui; 2020)](../literature/A_study_of_factors_influencing_the_price_of_apartments_Evidence_from_Vietnam.pdf)

All of these studies focus primarily on apartments and houses. For this study we want to check whether the same influencing factors that are relevant for apartments also apply to shared flats. In particular, features such as a balcony, the possibility of using parking spaces and proximity to the city center are considered.

Secondly, the length of time it takes for an apartment to be rented is considered. WG-gesucht gives some hints for a good advertisement in a corresponding [article](https://www.wg-gesucht.de/artikel/angebot-aufgeben-so-inserieren-sie-erfolgreich-ihre-wg-wohnung).
According to this article, the advantages of the apartment should be stated directly in the title. (e.g. location and price) The advertisement should also contain a meaningful description. In addition, complete information about the costs and the residential area are advantageous, as well as the indication of additional information. 
Good, expressive images are also helpful, but these could not be included in the web scraping.


### Case Study Results
As already described, the aim of the analysis is to examine whether the residents of a shared apartment have the same expectations of an apartment as the residents of their own apartment or whether there are other factors that determine demand and thus also the price. 
In the second part, the length of time that a shared flat advertisement remains online will be examined.

For both models, the variables are first described and the model quality is determined. The other results are then presented and placed in a scientific context. 

Finally, possible extensions are suggested and the findings are summarized

#### Variables
The price per square meter was used as the dependent variable. Independent variables that would also be related to apartments included the deposit amount, parking facilities, the presence of a garden or balcony, proximity to the City Center and the number of facts from the advertisements. Based on official data from the city of Cologne, the population density could also be included.
In addition, an exploratory investigation was carried out to determine which price drivers apply specifically to shared flats. For this purpose, a small survey was conducted among friends to collect possible price drivers. Data that could be mapped through the advertisements on WG-GESUCHT.de were also included in the model.
For this reason, the model also contains information on the length and sentiment of the description. It was assumed that a longer description is associated with a higher rental price because the landlord makes more effort to let the apartment.
The age limits were also to be examined, whereby a higher required age was also assumed to result in a higher rental price.
In addition, an ex-Cologne resident described the difference between the two sides of the Rhine. The left bank of the Rhine is said to be more popular than the right bank, which is why higher rents could also apply here.
Another influencing factor could be whether the apartment is only available for a limited period. The respondents did not agree on how this affects the price.
The last points are the size of the shared flat or the number of flatmates and whether smoking is allowed in the apartment. According to the respondents, a large number of flatmates should make the rent lower, as should permission to smoke.


#### Price Model

##### Variables
The price per square meter was used as the dependent variable. Independent variables that would also be related to apartments included the deposit amount, parking facilities, the presence of a garden or balcony, proximity to the City Center and the number of facts from the advertisements. Based on official data from the city of Cologne, the population density could also be included.
In addition, an exploratory investigation was carried out to determine which price drivers apply specifically to shared flats. For this purpose, a small survey was conducted among friends to collect possible price drivers. Data that could be mapped through the advertisements on WG-GESUCHT.de were also included in the model.
For this reason, the model also contains information on the length and sentiment of the description. It was assumed that a longer description is associated with a higher rental price because the landlord makes more effort to let the apartment.
The age limits were also to be examined, whereby a higher required age was also assumed to result in a higher rental price.
In addition, an ex-Cologne resident described the difference between the two sides of the Rhine. The left bank of the Rhine is said to be more popular than the right bank, which is why higher rents could also apply here.
Another influencing factor could be whether the apartment is only available for a limited period. The respondents did not agree on how this affects the price.
The last points are the size of the shared flat or the number of flatmates and whether smoking is allowed in the apartment. According to the respondents, a large number of flatmates should make the rent lower, as should permission to smoke.

##### Model quality
The model has an R-squared of 0.163 and can therefore explain 16.3% of the variability of the price per square meter. However, since a large number of predictors are included, the adjusted R-squared of 0.112 is more meaningful. 
The model is significant overall with an F-statistic of 3.214 and a p-value for this below 0.05.
In addition, the model was tested for multicollinearity and autocorrelation. The VIF values were tested for multicollinearity. These are all in a range between 1 and 3. The values indicate that there is no strong multicollinearity between the independent variables. 
Furthermore, there is almost no autocorrelation, which is described by the result of the Durbin Watson test of 1.988.
The results indicate a well-defined specification of the model.
##### Significant Factors 
As the data set was reduced from around 1000 to 334 data sets in order to fully include the main factors, a significance level of 0.1 was assumed for the factors in the regression.
Significant influencing factors that increase the price are the deposit amount (p=0.000), the time limit (p=0.073), the presence of a garden or balcony (p=0.096), the proximity to the city center (p=0.048) and the number of specified facts (p=0.073). Permission to smoke in the entire apartment (p=0.093) and to smoke in parts of the apartment (p=0.048) lowered the price.
The remaining factors such as available parking, specified age restrictions, flat share size or the descriptions have no significant influence.
##### Classification of results
Many of the variables examined in the literature, such as the number of bathrooms or the age of an apartment, could not be adequately recorded via the website. For some characteristics that were significant for apartments, it could be proven that they are also significant for shared flats. These include, for example, proximity to the City Center or features such as a balcony.
It is also interesting to compare the assessments with the actual influence of the factors specific to shared flats. Most of the factors mentioned turned out to be insignificant. However, it was possible to clarify the open question regarding the time limit. Temporary apartments are usually offered at a higher price. One reason for this could be that they are often furnished. It is also interesting to note that permission to smoke in the apartment lowers the price. This could be due to the fact that the number of smokers is lower and therefore the demand for these apartments is also lower.


#### Duration Model
                            OLS Regression Results                            
==============================================================================
Dep. Variable:      Online_since_in_h   R-squared:                       0.074
Model:                            OLS   Adj. R-squared:                  0.015
Method:                 Least Squares   F-statistic:                     1.244
Date:                Sun, 14 Jul 2024   Prob (F-statistic):              0.216
Time:                        10:25:52   Log-Likelihood:                -2336.2
No. Observations:                 334   AIC:                             4714.
Df Residuals:                     313   BIC:                             4794.
Df Model:                          20                                         
Covariance Type:                  HAC                                         
=====================================================================================================
                                        coef    std err          z      P>|z|      [0.025      0.975]
-----------------------------------------------------------------------------------------------------
const                               426.5312    182.534      2.337      0.019      68.772     784.291
Price_per_m²                         -1.0824      1.594     -0.679      0.497      -4.207       2.042
WG_Size                               0.3192     10.117      0.032      0.975     -19.510      20.149
Deposit_in_€                          0.0705      0.036      1.976      0.048       0.001       0.141
Appartmentsize in m²                  0.1777      0.175      1.018      0.309      -0.164       0.520
Intermediate Rent                   101.0676     38.457      2.628      0.009      25.693     176.442
left_rhine_side                     -86.7116     37.879     -2.289      0.022    -160.954     -12.470
Weighted_Average_Sentiment           49.6649     62.784      0.791      0.429     -73.389     172.718
Min_Age                               0.9705      2.747      0.353      0.724      -4.413       6.354
Max_Age                               0.4882      1.178      0.414      0.679      -1.822       2.798
Parking                             -52.9326     42.384     -1.249      0.212    -136.004      30.139
Floor                                11.6204     10.615      1.095      0.274      -9.184      32.425
Garden_Balcony                       30.7188     35.735      0.860      0.390     -39.321     100.758
Dist_center_in_km                    -6.3841      6.852     -0.932      0.351     -19.814       7.046
Title_Length                         -0.1337      0.586     -0.228      0.820      -1.283       1.015
Description_Length                   -0.0059      0.010     -0.561      0.575      -0.026       0.015
Fact_Count                           -3.8066      2.965     -1.284      0.199      -9.619       2.005
Population_per_km²                   -0.0066      0.005     -1.235      0.217      -0.017       0.004
Smoking_Rauchen nicht erwünscht     -61.6520     52.367     -1.177      0.239    -164.290      40.986
Smoking_Rauchen teilweise erlaubt   -36.1921     54.108     -0.669      0.504    -142.241      69.857
Smoking_Rauchen überall erlaubt     -88.3174     89.772     -0.984      0.325    -264.266      87.632
==============================================================================
Omnibus:                       88.199   Durbin-Watson:                   0.195
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              164.733
Skew:                           1.445   Prob(JB):                     1.69e-36
Kurtosis:                       4.865   Cond. No.                     8.82e+04
==============================================================================

Notes:
[1] Standard Errors are heteroscedasticity and autocorrelation robust (HAC) using 1 lags and without small sample correction
[2] The condition number is large, 8.82e+04. This might indicate that there are
strong multicollinearity or other numerical problems.

##### Variables
For the most part, the same variables were used to investigate the length of time an advertisement remains online. In this case, the dependent variable was the duration in hours. The price per square meter was included here as an additional influencing variable.
According to the WG-GESUCHT.de article, apartments are rented out particularly quickly if they contain meaningful descriptions and titles. The type of description can also be an influencing factor here. The relevance of an apartment's location was also emphasized.
The other variables are included in order to recognize whether certain features or conditions also play a role.
##### Model quality
The duration model has an R-squared of 0.074 and an adjusted R-squared of 0.015. This indicates that the independent variables only have a very small influence on the dependent variable. This thesis is confirmed by the F-statistic and its p-value. 
The F-statistic of 1.244 and the p-value of 0.216 indicate that the model is not significant. 
A further obstacle is the result of the Durbin Watson test. This indicates a high level of autocorrelation in the original model. In order to strengthen the significance of the predictors, a further regression model was created using Newex-West standard errors. These are robust against autocorrelation, which strengthens the quality of the predictors but does not change the structure of the model itself.
It was not possible to create a model with a different selection of variables and thus a significant F-statistic. The attempt to use only data sets that existed for at least one week was also unsuccessful.
Despite the non-significant model, assumptions can be formulated based on the predictors, which can be tested in further analyses if necessary.
##### Significant Factors 
Despite the large number of variables, only 3 variables have a significant influence in the model. The coefficients show that the deposit amount leads to a shared flat having to search longer for a suitable flatmate. This also applies to rentals that are only temporary.
The length of tenancy is positively influenced by the side of the Rhine. Shared flats on the left bank of the Rhine tend to find a tenant more quickly than those on the right bank.
As previously mentioned, the model is not significant, which is why the estimators and the associated p-values are not fully meaningful. The results should therefore be checked again with a different data set.
##### Classification of results
Even if the model itself is not significant, trends can still be identified. However, these do not match the descriptions of WG-GESUCHT.de. The data set did not confirm that longer descriptions or titles have a positive influence on the length of time an ad is online. 

#### Extensions and Limitations
Overall, both models show that a longer period of time would be useful for collecting the data. A larger data set would not only increase the significance of the model but also of the individual coefficients. 
In addition, the results should be compared with other major German cities in order to confirm the validity of the model.
However, there are also other ways of continuing to work with the current data set. For example, different sub-data could be examined or analyses with other regression models. Regression approaches other than the OLS method could be a useful idea, especially for the investigation of duration

#### Summary
In summary, it can be said that the rents of shared flats are influenced by similar factors as the rents of apartments. For example, proximity to the city center and amenities are definitely relevant. However, there are also other factors, such as the accuracy of the description and whether smoking is permitted. While smoking in most rental apartments is a matter for each tenant to decide for themselves, in a shared apartment the flatmates must adapt accordingly.
No exact predictions can be made as to how long an apartment will remain online. The model established is not significant and further data must be collected and other approaches pursued in order to determine influential factors. Nevertheless, trends can be identified that can be verified in further studies.

