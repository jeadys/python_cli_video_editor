from inspect import cleandoc
from moviepy.editor import VideoFileClip, CompositeVideoClip, concatenate, vfx


def time_symetrize(video):
    return concatenate([video, video.fx(vfx.time_mirror)])


def create_gif(final_output, f_input, f_starttime, f_endtime, f_measure, sway, f_fps):
    if f_measure == 'small':
        resize = 0.3
    elif f_measure == 'medium':
        resize = 0.6
    elif f_measure == 'large':
        resize = 0.9

    if sway:
        video = (VideoFileClip(str(f_input))).subclip(
            f_starttime, f_endtime).resize(resize).fx(time_symetrize)
    else:
        video = (VideoFileClip(str(f_input))).subclip(
            f_starttime, f_endtime).resize(resize)

    final_file = CompositeVideoClip([video])
    final_file.write_gif(str(final_output), fps=f_fps)

    # video.reader.close()
    # video.audio.reader.close_proc()


if __name__ == '__main__':
    print(cleandoc(f'''
        Make a gif from your videos.
        python editor.py gif -h, for more info
    '''))
