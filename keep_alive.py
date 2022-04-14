from flask import Flask
from threading import Thread
import requests
from bs4 import BeautifulSoup
import cloudscraper

def makeRequest():

    url = "http://hypixel.net/threads/hypixel-mafia-halloween-in-january-town-win-game-xlviii.3770594/"
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    print(soup.text)
    return

app = Flask('')

@app.route('/')
def home():
    makeRequest()
    return "I'm alive"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
