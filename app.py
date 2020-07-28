from flask import Flask,render_template,request
from bs4 import BeautifulSoup
import requests, time, smtplib
#from notify_run import Notify
from datetime import datetime
import re
import requests as r
from bs4 import BeautifulSoup as bs
app = Flask(__name__)
global stock3
@app.route("/", methods=['GET','POST'])
def home():
     if request.method == 'POST':
     	medicine_name= request.form.get('medicine_name')
     	link="https://www.1mg.com/search/all?filter=true&name="+medicine_name
     	html_page = r.get(link)
     	soup = BeautifulSoup(html_page.content,"html.parser")
     	for i in soup.find_all('div',{'class':['style__horizontal-card___1Zwmt','style__product-box___3oEU6']}):
     		link = i.find('a',href=True)
     		if link is None:
     			continue
     		link1 = link['href']
     		break
     	else:
     		link1="N/A" 
     	if link1=="N/A":
     		price="N/A"
     	else:
     		url1= "https://www.1mg.com"+link1
     		page1 = r.get(url1)
     		soup = bs(page1.content, "html.parser")
     		price=soup.find("span" , {"class": "l3Regular"}).text
     		link="https://www.1mg.com/search/all?filter=true&name="+medicine_name
     		html_page = r.get(link)
     		soup = BeautifulSoup(html_page.content,"html.parser")
     		quantity=soup.find(["div","span"] , {"class":[ "style__pack-size___3jScl","style__pack-size___254Cd"]}).text
     		title=soup.find(["div","span"] , {"class": ["style__pro-title___3G3rr","style__pro-title___3zxNC"]}).text
     		stock=soup.find("div" , {"class": "style__interaction___3cb12"}).text
     		if stock=="ADD":
     			a="available"
     		else:
     			a="N/A"
     			
     			
     	link3="https://www.practo.com/medicine-info/search?drug="+medicine_name 
     	s = r.get(link3)
     	soup = BeautifulSoup(s.content,'html.parser')
     	for i in soup.find_all("div" , {"class":"shdzcg-1 cjDIVa"}):
     		link = i.find('a',href=True)
     		if link is None:
     			continue
     		link4 = link['href']
     		break
     	else:
     		link1="N/A"
     	if link1=="N/A":
     		print("N/A")
     	else:
     		quantity3=soup.find("div", {"class":"s4h2ti-3 RQtd"}).text
     		#price3=soup.find("div" , {"class": "s13j2pak-2 hfenSr"}).text
     		for i in soup.find('div',{'class':'shdzcg-1 cjDIVa'}):
     			stock2=i.find('span',{'class':'s10ai0bh-0 cDKUIr'})
     			if stock2 is None:
     				continue
     			stock2=stock2.text
     		if stock2=="Add to cart":
     			stock5="available"
     		else:
     			stock5="Out of Stock"
     		if stock5=="available":
     				price3=	price3=price3=soup.find("div" , {"class": "s13j2pak-2 hfenSr"}).text
     		else:
     			price3="price_not_availble"
     		print(price3)
     		link5="https://www.practo.com"+str(link4)
     	link3="https://www.zoylo.com/medicines/catalogsearch/result/?q="+medicine_name
     	html_page = r.get(link3)
     	soup = BeautifulSoup(html_page.content,"html.parser")
     	s=soup.find(['div','span'], {'class':['message notice','price']}).text
     	s=s[2:3]
     	print(s)
     	if s=="Y":
     		link6="N/A"
     		price4="N/A"
     		stock3="N/A"
     		quantity4="N/A"
     		title4=""
     	else:
     		 for i in soup.find_all("div" ,{"class":"product details product-item-details"}):
     		 	link = i.find('a',href=True)
     		 	if link is None:
     		 		continue
     		 	link6=link['href']
     		 	break
     		 else:
     		 	link6=link3
     		 price4=soup.find("span" , {"class": "price"}).text
     		 print(price4)
     		 html_page = r.get(link6)
     		 soup = bs(html_page.content,"html.parser")
     		 for i in soup.find_all("div" ,{"class":"col-md-12 section-three"}):
     		 	link=i.find("button" ,{"class":"action primary tocart"})
     		 	if link is None:
     		 		continue
     		 	link=link.text
     		 	link=link[1:2]
     		 	print(link)
     		 	break
     		 if link=='A':
     		 	stock3="Medicine_available"
     		 else:
     		 	stock3="not_available"
     		 if stock3=="not_available":
     		 	quantity4=""
     		 	title4=""
     		 else:
     		 	quantity4=soup.find("div" ,{"class":"col-lg-8 pack-size"}).text
     		 	title4=soup.find("div" ,{"class":"pro-name"}).text
     	
     	
     	link10= "https://pharmeasy.in/search/all?name="+medicine_name
     	p=r.get(link2)
     	soup = BeautifulSoup(p.text, 'html.parser')
     	for i in soup.find_all("div" , {"class":"GvJNB"}):
     	    link = i.find('a',href=True)
     	    if link is None:
     	    	continue
     	    link2 = link['href']
     	    break
     	else:
     		link2="N/A" 
     	if link2=="N/A":
     		price="N/A"
     	else:
     	  url3="https://pharmeasy.in"+link2
     	  s=r.get(link10)
     	  soup1 = BeautifulSoup(s.text, 'html.parser')
     	  for i in soup1.find('div',{'class':'_3bwoY'}):
     	  			link = i.find('button',{'class':'_2FE4Z h1H8I _1JBjj notifyMeBtn'})
     	  			if link is None:
     	  				 continue
     	  			link2=link.text
     	  			break
     	  else:
     	  		link2="N/A"
     	  if link2=="Notify Me":
     	  		stock=" not availble"
     	  else:
     	  		stock="availble"
     	  title1= soup.find('h1',{'class':'ooufh'}).text
     	  quantity1= soup.find('div',{'class':'_36aef'}).text
     	  price1=soup1.find("div" , {"class":"_1_yM9"}).text
     	  return render_template("flask_weather_app.html",link2=url1,quantity=quantity,title=title,a=a,title1=title1,price1=price1,url1=url1,url3=url3,quantity3=quantity3,p=stock5,link=link3,stock=stock,link5=link5,price=price,quantity1=quantity1,price3=price3,link6=link6,price4=price4,quantity4=quantity4,stock3=stock3,title4=title4)
     return render_template("flask_weather_app.html")
if __name__ == '__main__':
  app.run(debug=True)
  app.run()

