from app import db

class TropicalCyclone(db.Model):
    __tablename__ = 'tropical_cyclone'

    tropical_cyclone_id = db.Column(db.Integer, primary_key=True)
    place = db.Column(db.String(255), nullable=True)
    description_text = db.Column(db.String(255), nullable=True)
    image = db.Column(db.String(255), nullable=True)
    created_by = db.Column(db.TIMESTAMP, server_default=db.func.now())
    updated_by = db.Column(db.TIMESTAMP, server_default=db.func.now())

    def __init__(self, place, description_text, image, created_by, updated_by):
        self.place = place
        self.description_text = description_text
        self.image = image
        self.created_by = created_by
        self.updated_by = updated_by

db.create_all()
db.session.commit()