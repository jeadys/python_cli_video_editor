import overwrite
from inspect import cleandoc
from moviepy.editor import VideoFileClip, CompositeVideoClip, concatenate, vfx


def time_symetrize(video):
    return concatenate([video, video.fx(vfx.time_mirror)])


def create_gif(f_input, f_output, f_starttime, f_endtime, f_measure, sway, f_fps, f_overwrite):
    if f_measure == 'small':
        resize = 0.3
    elif f_measure == 'medium':
        resize = 0.6
    elif f_measure == 'large':
        resize = 0.9

    if sway:
        video = (VideoFileClip(str(f_input))).subclip(
            f_starttime, f_endtime).resize(resize).fx(time_symetrize)

        new_filename = f'sway-{str(f_input.name)}'.replace(
            str(f_input.suffix), '.gif')
    else:
        video = (VideoFileClip(str(f_input))).subclip(
            f_starttime, f_endtime).resize(resize)

        new_filename = str(f_input.name).replace(
            str(f_input.suffix), '.gif')

    final_output = f_output.joinpath(new_filename)
    final_file = CompositeVideoClip([video])

    if f_overwrite or overwrite.check_overwrite(final_output):
        final_file.write_gif(str(final_output), fps=f_fps)

    # video.reader.close()
    # video.audio.reader.close_proc()


if __name__ == '__main__':
    print(cleandoc(f'''
        Make a gif from your videos.
        python editor.py gif -h, for more info
    '''))
