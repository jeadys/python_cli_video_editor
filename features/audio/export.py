from pathlib import Path
from concurrent.futures import ProcessPoolExecutor

from helpers.info import class_info
from helpers.overwrite import check_overwrite

from moviepy.editor import VideoFileClip


class Audio:
    def __init__(self, files, audio_format, f_output, f_overwrite):
        self.files = files
        self.audio_format = audio_format
        self.f_output = f_output
        self.f_overwrite = f_overwrite

    def process_audio(self, file):
        video = VideoFileClip(str(file))
        audio = video.audio
        new_filename = f'audio_{str(file.name)}'.replace(
            str(file.suffix), self.audio_format)

        # We want different audio export of a video together in one folder, so the output doesn't become a mess.
        final_folder = self.f_output.joinpath(file.stem)
        Path(final_folder).mkdir(parents=True, exist_ok=True)

        final_output = final_folder.joinpath(new_filename)
        audio.write_audiofile(str(final_output))

        video.close()

    def audio_processor(self):
        with ProcessPoolExecutor() as executor:
            executor.map(self.process_audio, self.files)


if __name__ == '__main__':
    class_info(Audio)
