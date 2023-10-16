import requests
from bs4 import BeautifulSoup
from lxml import etree
from fastapi import FastAPI


# uvicorn getPrice:app --reload --host 0.0.0.0

#http://58.82.196.1:8000/natural

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to check iphone price API"}


@app.get("/natural")

async def get_natural_price():

    # Send a GET request to the webpage
    url = "https://www.iphonepricehk.com/iphone-15-plus-pro-max-price"
    response = requests.get(url)

    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Convert the BeautifulSoup object to an lxml etree object
    tree = etree.HTML(str(soup))


    # Evaluate the XPath expression on the etree object

    model_source = tree.xpath('//*[@id="iphoneprice-info"]/div[2]/div[1]/div[7]/div/div/div[2]/div[2]/div[8]/span[1]')
    model = model_source[0].text

    recycle_price_source = tree.xpath('//*[@id="iphoneprice-info"]/div[2]/div[1]/div[7]/div/div/div[2]/div[2]/div[8]/span[2]')
    recycle_price = recycle_price_source[0].text

    price_diff_source = tree.xpath('//*[@id="iphoneprice-info"]/div[2]/div[1]/div[7]/div/div/div[2]/div[2]/div[8]/span[3]')
    price_diff = price_diff_source[0].text.replace("(", "").replace(")", "")

    last_update_source = tree.xpath('//*[@id="iphoneprice-info"]/div[2]/div[1]/div[7]/div/small')
    last_update = last_update_source[0].text.replace("截至 ","")
   
    
    price = {
        "model": model,
        "recycle_price": recycle_price,
        "price_diff": price_diff,
        "last_update": last_update
       
    }
    
    return{"natural": price}


@app.get("/white")

async def get_white_price():
    
     # Send a GET request to the webpage
    url = "https://www.iphonepricehk.com/iphone-15-plus-pro-max-price"
    response = requests.get(url)

    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Convert the BeautifulSoup object to an lxml etree object
    tree = etree.HTML(str(soup))


    # Evaluate the XPath expression on the etree object

    model_source = tree.xpath('//*[@id="iphoneprice-info"]/div[2]/div[1]/div[7]/div/div/div[2]/div[2]/div[7]/span[1]')
    model = model_source[0].text
    

    recycle_price_source = tree.xpath('//*[@id="iphoneprice-info"]/div[2]/div[1]/div[7]/div/div/div[2]/div[2]/div[7]/span[2]')
    recycle_price = recycle_price_source[0].text

    price_diff_source = tree.xpath('//*[@id="iphoneprice-info"]/div[2]/div[1]/div[7]/div/div/div[2]/div[2]/div[7]/span[3]')
    price_diff = price_diff_source[0].text.replace("(", "").replace(")", "")

    last_update_source = tree.xpath('//*[@id="iphoneprice-info"]/div[2]/div[1]/div[7]/div/small')
    last_update = last_update_source[0].text.replace("截至 ","")
   
    
    price = {
        "model": model,
        "recycle_price": recycle_price,
        "price_diff": price_diff,
        "last_update": last_update
       
    }
    
    return{"white": price}
