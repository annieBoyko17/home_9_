from bs4 import BeautifulSoup
import requests
response = requests.get("https://coinmarketcap.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/markets/"})
    res = soup_list[0].find("span")
    print(res.text)

next = input("Do you want to see the other currencies?(yes or no)")
if next == "yes":
    curr = input("Choose the currency: 1-Ethereum; 2-Tether; 3-BNB; 4-Binance USD")
    if curr == "1":
        response = requests.get("https://coinmarketcap.com/")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup_list = soup.find_all("a", {"href": "/currencies/ethereum/markets/"})
            res = soup_list[0].find("span")
            print(res.text)

    if curr == "2":
        response = requests.get("https://coinmarketcap.com/")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup_list = soup.find_all("a", {"href": "/currencies/tether/markets/"})
            res = soup_list[0].find("span")
            print(res.text)

    if curr == "3":
        response = requests.get("https://coinmarketcap.com/")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup_list = soup.find_all("a", {"href": "/currencies/bnb/markets/"})
            res = soup_list[0].find("span")
            print(res.text)

    if curr == "4":
        response = requests.get("https://coinmarketcap.com/")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup_list = soup.find_all("a", {"href": "/currencies/binance-usd/markets/"})
            res = soup_list[0].find("span")
            print(res.text)

if next == "no":
    print("Ok, I will show you course of Bitcoin again")
    response = requests.get("https://coinmarketcap.com/")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/markets/"})
        res = soup_list[0].find("span")
        print(res.text)
