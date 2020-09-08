from flask import Flask, request, make_response
from app import app, db
from datetime import datetime

from src.models.ForecastTrack import *

@app.route('/api/forecast-track', methods=['POST'])
def create_forecast_track():
    if request.json:
        description_id = request.json['descriptionId']
        forecast_hour = request.json['forecastHour']
        latitude = request.json['latitude']
        longitude = request.json['longitude']
        intensity = request.json['intensity']
        now = datetime.now()

        forecast_track = ForecastTrack(description_id, forecast_hour, latitude, longitude, intensity, now, now)
        db.session.add(forecast_track)
        db.session.commit()

    data = {
        "message": "create forecast track",
    }
    return make_response(data, 201)

@app.route('/api/forecast-track', methods=['GET'])
def get_all_forecast_track():
    forecast_track_list = ForecastTrack.query.order_by(ForecastTrack.forecast_track_id).all()

    formatted_forecast_track_list = []
    for forecast_track in forecast_track_list:
        obj = {
            "id": forecast_track.forecast_track_id,
            "description_id": forecast_track.description_id,
            "forecast_hour": forecast_track.forecast_hour,
            "latitude": forecast_track.latitude,
            "longitude": forecast_track.longitude,
            "intensity": forecast_track.intensity,
            "created_by": str(forecast_track.created_by),
            "updated_by": str(forecast_track.updated_by)
        }
        formatted_forecast_track_list.append(obj)

    data = {
        "message": "get all forecast track",
        "forecastTracks": formatted_forecast_track_list
    }
    return make_response(data, 200)

# @app.route('/api/forecast-track/<id>', methods=['GET'])
# def get_forecast_track_by_id(id):
#     id = request.view_args["id"]

#     if id is not None:
#         forecast_track = ForecastTrack.query.filter_by(forecast_track_id=id).first()
#         if forecast_track:
#             obj = {
#                 "id": forecast_track.forecast_track_id,
#                 "description_id": forecast_track.description_id,
#                 "forecast_hour": forecast_track.forecast_hour,
#                 "latitude": forecast_track.latitude,
#                 "longitude": forecast_track.longitude,
#                 "intensity": forecast_track.intensity,
#                 "created_by": str(forecast_track.created_by),
#                 "updated_by": str(forecast_track.updated_by)
#             }

#             data = {
#                 "message": "get forecast track by id",
#                 "forecastTrack": obj
#             }
#             return make_response(data, 200)
#         else:
#             data = {
#                 "message": "get forecast track by id",
#                 "forecastTrack": {}
#             }
#             return make_response(data, 200)

@app.route('/api/forecast-track/<descriptionId>', methods=['GET'])
def get_forecast_track_by_description_id(descriptionId):
    description_id = request.view_args["descriptionId"]

    if description_id is not None:
        forecast_track_list = ForecastTrack.query.order_by(ForecastTrack.forecast_track_id).all()

        formatted_forecast_track_list = []
        for forecast_track in forecast_track_list:
            if forecast_track.description_id == description_id:
                obj = {
                    "id": forecast_track.forecast_track_id,
                    "description_id": forecast_track.description_id,
                    "forecast_hour": forecast_track.forecast_hour,
                    "latitude": forecast_track.latitude,
                    "longitude": forecast_track.longitude,
                    "intensity": forecast_track.intensity,
                    "created_by": str(forecast_track.created_by),
                    "updated_by": str(forecast_track.updated_by)
                }
                formatted_forecast_track_list.append(obj)

        data = {
            "message": "get all forecast track",
            "forecastTracks": formatted_forecast_track_list
        }
        return make_response(data, 200)

@app.route('/api/forecast-track/<id>', methods=['PUT'])
def update_forecast_track_by_id(id):
    id = request.view_args["id"]

    if id is not None:
        forecast_track = ForecastTrack.query.filter_by(forecast_track_id=id).first()
        if forecast_track:
            if request.json:
                description_id = request.json['descriptionId']
                forecast_hour = request.json['forecastHour']
                latitude = request.json['latitude']
                longitude = request.json['longitude']
                intensity = request.json['intensity']

                now = datetime.now()

                forecast_track.description_id = description_id
                forecast_track.forecast_hour = forecast_hour
                forecast_track.latitude = latitude
                forecast_track.longitude = longitude
                forecast_track.intensity = intensity
                forecast_track.updated_by = now

                db.session.commit()

                data = {
                    "message": "update forecast track by id",
                }
                return make_response(data, 200)
        else:
            data = {
                "message": "no this record",
            }
            return make_response(data, 200)

@app.route('/api/forecast-track/<id>', methods=['DELETE'])
def delete_forecast_track_by_id(id):
    id = request.view_args["id"]

    if id is not None:
        forecast_track = ForecastTrack.query.filter_by(forecast_track_id=id).first()
        if forecast_track:
            db.session.delete(forecast_track)
            db.session.commit()

            data = {
                "message": "delete forecast track by id",
            }
            return make_response(data, 200)
        else:
            data = {
                "message": "no this record",
            }
            return make_response(data, 200)