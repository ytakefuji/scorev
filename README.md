# scorev
scorev is a PyPI tool for scoring COVID-19 policies in a filename 'countries' with vaccine rates 
such as at least 1 dose, fully vaccinated, and booster given.

scorev subsumes PyPI scorecovid application.

The score is calculated by dividing the number of deaths due to COVID-19.
Generated result.csv has the following determinants:
deaths, population, score, onedose (rate: at least 1 dose), full (rate: fully vaccinated), booster (rate: booster given).

Data is scraped from the following site:

https://covid.ourworldindata.org/data/owid-covid-data.csv
