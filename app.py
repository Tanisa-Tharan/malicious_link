# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 23:14:28 2020

@author: hp
"""


from flask import Flask,render_template,url_for,request
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

@app.route('/')
def home():
    string = request.args.get("bla")+""
    URL = 'https://www.urlvoid.com/scan/'+string
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'lxml')
    result=""
    for d in soup.findAll('table'):
        result=d.find('span',class_="label label-success")
        if result is None:
            result=d.find('span',class_="label label-danger")
        result=result.text
        break
    numbers = re.findall('[0-9]+', result)
    if(len(numbers)==0):
        return "0"
    return numbers[0]
if __name__ == '__main__':
	app.run(debug=True)