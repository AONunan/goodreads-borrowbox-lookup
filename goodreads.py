import xml.etree.ElementTree as ET
import urllib.request
import json

# Return an array of Python dictionaries for each book in your Goodreads "to-read" list
def get_goodreads_books():
  xml_file = "goodreads.xml"

  with open("credentials.json") as json_file:
    data = json.load(json_file)

    key = data["goodreads"]["key"]
    user_id = data["goodreads"]["user_id"]

  url = "https://www.goodreads.com/review/list?v=2&key={}&id={}&per_page=200&shelf=to-read".format(key, user_id)

  urllib.request.urlretrieve(url, xml_file)

  tree = ET.parse(xml_file)
  reviews = tree.getroot()[2]

  books = []
  book_dict = {}

  for review in reviews:

    for book in review.iter("book"):

      for title_without_series in book.iter("title_without_series"):
        book_title = title_without_series.text

      for authors in book.iter("authors"):
        for author in authors.iter("author"):
          for name in author.iter("name"):
            book_author = name.text

    book_dict["title"] = book_title
    book_dict["author"] = book_author

    books.append(book_dict)
    book_dict = {} # Reset

  return books

