import overwrite


def export_audio(video, f_input, f_output, f_overwrite):
    audio = video.audio
    new_filename = f'audio-{str(f_input.name)}'.replace(
        str(f_input.suffix), '.wav')
    final_output = f_output.joinpath(new_filename)

    if f_overwrite or overwrite.check_overwrite(final_output):
        audio.write_audiofile(str(final_output))
