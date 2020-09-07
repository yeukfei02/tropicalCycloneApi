from flask import Flask, request, make_response
from app import app, db
from datetime import datetime

from src.models.TrackHistory import *

@app.route('/api/track-history', methods=['POST'])
def create_track_history():
    if request.json:
        description_id = request.json['descriptionId']
        synoptic_time = request.json['synopticTime']
        latitude = request.json['latitude']
        longitude = request.json['longitude']
        intensity = request.json['intensity']
        now = datetime.now()

        track_history = TrackHistory(description_id, synoptic_time, latitude, longitude, intensity, now, now)
        db.session.add(track_history)
        db.session.commit()

    data = {
        "message": "create track history",
    }
    return make_response(data, 201)

@app.route('/api/track-history', methods=['GET'])
def get_all_track_history():
    track_history_list = TrackHistory.query.order_by(TrackHistory.track_history_id).all()

    formatted_track_history_list = []
    for track_history in track_history_list:
        obj = {
            "id": track_history.track_history_id,
            "description_id": track_history.description_id,
            "synoptic_time": track_history.synoptic_time,
            "latitude": track_history.latitude,
            "longitude": track_history.longitude,
            "intensity": track_history.intensity,
            "created_by": str(track_history.created_by),
            "updated_by": str(track_history.updated_by)
        }
        formatted_track_history_list.append(obj)

    data = {
        "message": "get all track history",
        "trackHistorys": formatted_track_history_list
    }
    return make_response(data, 200)

# @app.route('/api/track-history/<id>', methods=['GET'])
# def get_track_history_by_id(id):
#     id = request.view_args["id"]

#     if id is not None:
#         track_history = TrackHistory.query.filter_by(track_history_id=id).first()
#         if track_history:
#             obj = {
#                 "id": track_history.track_history_id,
#                 "description_id": track_history.description_id,
#                 "synoptic_time": track_history.synoptic_time,
#                 "latitude": track_history.latitude,
#                 "longitude": track_history.longitude,
#                 "intensity": track_history.intensity,
#                 "created_by": str(track_history.created_by),
#                 "updated_by": str(track_history.updated_by)
#             }

#             data = {
#                 "message": "get track history by id",
#                 "trackHistory": obj
#             }
#             return make_response(data, 200)
#         else:
#             data = {
#                 "message": "get track history by id",
#                 "trackHistory": {}
#             }
#             return make_response(data, 200)

@app.route('/api/track-history/<descriptionId>', methods=['GET'])
def get_track_history_by_id(descriptionId):
    description_id = request.view_args["descriptionId"]

    if description_id is not None:
        track_history = TrackHistory.query.filter_by(description_id=description_id).first()
        if track_history:
            obj = {
                "id": track_history.track_history_id,
                "description_id": track_history.description_id,
                "synoptic_time": track_history.synoptic_time,
                "latitude": track_history.latitude,
                "longitude": track_history.longitude,
                "intensity": track_history.intensity,
                "created_by": str(track_history.created_by),
                "updated_by": str(track_history.updated_by)
            }

            data = {
                "message": "get track history by description_id",
                "trackHistory": obj
            }
            return make_response(data, 200)
        else:
            data = {
                "message": "get track history by description_id",
                "trackHistory": {}
            }
            return make_response(data, 200)

@app.route('/api/track-history/<id>', methods=['PUT'])
def update_track_history_by_id(id):
    id = request.view_args["id"]

    if id is not None:
        track_history = TrackHistory.query.filter_by(track_history_id=id).first()
        if track_history:
            if request.json:
                description_id = request.json['descriptionId']
                synoptic_time = request.json['synopticTime']
                latitude = request.json['latitude']
                longitude = request.json['longitude']
                intensity = request.json['intensity']

                now = datetime.now()

                track_history.description_id = description_id
                track_history.synoptic_time = synoptic_time
                track_history.latitude = latitude
                track_history.longitude = longitude
                track_history.intensity = intensity
                track_history.updated_by = now

                db.session.commit()

                data = {
                    "message": "update track history by id",
                }
                return make_response(data, 200)
        else:
            data = {
                "message": "no this record",
            }
            return make_response(data, 200)

@app.route('/api/track-history/<id>', methods=['DELETE'])
def delete_track_history_by_id(id):
    id = request.view_args["id"]

    if id is not None:
        track_history = TrackHistory.query.filter_by(track_history_id=id).first()
        if track_history:
            db.session.delete(track_history)
            db.session.commit()

            data = {
                "message": "delete track history by id",
            }
            return make_response(data, 200)
        else:
            data = {
                "message": "no this record",
            }
            return make_response(data, 200)