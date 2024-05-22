from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import EmbeddedDocumentField, StringField, ListField, ReferenceField, BooleanField, EmailField
from connect import connect

connect(host='mongodb+srv://fragile_data@firstcluster.dvmoxij.mongodb.net/', ssl=True)

class Tag(EmbeddedDocument):
    name = StringField(required=True)


class Author(Document):
    name = StringField(required=True)
    born = StringField()
    born_in = StringField()
    desc = StringField()


class Quote(Document):
    quote = StringField(required=True)
    tags = ListField(EmbeddedDocumentField(Tag))
    author = ReferenceField(Author, required=True)

class Contact(Document):
    name = StringField(required=True)
    email = EmailField(required=True)
    sent = BooleanField(default=False)