# Overview

This script scans your Goodreads "to-read" shelf and searches [Borrowbox](https://fe.bolindadigital.com/wldcs_bol_fo/b2i/mainPage.html?b2bSite=4825&fromPage=1) for each book.

# Prerequisites

## Packages

```
sudo pip3 install -r requirements.txt
```

## Goodreads credentials

Create a file called "credentials.json", following the same structure as "credentials_example.json". Replace the values for `<key>` and `<user_id>`. These values can be obtained from [here](https://www.goodreads.com/api/keys).

# To run

```
python3 main.py
```
