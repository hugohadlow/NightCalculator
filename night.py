# Calculate night flight time for a flight.
# Does not support crossing midnight.

from datetime import datetime, timedelta


def calculate_night_flight(t_dep, t_arr, civil_twilight_origin, civil_twilight_dest):
    # Convert all inputs to Unix timestamps for math
    dep = time_string_to_datetime(t_dep)
    arr = time_string_to_datetime(t_arr)
    cvt_origin = time_string_to_datetime(civil_twilight_origin)
    cvt_destination = time_string_to_datetime(civil_twilight_dest)

    noon = time_string_to_datetime("12:00")
    if ((cvt_origin > noon > cvt_destination) or
            (cvt_origin < noon < cvt_destination)):
        print("Not supported: civil twilights at origin and destination must both be before noon or after noon.")
        return None

    if cvt_origin < noon: #Early flight
        if dep < cvt_origin and arr < cvt_destination:  # Entire flight is in darkness.
            return timedelta_to_string(arr - dep)

        if dep > cvt_origin and arr > cvt_destination:  # Entire flight is during daylight.
            return "0:00"

    else: #Late flight
        if dep > cvt_origin and arr > cvt_destination:  # Entire flight is in darkness.
            return timedelta_to_string(arr - dep)

        if dep < cvt_origin and arr < cvt_destination:  # Entire flight is during daylight.
            return "0:00"

    flight_duration = arr-dep
    night_difference_at_origin = cvt_origin - dep
    night_difference_at_destination = arr - cvt_destination
    total_night_difference = night_difference_at_origin + night_difference_at_destination

    night_flight_time_seconds = night_difference_at_origin * flight_duration.total_seconds() / total_night_difference.total_seconds()

    return timedelta_to_string(night_flight_time_seconds)


def time_string_to_datetime(time_str):
    return datetime.strptime(time_str,"%H:%M")

def timedelta_to_string(td):
    return f'{td.seconds // 3600}:{str((td.seconds // 60) % 60).zfill(2)}'

if __name__ == "__main__":
    print("--- Night Flight Time calculator (UTC) ---")
    try:
        dep = input("Enter DEPARTURE time in format HH:MM ")
        arr = input("Enter ARRIVAL time (UTC) in format HH:MM ")
        cvt_origin = input("Enter ORIGIN CIVIL TWILIGHT time (UTC) in format HH:MM ")
        cvt_destination = input("Enter DESTINATION CIVIL TWILIGHT time (UTC) in format HH:MM ")

        result = calculate_night_flight(dep, arr, cvt_origin, cvt_destination)

        print(f"Calculated Night Flight Time: {result}")
    except ValueError:
        print("\nError: Please use the format HH:MM (e.g., 13:45)")

