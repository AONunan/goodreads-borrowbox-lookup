import time
from difflib import SequenceMatcher

from borrowbox import get_borrowbox_results, parse_borrowbox_results
from goodreads import get_goodreads_books

def compare(a, b):
  return SequenceMatcher(None, a, b).ratio() # Return the similarity of two strings, on a scale between 0 and 1

def main():

  base_url = "https://fe.bolindadigital.com/wldcs_bol_fo/b2i/"

  book_format = "eAudiobooks"
  # book_format = "eBooks"

  for goodreads_book in get_goodreads_books():
    print("**************************************************")
    print(f"Searching for '{goodreads_book['title']}' by {goodreads_book['author']}.")
    print()
  
    borrowbox_result_page = get_borrowbox_results(goodreads_book['title'], book_format)
    borrowbox_result = parse_borrowbox_results(borrowbox_result_page, book_format)

    if borrowbox_result != "":

      # Check that the book title and the author name are similar to the Goodreads source, as Borrowbox will sometimes return a search result even if it's not what you are looking for
      if compare(borrowbox_result['title'], goodreads_book['title']) > 0.5 and compare(borrowbox_result['author'], goodreads_book['author']) > 0.5:
        print(f"Title:     {borrowbox_result['title']}")
        print(f"Author:    {borrowbox_result['author']}")

        if(book_format == "eAudiobooks"):
          print(f"Narrator:  {borrowbox_result['narrator']}")
  
        print(f"URL:       {base_url}{borrowbox_result['url']}")
        print(f"Available: {borrowbox_result['available']}")
      else:
        print("No results found.")
      
    else:
      print("No results found.")

    print()
    time.sleep(1) # Introduce delay so too many requests are not being made in a quick succession

if __name__ == '__main__':
    main()
