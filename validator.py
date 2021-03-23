from pathlib import Path
from colors import Color
from inspect import cleandoc
from moviepy.editor import VideoFileClip
import sys


def classInfo():
    method_list = [attribute for attribute in dir(Validation) if callable(
        getattr(Validation, attribute)) and attribute.startswith('__') is False]

    for method in method_list:
        print(method)


class Validation:
    def __init__(self, f_input, f_output, f_starttime, f_endtime, f_measure, f_position):
        self.f_input = Path(f_input)
        self.f_output = Path(f_output)
        self.f_starttime = f_starttime
        self.f_endtime = f_endtime
        self.f_measure = f_measure.lower()
        self.v_position, self.h_position = f_position.lower().split('_')

    def check_path(self):
        Path(self.f_output).mkdir(parents=True, exist_ok=True)

        if self.f_input.is_file() and self.f_output.is_dir():
            print(cleandoc(f'''
            {Color.OKGREEN}VALID INPUT/OUTPUT{Color.ENDC}
            '''))

            self.check_extension()
        else:
            print(cleandoc(f'''
            {Color.WARNING}INVALID INPUT/OUTPUT{Color.ENDC}
            '''))

    def check_extension(self):
        video_extensions = ['.mp4', '.mov', '.mkv']
        photo_extensions = ['.jpeg', '.jpg', '.png']

        print(cleandoc(f'''
        {Color.HEADER}EXTENSION CHECK{Color.ENDC}
        extension   (type)       {self.f_input.suffix}
        '''))

        if self.f_input.suffix in video_extensions:
            self.check_time()
        elif self.f_input.suffix in photo_extensions:
            pass  # DO SOMETHING
        else:
            print(cleandoc(f'''
            {Color.WARNING}EXTENSION {self.f_input.suffix} INVALID{Color.ENDC}
            '''))

    def check_time(self):
        video = VideoFileClip(str(self.f_input))
        video_length = round(video.duration)

        print(cleandoc(f'''
        {Color.HEADER}TIME CHECK{Color.ENDC}
        length      (seconds)    {video_length}
        start       (seconds)    {self.f_starttime}
        end         (seconds)    {self.f_endtime}
        '''))

        if self.f_starttime >= 0 and self.f_starttime < video_length and self.f_endtime > 0 and self.f_endtime < video_length and self.f_starttime < self.f_endtime:
            self.check_position()
        elif self.f_starttime > video_length or self.f_endtime > video_length:
            print(
                f'{Color.WARNING}STARTTIME OR ENDTIME CAN NOT BE BIGGER THAN VIDEO LENGTH{Color.ENDC}')
        elif self.f_starttime > self.f_endtime:
            print(
                f'{Color.WARNING}STARTTIME CAN NOT BE BIGGER THAN ENDTIME{Color.ENDC}')
        elif self.f_starttime < self.f_endtime < 0:
            print(
                f'{Color.WARNING}STARTTIME OR ENDTIME CAN NOT BE NEGATIVE NUMBERS{Color.ENDC}')
        elif self.f_starttime == self.f_endtime:
            print(
                f'{Color.WARNING}STARTTIME AND ENDTIME CAN NOT BE EQUAL{Color.ENDC}')
        else:
            print(f'{Color.ERROR}TRY AGAIN{Color.ENDC}')

        video.reader.close()
        video.audio.reader.close_proc()

    def check_position(self):
        v_pos = ['bottom', 'top']
        h_pos = ['left', 'right']

        print(cleandoc(f'''
        {Color.HEADER}POSITION CHECK{Color.ENDC}
        vertical    (position)   {self.v_position}
        horizontal  (position)   {self.h_position}
        '''))

        if self.v_position in v_pos and self.h_position in h_pos:
            pass  # DO SOMETHING
        else:
            print(cleandoc(f'''
            {Color.WARNING}POSITION {self.v_position} {self.h_position} INVALID{Color.ENDC}
            '''))

    def check_measurement(self):
        measurements = ['small', 'medium', 'large']

        print(cleandoc(f'''
        {Color.HEADER}MEASUREMENT CHECK{Color.ENDC}
        measure     (size)       {self.f_measure}
        '''))

        if self.f_measure in measurements:
            pass  # DO SOMETHING


if __name__ == '__main__':
    classInfo()
