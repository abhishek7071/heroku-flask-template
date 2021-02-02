from flask import Flask,render_template,request
from bs4 import BeautifulSoup
import requests, time, smtplib
#from notify_run import Notify
from datetime import datetime
import re
import requests as r
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

app = Flask(__name__)
global stock3
@app.route("/", methods=['GET','POST'])
def home():
     if request.method == 'POST':
     	medicine_name= request.form.get('medicine_name')
     	link="https://m.netmeds.com/catalogsearch/result?q="+medicine_name
     	chrome_options = Options()
     	options = Options()
     	chrome_options = webdriver.ChromeOptions()
     	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
     	chrome_options.add_argument("--headless")
     	chrome_options.add_argument("--disable-dev-shm-usage")
     	chrome_options.add_argument("--no-sandbox")
     	driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
     	driver.get(link)
     	elm = driver.find_element_by_tag_name('html')
     	time.sleep(2)
     	page_source = driver.page_source
     	driver.quit()
     	soup = bs(page_source, 'html.parser')
     	for i in soup.find_all('div',{'class':'drug_list'}):
     	  j=soup.find("div",attrs = {'class':'cart_btn'}).text
     	  if j is None:
     	    continue
     	  print(j)
     	  break
     	else:
     	  j="Y"
     	print(j)
     	if j=="Y":
     	  price="N"
     	else:
     	  stock=soup.find("div",attrs = {'class':'cart_btn'}).text
     	  price=soup.find("span",attrs = {'class':'final-price'}).text
     	  mt=soup.find("div",attrs = {'class':'info'}).text
     			
     			
     	link3="https://www.practo.com/medicine-info/search?drug="+medicine_name 
     	s = r.get(link3)
     	soup = BeautifulSoup(s.content,'html.parser')
     	for i in soup.find_all("div" , {"class":"shdzcg-1 cjDIVa"}):
     		link = i.find('a',href=True)
     		if link is None:
     			continue
     		link1 = link['href']
     		break
     	else:
     		link1="N/A"
     	print(link1)
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
     		link5="https://www.practo.com"+str(link1)
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
     	p=r.get(link10)
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
     	  return render_template("flask_weather_app.html",title=mt,quantity=mt,title1=title1,price1=price1,url3=url3,quantity3=quantity3,p=stock5,link=link3,stock=stock,link5=link5,price=price,quantity1=quantity1,price3=price3,link6=link6,price4=price4,quantity4=quantity4,stock3=stock3,title4=title4)
     return render_template("flask_weather_app.html")
if __name__ == '__main__':
  app.run(debug=True)
  app.run()

