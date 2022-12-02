from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

# NOTE: The page at the given URL is maintained by "wikipedia", which might be updated in future.

brown_dwarfs_url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs#Field_brown_dwarfs'

page = requests.get(brown_dwarfs_url)

soup = bs(page.text,'html.parser')

star_table = soup.find_all('table')

table_rows = star_table[7].find_all('tr')


temp_list= []
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.strip() for i in td]
    temp_list.append(row)



Star_names = []
Distance =[]
Mass = []
Radius =[]



for i in range(1,len(temp_list)-1):

    if(temp_list[i][8]!=""):
        Star_names.append(temp_list[i][0])
        Distance.append(temp_list[i][5])
        Radius.append(temp_list[i][8])

        if(temp_list[i][7]!=""):
            Mass.append(0.000954588*float(temp_list[i][7]))
            Radius.append(0.102763*float(temp_list[i][8]))

        else:
            Mass.append("")
            Radius.append("")
            

df1 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius'])
print(df1)
df1.to_csv('brown_dwarfs.csv')