from app import db
from src.models.TrackHistory import *
import unittest
from datetime import datetime

import os
import sys
sys.path.insert(1, os.getcwd())


class TrackHistoryTest(unittest.TestCase):
    id = 0

    @classmethod
    def setUpClass(cls):
        last_track_history = TrackHistory.query.order_by(
            TrackHistory.track_history_id.desc()).first()
        if last_track_history:
            cls.id = last_track_history.track_history_id

    def test_001_create_track_history(self):
        print('test_001_create_track_history start')

        description_id = "AAABBB123"
        synoptic_time = "2020-03-21 15:30"
        latitude = 22.22
        longitude = 33.33
        intensity = 50
        now = datetime.now()

        track_history = TrackHistory(
            description_id, synoptic_time, latitude, longitude, intensity, now, now)
        db.session.add(track_history)
        db.session.commit()

        self.assertTrue(track_history is not None)

        if track_history:
            self.assertIsNotNone(track_history.description_id)
            self.assertIsNotNone(track_history.synoptic_time)
            self.assertIsNotNone(track_history.latitude)
            self.assertIsNotNone(track_history.longitude)
            self.assertIsNotNone(track_history.intensity)
            self.assertIsNotNone(str(track_history.created_by))
            self.assertIsNotNone(str(track_history.updated_by))

        print('test_001_create_track_history end')

    def test_002_get_track_history(self):
        print('test_002_get_track_history start')

        track_history_list = TrackHistory.query.order_by(
            TrackHistory.track_history_id).all()

        self.assertTrue(track_history_list is not None)

        if track_history_list:
            for track_history in track_history_list:
                self.assertIsNotNone(track_history.description_id)
                self.assertIsNotNone(track_history.synoptic_time)
                self.assertIsNotNone(track_history.latitude)
                self.assertIsNotNone(track_history.longitude)
                self.assertIsNotNone(track_history.intensity)
                self.assertIsNotNone(str(track_history.created_by))
                self.assertIsNotNone(str(track_history.updated_by))

        print('test_002_get_track_history end')

    def test_003_get_track_history_by_id(self):
        print('test_003_get_track_history_by_id start')

        track_history = TrackHistory.query.filter_by(
            track_history_id=self.id).first()

        self.assertTrue(track_history is not None)

        if track_history:
            self.assertIsNotNone(track_history.description_id)
            self.assertIsNotNone(track_history.synoptic_time)
            self.assertIsNotNone(track_history.latitude)
            self.assertIsNotNone(track_history.longitude)
            self.assertIsNotNone(track_history.intensity)
            self.assertIsNotNone(str(track_history.created_by))
            self.assertIsNotNone(str(track_history.updated_by))

        print('test_003_get_track_history_by_id end')

    def test_004_update_track_history_by_id(self):
        print('test_004_update_track_history_by_id start')

        track_history = TrackHistory.query.filter_by(
            track_history_id=self.id).first()

        self.assertTrue(track_history is not None)

        if track_history:
            description_id = "EEEHHH123"
            synoptic_time = "2025-05-25 15:30"
            latitude = 55.5
            longitude = 66.666
            intensity = 880
            now = datetime.now()

            track_history.description_id = description_id
            track_history.synoptic_time = synoptic_time
            track_history.latitude = latitude
            track_history.longitude = longitude
            track_history.intensity = intensity
            track_history.updated_by = now

            db.session.commit()

            self.assertIsNotNone(track_history.description_id)
            self.assertIsNotNone(track_history.synoptic_time)
            self.assertIsNotNone(track_history.latitude)
            self.assertIsNotNone(track_history.longitude)
            self.assertIsNotNone(track_history.intensity)
            self.assertIsNotNone(str(track_history.created_by))
            self.assertIsNotNone(str(track_history.updated_by))

        print('test_004_update_track_history_by_id end')

    def test_005_delete_track_history_by_id(self):
        print('test_005_delete_track_history_by_id start')

        track_history = TrackHistory.query.filter_by(
            track_history_id=self.id).first()

        self.assertTrue(track_history is not None)

        if track_history:
            db.session.delete(track_history)
            db.session.commit()

        print('test_005_delete_track_history_by_id end')


if __name__ == '__main__':
    unittest.main()
