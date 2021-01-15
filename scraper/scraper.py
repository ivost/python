"""

"""
import requests
from bs4 import BeautifulSoup

KEYWORD="birds"
url = f"https://www.google.com/search?q={KEYWORD}&tbm=isch&ved=2ahUKEwjgrPq3n8vqAhWViZ4KHYxoC9cQ2-cCegQIABAA&oq=people+face+closeup&gs_lcp=CgNpbWcQA1DRNljRNmCYOWgAcAB4AIABT4gBT5IBATGYAQCgAQGqAQtnd3Mtd2l6LWltZw&sclient=img&ei=8NsMX-D0DpWT-gSM0a24DQ&start=##&sa=N"

idx = 1
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





