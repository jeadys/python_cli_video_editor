from pathlib import Path
from inspect import cleandoc
from features.gif import create_gif
from features.cut import Cut
from validations.colors import Color
from validations.convert import convert_to_seconds, convert_to_hms
from moviepy.editor import VideoFileClip
from features.audio.export import export_audio
from features.watermark import Watermark
from features.snapshot import create_snapshot


def classInfo():
    method_list = [attribute for attribute in dir(Validate) if callable(
        getattr(Validate, attribute)) and attribute.startswith('__') is False]

    for method in method_list:
        print(method)


class Validate:
    def __init__(self, **value):
        self.command = value['command']
        self.f_input = Path(value['input'])
        self.f_output = Path(value['output'])
        self.f_overwrite = value['overwrite']
        # self.video = VideoFileClip(str(self.f_input))
        # self.video_duration = round(self.video.duration)
        self.bulk = value['bulk']
        self.f_fps = value['fps']
        self.files = None
        if self.command == 'gif' or self.command == 'watermark':
            self.f_measure = value['measure'].lower()
        if self.command == 'gif':
            self.f_starttime = convert_to_seconds(value['start'])
            self.f_endtime = convert_to_seconds(value['end'])
            self.sway = value['sway']
        if self.command == 'watermark':
            self.v_position, self.h_position = value['position'].lower().split(
                '_')
        if self.command == 'cut':
            self.f_parts = value['parts']
        if self.command == 'snapshot':
            self.f_interval = value['interval']

    def check_path(self):
        Path(self.f_output).mkdir(parents=True, exist_ok=True)

        if (self.f_input.is_dir() and self.bulk or self.f_input.is_file() and not self.bulk) and self.f_output.is_dir():
            print(cleandoc(f'''
            {Color.OKGREEN}valid input/output{Color.ENDC}
            '''))

            return self.retrieve_files()
        else:
            print(cleandoc(f'''
            {Color.WARNING}invalid input/output{Color.ENDC}
            '''))

    def retrieve_files(self):
        print(cleandoc(f'''
        {Color.HEADER}EXTENSION CHECK{Color.ENDC}
        extension   (type)       {self.f_input.suffix}
        '''))

        video_extensions = ['mp4', '.mp4', 'mov', '.mov', 'mkv', '.mkv']

        self.files = [self.f_input] if not self.bulk else [file for file in Path(self.f_input).glob(
            '*') if file.suffix in video_extensions]

        if self.command == 'gif' or self.command == 'watermark':
            return self.check_measurement()
        elif self.command == 'cut':
            return Cut(self.files, self.f_output, self.f_parts, self.f_fps, self.f_overwrite).cut_processor()
        elif self.command == 'audio':
            return export_audio(self.video, self.f_input, self.f_output, self.f_overwrite)
        elif self.command == 'snapshot':
            return create_snapshot(self.video, self.f_input, self.f_output, self.video_duration, self.f_interval, self.f_overwrite)
        return False

    def check_measurement(self):
        measurements = ['small', 'medium', 'large']

        print(cleandoc(f'''
        {Color.HEADER}MEASUREMENT CHECK{Color.ENDC}
        measure     (size)       {self.f_measure}
        '''))

        if self.f_measure in measurements:
            if self.command == 'gif':
                return self.check_time()
            elif self.command == 'watermark':
                return self.check_position()
        else:
            print(cleandoc(f'''
            {Color.WARNING}MEASUREMENT {self.f_measure} INVALID{Color.ENDC}
            '''))

    def check_time(self):
        if self.f_starttime and self.f_endtime is not False:

            print(cleandoc(f'''
            {Color.HEADER}TIME CHECK{Color.ENDC}
            length      (seconds)    {self.video_duration}
            start       (seconds)    {self.f_starttime}
            end         (seconds)    {self.f_endtime}
            '''))

            if self.f_starttime >= 0 and self.f_starttime < self.video_duration and self.f_endtime > 0 and self.f_endtime < self.video_duration and self.f_starttime < self.f_endtime:
                return create_gif(self.f_input, self.f_output, self.f_starttime, self.f_endtime, self.f_measure, self.sway, self.f_fps, self.f_overwrite)
            elif self.f_starttime > self.video_duration or self.f_endtime > self.video_duration:
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
        else:
            print(f'{Color.WARNING}USE HH:MM:SS TIME FORMAT{Color.ENDC}')

    def check_position(self):
        v_pos = ['bottom', 'top']
        h_pos = ['left', 'right']

        print(cleandoc(f'''
        {Color.HEADER}POSITION CHECK{Color.ENDC}
        vertical    (position)   {self.v_position}
        horizontal  (position)   {self.h_position}
        '''))

        if self.v_position in v_pos and self.h_position in h_pos:
            return Watermark(self.files, self.f_output, self.v_position, self.h_position, self.f_measure, self.f_fps, self.f_overwrite).watermark_processor()
        else:
            print(cleandoc(f'''
            {Color.WARNING}POSITION {self.v_position} {self.h_position} INVALID{Color.ENDC}
            '''))


if __name__ == '__main__':
    classInfo()
