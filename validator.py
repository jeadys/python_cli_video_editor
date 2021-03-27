from colors import Color
from pathlib import Path
from inspect import cleandoc
from features import gif, watermark, cut
from moviepy.editor import VideoFileClip


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
        self.video = VideoFileClip(str(self.f_input))
        self.video_duration = round(self.video.duration)
        self.f_fps = value['fps'] if value['fps'] else self.video.fps
        if self.command == 'gif' or self.command == 'watermark':
            self.f_measure = value['measure'].lower()
        if self.command == 'gif':
            self.f_starttime = value['start']
            self.f_endtime = value['end']
            self.sway = value['sway']
        elif self.command == 'watermark':
            self.v_position, self.h_position = value['position'].lower().split(
                '_')
        elif self.command == 'cut':
            self.f_parts = value['parts']

    def check_path(self):
        Path(self.f_output).mkdir(parents=True, exist_ok=True)

        if self.f_input.is_file() and self.f_output.is_dir():
            print(cleandoc(f'''
            {Color.OKGREEN}valid input/output{Color.ENDC}
            '''))

            return self.check_extension()
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
            if self.command == 'gif' or self.command == 'watermark':
                return self.check_measurement()
            elif self.command == 'cut':
                return self.set_naming()
            else:
                pass  # DO SOMETHING
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
            if self.command == 'gif':
                return self.check_time()
            elif self.command == 'watermark':
                return self.check_position()
        else:
            print(cleandoc(f'''
            {Color.WARNING}MEASUREMENT {self.f_measure} INVALID{Color.ENDC}
            '''))

    def check_time(self):
        print(cleandoc(f'''
        {Color.HEADER}TIME CHECK{Color.ENDC}
        length      (seconds)    {self.video_duration}
        start       (seconds)    {self.f_starttime}
        end         (seconds)    {self.f_endtime}
        '''))

        if self.f_starttime >= 0 and self.f_starttime < self.video_duration and self.f_endtime > 0 and self.f_endtime < self.video_duration and self.f_starttime < self.f_endtime:
            self.set_naming()
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

    def check_position(self):
        v_pos = ['bottom', 'top']
        h_pos = ['left', 'right']

        print(cleandoc(f'''
        {Color.HEADER}POSITION CHECK{Color.ENDC}
        vertical    (position)   {self.v_position}
        horizontal  (position)   {self.h_position}
        '''))

        if self.v_position in v_pos and self.h_position in h_pos:
            self.set_naming()
        else:
            print(cleandoc(f'''
            {Color.WARNING}POSITION {self.v_position} {self.h_position} INVALID{Color.ENDC}
            '''))

    def set_naming(self):
        if self.command == 'gif':
            if self.sway:
                new_filename = f'sway-{str(self.f_input.name)}'.replace(
                    str(self.f_input.suffix), '.gif')
            else:
                new_filename = str(self.f_input.name).replace(
                    str(self.f_input.suffix), '.gif')
        elif self.command == 'watermark':
            new_filename = f'watermark-{str(self.f_input.name)}'
        elif self.command == 'cut':
            return cut.create_cut(self.f_input, self.f_output, self.f_parts, self.video_duration, self.f_fps)

        final_output = self.f_output.joinpath(new_filename)
        return self.check_overwrite(final_output)

    def check_overwrite(self, final_output):
        print(cleandoc(f'''
        {Color.HEADER}OVERWRITE CHECK{Color.ENDC}
        name        (file)       {final_output.name}
        dir         (folder)     {final_output}
        '''))

        while True:
            if final_output.is_file() and self.f_overwrite is False:
                overwrite = input(
                    f'{Color.WARNING}{final_output.name} already exists in this directory. Overwrite ?{Color.ENDC} [y/N] ')
                if overwrite.lower() == 'y':
                    if self.command == 'gif':
                        return gif.create_gif(
                            final_output, self.f_input, self.f_starttime, self.f_endtime, self.f_measure, self.sway, self.f_fps)
                    elif self.command == 'watermark':
                        return watermark.create_watermark(
                            final_output, self.f_input, self.v_position, self.h_position, self.f_measure, self.f_fps)
                    break
                elif overwrite.lower() == 'n':
                    print(f'{Color.OKGREEN}exiting...{Color.ENDC}')
                    break
                else:
                    continue
            else:
                if self.command == 'gif':
                    return gif.create_gif(final_output, self.f_input,
                                          self.f_starttime, self.f_endtime, self.f_measure, self.sway, self.f_fps)
                elif self.command == 'watermark':
                    return watermark.create_watermark(
                        final_output, self.f_input, self.v_position, self.h_position, self.f_measure, self.f_fps)
                break


if __name__ == '__main__':
    classInfo()
