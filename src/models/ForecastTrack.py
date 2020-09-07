from app import db

class ForecastTrack(db.Model):
    __tablename__ = 'forecast_track'

    forecast_track_id = db.Column(db.Integer, primary_key=True)
    description_id = db.Column(db.String(255), nullable=True)
    forecast_hour = db.Column(db.Integer(), nullable=True)
    latitude = db.Column(db.Float(), nullable=True)
    longitude = db.Column(db.Float(), nullable=True)
    intensity = db.Column(db.Integer(), nullable=True)
    created_by = db.Column(db.TIMESTAMP, server_default=db.func.now())
    updated_by = db.Column(db.TIMESTAMP, server_default=db.func.now())

    def __init__(self, description_id, forecast_hour, latitude, longitude, intensity, created_by, updated_by):
        self.description_id = description_id
        self.forecast_hour = forecast_hour
        self.latitude = latitude
        self.longitude = longitude
        self.intensity = intensity
        self.created_by = created_by
        self.updated_by = updated_by

db.create_all()
db.session.commit()