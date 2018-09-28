import os
from datetime import datetime

import requests
from bs4 import BeautifulSoup

import urllib
from urlparse import parse_qs, urlparse

def makeFolder(folder_name):
    now = datetime.now()
    real_folder_name = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + " "
    real_folder_name += str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + " "
    real_folder_name += folder_name
    os.mkdir("./Background/" + real_folder_name)
    return real_folder_name

def saveImage(image_url, image_name, folder_name):
    urllib.urlretrieve(image_url, "./Background/" + folder_name + "/" + image_name + ".jpg")
    return

def downloadImages(search):
    req = requests.get("https://www.google.co.kr/search?tbm=isch&q=" + search)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    images_table = soup.find("table", {"class": "images_table"})
    images = images_table.findAll("img")
    links = images_table.findAll("a")
    
    if len(images) == len(links):
        length = len(images)
    elif len(images) > len(links):
        length = len(links)
    elif len(images) > len(links):
        length = len(images)

    folder_name = makeFolder(search)
    for temp in range(0, length):
        saveImage(images[temp]["src"], str(temp), folder_name)
    return

downloadImages(raw_input("Download Search : "))
