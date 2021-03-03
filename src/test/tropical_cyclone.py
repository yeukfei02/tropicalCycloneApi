from app import db
from src.models.TropicalCyclone import *
import unittest
from datetime import datetime

import os
import sys
sys.path.insert(1, os.getcwd())


class TropicalCycloneTest(unittest.TestCase):
    id = 0

    @classmethod
    def setUpClass(cls):
        last_tropical_cyclone = TropicalCyclone.query.order_by(
            TropicalCyclone.tropical_cyclone_id.desc()).first()
        if last_tropical_cyclone:
            cls.id = last_tropical_cyclone.tropical_cyclone_id

    def test_001_create_tropical_cyclone(self):
        print('test_001_create_tropical_cyclone start')

        place = "test"
        description_id = "AAABBB123"
        description_text = "test2"
        image = "test3"
        now = datetime.now()

        tropical_cyclone = TropicalCyclone(
            place, description_id, description_text, image, now, now)
        db.session.add(tropical_cyclone)
        db.session.commit()

        self.assertTrue(tropical_cyclone is not None)

        if tropical_cyclone:
            self.assertIsNotNone(tropical_cyclone.place)
            self.assertIsNotNone(tropical_cyclone.description_id)
            self.assertIsNotNone(tropical_cyclone.description_text)
            self.assertIsNotNone(tropical_cyclone.image)
            self.assertIsNotNone(str(tropical_cyclone.created_by))
            self.assertIsNotNone(str(tropical_cyclone.updated_by))

        print('test_001_create_tropical_cyclone end')

    def test_002_get_tropical_cyclone(self):
        print('test_002_get_tropical_cyclone start')

        tropical_cyclone_list = TropicalCyclone.query.order_by(
            TropicalCyclone.tropical_cyclone_id).all()

        self.assertTrue(tropical_cyclone_list is not None)

        if tropical_cyclone_list:
            for tropical_cyclone in tropical_cyclone_list:
                self.assertIsNotNone(tropical_cyclone.place)
                self.assertIsNotNone(tropical_cyclone.description_id)
                self.assertIsNotNone(tropical_cyclone.description_text)
                self.assertIsNotNone(tropical_cyclone.image)
                self.assertIsNotNone(str(tropical_cyclone.created_by))
                self.assertIsNotNone(str(tropical_cyclone.updated_by))

        print('test_002_get_tropical_cyclone end')

    def test_003_get_tropical_cyclone_by_id(self):
        print('test_003_get_tropical_cyclone_by_id start')

        tropical_cyclone = TropicalCyclone.query.filter_by(
            tropical_cyclone_id=self.id).first()

        self.assertTrue(tropical_cyclone is not None)

        if tropical_cyclone:
            self.assertIsNotNone(tropical_cyclone.place)
            self.assertIsNotNone(tropical_cyclone.description_id)
            self.assertIsNotNone(tropical_cyclone.description_text)
            self.assertIsNotNone(tropical_cyclone.image)
            self.assertIsNotNone(str(tropical_cyclone.created_by))
            self.assertIsNotNone(str(tropical_cyclone.updated_by))

        print('test_003_get_tropical_cyclone_by_id end')

    def test_004_update_tropical_cyclone_by_id(self):
        print('test_004_update_tropical_cyclone_by_id start')

        tropical_cyclone = TropicalCyclone.query.filter_by(
            tropical_cyclone_id=self.id).first()

        self.assertTrue(tropical_cyclone is not None)

        if tropical_cyclone:
            place = "aaa"
            description_id = "EEEGGG123"
            description_text = "bbb"
            image = "ccc"
            now = datetime.now()

            tropical_cyclone.place = place
            tropical_cyclone.description_id = description_id
            tropical_cyclone.description_text = description_text
            tropical_cyclone.image = image
            tropical_cyclone.updated_by = now

            db.session.commit()

            self.assertIsNotNone(tropical_cyclone.place)
            self.assertIsNotNone(tropical_cyclone.description_id)
            self.assertIsNotNone(tropical_cyclone.description_text)
            self.assertIsNotNone(tropical_cyclone.image)
            self.assertIsNotNone(str(tropical_cyclone.created_by))
            self.assertIsNotNone(str(tropical_cyclone.updated_by))

        print('test_004_update_tropical_cyclone_by_id end')

    def test_005_delete_tropical_cyclone_by_id(self):
        print('test_005_delete_tropical_cyclone_by_id start')

        tropical_cyclone = TropicalCyclone.query.filter_by(
            tropical_cyclone_id=self.id).first()

        self.assertTrue(tropical_cyclone is not None)

        if tropical_cyclone:
            db.session.delete(tropical_cyclone)
            db.session.commit()

        print('test_005_delete_tropical_cyclone_by_id end')


if __name__ == '__main__':
    unittest.main()
