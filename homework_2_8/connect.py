from mongoengine import connect

if __name__ == '__main__':
    connect(host=f'mongodb+srv://fragile_data@firstcluster.dvmoxij.mongodb.net/', ssl=True)