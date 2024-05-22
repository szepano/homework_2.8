import pika
from connect import connect
from models import Contact
from faker import Faker

# connect(host=f'mongodb+srv://bartszczepan04:A501796b@firstcluster.dvmoxij.mongodb.net/', ssl=True)

creadentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=creadentials))
channel = connection.channel()
channel.queue_declare(queue='email_queue', durable=True)


def create_contacts(n: int):
    fake = Faker()
    contacts = []

    for i in range(n):
        contact = Contact(name=fake.name(),
                          email=fake.email())
        contact.save()
        contacts.append(contact)
    return contacts


def send(contacts: list):
    for i in contacts:
        
        channel.basic_publish(
            exchange='',
            routing_key='email_queue',
            body=str(i.id),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            )
        )
        print(f'Sent {i.id} to queue')
    connection.close()

if __name__ == '__main__':
    contacts = create_contacts(5)
    send(contacts)