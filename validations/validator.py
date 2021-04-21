from pathlib import Path
from inspect import cleandoc
from features.gif import Gif
from features.cut import Cut
from validations.colors import Color
from validations.convert import convert_to_seconds, convert_to_hms
from validations.messenger import error_message_time
from moviepy.editor import VideoFileClip
from features.audio.export import Audio
from features.watermark import Watermark
from features.snapshot import Snapshot


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
        if self.command == 'audio':
            self.audio_format = value['export']

    def check_path(self):
        Path(self.f_output).mkdir(parents=True, exist_ok=True)

        if (self.f_input.is_dir() and self.bulk or self.f_input.is_file() and not self.bulk) and self.f_output.is_dir():
            return self.retrieve_files()

        print(cleandoc(f'''
        {Color.WARNING}invalid input/output{Color.ENDC}
        '''))

    def retrieve_files(self):
        video_formats = ['mp4', '.mp4', 'mov', '.mov', 'mkv', '.mkv']

        self.files = [self.f_input] if not self.bulk else [file for file in Path(self.f_input).glob(
            '*') if file.suffix in video_formats]

        if self.command == 'gif':
            return self.check_time()
        elif self.command == 'watermark':
            return Watermark(self.files, self.f_output, self.v_position, self.h_position, self.f_measure, self.f_fps, self.f_overwrite).watermark_processor()
        elif self.command == 'cut':
            return Cut(self.files, self.f_output, self.f_parts, self.f_fps, self.f_overwrite).cut_processor()
        elif self.command == 'audio':
            return Audio(self.files, self.audio_format, self.f_output, self.f_overwrite).audio_processor()
        elif self.command == 'snapshot':
            return Snapshot(self.files, self.f_output, self.f_interval, self.f_overwrite).snapshot_processor()
        return False

    def check_time(self):
        if self.f_starttime is not False and self.f_endtime is not False:
            if self.f_starttime >= 0 and self.f_starttime < self.video_duration and self.f_endtime > 0 and self.f_endtime < self.video_duration and self.f_starttime < self.f_endtime:
                return Gif(self.files, self.f_output, self.f_starttime, self.f_endtime, self.f_measure, self.sway, self.f_fps, self.f_overwrite).gif_processor()

        return error_message_time(self.f_starttime, self.f_endtime, self.video_duration)


if __name__ == '__main__':
    classInfo()
