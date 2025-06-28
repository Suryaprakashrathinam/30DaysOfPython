'''import requests

def fetch_the_page(url):
    try:
        output = requests.get(url)
        output.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error Occured! Cant fetch the file:", e)

    return
if __name__ == '__main__':
    url = 'https://idrw.org/'
    page = fetch_the_page(url)
    print(page)'''

import requests

def fetch_the_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text  # Return the page content
    except requests.exceptions.RequestException as e:
        print("Error occurred! Can't fetch the file:", e)
        return None

if __name__ == '__main__':
    url = "https://idrw.org/"
    page = fetch_the_page(url)
    if page:
        print(page)
