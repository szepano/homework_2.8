from mongoengine import connect

if __name__ == '__main__':
    connect(host=f'connection URI', ssl=True)