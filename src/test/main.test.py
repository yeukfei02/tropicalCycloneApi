from src.test.tropical_cyclone import TropicalCycloneTest
from src.test.forecast_track import ForecastTrackTest
from src.test.track_history import TrackHistoryTest

import unittest

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(TropicalCycloneTest())
    suite.addTest(ForecastTrackTest())
    suite.addTest(TrackHistoryTest())

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = test_suite()
    runner.run(test_suite)