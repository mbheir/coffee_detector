from bs4 import BeautifulSoup
import random

def write_quotes_to_file():
    f = open("coffee_html.html","r",encoding="utf8")
    w = open("quotes.txt", "a",encoding="utf8")
    # print(f.read())
    soup = BeautifulSoup(f.read(),'html.parser')
    f.close()

    for block in soup.blockquote.next_siblings:
        if block!='\n':
            try:
                quote = block.p.get_text()
                footer = block.footer.get_text()
                print(f'{quote}{footer}')
                w.write(f'{quote}{footer}\n')
            except:
                pass
    w.close()

def read_quote():
    f = open("quotes.txt","r",encoding="utf8")
    quotes = f.read().split('\n')
    return random.choice(quotes)
