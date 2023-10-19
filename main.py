from bs4 import BeautifulSoup
import requests
#import bs4
res=requests.get('https://lesnoi.by')
with open('tst.html','w') as file_ob:
    file_ob.write(res.text)
with open('tst.html','r') as file_ob:
    src=file_ob.read()
#print(src)
soup=BeautifulSoup(src,"lxml")
#print(soup.text)
all_a=soup.find_all('a')
for item in all_a:
    item_text=item.text
    item_url=item.get("href")
    print(f"{item_text}:{item_url}")
#print(all_a)
#for link in soup.find_all('a'):
#    print(link.get('href'))
#page_h1=soup.find_all("h2")

#for item in src:
#    print(item.text)

#print(soup.get_text())

#for i in soup.find_all()