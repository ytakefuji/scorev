import pandas as pd
import subprocess as sp
sp.call('wget -nc https://covid.ourworldindata.org/data/owid-covid-data.csv', shell=True)
sp.call('wget -nc https://github.com/ytakefuji/scorev/raw/main/oecd.csv',shell=True)

d=pd.read_csv('owid-covid-data.csv')
lastday=str(d.date.iloc[-2:]).split()[1]
last2=str(d.date.iloc[-2:]).split()[1]
last3=str(d.date.iloc[-3:]).split()[1]
last4=str(d.date.iloc[-4:]).split()[1]
last5=str(d.date.iloc[-5:]).split()[1]
print(lastday)
print(last2)
print(last3)
print(last4)
print(last5)
countries=pd.read_csv('oecd.csv')
countries=countries.country
n=len(countries)
dd=pd.DataFrame(
  {
   "country": countries,
   "deaths": range(n),
   "population": range(n),
   "score": range(n),
   "1dose": range(n),
   "full": range(n),
   "booster": range(n),
  })
#print(dd)

def main():
 for i in countries:
  dd.loc[dd.country==i,'deaths']=int(d.loc[(d.date==last2) & (d.location==i),'total_deaths'].tolist().pop())
  dd.loc[dd.country==i,'population']=round(float((d.loc[(d.location==i) & (d.date==lastday),'population']/1000000)),2)
  dd.loc[dd.country==i,'score']=round(float(dd.loc[dd.country==i,'deaths']/dd.loc[dd.country==i,'population']),2)
  dd.loc[dd.country==i,'1dose']=round(float(d.loc[(d.location==i) & (d.date==lastday),'people_vaccinated_per_hundred']),2)
  dd.loc[dd.country==i,'full']=round(float(d.loc[(d.location==i) & (d.date==lastday),'people_fully_vaccinated_per_hundred']),2)
  dd.loc[dd.country==i,'booster']=round(float(d.loc[(d.location==i) & (d.date==lastday),'total_boosters_per_hundred']),2)
 ddd=dd.sort_values(by=['score'])
 ddd.to_csv('result.csv',index=False)
 ddd=pd.read_csv('result.csv',index_col=0)
 print(ddd)

main()
