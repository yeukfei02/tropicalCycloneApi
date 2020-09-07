from flask import Flask, request, make_response
from app import app, db
from datetime import datetime

from src.models.TropicalCyclone import *

@app.route('/api/tropical-cyclone', methods=['POST'])
def create_tropical_cyclone():
    if request.json:
        place = request.json['place']
        description_text = request.json['descriptionText']
        image = request.json['image']
        now = datetime.now()

        tropical_cyclone = TropicalCyclone(place, description_text, image, now, now)
        db.session.add(tropical_cyclone)
        db.session.commit()

    data = {
        "message": "create tropical cyclone",
    }
    return make_response(data, 201)

@app.route('/api/tropical-cyclone', methods=['GET'])
def get_all_tropical_cyclone():
    tropical_cyclone_list = TropicalCyclone.query.order_by(TropicalCyclone.tropical_cyclone_id).all()

    formatted_tropical_cyclone_list = []
    for tropical_cyclone in tropical_cyclone_list:
        obj = {
            "id": tropical_cyclone.tropical_cyclone_id,
            "place": tropical_cyclone.place,
            "description_text": tropical_cyclone.description_text,
            "image": tropical_cyclone.image,
            "created_by": str(tropical_cyclone.created_by),
            "updated_by": str(tropical_cyclone.updated_by)
        }
        formatted_tropical_cyclone_list.append(obj)

    data = {
        "message": "get all tropical cyclone",
        "tropicalCyclones": formatted_tropical_cyclone_list
    }
    return make_response(data, 200)

@app.route('/api/tropical-cyclone/<id>', methods=['GET'])
def get_tropical_cyclone_by_id(id):
    id = request.view_args["id"]

    if id is not None:
        tropical_cyclone = TropicalCyclone.query.filter_by(tropical_cyclone_id=id).first()
        if tropical_cyclone:
            obj = {
                "id": tropical_cyclone.tropical_cyclone_id,
                "place": tropical_cyclone.place,
                "description_text": tropical_cyclone.description_text,
                "image": tropical_cyclone.image,
                "created_by": str(tropical_cyclone.created_by),
                "updated_by": str(tropical_cyclone.updated_by)
            }

            data = {
                "message": "get tropical cyclone by id",
                "tropicalCyclone": obj
            }
            return make_response(data, 200)
        else:
            data = {
                "message": "get tropical cyclone by id",
                "tropicalCyclone": {}
            }
            return make_response(data, 200)

@app.route('/api/tropical-cyclone/<id>', methods=['PUT'])
def update_tropical_cyclone_by_id(id):
    id = request.view_args["id"]

    if id is not None:
        tropical_cyclone = TropicalCyclone.query.filter_by(tropical_cyclone_id=id).first()
        if tropical_cyclone:
            if request.json:
                place = request.json['place']
                description_text = request.json['descriptionText']
                image = request.json['image']

                now = datetime.now()

                tropical_cyclone.place = place
                tropical_cyclone.description_text = description_text
                tropical_cyclone.image = image
                tropical_cyclone.updated_by = now

                db.session.commit()

                data = {
                    "message": "update tropical cyclone by id",
                }
                return make_response(data, 200)
        else:
            data = {
                "message": "no this record",
            }
            return make_response(data, 200)

@app.route('/api/tropical-cyclone/<id>', methods=['DELETE'])
def delete_tropical_cyclone_by_id(id):
    id = request.view_args["id"]

    if id is not None:
        tropical_cyclone = TropicalCyclone.query.filter_by(tropical_cyclone_id=id).first()
        if tropical_cyclone:
            db.session.delete(tropical_cyclone)
            db.session.commit()

            data = {
                "message": "delete tropical cyclone by id",
            }
            return make_response(data, 200)
        else:
            data = {
                "message": "no this record",
            }
            return make_response(data, 200)