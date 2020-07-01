import requests
import pandas as pd
import datetime
import csv
from bs4 import BeautifulSoup
#headers = headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
#url = "https://www.ebay-kleinanzeigen.de/s-zu-verschenken/osnabrueck/c192l3117" # URL koennte auch ein zusammengesetzter String sein, Schleife für Kontrolle von Postleitzahl und Stadt

with open('Eine Seite.html') as html_file: #Offline-Funktionalität
	html_soup = BeautifulSoup(html_file, 'html.parser')	

titel = []
beschreibung = []
postleitzahl = []
stadt = []
zeit = []

#response = requests.get(url, headers= headers) Für Online wieder einschalten

#html_soup = BeautifulSoup(response.text, 'html.parser') Für Online wieder einschalten
type(html_soup)
#print(response.text)

seite_container  = html_soup.find_all('li', class_ = 'ad-listitem lazyload-item') #Jedes Item der Liste wird herausgefiltert

for container in seite_container: #In dieser Schleife sollen die Informationen aus der Liste extrahiert werden
	
	
	#Titel
	rohbeschreibung = container.h2.a.text
	titel.append(rohbeschreibung.splitlines())



	#Beschreibung
	roh = container.article.p.text
	beschreibung.append(roh.splitlines())

	#Postleitzahl und Ort
	postort = []
	temp_ort = container.find("div", class_ = "aditem-details")
	
	postort = temp_ort.text.splitlines()
	postort = [x.strip(' ') for x in postort]
	
	stadt.append(postort[2:3])
	postleitzahl.append(postort[1:2])

	#Zeit....was mach ich mit sachen von gestern ?
	zeitlist = []
	temp_zeit = container.find("div", class_ = "aditem-addon")
	
	zeitlist = temp_zeit.text.splitlines()
	zeitlist = [x.strip(' ') for x in zeitlist]
	zeitlist = [x.strip('Heute, ') for x in zeitlist]
	zeitlist = zeitlist[1]
	zeit.append(zeitlist)	
	
	







ergebnis_df = pd.DataFrame({
'titel': titel,
'beschreibung': beschreibung,
'postleitzahl': stadt,
'stadt': stadt,
'zeit': zeit})
#Zeit des Erfassens todatetime, 
#selenium ginge auch Simulation eines Browsers
#Delta Verlauf
#Fuzzy matching

#Speichern"""

print(ergebnis_df)
ergebnis_df.to_csv("Testseite.csv")