from pathlib import Path
from inspect import cleandoc
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor

from helpers.info import class_info
from helpers.overwrite import check_overwrite

from moviepy.editor import VideoFileClip, CompositeVideoClip

"""
The cut functionality allows the end user to split their video(s) in to multiple parts.
This is done by checking the video duration time and collecting the start and end time of each part.
When part of the video file is written these start and end times are used to create the video part.

This can be done in singular and bulk, with the help of multiprocessing technology this feature is sped up by a lot.

*IMPORT*
Each time the video file is opened and the manipulation is done it needs to be closed!
This is to avoid errors like too many files open.
"""


class Cut:
    def __init__(self, files, f_output, f_parts, f_fps, f_overwrite):
        self.files = files
        self.f_output = f_output
        self.f_parts = f_parts
        self.f_fps = f_fps
        self.f_overwrite = f_overwrite

    def process_cut(self, file):
        video = VideoFileClip(str(file))
        video_duration = round(video.duration)
        part_duration = 0
        start_part = [0]
        end_part = []

        for _ in range(int(self.f_parts)):
            part_duration += video_duration / self.f_parts
            start_part.append(round(part_duration, 2))
            end_part.append(round(part_duration, 2))

        for f_part in range(int(self.f_parts)):
            video = video.subclip(
                (start_part[int(f_part)]), (end_part[int(f_part)]))
            new_filename = f'part_{f_part + 1}_of_{self.f_parts}_{file.name}'

            # We want parts of a video together in one folder, so the output doesn't become a mess.
            final_folder = self.f_output.joinpath(file.stem)
            Path(final_folder).mkdir(parents=True, exist_ok=True)

            final_output = final_folder.joinpath(new_filename)
            final_file = CompositeVideoClip([video])
            final_file.write_videofile(
                str(final_output), fps=self.f_fps if self.f_fps else video.fps, temp_audiofile=Path(final_folder.joinpath(f'{file.stem}_TEMP_FILE.mp3')))

        video.close()

    def cut_processor(self):
        with ProcessPoolExecutor() as executor:
            executor.map(self.process_cut, self.files)


if __name__ == '__main__':
    class_info(Cut)
