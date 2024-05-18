from connect import connect
from models import Quote, Author, Tag

connect(host=f'mongodb+srv://bartszczepan04:A501796b@firstcluster.dvmoxij.mongodb.net/', ssl=True)


def by_author(author_name):

    author = Author.objects(name__iexact=author_name[0]).first()
    q_raw = Quote.objects(author=author)
    quotes = [q for q in q_raw]

    print(f'Quotes by {author.name}:')
    for i in quotes:
        print(i.quote)


def by_tag(tag: list):
    '''Możliwe, że trochę niezgodne z zadaniem ale zamiast dwóch różnych funkcji dla tags i tag osobno
        używam jednej dzięki __all'''

    quote_raw = Quote.objects(tags__name__all=tag)
    if not quote_raw:
        print(f"Couldn't find a quote with given tags: {tag}")
        return
    quotes = [q for q in quote_raw]
    for i in quotes:
        print(i.quote)

def help():
    print(f"Available commands:\nname: <author name> - see quotes from inserted author (case insensitive)\ntag: <tag1,tag2> - search quotes with ALL given tags (second tag is optional)\nexit - self-explanatory")

commands_dict = {
    'help': help,
    'name': by_author,
    'tag': by_tag
}


def interaction():
    while True:
        line = input(f'To see available commands enter "help"\nEnter command: ')
        if line =='exit':
            break
        if line == 'help':
            help()
            continue
        parts = line.split(': ')
        command = parts[0]
        args = [parts[1]]
        if ',' in args:
            args = [t for t in args.split(',')]
        commands_dict[command](args)

if __name__ == '__main__':
    interaction()