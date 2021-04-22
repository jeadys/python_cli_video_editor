import concurrent.futures
from pathlib import Path
from inspect import cleandoc
from datetime import datetime
from validations.overwrite import check_overwrite
from moviepy.editor import VideoFileClip, CompositeVideoClip


class Cut:
    def __init__(self, files, f_output, f_parts, f_fps, f_overwrite):
        self.files = files
        self.f_output = f_output
        self.f_parts = f_parts
        self.f_fps = f_fps
        self.f_overwrite = f_overwrite

    def process_cut(self, file):
        video_file = VideoFileClip(str(file))
        video_duration = round(video_file.duration)
        part_duration = 0
        start_part = [0]
        end_part = []

        for _ in range(int(self.f_parts)):
            part_duration += video_duration / self.f_parts
            start_part.append(round(part_duration, 2))
            end_part.append(round(part_duration, 2))

        for f_part in range(int(self.f_parts)):
            video = VideoFileClip(str(file)).subclip(
                (start_part[int(f_part)]), (end_part[int(f_part)]))

            new_filename = f'part_{f_part + 1}_of_{self.f_parts}_{str(file.name)}'

            # We want parts of a video together in one folder, so the output doesn't become a mess.
            final_folder = self.f_output.joinpath(file.stem)
            Path(final_folder).mkdir(parents=True, exist_ok=True)

            final_output = final_folder.joinpath(new_filename)
            final_file = CompositeVideoClip([video])
            final_file.write_videofile(
                str(final_output), fps=self.f_fps if self.f_fps else video_file.fps)

            video.reader.close()
            video.audio.reader.close_proc()

    def cut_processor(self):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            executor.map(self.process_cut, self.files)


if __name__ == '__main__':
    print(cleandoc(f'''
        Cut video into multiple parts.
        python editor.py cut -h, for more info
    '''))
