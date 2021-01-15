"""

https://google-images-download.readthedocs.io/en/latest/examples.html

git clone https://github.com/hardikvasa/google-images-download.git

pip install google_images_download

"chromedriver": "/Users/ivo/tools/chromedriver",

"chromedriver": "C:\\Drivers\\chromedriver\\chromedriver.exe",

"""
from google_images_download import google_images_download

CHROME = "/Users/ivo/tools/chromedriver"

response = google_images_download.googleimagesdownload()

arguments = {"keywords": "birds,bears",
             "chromedriver": CHROME,
             "limit": 10,
             "print_urls": True}

paths = response.download(arguments)

print(paths)
