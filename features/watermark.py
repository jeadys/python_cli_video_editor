from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip
from inspect import cleandoc


def create_watermark(final_output, f_input, v_position, h_position, f_measure):
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
    final_file.write_videofile(str(final_output))

    video.reader.close()
    video.audio.reader.close_proc()


if __name__ == '__main__':
    print(cleandoc(f'''
        Add a watermark to your videos.
        python editor.py watermark -h, for more info
    '''))
