"""

"""
import requests
from bs4 import BeautifulSoup

#url = "https://www.google.com/search?q=Closeup+Covid+Face+Masks&hl=en&gbv=1&tbm=isch&start=##&sa=N"
# mask
#url = "https://www.google.com/search?q=Closeup+Covid+Face+Masks&hl=en&sxsrf=ALeKk02Vd1XNFhc-eD5dlDbF_BaGc7CSYQ:1594673474577&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj5hvDPjcvqAhUoFjQIHRkbCagQ_AUICSgC&start=##&sa=N"

# no mask
url = "https://www.google.com/search?q=people+face+closeup&tbm=isch&ved=2ahUKEwjgrPq3n8vqAhWViZ4KHYxoC9cQ2-cCegQIABAA&oq=people+face+closeup&gs_lcp=CgNpbWcQA1DRNljRNmCYOWgAcAB4AIABT4gBT5IBATGYAQCgAQGqAQtnd3Mtd2l6LWltZw&sclient=img&ei=8NsMX-D0DpWT-gSM0a24DQ&start=##&sa=N"

idx = 1
# import time
# milliseconds = int(round(time.time() * 1000))
fcount = 0

done = False
while not done:
    url1 = url.replace("##", str(idx))
    #done = True
    idx += 20
    print("url", url1)
    page = requests.get(url1)

    if page.status_code != 200:
        print("ERROR", page.status_code)
        break
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())

    #for img in soup.find_all('a'):
        #<a href = "/url?q=https://www.pinterest.com/pin/204280533082051994/&amp;sa=U&amp;ved=2ahUKEwjnlJ-VoMvqAhVLKDQIHdpAA4MQr4kDMBF6BAgCEAI&amp;usg=AOvVaw24A4Gv2tB9JDTXHcOd7AKl" >

    for img in soup.find_all('img'):
        url2 = img.attrs["src"]
        if not url2.startswith('http'):
            continue
        if not "?q=" in url2:
            continue

        pos1 = url2.rindex(":")
        pos2 = url2.rindex("&")
        if not 0 < pos1 < pos2:
            continue

        response = requests.get(url2)
        if response.status_code != 200:
            continue

        file = f'/tmp/{url2[pos1+1:pos2]}.jpg'
        print("writing ", fcount, file)
        with open(file, 'wb') as f:
            f.write(response.content)
            f.close()
            fcount += 1

print("files:", fcount)





