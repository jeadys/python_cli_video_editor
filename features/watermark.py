from inspect import cleandoc
from validations.overwrite import check_overwrite
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip


def create_watermark(f_input, f_output, v_position, h_position, f_measure, f_fps, f_overwrite):
    if f_measure == 'small':
        resize = 30
    elif f_measure == 'medium':
        resize = 60
    elif f_measure == 'large':
        resize = 90

    video = (VideoFileClip(str(f_input)))

    watermark = (ImageClip('assets/watermark.png')).set_duration(video.duration).resize(
        height=resize).margin(right=8, top=8, left=8, bottom=8, opacity=0).set_pos((h_position, v_position))

    new_filename = f'watermark-{str(f_input.name)}'
    final_output = f_output.joinpath(new_filename)
    final_file = CompositeVideoClip([video, watermark])

    if f_overwrite or check_overwrite(final_output):
        final_file.write_videofile(str(final_output), fps=f_fps)

    video.reader.close()
    video.audio.reader.close_proc()


if __name__ == '__main__':
    print(cleandoc(f'''
        Add a watermark to your videos.
        python editor.py watermark -h, for more info
    '''))
