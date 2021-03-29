import unittest
from datetime import datetime
from app import db
from src.models.ForecastTrack import ForecastTrack

import os
import sys
sys.path.insert(1, os.getcwd())


class ForecastTrackTest(unittest.TestCase):
    id = 0

    @classmethod
    def setUpClass(cls):
        last_forecast_track = ForecastTrack.query.order_by(
            ForecastTrack.forecast_track_id.desc()).first()
        if last_forecast_track:
            cls.id = last_forecast_track.forecast_track_id

    def test_001_create_forecast_track(self):
        print('test_001_create_forecast_track start')

        description_id = "AAABBB123"
        forecast_hour = 21
        latitude = 100.11
        longitude = 10.22
        intensity = 30
        now = datetime.now()

        forecast_track = ForecastTrack(
            description_id, forecast_hour, latitude, longitude, intensity, now, now)
        db.session.add(forecast_track)
        db.session.commit()

        self.assertTrue(forecast_track is not None)

        if forecast_track:
            self.assertIsNotNone(forecast_track.description_id)
            self.assertIsNotNone(forecast_track.forecast_hour)
            self.assertIsNotNone(forecast_track.latitude)
            self.assertIsNotNone(forecast_track.longitude)
            self.assertIsNotNone(forecast_track.intensity)
            self.assertIsNotNone(str(forecast_track.created_by))
            self.assertIsNotNone(str(forecast_track.updated_by))

        print('test_001_create_forecast_track end')

    def test_002_get_forecast_track(self):
        print('test_002_get_forecast_track start')

        forecast_track_list = ForecastTrack.query.order_by(
            ForecastTrack.forecast_track_id).all()

        self.assertTrue(forecast_track_list is not None)

        if forecast_track_list:
            for forecast_track in forecast_track_list:
                self.assertIsNotNone(forecast_track.description_id)
                self.assertIsNotNone(forecast_track.forecast_hour)
                self.assertIsNotNone(forecast_track.latitude)
                self.assertIsNotNone(forecast_track.longitude)
                self.assertIsNotNone(forecast_track.intensity)
                self.assertIsNotNone(str(forecast_track.created_by))
                self.assertIsNotNone(str(forecast_track.updated_by))

        print('test_002_get_forecast_track end')

    def test_003_get_forecast_track_by_id(self):
        print('test_003_get_forecast_track_by_id start')

        forecast_track = ForecastTrack.query.filter_by(
            forecast_track_id=self.id).first()

        self.assertTrue(forecast_track is not None)

        if forecast_track:
            self.assertIsNotNone(forecast_track.description_id)
            self.assertIsNotNone(forecast_track.forecast_hour)
            self.assertIsNotNone(forecast_track.latitude)
            self.assertIsNotNone(forecast_track.longitude)
            self.assertIsNotNone(forecast_track.intensity)
            self.assertIsNotNone(str(forecast_track.created_by))
            self.assertIsNotNone(str(forecast_track.updated_by))

        print('test_003_get_forecast_track_by_id end')

    def test_004_update_forecast_track_by_id(self):
        print('test_004_update_forecast_track_by_id start')

        forecast_track = ForecastTrack.query.filter_by(
            forecast_track_id=self.id).first()

        self.assertTrue(forecast_track is not None)

        if forecast_track:
            description_id = "CCCDDD556"
            forecast_hour = 29
            latitude = 8.11
            longitude = 88.22
            intensity = 99
            now = datetime.now()

            forecast_track.description_id = description_id
            forecast_track.forecast_hour = forecast_hour
            forecast_track.latitude = latitude
            forecast_track.longitude = longitude
            forecast_track.intensity = intensity
            forecast_track.updated_by = now

            db.session.commit()

            self.assertIsNotNone(forecast_track.description_id)
            self.assertIsNotNone(forecast_track.forecast_hour)
            self.assertIsNotNone(forecast_track.latitude)
            self.assertIsNotNone(forecast_track.longitude)
            self.assertIsNotNone(forecast_track.intensity)
            self.assertIsNotNone(str(forecast_track.created_by))
            self.assertIsNotNone(str(forecast_track.updated_by))

        print('test_004_update_forecast_track_by_id end')

    def test_005_delete_forecast_track_by_id(self):
        print('test_005_delete_forecast_track_by_id start')

        forecast_track = ForecastTrack.query.filter_by(
            forecast_track_id=self.id).first()

        self.assertTrue(forecast_track is not None)

        if forecast_track:
            db.session.delete(forecast_track)
            db.session.commit()

        print('test_005_delete_forecast_track_by_id end')


if __name__ == '__main__':
    unittest.main()
