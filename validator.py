from colors import Color
from pathlib import Path
from inspect import cleandoc
from features import gif, watermark
from moviepy.editor import VideoFileClip


def classInfo():
    method_list = [attribute for attribute in dir(Validation) if callable(
        getattr(Validation, attribute)) and attribute.startswith('__') is False]

    for method in method_list:
        print(method)


class Validation:
    def __init__(self, f_feature, f_input, f_output, f_starttime, f_endtime, f_measure, f_position):
        self.f_feature = f_feature
        self.f_input = Path(f_input)
        self.f_output = Path(f_output)
        self.f_starttime = f_starttime
        self.f_endtime = f_endtime
        self.f_measure = f_measure.lower()
        self.v_position, self.h_position = f_position.lower().split('_')
        self.video = VideoFileClip(str(self.f_input))
        self.video_length = round(self.video.duration)

    def check_path(self):
        Path(self.f_output).mkdir(parents=True, exist_ok=True)

        if self.f_input.is_file() and self.f_output.is_dir():
            print(cleandoc(f'''
            {Color.OKGREEN}valid input/output{Color.ENDC}
            '''))

            self.check_extension()
        else:
            print(cleandoc(f'''
            {Color.WARNING}invalid input/output{Color.ENDC}
            '''))

    def check_extension(self):
        video_extensions = ['.mp4', '.mov', '.mkv']
        photo_extensions = ['.jpeg', '.jpg', '.png']

        print(cleandoc(f'''
        {Color.HEADER}EXTENSION CHECK{Color.ENDC}
        extension   (type)       {self.f_input.suffix}
        '''))

        if self.f_input.suffix in video_extensions:
            self.check_measurement()
        elif self.f_input.suffix in photo_extensions:
            pass  # DO SOMETHING
        else:
            print(cleandoc(f'''
            {Color.WARNING}EXTENSION {self.f_input.suffix} INVALID{Color.ENDC}
            '''))

    def check_measurement(self):
        measurements = ['small', 'medium', 'large']

        print(cleandoc(f'''
        {Color.HEADER}MEASUREMENT CHECK{Color.ENDC}
        measure     (size)       {self.f_measure}
        '''))

        if self.f_measure in measurements:
            if self.f_feature == 'gif':
                self.check_time()
            elif self.f_feature == 'watermark':
                self.check_position()
        else:
            print(cleandoc(f'''
            {Color.WARNING}MEASUREMENT {self.f_measure} INVALID{Color.ENDC}
            '''))

    def check_time(self):
        print(cleandoc(f'''
        {Color.HEADER}TIME CHECK{Color.ENDC}
        length      (seconds)    {self.video_length}
        start       (seconds)    {self.f_starttime}
        end         (seconds)    {self.f_endtime}
        '''))

        if self.f_starttime >= 0 and self.f_starttime < self.video_length and self.f_endtime > 0 and self.f_endtime < self.video_length and self.f_starttime < self.f_endtime:
            gif.create_gif(self.f_input, self.f_output,
                           self.f_starttime, self.f_endtime, self.f_measure, self.f_feature)
        elif self.f_starttime > self.video_length or self.f_endtime > self.video_length:
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

        self.video.reader.close()
        self.video.audio.reader.close_proc()

    def check_position(self):
        v_pos = ['bottom', 'top']
        h_pos = ['left', 'right']

        print(cleandoc(f'''
        {Color.HEADER}POSITION CHECK{Color.ENDC}
        vertical    (position)   {self.v_position}
        horizontal  (position)   {self.h_position}
        '''))

        if self.v_position in v_pos and self.h_position in h_pos:
            watermark.create_watermark(self.f_input, self.f_output,
                                       self.v_position, self.h_position, self.f_measure, self.f_feature)
        else:
            print(cleandoc(f'''
            {Color.WARNING}POSITION {self.v_position} {self.h_position} INVALID{Color.ENDC}
            '''))


if __name__ == '__main__':
    classInfo()
