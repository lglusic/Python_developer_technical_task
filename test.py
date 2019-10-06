
import unittest
import json
import requests
import urllib.request
from validator_collection import validators, checkers
from bs4 import BeautifulSoup
import crawler  # code with crawler


def data_get_urls():
    html = """<ul class="repo-list">
<li class="repo-list-item d-flex flex-column flex-md-row flex-justify-start py-4 public source">
<div class="col-12 col-md-8 pr-md-3">
<h3>
<a class="v-align-middle" data-hydro-click='{"event_type":"search_result.click","payload":{"page_number":1,"per_page":10,"query":"openstack nova css","result_position":1,"click_id":55005225,"result":{"id":55005225,"global_relay_id":"MDEwOlJlcG9zaXRvcnk1NTAwNTIyNQ==","model_name":"Repository","url":"https://github.com/atuldjadhav/DropBox-Cloud-Storage"},"client_id":null,"originating_request_id":"C1BB:47B52:3338B5B:4D82682:5D9A1F2E","originating_url":"https://github.com/search?q=openstack+nova+css&amp;type=Repositories","referrer":null,"user_id":null}}' data-hydro-click-hmac="37fc58c505a16e63ff094c91d7f75253eef81aa1203f873225d643f873587e15" href="/atuldjadhav/DropBox-Cloud-Storage">atuldjadhav/DropBox-Cloud-Storage</a>
</h3>
<p class="col-12 col-md-9 d-inline-block text-gray mb-2 pr-4">
        Technologies:- <em>Openstack</em> <em>NOVA</em>, NEUTRON, SWIFT, CINDER API's, JAVA, JAX-RS, MAVEN, JSON, HTML5, <em>CSS</em>, JAVASCRIPT, ANGUL…
      </p>
<div class="d-flex flex-wrap">
<p class="f6 text-gray mr-3 mb-0 mt-2">
          Updated <relative-time class="no-wrap" datetime="2016-03-29T19:40:33Z">Mar 29, 2016</relative-time>
</p>
</div>
</div>
<div class="flex-shrink-0 col-6 col-md-4 pt-2 pr-md-3 d-flex">
<div class="text-gray flex-auto min-width-0">
<div class="mr-3">
<span>
<span class="repo-language-color" style="background-color: #563d7c"></span>
<span itemprop="programmingLanguage">CSS</span>
</span>
</div>
</div>
</div>
</li>
<li class="repo-list-item d-flex flex-column flex-md-row flex-justify-start py-4 public source">
<div class="col-12 col-md-8 pr-md-3">
<h3>
<a class="v-align-middle" data-hydro-click='{"event_type":"search_result.click","payload":{"page_number":1,"per_page":10,"query":"openstack nova css","result_position":2,"click_id":185224246,"result":{"id":185224246,"global_relay_id":"MDEwOlJlcG9zaXRvcnkxODUyMjQyNDY=","model_name":"Repository","url":"https://github.com/michealbalogun/Horizon-dashboard"},"client_id":null,"originating_request_id":"C1BB:47B52:3338B5B:4D82682:5D9A1F2E","originating_url":"https://github.com/search?q=openstack+nova+css&amp;type=Repositories","referrer":null,"user_id":null}}' data-hydro-click-hmac="b81b9a5e50ef7bb5e23e137badf9c6fb206b4fed653afca72df30d7695643f50" href="/michealbalogun/Horizon-dashboard">michealbalogun/Horizon-dashboard</a>
</h3>
<p class="col-12 col-md-9 d-inline-block text-gray mb-2 pr-4">
        ' COMPRESS_<em>CSS</em>_HASHING_METHOD = 'hash' COMPRESS_PARSER = 'compressor.parser.HtmlParser' INSTALLED_APPS = [ '<em>openstack</em>_…
      </p>
<div class="d-flex flex-wrap">
<p class="f6 text-gray mr-3 mb-0 mt-2">
          Updated <relative-time class="no-wrap" datetime="2019-05-06T15:34:48Z">May 6, 2019</relative-time>
</p>
</div>
</div>
<div class="flex-shrink-0 col-6 col-md-4 pt-2 pr-md-3 d-flex">
<div class="text-gray flex-auto min-width-0">
<div class="mr-3">
<span>
<span class="repo-language-color" style="background-color: #3572A5"></span>
<span itemprop="programmingLanguage">Python</span>
</span>
</div>
</div>
<div class="pl-2 pl-md-0 text-right flex-auto min-width-0">
<a class="muted-link" href="/michealbalogun/Horizon-dashboard/stargazers">
<svg aria-label="star" class="octicon octicon-star" height="16" role="img" version="1.1" viewbox="0 0 14 16" width="14"><path d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z" fill-rule="evenodd"></path></svg>
          2
        </a>
</div>
</div>
</li>
</ul>"""
    return html

def data_next_page_1():
    html = """<ul class="repo-list">
<li class="repo-list-item d-flex flex-column flex-md-row flex-justify-start py-4 public source">
<div class="col-12 col-md-8 pr-md-3">
<h3>
<a class="v-align-middle" data-hydro-click='{"event_type":"search_result.click","payload":{"page_number":1,"per_page":10,"query":"python crawler json","result_position":1,"click_id":112169994,"result":{"id":112169994,"global_relay_id":"MDEwOlJlcG9zaXRvcnkxMTIxNjk5OTQ=","model_name":"Repository","url":"https://github.com/gaojiuli/toapi"},"client_id":null,"originating_request_id":"C22A:47B55:3DE44DF:5E1BDAD:5D9A24A8","originating_url":"https://github.com/search?q=python+crawler+json&amp;type=Repositories","referrer":null,"user_id":null}}' data-hydro-click-hmac="b198ee8f212312e3c90653eb5df12d4cf0dee75d93b2175929fcd8a8d00113ae" href="/gaojiuli/toapi">gaojiuli/toapi</a>
</h3>
</div>
</li>
</ul>
<div class="paginate-container codesearch-pagination-container">
<div class="d-flex d-md-inline-block pagination" data-pjax="true"><span class="previous_page disabled">Previous</span> <em class="current" data-total-pages="5">1</em> <a href="/search?p=2&amp;q=python+crawler+json&amp;type=Repositories" rel="next">2</a> <a href="/search?p=3&amp;q=python+crawler+json&amp;type=Repositories">3</a> <a href="/search?p=4&amp;q=python+crawler+json&amp;type=Repositories">4</a> <a href="/search?p=5&amp;q=python+crawler+json&amp;type=Repositories">5</a> <a class="next_page" href="/search?p=2&amp;q=python+crawler+json&amp;type=Repositories" rel="next">Next</a></div>
</div>"""
    return html

def data_next_page_2():
    html = """<ul class="repo-list">
<li class="repo-list-item d-flex flex-column flex-md-row flex-justify-start py-4 public source">
<div class="col-12 col-md-8 pr-md-3">
<h3>
<a class="v-align-middle" data-hydro-click='{"event_type":"search_result.click","payload":{"page_number":5,"per_page":10,"query":"python crawler json","result_position":1,"click_id":27019746,"result":{"id":27019746,"global_relay_id":"MDEwOlJlcG9zaXRvcnkyNzAxOTc0Ng==","model_name":"Repository","url":"https://github.com/catsky/ausfish-species-identification"},"client_id":null,"originating_request_id":"C236:1EA27:452BAC1:69819F0:5D9A2551","originating_url":"https://github.com/search?p=5&amp;q=python+crawler+json&amp;type=Repositories","referrer":null,"user_id":null}}' data-hydro-click-hmac="89e9c3ca080957c96b42645437a12b165a0f5d06cf76d85b280d1e5f7e306da4" href="/catsky/ausfish-species-identification">catsky/ausfish-species-identification</a>
</h3>
</div>
</li>
</ul>
<div class="paginate-container codesearch-pagination-container">
<div class="d-flex d-md-inline-block pagination" data-pjax="true"><a class="previous_page" href="/search?p=4&amp;q=python+crawler+json&amp;type=Repositories" rel="prev">Previous</a> <a href="/search?p=1&amp;q=python+crawler+json&amp;type=Repositories">1</a> <a href="/search?p=2&amp;q=python+crawler+json&amp;type=Repositories">2</a> <a href="/search?p=3&amp;q=python+crawler+json&amp;type=Repositories">3</a> <a href="/search?p=4&amp;q=python+crawler+json&amp;type=Repositories" rel="prev">4</a> <em class="current" data-total-pages="5">5</em> <span class="next_page disabled">Next</span></div>
</div>"""
    return html

def data_get_owner():
    html = """<div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
<div class="repohead-details-container clearfix container">
<ul class="pagehead-actions">
<li>
<a aria-label="You must be signed in to watch a repository" class="tooltipped tooltipped-s btn btn-sm btn-with-count" data-hydro-click='{"event_type":"authentication.click","payload":{"location_in_page":"notification subscription menu watch","repository_id":null,"auth_type":"LOG_IN","client_id":null,"originating_request_id":"C279:25B3:32ADC05:4D559B0:5D9A297F","originating_url":"https://github.com/atuldjadhav/DropBox-Cloud-Storage","referrer":null,"user_id":null}}' data-hydro-click-hmac="eb08aa3fc4e2e3be98757e4703939bd240b3924f3941375f40d3911faf7fe3a8" href="/login?return_to=%2Fatuldjadhav%2FDropBox-Cloud-Storage" rel="nofollow">
<svg aria-hidden="true" class="octicon octicon-eye v-align-text-bottom" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z" fill-rule="evenodd"></path></svg>
    Watch
</a> <a aria-label="1 user is watching this repository" class="social-count" href="/atuldjadhav/DropBox-Cloud-Storage/watchers">
      1
    </a>
</li>
<li>
<a aria-label="You must be signed in to star a repository" class="btn btn-sm btn-with-count tooltipped tooltipped-s" data-hydro-click='{"event_type":"authentication.click","payload":{"location_in_page":"star button","repository_id":55005225,"auth_type":"LOG_IN","client_id":null,"originating_request_id":"C279:25B3:32ADC05:4D559B0:5D9A297F","originating_url":"https://github.com/atuldjadhav/DropBox-Cloud-Storage","referrer":null,"user_id":null}}' data-hydro-click-hmac="152500872b41e7f2665c2a3d8130252e4d606b92b943c2b53e0c5ce723a4baa4" href="/login?return_to=%2Fatuldjadhav%2FDropBox-Cloud-Storage" rel="nofollow">
<svg aria-hidden="true" class="octicon octicon-star v-align-text-bottom" height="16" version="1.1" viewbox="0 0 14 16" width="14"><path d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z" fill-rule="evenodd"></path></svg>
      Star
</a>
<a aria-label="0 users starred this repository" class="social-count js-social-count" href="/atuldjadhav/DropBox-Cloud-Storage/stargazers">
      0
    </a>
</li>
<li>
<a aria-label="You must be signed in to fork a repository" class="btn btn-sm btn-with-count tooltipped tooltipped-s" data-hydro-click='{"event_type":"authentication.click","payload":{"location_in_page":"repo details fork button","repository_id":55005225,"auth_type":"LOG_IN","client_id":null,"originating_request_id":"C279:25B3:32ADC05:4D559B0:5D9A297F","originating_url":"https://github.com/atuldjadhav/DropBox-Cloud-Storage","referrer":null,"user_id":null}}' data-hydro-click-hmac="61d60046b44579d1303cca435fedea9cb2731461dbddcf8ff6717529bf5c12a7" href="/login?return_to=%2Fatuldjadhav%2FDropBox-Cloud-Storage" rel="nofollow">
<svg aria-hidden="true" class="octicon octicon-repo-forked v-align-text-bottom" height="16" version="1.1" viewbox="0 0 10 16" width="10"><path d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z" fill-rule="evenodd"></path></svg>
        Fork
</a>
<a aria-label="0 users forked this repository" class="social-count" href="/atuldjadhav/DropBox-Cloud-Storage/network/members">
      0
    </a>
</li>
</ul>
<h1 class="public">
<svg aria-hidden="true" class="octicon octicon-repo" height="16" version="1.1" viewbox="0 0 12 16" width="12"><path d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z" fill-rule="evenodd"></path></svg>
<span class="author" itemprop="author"><a class="url fn" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=17938694" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/atuldjadhav" rel="author">atuldjadhav</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/atuldjadhav/DropBox-Cloud-Storage">DropBox-Cloud-Storage</a></strong>
</h1>
</div>
<nav aria-label="Repository" class="hx_reponav reponav js-repo-nav js-sidenav-container-pjax container" data-pjax="#js-repo-pjax-container" itemscope="" itemtype="http://schema.org/BreadcrumbList">
<span itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
<a aria-current="page" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /atuldjadhav/DropBox-Cloud-Storage" href="/atuldjadhav/DropBox-Cloud-Storage" itemprop="url">
<svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewbox="0 0 14 16" width="14"><path d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z" fill-rule="evenodd"></path></svg>
<span itemprop="name">Code</span>
<meta content="1" itemprop="position"/>
</a> </span>
<span itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
<a class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /atuldjadhav/DropBox-Cloud-Storage/issues" href="/atuldjadhav/DropBox-Cloud-Storage/issues" itemprop="url">
<svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewbox="0 0 14 16" width="14"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z" fill-rule="evenodd"></path></svg>
<span itemprop="name">Issues</span>
<span class="Counter">0</span>
<meta content="2" itemprop="position"/>
</a> </span>
<span itemprop="itemListElement" itemscope="" itemtype="http://schema.org/ListItem">
<a class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls checks /atuldjadhav/DropBox-Cloud-Storage/pulls" href="/atuldjadhav/DropBox-Cloud-Storage/pulls" itemprop="url">
<svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewbox="0 0 12 16" width="12"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z" fill-rule="evenodd"></path></svg>
<span itemprop="name">Pull requests</span>
<span class="Counter">0</span>
<meta content="3" itemprop="position"/>
</a> </span>
<a class="js-selected-navigation-item reponav-item" data-hotkey="g b" data-selected-links="repo_projects new_repo_project repo_project /atuldjadhav/DropBox-Cloud-Storage/projects" href="/atuldjadhav/DropBox-Cloud-Storage/projects">
<svg aria-hidden="true" class="octicon octicon-project" height="16" version="1.1" viewbox="0 0 15 16" width="15"><path d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z" fill-rule="evenodd"></path></svg>
      Projects
      <span class="Counter">0</span>
</a>
<a class="js-selected-navigation-item reponav-item" data-selected-links="security alerts policy code_scanning /atuldjadhav/DropBox-Cloud-Storage/security/advisories" data-skip-pjax="true" href="/atuldjadhav/DropBox-Cloud-Storage/security/advisories">
<svg aria-hidden="true" class="octicon octicon-shield" height="16" version="1.1" viewbox="0 0 14 16" width="14"><path d="M0 2l7-2 7 2v6.02C14 12.69 8.69 16 7 16c-1.69 0-7-3.31-7-7.98V2zm1 .75L7 1l6 1.75v5.268C13 12.104 8.449 15 7 15c-1.449 0-6-2.896-6-6.982V2.75zm1 .75L7 2v12c-1.207 0-5-2.482-5-5.985V3.5z" fill-rule="evenodd"></path></svg>
      Security
</a>
<a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse people /atuldjadhav/DropBox-Cloud-Storage/pulse" href="/atuldjadhav/DropBox-Cloud-Storage/pulse">
<svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z" fill-rule="evenodd"></path></svg>
      Insights
</a>
</nav>
</div>"""
    return html

def data_language_data_1():
    html = """<li>
<a data-ga-click="Repository, language stats search click, location:repo overview" href="/atuldjadhav/DropBox-Cloud-Storage/search?l=css">
<span class="color-block language-color" style="background-color:#563d7c;"></span>
<span class="lang">CSS</span>
<span class="percent">52.0%</span>
</a>
</li>"""
    return html

def data_language_data_2():
    html = """<li>
<span>
<span class="color-block language-color" style="background-color:#ededed;"></span>
<span class="lang">Other</span>
<span class="percent">0.3%</span>
</span>
</li>"""
    return html

def data_create_url():
    data = {'keywords': ['python', 'crawler', 'json'], 'type': 'Repositories'}
    return data

def data_proxies():
    proxies = {0: '194.126.37.94:8080', 1: '13.78.125.167:8080'}
    return proxies


class test_crawler(unittest.TestCase):

    def test_read_input(self):
        data = crawler.read_input("test_input.txt")
        self.assertTrue(checkers.is_json(data))

    def test_create_url(self):
        url = crawler.create_url(data_create_url())
        self.assertEqual(url, "https://github.com/search?q=python+crawler+json&type=Repositories")

    def test_request(self):
        url = "https://github.com/search?q=python+crawler+json&type=Repositories"
        proxies = {0: '194.126.37.94:8080', 1: '13.78.125.167:8080'}
        code, response_data = crawler.request(url, proxies)
        self.assertEqual(code, 200)
        self.assertTrue(checkers.is_not_empty(response_data))

    def test_get_urls(self):
        html = BeautifulSoup(data_get_urls(), "lxml")
        repo_data = crawler.get_urls(html, data_proxies())
        self.assertEqual(repo_data[0]["url"], "https://github.com/atuldjadhav/DropBox-Cloud-Storage")
        self.assertEqual(repo_data[1]["url"], "https://github.com/michealbalogun/Horizon-dashboard")

    def test_next_page(self):
        html_1 = BeautifulSoup(data_next_page_1(), "lxml")
        page_url = crawler.next_page(html_1.body.ul)
        self.assertEqual(page_url, "https://github.com/search?p=2&q=python+crawler+json&type=Repositories")
        html_2 = BeautifulSoup(data_next_page_2(), "lxml")
        page_url = crawler.next_page(html_2.body.ul)
        self.assertEqual(page_url, None)

    def test_get_owner(self):
        html = BeautifulSoup(data_get_owner(), "lxml")
        owner = crawler.get_owner(html)
        self.assertEqual(owner["owner"], "atuldjadhav")

    def test_language_data(self):
        html_1 = BeautifulSoup(data_language_data_1(), "lxml")
        lang, lang_val = crawler.language_data(html_1.body.li)
        self.assertEqual(lang, "CSS")
        self.assertEqual(lang_val, 52.0)
        html_2 = BeautifulSoup(data_language_data_2(), "lxml")
        lang, lang_val = crawler.language_data(html_2.body.li)
        self.assertEqual(lang, "Other")
        self.assertEqual(lang_val, 0.3)


if __name__ == '__main__':
    unittest.main()
