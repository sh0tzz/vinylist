import menart
import csv

MENART_URL = 'https://www.menartshop.hr/hr/291_glazba/?medij=lp|lp3&dostupno=1&cijena=3|4599&pagepos='
catalog = menart.scrape(MENART_URL, pages=166)

fields = ['SlikaURL', 'Ime', 'CijenaKN', 'CijenaEUR']

with open('catalog.csv', 'w') as f:
	write = csv.writer(f)
	write.writerow(fields)
	write.writerows(catalog)
