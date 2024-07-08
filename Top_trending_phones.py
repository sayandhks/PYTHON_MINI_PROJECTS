#a program to list top trending  10 mobile phones from gadgets360
from bs4 import BeautifulSoup
import requests

url = "https://www.gadgets360.com/mobiles/best-phones"
content = requests.get(url).text
doc = BeautifulSoup(content, "html.parser")
rows=doc.find_all("tr")
count=0
mobile_datas=[]
for row in rows:
    datas=(row.find_all("td"))
    for data in datas:
        if count==664:
            break
        else:
            mobile_datas.append(data.string)
            count+=1
count_mobiles=0
print("--------------TOP 10 TRENDING SMART-PHONES IN INDIA-----------------")
for mobile_data in mobile_datas:
    if count_mobiles==10:
        break
    if "Specifications" in mobile_data:

        print("####################################################################")
        print(count_mobiles+1,end=" : ")
        print(mobile_data[:len(mobile_data)-14])

        count_mobiles+=1
    else:
        pass









