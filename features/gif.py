from moviepy.editor import VideoFileClip, CompositeVideoClip
from inspect import cleandoc


def create_gif(final_output, f_input, f_starttime, f_endtime, f_measure):
    if f_measure == 'small':
        resize = 0.3
    elif f_measure == 'medium':
        resize = 0.6
    elif f_measure == 'large':
        resize = 0.9

    video = (VideoFileClip(str(f_input))).subclip(
        f_starttime, f_endtime).resize(resize)

    final_file = CompositeVideoClip([video])
    final_file.write_gif(str(final_output))

    video.reader.close()
    video.audio.reader.close_proc()


if __name__ == '__main__':
    print(cleandoc(f'''
        Make a gif from your videos.
        python editor.py gif -h, for more info
    '''))
