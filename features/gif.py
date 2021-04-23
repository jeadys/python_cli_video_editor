from pathlib import Path
from inspect import cleandoc
from concurrent.futures import ProcessPoolExecutor

from helpers.info import class_info
from helpers.overwrite import check_overwrite

from moviepy.editor import VideoFileClip, CompositeVideoClip, concatenate_videoclips, vfx

"""
The gif functionality allows the end user to create gifs from a video.
This is done by passing a start and end time of where the gif needs to take the frames from.

This can be done in singular and bulk, with the help of multiprocessing technology this feature is sped up by a lot.

Some extra attributes can be passed such as measure and the type of gif, see README.md for further details.

*IMPORT*
Each time the video file is opened and the manipulation is done it needs to be closed!
This is to avoid errors like too many files open.
"""


class Gif:
    def __init__(self, files, f_output, f_starttime, f_endtime, f_measure, sway, f_fps, f_overwrite):
        self.files = files
        self.f_output = f_output
        self.f_starttime = f_starttime
        self.f_endtime = f_endtime
        self.f_measure = f_measure
        self.sway = sway
        self.f_fps = f_fps
        self.f_overwrite = f_overwrite
        self.resize = {'small': 0.3, 'medium': 0.6, 'large': 0.9}

    def process_gif(self, file):
        video = VideoFileClip(str(file)).subclip(
            self.f_starttime, self.f_endtime).resize(self.resize[self.f_measure])

        if self.sway:
            video = concatenate_videoclips([video, video.fx(vfx.time_mirror)])
            new_filename = f'sway_{file.name}'.replace(file.suffix, '.gif')
        else:
            new_filename = file.name.replace(file.suffix, '.gif')

        # We want related gif material in one folder, so the output doesn't become a mess.
        final_folder = self.f_output.joinpath(file.stem)
        Path(final_folder).mkdir(parents=True, exist_ok=True)

        final_output = final_folder.joinpath(new_filename)
        final_file = CompositeVideoClip([video])
        final_file.write_gif(
            str(final_output), fps=self.f_fps if self.f_fps else video.fps)

        video.close()

    def gif_processor(self):
        with ProcessPoolExecutor() as executor:
            executor.map(self.process_gif, self.files)


if __name__ == '__main__':
    class_info(Gif)
