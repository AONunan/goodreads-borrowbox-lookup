import requests
import urllib.parse
from bs4 import BeautifulSoup

# Search Borrowbox and return the results as a HTML page
def get_borrowbox_results(book_title):

  base_url = 'https://fe.bolindadigital.com/wldcs_bol_fo/b2i/search.html?'
  parameters = {"filter": "all",
                "q": book_title,
                "b2bSite": "4825",
                "searchBy": "TITLE",
                "orderBy": "relevance",
                "loanFormat": "eAudiobooks"}
  url = base_url + urllib.parse.urlencode(parameters)

  page = requests.get(url)
  return page.text # Return the contents of the page as HTML

# Parse the HTML and return the first result as a Python dictionary
def parse_borrowbox_results(page):

  soup = BeautifulSoup(page, 'html.parser')

  result = {}

  try:
    search_result = soup.find("div", class_="productVerticalDetails")

    result["title"] = search_result.find("div", class_="productVerticalTitle").attrs["title"]
    result["url"] = search_result.find("div", class_="productVerticalTitle").find("a").attrs["href"]
    result["author"] = search_result.find("div", class_="productVerticalAuthor").attrs["title"]
    result["narrator"] = search_result.find("div", class_="productVerticalSpeaker").attrs["title"]
  
    try:
      result["available"] = search_result.find("div", class_="productVerticalAvailable").find("b").contents[-1].split()[-1]
    except:
      result["available"] = "Available now"

  except:
    result = ""

  return result
  



