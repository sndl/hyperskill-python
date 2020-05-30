import sys
import os
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore

# Colorama initialization
init()

history = deque()
tags_to_scrape = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']

cache_dir = sys.argv[1]
if not os.path.exists(cache_dir):
    os.mkdir(cache_dir)


def open_page(url):
    trimmed_url = url.replace('http://', '').replace('https://', '')
    if '.' in trimmed_url:
        trimmed_url = '.'.join(trimmed_url.split('.')[:-1])

    cache_file_path = cache_dir + '/' + trimmed_url

    if not url.startswith('http'):
        url = 'http://' + url

    # TODO: There is no cache invalidation
    if os.path.isfile(cache_file_path):
        with open(cache_file_path) as cache:
            return cache.read()
    else:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        content = []

        # TODO: make traversing through the page and tags more efficient (but I'm too lazy right now)
        for tag in tags_to_scrape:
            for found_tag in soup.find_all(tag):
                if tag == 'a':
                    # TODO: URLs are not clickable, just colored
                    text = Fore.BLUE + found_tag.get_text()
                else:
                    text = found_tag.get_text()

                content.append(text)

        content = ''.join(content)

        with open(cache_file_path, 'w') as cache:
            cache.write(content)

        return content


def menu():
    while True:
        command = input()

        if command == 'exit':
            break

        elif command == 'back':
            if len(history) <= 1:
                print('History is empty!')
                continue

            history.pop()
            page = history.pop()

            print(open_page(page))

        else:
            try:
                print(open_page(command))
                history.append(command)

            except requests.exceptions.ConnectionError:
                print('Error: Incorrect URL')


menu()
