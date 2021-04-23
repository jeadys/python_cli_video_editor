import datetime

"""
The --start and --end arguments are passed in HH:MM:SS format. 
MoviePy requires input in seconds, so this convertion is needed.
"""


def convert_to_seconds(time_str):
    try:
        datetime.datetime.strptime(time_str, '%H:%M:%S')
        h, m, s = time_str.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)
    except (ValueError, TypeError) as e:
        return False


def convert_to_hms(time_sec):
    try:
        return datetime.timedelta(seconds=time_sec)
    except (ValueError, TypeError) as e:
        return False
