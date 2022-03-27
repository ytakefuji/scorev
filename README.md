# scorev
scorev is a PyPI tool for scoring COVID-19 policies in a filename 'oecd.csv' with vaccine rates 
such as at least 1 dose, fully vaccinated, and booster given.

scorev subsumes PyPI scorecovid application.

The score is calculated by dividing the number of deaths due to COVID-19.
Generated result.csv has the following determinants:
deaths, population, score, 1dose (rate: at least 1 dose), full (rate: fully vaccinated), booster (rate: booster given).

Vaccine rates such as 1dose, full, and booster are unreliable 
since some countries do not often update.

The current program checks the last 8 days in the dataset.

Data is scraped from the following site:

https://covid.ourworldindata.org/data/owid-covid-data.csv

# How to install scorev
$ pip install scorev

# How to run scorev
$ scorerev

<img src='https://github.com/ytakefuji/scorev/raw/main/result.png' width=800 height=1300 >

# How to modify country names
Modify oecd.csv file for adding and deleting countries.
