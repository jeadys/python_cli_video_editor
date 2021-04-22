import concurrent.futures
from pathlib import Path
from inspect import cleandoc
from validations.overwrite import check_overwrite
from moviepy.editor import VideoFileClip, CompositeVideoClip, concatenate_videoclips, vfx


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
        with concurrent.futures.ProcessPoolExecutor() as executor:
            executor.map(self.process_gif, self.files)


if __name__ == '__main__':
    print(cleandoc(f'''
        Make a gif from your videos.
        python editor.py gif -h, for more info
    '''))
