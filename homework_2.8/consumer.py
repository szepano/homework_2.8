import pika
from models import Contact
from bson import ObjectId

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='email_queue', durable=True)
print(f'Waiting for messages. To exit press CTRL + C')

def send_email_stub(contact):
    print(f'Sending email to {contact.name}: {contact.email}')
    contact.sent = True
    contact.save()

def callback(ch, method, properties, body):
    contact = Contact.objects(id=ObjectId(body.decode())).first()
    if contact:
        send_email_stub(contact)
        print(f'Email sent to {contact.name}')
    else:
        print(f'Contact with id: {body} not found')
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='email_queue', on_message_callback=callback)

if __name__ == '__main__':
    channel.start_consuming()