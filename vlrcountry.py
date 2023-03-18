from bs4 import BeautifulSoup
import requests
import csv

def scrapeVAL():
    #set url
    url='https://www.vlr.gg/event/stats/1188/champions-tour-2023-lock-in-s-o-paulo'
    page=requests.get(url).text
    soup=BeautifulSoup(page, 'lxml')
    #get the table of players
    table=soup.find('tbody')
    #get the rows
    rows=table.find_all('tr')
    #create csv file
    with open('countries.csv','w',newline='') as file:
        writer=csv.writer(file)
        #grab each flag 
        for row in rows:
            country=row.find('i')['class'][1]
            country=country.split("-")[1]
            #write each country to a csv
            writer.writerow([country])
            

if __name__ == "__main__":
    scrapeVAL()