from .overwrite import check_overwrite
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip
from pathlib import Path


def create_watermark(f_input, f_output, v_position, h_position, f_measure, f_feature):
    new_filename = f'watermark-{str(f_input.name)}'

    if f_measure == 'small':
        resize = 30
    elif f_measure == 'medium':
        resize = 60
    elif f_measure == 'large':
        resize = 90

    video = (VideoFileClip(str(f_input)))

    watermark = (ImageClip("assets/watermark.png")).set_duration(video.duration).resize(
        height=resize).margin(right=8, top=8, left=8, bottom=8, opacity=0).set_pos((h_position, v_position))

    final_file = CompositeVideoClip([video, watermark])
    final_output = f_output.joinpath(new_filename)

    check_overwrite(final_file, final_output, f_feature, video)
