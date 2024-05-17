from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import EmbeddedDocumentField, StringField, ListField, ReferenceField

class Tag(EmbeddedDocument):
    name = StringField()


class Author(Document):
    name = StringField()
    born = StringField()
    born_in = StringField()
    desc = StringField()


class Quote(EmbeddedDocument):
    quote = StringField()
    tags = ListField(EmbeddedDocumentField(Tag))
    author = ReferenceField(Author)