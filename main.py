
import requests
from bs4 import BeautifulSoup
links_list=['https://www.amazon.eg/s?k=iphone+14+pro+max&i=electronics&rh=n%3A21832883031%2Cp_n_operating_system_browse-bin%3A22079940031%2Cp_n_feature_four_browse-bin%3A26868023031&dc&qid=1671224182',
            'https://www.amazon.eg/-/en/s?k=iphone+14+pro+max&i=electronics&rh=n%3A21832883031%2Cp_n_operating_system_browse-bin%3A22079940031%2Cp_n_feature_four_browse-bin%3A26868023031&dc&page=2&qid=1671284916&ref=sr_pg_2'        ]
counter=1
r=0
lis=[]
for i in links_list:
    page = requests.get(links_list[r])
    soup =BeautifulSoup(page.content,"html.parser")
    res=soup.findAll('span',attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
    rate=soup.findAll('span',attrs={'class':'a-icon-alt'})
    image = soup.findAll('img', attrs={'class': 's-image'})

    for x in range(len(res)):
        print(f"{counter}-{res[x].text}")
        print(f"rate : {rate[x].text}")
        print(image[x].text)
        counter+=1


    r+=1