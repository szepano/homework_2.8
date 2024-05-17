from mongoengine import connect

if __name__ == '__main__':
    connect(host=f'mongodb+srv://bartszczepan04:A501796b@firstcluster.dvmoxij.mongodb.net/', ssl=True)