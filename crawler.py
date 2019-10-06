
import json
import requests
import urllib.request
from bs4 import BeautifulSoup


"""
-------------------
reading input file
-------------------
"""
def read_input(input_file):
    with open(input_file) as json_file:
        data = json.load(json_file)
        return data

"""
-----------------------------------------------
creating url for github from keywords and type
-----------------------------------------------
"""
def create_url(data):
    url = "https://github.com/search?q="
    for kw in data["keywords"]:
        url = url + kw
        if kw is not data["keywords"][-1]:
            url = url + "+"
    url = url + "&type=" + data["type"]
    return url

"""
-----------------------------------
converting proxies into dictionary
-----------------------------------
"""
def proxies_dict(proxies):
    proxies = {i: proxies[i] for i in range(0, len(proxies))}
    return proxies

"""
------------------------------
getting response from request
------------------------------
"""
def request(url, proxies):
    response = requests.get(url, proxies=proxies)
    html = BeautifulSoup(response.text, "lxml")
    return response.status_code ,html

"""
-------------------------------------
navigating in html to search results
-------------------------------------
"""
def html_navigation(response_html):
    # navigating to desired data
    html = response_html.html.body
    html = html.contents[7]
    html = html.main
    html = html.div
    html = html.contents[5]
    html = html.div
    html = html.ul
    return html

"""
--------------------
get repository urls
--------------------
"""
def get_urls(html, proxies):
    repo_data = []
    html = html.li
    while html != None:
        repo = html.div.h3.a["href"]
        repo_url = {"url": "https://github.com" + repo}
        """--------------------------------------------------------------------------------------
        | EXTRACTING EXTRA REPOSITORY DATA                                                      |
        | -> comment next two lines of code to get only repository links                        |
        | -> uncomment next two lines of code to get repository links and extra repository data |
        --------------------------------------------------------------------------------------"""
        #extra_data = get_extra_data(repo_url["url"], proxies)
        #repo_url.update(extra_data)
        """--------------------------
        | END EXTRACTING EXTRA DATA |
        --------------------------"""
        # append repository data
        repo_data.append(repo_url)
        html = html.next_sibling.next_sibling
    return repo_data

"""
------------------------------------------
navigating to next page of search results
------------------------------------------
"""
def next_page(html):
    html = html.next_sibling.next_sibling
    # check if there is more pages
    if html == None:
        page_url = None
        return page_url
    html = html.div
    html = html.contents[-1]
    # check if this is last page
    if len(html["class"]) == 2:
        page_url = None
    else:
        url = html["href"]
        page_url = "https://github.com" + url
    return page_url

"""
------------------------------------
get extra data from repository page
------------------------------------
"""
def get_extra_data(url, proxies):
    response_code, response_html = request(url, proxies)
    html = response_html.html.body
    html = html.contents[7]
    html = html.div
    html = html.main
    html = html.div
    owner = get_owner(html)
    lang_stats = get_lang_stats(html.next_sibling.next_sibling)
    extra_data = {"extra": {}}
    extra_data["extra"].update(owner)
    extra_data["extra"].update(lang_stats)
    return extra_data

"""
------------------------
get owner of repository
------------------------
"""
def get_owner(html):
    html = html.div
    html = html.h1
    owner = html.span.text
    owner = {"owner": owner}
    return owner

"""
-------------------------------------
get all language stats of repository
-------------------------------------
"""
def get_lang_stats(html):
    html = html.div
    html = html.details
    # check if cantains language details
    if len(html["class"]) != 1:
        return {}
    html = html.contents[3]
    html = html.ol
    html = html.li
    # get all languages
    lang_data = {"language_stats": {}}
    while html != None:
        lang, lang_val = language_data(html)
        #append language stats
        lang_data["language_stats"].update({lang: lang_val})
        html = html.next_sibling.next_sibling
    return lang_data

"""
------------------
get language data
------------------
"""
def language_data(html):
    if html.next_element.next_element.name == "a":
        # language data
        lang = html.a.contents[3].text
        lang_val = html.a.contents[5].text
    else:
        # others
        lang = html.span.contents[3].text
        lang_val = html.span.contents[5].text
    lang_val = float(lang_val[:-1])
    return lang, lang_val

"""
--------------------------
extracting data from html
--------------------------
"""
def extracting_data(url, proxies):
    #all repository links
    repo_urls = []
    while url != None:
        # getting response from request
        response_code, html = request(url, proxies)
        # navigating to desired data
        html = html_navigation(html)
        # extracting data
        repo = get_urls(html, proxies)
        repo_urls = repo_urls + repo
        url = next_page(html)
    return repo_urls

"""
------------------------------------------------------
writing repository data in json format to output file
------------------------------------------------------
"""
def write_result(output_data, output_file):
    with open(output_file, 'w') as outfile:
        json.dump(output_data, outfile, indent=2)


def main():
    input_file = "input_short.txt"
    output_file = "output.txt"

    data = read_input(input_file)
    url = create_url(data)
    proxies = proxies_dict(data["proxies"])
    repo_urls = extracting_data(url, proxies)
    write_result(repo_urls, output_file)


if __name__ == "__main__":
    main()

