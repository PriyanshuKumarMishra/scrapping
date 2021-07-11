import json
from bs4 import BeautifulSoup
import requests
op,bp,data,d=open('scrap.json'),open('scrp.json','w'),[],1
check=json.load(op)
for n in check:
    data_dic={}
    url=n["Link"]
    page=requests.get(url) 
    soup=BeautifulSoup(page.text,"html.parser")
    body_of_web=soup.find("body")
    country_more,director_list,genre_list=body_of_web.find("div",attrs={"class":'article','id':'titleDetails'}).findAll("div"),body_of_web.find("div",class_="credit_summary_item").findAll('a'),body_of_web.find('div', class_ = 'subtext').findAll('a')
    data_dic['bio'],data_dic['name'],data_dic['year'],data_dic['director'],data_dic['genre']=body_of_web.find("div",class_="summary_text").text.strip(),body_of_web.find("h1").text[:-8],int(body_of_web.h1.span.a.text),[i.text.strip() for i in director_list],[i.text for i in genre_list[:-1]]
    for i in country_more:
        tag=i.findAll("h4")
        for text in tag:
            if 'Language:' in text:
                tag2=i.findAll('a')
                data_dic['language']=[language.text for language in tag2] 
            elif "Country:" in text:
                tag2=i.findAll('a')
                data_dic['country']=[''.join(country.text) for country in tag2]  
    data_dic['img link']='https://www.imdb.com/'+(body_of_web.find_all("div",class_="poster")[0].a['href'])
    time=body_of_web.find("div",class_='subtext').time.text.strip()
    time2=int(time[0])*60
    if 'min' in time:
        a=time.strip('min').split('h')
        data_dic['run time']=str(time2+int(a[1]))+' minutes'
    data.append(data_dic)
    if d==10:
        break
    d+=1
json.dump(data,bp)