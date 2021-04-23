from helpers.colors import Color

"""
The --start and --end time arguments check, to avoid invalid time inputs
"""


def error_message_time(f_starttime, f_endtime, video_duration):
    if f_starttime is False or f_endtime is False:
        print(f'{Color.WARNING}USE HH:MM:SS TIME FORMAT{Color.ENDC}')
    elif f_starttime > video_duration or f_endtime > video_duration:
        print(
            f'{Color.WARNING}STARTTIME OR ENDTIME CAN NOT BE BIGGER THAN VIDEO LENGTH{Color.ENDC}')
    elif f_starttime > f_endtime:
        print(
            f'{Color.WARNING}STARTTIME CAN NOT BE BIGGER THAN ENDTIME{Color.ENDC}')
    elif f_starttime < f_endtime < 0:
        print(
            f'{Color.WARNING}STARTTIME OR ENDTIME CAN NOT BE NEGATIVE NUMBERS{Color.ENDC}')
    elif f_starttime == f_endtime:
        print(
            f'{Color.WARNING}STARTTIME AND ENDTIME CAN NOT BE EQUAL{Color.ENDC}')
