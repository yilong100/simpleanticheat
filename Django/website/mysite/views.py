from django.shortcuts import render
from django.http import HttpResponse
import requests
import webbrowser
import bs4


def index(request):
    return render(request, 'mysite/cheggy.html')


def manual_search(search_item):
    res = requests.get('https://google.com/search?q=' + str(search_item))
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # selects all the links on the first page found on google.com
    linkElements = soup.select('.kCrYT > a')

    linkToOpen = min(10, len(linkElements))

    count = 1

    a_list = []

    print("Searching for " + search_item + "......"))
    print()

    for i in range(linkToOpen):
        # gets links found on google.com
        link='https://google.com' + linkElements[i].get('href')
        webbrowser.open(link)
        print(str(count) + ". " + link)
        print()
        count += 1

    print()
    print("Search for " + search_item + " Complete.")
    print()
    print()
    print()

def search_by_text_file(text_file):
    # opens text file and seperates items into list by newline character
    file=open(text_file, 'r')
    file_contents=file.readlines()
    search_list=[]

    for item in file_contents:
        item=item.strip("\n")
        search_list.append(item)

    file.close()

    for search_item in search_list:
        res=requests.get('https://google.com/search?q=' + str(search_item))
        res.raise_for_status()

        soup=bs4.BeautifulSoup(res.text, "html.parser")

        # selects all the links on the first page found on google.com
        linkElements=soup.select('.kCrYT > a')

        linkToOpen=min(10, len(linkElements))

        count=1

        print("Searching for " + search_item + "......")
        print()

        for i in range(linkToOpen):
            # gets links found on google.com
            link='https://google.com' + linkElements[i].get('href')
            webbrowser.open(link)
            print(str(count) + ". " + link)
            print()
            count += 1

        print()
        print("Search for " + search_item + " Complete.")
        print()
        print()
        print()
