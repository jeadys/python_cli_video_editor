from pathlib import Path
import concurrent.futures
from moviepy.editor import VideoFileClip
from validations.overwrite import check_overwrite


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

        video.reader.close()
        video.audio.reader.close_proc()

    def audio_processor(self):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            executor.map(self.process_audio, self.files)
