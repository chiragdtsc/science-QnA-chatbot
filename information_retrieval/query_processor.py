import requests
from bs4 import BeautifulSoup

class ContextRetrieval:

    def __init__(self, query):
        self.query = query

    def get_source(self):
        url = "https://www.google.com/search?q="
        try:
            response = requests.get(url + self.query)
            return response

        except requests.exceptions.RequestException as e:
            print(e)

    def parse_results(self, response):
        css_identifier_snippets = '.BNeawe'
        
        soup = BeautifulSoup(response.text, 'lxml')
        result = list()
        
        snippets = soup.select(css_identifier_snippets)

        for section in snippets:
            content = section.find('div')
            if content:
                result.append(content.find('div').text)
            
        return result

    def extractFeaturedArticle (self, response):
        css_identifier_result = '.kCrYT'
        soup = BeautifulSoup(response.text, 'lxml')
        divs = soup.select(css_identifier_result)
        for d in divs:
            a = d.find('a')
            if a:
                featured_url = a.attrs['href']
                return featured_url[7:]

    def web_search(self):
        response = self.get_source()
        results = self.parse_results(response)
        # featured_article = self.extractFeaturedArticle(response)
        return results

