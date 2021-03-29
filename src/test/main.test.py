import unittest

import os
import sys
sys.path.insert(1, os.getcwd())

from src.test.trackHistory import TrackHistoryTest
from src.test.forecastTrack import ForecastTrackTest
from src.test.tropicalCyclone import TropicalCycloneTest


def test_suite():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(
        TropicalCycloneTest)
    return suite


def test_suite2():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ForecastTrackTest)
    return suite


def test_suite3():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TrackHistoryTest)
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = test_suite()
    runner.run(test_suite)

    test_suite2 = test_suite2()
    runner.run(test_suite2)

    test_suite3 = test_suite3()
    runner.run(test_suite3)
