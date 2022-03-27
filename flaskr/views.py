from flask import request, jsonify

from flaskr import app, db
from flaskr.models import NoteModel
from flaskr.schemas import NoteSchema

note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)


@app.route('/note/')
def note_list():
    app.logger.info("Listing all note list.")
    all_notes = NoteModel.query.all()
    return jsonify(notes_schema.dump(all_notes))


@app.route('/note/', methods=['POST'])
def create_note():
    data = request.get_json()
    note = NoteModel(**data)
    db.session.add(note)
    db.session.commit()
    return note_schema.jsonify(note), 201


@app.route('/note/<int:note_id>/', methods=["GET"])
def note_detail(note_id):
    note = NoteModel.query.get(note_id)
    return note_schema.jsonify(note)
