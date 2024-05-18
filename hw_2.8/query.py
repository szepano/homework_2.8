from connect import connect
from models import Quote, Author, Tag

connect(host=f'mongodb+srv://bartszczepan04:A501796b@firstcluster.dvmoxij.mongodb.net/', ssl=True)

def get_quotes(author_name):

    author = Author.objects(name=author_name).first()
    q_raw = Quote.objects(author=author)
    quotes = [q for q in q_raw]

    print(f'Quotes by {author.name}:')
    for i in quotes:
        print(i.quote)

if __name__ == '__main__':
    get_quotes('Albert Einstein')