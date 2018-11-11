import requests
from bs4 import BeautifulSoup
import re
Message1 = "Pahe.in Download Link Grabber"
Message2 = "https://github.com/lazuardyk"
print('='*50)
print(Message1)
print(Message2)
print('='*50)

x = input("Masukkan judul film:\n")
payload = {"s":x}
cookies = {"_ga":"GA1.2.1944094503.1519133778", "a":"ccb5j7gmd7df2fifh9m87sf0t5459bj7", "_gid":"GA1.2.2108951550.1541772422", "_popfired":"5", "token_Qg4AAAAAAAAAVsIaMNocEjxUMzDNH0yOsXw0VIM":"A1vm2Vhb5wjMAQAgCah5Knqe3KSQ1/Ss2/ELeIixrl9nbeemrOuKIfs41YsBACC4bMvAJlUbH6CpnuHR1Mrm5DpvHtGIPIc09cj1c5HLLA=="}
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
cari = requests.get("https://pahe.in/?", params=payload, cookies=cookies, headers=header).text
soup = BeautifulSoup(cari, "html.parser")
try:
    linkfilm = soup.find_all('h2')
    linkfilm = linkfilm[3]
    linkfilm = re.search(r'href="(.*)">', str(linkfilm)).group(1)
    judul = re.search(r'pahe.in/(.*)/', linkfilm).group(1)
    print("\nMengambil film:",judul)
    buka = requests.get(linkfilm, cookies=cookies, headers=header).text
    soup2 = BeautifulSoup(buka, "html.parser")
    linkredir = soup2.find('div', class_="box-inner-block")
    linkredir = re.findall(r'href="(.*)" rel', str(linkredir))
    listlink = list()
    for link in linkredir:
        laman = re.search(r'(.*)\?id=', link).group(1)
        data = re.search(r'\?id=(.*)', link).group(1)
        header2 = {"Content-Type":"application/x-www-form-urlencoded"}
        get = {"get":data}
        req = requests.post(laman, headers=header2, data=get).text
        soup3 = BeautifulSoup(req, "html.parser")
        linkjos = re.search(r"var a='(.*)';window", str(soup3)).group(1)
        soup4 = BeautifulSoup(requests.get(linkjos).text, "html.parser")
        linkdl = soup4.find_all('a')
        try:
            linkdl = linkdl[3]
            linkdl = re.search(r'href="(.*)" rel', str(linkdl)).group(1)
            print(linkdl)
        except:
            pass
except:
    print("Film tidak ditemukan")
