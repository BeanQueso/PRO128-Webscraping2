from bs4 import BeautifulSoup
import csv
import requests
import pandas as pd

start_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(start_url)
print(page)
def scrape():
    headers = ["Star", "Distance", "Mass", "Radius"]
    star_data = []

    soup = BeautifulSoup(page.text, 'html.parser')

    star_table = soup.find('table')
    temp_list = []
    table_rows = star_table.find_all('tr')
    
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text.rstrip() for i in td] 
        temp_list.append(row)
        
    Star = []
    Distance =[]
    Mass = []
    Radius =[]

    for i in range(1,len(temp_list)):
        Star.append(temp_list[i][0]) 
        Distance.append(temp_list[i][5])
        Mass.append(temp_list[i][7]) 
        Radius.append(temp_list[i][8]) 
        
        
    df2 = pd.DataFrame(list(zip(Star,Distance,Mass,Radius)),columns=['Star','Distance','Mass','Radius'])
    
    print(df2)

    df2.to_csv('brown_dwarfs.csv')

scrape()
