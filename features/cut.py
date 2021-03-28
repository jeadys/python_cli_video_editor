from pathlib import Path
from inspect import cleandoc
from datetime import datetime
from validations.overwrite import check_overwrite
from moviepy.editor import VideoFileClip, CompositeVideoClip


def create_cut(f_input, f_output, f_parts, video_duration, f_fps, f_overwrite):
    part_duration = 0
    start_part = [0]
    end_part = []

    for _ in range(int(f_parts)):
        part_duration += video_duration / f_parts
        start_part.append(round(part_duration, 2))
        end_part.append(round(part_duration, 2))

    for f_part in range(int(f_parts)):
        video = (VideoFileClip(str(f_input))
                 .subclip((start_part[int(f_part)]), (end_part[int(f_part)])))

        new_filename = f'part-{f_part + 1}-of-{f_parts}-{str(f_input.name)}'
        final_output = f_output.joinpath(new_filename)
        final_file = CompositeVideoClip([video])

        if f_overwrite or check_overwrite(final_output):
            final_file.write_videofile(str(final_output), fps=f_fps)

        video.reader.close()
        video.audio.reader.close_proc()


if __name__ == '__main__':
    print(cleandoc(f'''
        Cut video into multiple parts.
        python editor.py cut -h, for more info
    '''))
