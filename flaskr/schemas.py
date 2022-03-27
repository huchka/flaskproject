from flaskr import ma
from flaskr.models import NoteModel


class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NoteModel

