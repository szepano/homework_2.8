import json
from homework_2_8.models import Tag, Author, Quote
import sys

def insert_from_json(authors_file='authors.json', quotes_file='quotes.json'):

    author_dict = {}

    with open(authors_file, 'r', encoding='utf-8') as fh1:
        authors = json.load(fh1)

    for i in authors:
        new_auth = Author(name=i['fullname'],
                        born=i['born_date'],
                        born_in=i['born_location'],
                        desc=i['description']
                        )
        author_dict[i['fullname']] = new_auth
        new_auth.save()
    
    with open(quotes_file, 'r', encoding='utf-8') as fh2:
        quotes = json.load(fh2)

    for i in quotes:
        tags_ = [Tag(name=t) for t in i['tags']]
        quote = Quote(quote=i['quote'],
                      tags=tags_,
                      author = author_dict[i['author']])
        quote.save()
        

        
if __name__ == '__main__':
    print(sys.path)
    insert_from_json(sys.argv[1], sys.argv[2])