import requests
import re
import json
import os
import shutil

def search(keywords):
    url = 'https://duckduckgo.com/'
    params = {'q': keywords}

    res = requests.post(url, data=params)
    searchObj = re.search(r'vqd=([\d-]+)\&', res.text, re.M|re.I)

    if not searchObj:
        print("Token Parsing Failed !")
        return -1


    headers = {
        'authority': 'duckduckgo.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'sec-fetch-dest': 'empty',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.3',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': 'https://duckduckgo.com/',
        'accept-language': 'en-US,en;q=0.9',
    }

    params = (
        ('l', 'us-en'),
        ('o', 'json'),
        ('q', keywords),
        ('vqd', searchObj.group(1)),
        ('f', ',,,'),
        ('p', '2')
    )

    requestUrl = url + "i.js"

    res = requests.get(requestUrl, headers=headers, params=params)
    data = json.loads(res.text)
    return data["results"]

def save_image(image_object: dict, save_directory: str) -> None:
    url = image_object["image"]
    filename = os.path.join(save_directory, url.split("/")[-1])

    try:
        res = requests.get(url, stream=True)
        res.raise_for_status()  # Raises stored HTTPError, if one occurred.

        if res.status_code == 200:
            with open(filename, 'wb') as f:
                res.raw.decode_content = True
                shutil.copyfileobj(res.raw, f)
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred while trying to download {url}: {http_err}')
    except Exception as err:
        print(f'An error occurred while trying to download {url}: {err}')


save_directory = "./images"

# Make directory if it doesn't exist
os.makedirs(save_directory, exist_ok=True)

# Do a search and save the images
image_objects = search("cars")
for img_obj in image_objects:
    
    save_image(img_obj, save_directory)