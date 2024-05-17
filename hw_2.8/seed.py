import json
# from models import Tag, Decription, Author, Quote


'''dla cytatów'''
def get_quotes():
    with open('quotes.json', 'r') as fh:
        quotes_raw = json.load(fh)

    print(quotes_raw[0])


if __name__ == '__main__':
    get_quotes()