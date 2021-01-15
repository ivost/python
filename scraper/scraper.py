"""
https://requests.readthedocs.io/en/master/
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
https://www.dataquest.io/blog/web-scraping-tutorial-python/
https://medium.com/@intprogrammer/how-to-scrape-google-for-images-to-train-your-machine-learning-classifiers-on-565076972ce


https://www.google.com/_/VisualFrontendUi/data/batchexecute?rpcids=HoAMBc&f.sid=-5684935023478549336&bl=boq_visualfrontendserver_20200709.09_p0&hl=en&soc-app=162&soc-platform=1&soc-device=1&authuser=0&_reqid=774169&rt=c


fetch("https://www.google.com/_/VisualFrontendUi/data/batchexecute?rpcids=HoAMBc&f.sid=-5684935023478549336&bl=boq_visualfrontendserver_20200709.09_p0&hl=en&soc-app=162&soc-platform=1&soc-device=1&authuser=0&_reqid=175291&rt=c", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-client-data": "CJe2yQEIpLbJAQjBtskBCKmdygEI58jKAQ==",
    "x-goog-ext-190139975-jspb": "[\"US\",\"ZZ\"]",
    "x-same-domain": "1"
  },
  "referrer": "https://www.google.com/",
  "referrerPolicy": "origin",
  "body": "f.req=%5B%5B%5B%22HoAMBc%22%2C%22%5Bnull%2Cnull%2C%5B1%2Cnull%2C414%2C1%2C954%2C%5B%5B%5C%22cM5d29Y3WOyizM%5C%22%2C178%2C283%2C117795408%5D%5D%2C%5B%5D%2C%5B%5D%2Cnull%2Cnull%2Cnull%2C528%2C100%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5C%22closeup%20face%20covid%20mask%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at=ABrGKkTOcV0lpQh3y--C-4GtgUzr%3A1594611364052&",
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
});


curl 'https://www.google.com/_/VisualFrontendUi/data/batchexecute?rpcids=HoAMBc&f.sid=-5684935023478549336&bl=boq_visualfrontendserver_20200709.09_p0&hl=en&soc-app=162&soc-platform=1&soc-device=1&authuser=0&_reqid=175291&rt=c' \
  -H 'authority: www.google.com' \
  -H 'x-same-domain: 1' \
  -H 'x-goog-ext-190139975-jspb: ["US","ZZ"]' \
  -H 'dnt: 1' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36' \
  -H 'content-type: application/x-www-form-urlencoded;charset=UTF-8' \
  -H 'accept: */*' \
  -H 'origin: https://www.google.com' \
  -H 'x-client-data: CJe2yQEIpLbJAQjBtskBCKmdygEI58jKAQ==' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://www.google.com/' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cookie: SEARCH_SAMESITE=CgQI2Y8B; HSID=AA6x4-ompVBR8-Wjw; SSID=AB70XDHf2KSPJR4oD; APISID=jTE8M5-B1YIAoURu/A4zZS1cR6hwVCZdj0; SAPISID=X30BmT65vo5M1wVA/Af52DveEbqnQpGnoW; __Secure-HSID=AA6x4-ompVBR8-Wjw; __Secure-SSID=AB70XDHf2KSPJR4oD; __Secure-APISID=jTE8M5-B1YIAoURu/A4zZS1cR6hwVCZdj0; __Secure-3PAPISID=X30BmT65vo5M1wVA/Af52DveEbqnQpGnoW; ANID=AHWqTUk7tGBSN4Qr6CGRyjHUpwRsUXcI8HyjGpwpXrU6fT7rWJBGXcHF7ChdHdLk; S=billing-ui-v3=vWMoMfP0aiUQX9y0KzWQP_kSOUsk3uA_:billing-ui-v3-efe=vWMoMfP0aiUQX9y0KzWQP_kSOUsk3uA_; SID=ygcbhh8uL6ms9_KQ5LXt6vQHK8Zo2OydXurKibyiOj451mDmtmY0tbs8Oy3DoWV2KtUegA.; __Secure-3PSID=ygcbhh8uL6ms9_KQ5LXt6vQHK8Zo2OydXurKibyiOj451mDmhrFwJN3GEzfUcMM6LPQtrQ.; NID=204=yBjzjJWWcfPAgf5DsVMVIbnlLCm1bYpmhCKi5PacBvSQcDj3HmoheX4bU5NbJx5LT5AiKhWc04574GdStS1eRlyeDykcPfabnBFAPQvaER5Zna7hgFKdqmfHv_tEt-oy4Tm5_bJFDodIa3-37b1GM9HZphQGhTRrK_VtNWNqfwOR1MPv5ly9MalBRpkSnS_2D-rOf20WoMd8b9KC4X1L_aObgPRI4Ln2kzggjtgf88Hh4ADY4w9nylCsYgpZ7Vj3Jc8_HKAMn9-n; OTZ=5538407_84_88_104280_84_446940; 1P_JAR=2020-07-13-03; SIDCC=AJi4QfFi6cLWFKn7rL9x5FH9kvxg5BBsSz8F2jzY4oRdUcvrBxayb0r48L_vOvyWwf7wpvQpbg4' \
  --data-raw 'f.req=%5B%5B%5B%22HoAMBc%22%2C%22%5Bnull%2Cnull%2C%5B1%2Cnull%2C414%2C1%2C954%2C%5B%5B%5C%22cM5d29Y3WOyizM%5C%22%2C178%2C283%2C117795408%5D%5D%2C%5B%5D%2C%5B%5D%2Cnull%2Cnull%2Cnull%2C528%2C100%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5C%22closeup%20face%20covid%20mask%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at=ABrGKkTOcV0lpQh3y--C-4GtgUzr%3A1594611364052&' \
  --compressed


<a href="/url?q=https://www.pinterest.com/pin/204280533082051994/&amp;sa=U&amp;ved=2ahUKEwjnlJ-VoMvqAhVLKDQIHdpAA4MQr4kDMBF6BAgCEAI&amp;usg=AOvVaw24A4Gv2tB9JDTXHcOd7AKl">

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





