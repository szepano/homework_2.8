import json
from models import Tag, Author, Quote


def insert_from_json(authors_file, quotes_file):

    with open(authors_file, 'r') as fh:
        authors = json.load(fh)

    for i in authors:
        new_auth = Author(name=i['fullname'],
                        born=i['born_date'],
                        born_in=i['born_location'],
                        desc=i['description']
                        ).save()
    
    with open(quotes_file, 'r') as fh:
        quotes = json.load(fh)

    for i in quotes:
        tags = Tag(name=(t for t in i['tags']))
        

if __name__ == '__main__':
    insert_from_json('authors.json', 'quotes.json')