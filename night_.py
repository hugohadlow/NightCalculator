import unittest
from night import calculate_night_flight


class TestNightFlight(unittest.TestCase):

    def test_twilight_origin_before_noon_twilight_destination_after_noon(self):
        """Scenario: Civil twilight given for origin is before noon,
        but civil twilight given for destination is after noon.
        Not supported."""
        dep = "05:00"
        arr = "07:00"
        cvt_origin = "08:00"
        cvt_dest = "16:00"

        result = calculate_night_flight(dep, arr, cvt_origin, cvt_dest)
        self.assertEqual(None, result)  # Not supported

    def test_twilight_destination_before_noon_twilight_origin_after_noon(self):
        """Scenario: Civil twilight given for destination is before noon,
        but civil twilight given for origin is after noon.
        Not supported."""
        dep = "05:00"
        arr = "07:00"
        cvt_origin = "16:00"
        cvt_dest = "08:00"

        result = calculate_night_flight(dep, arr, cvt_origin, cvt_dest)
        self.assertEqual(None, result)  # Not supported

# Early scenarios
    def test_early_full_night(self):
        """Scenario: Entire flight is at night (before sunrise)"""
        dep = "05:00"
        arr = "07:00"
        cvt_origin = "08:00"
        cvt_dest = "08:00"

        result = calculate_night_flight(dep, arr, cvt_origin, cvt_dest)
        self.assertEqual("2:00", result)  # Full 2 hours should be night

    def test_early_full_day(self):
        """Scenario: Entire flight is during the day (after sunrise)"""
        dep = "09:00"
        arr = "18:00"
        cvt_origin = "08:00"
        cvt_dest = "08:00"

        result = calculate_night_flight(dep, arr, cvt_origin, cvt_dest)
        self.assertEqual("0:00", result)

    def test_early_part_night_cvt_earlier_at_origin(self):
        """Scenario: Flight crosses sunrise.
        Civil twilight at origin is earlier than at destination."""
        dep = "05:00"
        arr = "10:00"
        cvt_origin = "06:00"
        cvt_dest = "07:00"

        result = calculate_night_flight(dep, arr, cvt_origin, cvt_dest)
        self.assertEqual("1:15", result)

    def test_early_part_night_cvt_earlier_at_destination(self):
        """Scenario: Flight crosses sunrise.
        Civil twilight at destination is earlier than at origin."""
        dep = "05:00"
        arr = "10:00"
        cvt_origin = "07:00"
        cvt_dest = "06:00"

        result = calculate_night_flight(dep, arr, cvt_origin, cvt_dest)
        self.assertEqual("1:40", result)

    def test_early_part_night_cvt_very_early_at_destination(self):
        """Scenario: Flight crosses sunrise.
        Civil twilight at destination is earlier than at origin."""
        dep = "05:00"
        arr = "10:00"
        cvt_origin = "11:00"
        cvt_dest = "04:00"

        result = calculate_night_flight(dep, arr, cvt_origin, cvt_dest)
        self.assertEqual("2:30", result)


    def test_early_depart_after_dawn_arrive_before_dawn(self):
        """Scenario: Early flight departs after dawn, but somehow arrives before dawn.
        Civil twilight at destination is earlier than at origin."""
        dep = "06:00"
        arr = "07:00"
        cvt_origin = "05:00"
        cvt_dest = "08:00"

        result = calculate_night_flight(dep, arr, cvt_origin, cvt_dest)
        self.assertEqual("0:30", result)

    #Late scenarios
    def test_late_full_night(self):
        """Scenario: Entire flight is at night (after sunset)"""
        dep = "20:00"
        arr = "22:00"
        cvt_origin = "17:00"
        cvt_dest = "17:00"

        result = calculate_night_flight(dep, arr, cvt_origin, cvt_dest)
        self.assertEqual("2:00", result)  # Full 2 hours should be night


    def test_late_full_day(self):
        """Scenario: Entire flight is during the day (before sunset)"""
        dep = "12:00"
        arr = "17:00"
        cvt_origin = "18:00"
        cvt_dest = "18:00"

        result = calculate_night_flight(dep, arr, cvt_origin, cvt_dest)
        self.assertEqual("0:00", result)

    def test_late_part_night_cvt_earlier_at_origin(self):
        """Scenario: Flight crosses sunset.
        Civil twilight at origin is earlier than at destination."""
        dep = "16:00"
        arr = "22:00"
        cvt_origin = "18:00"
        cvt_dest = "19:00"

        result = calculate_night_flight(dep, arr, cvt_origin, cvt_dest)
        self.assertEqual("3:36", result)
        #For late flights, night flight time is the time *after* civil twilight

    def test_late_part_night_cvt_earlier_at_destination(self):
        """Scenario: Flight crosses sunset.
        Civil twilight at destination is earlier than at origin."""
        dep = "16:00"
        arr = "22:00"
        cvt_origin = "19:00"
        cvt_dest = "18:00"

        result = calculate_night_flight(dep, arr, cvt_origin, cvt_dest)
        self.assertEqual("3:25", result)

    def test_late_depart_after_dusk_arrive_before_dusk(self):
        """Scenario: Late flight departs after dusk, but somehow arrives before dusk.
        Civil twilight at destination is earlier than at origin."""
        dep = "19:00"
        arr = "20:00"
        cvt_origin = "16:00"
        cvt_dest = "22:00"

        result = calculate_night_flight(dep, arr, cvt_origin, cvt_dest)
        self.assertEqual("0:24", result)


if __name__ == '__main__':
    unittest.main()