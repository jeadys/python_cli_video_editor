from inspect import cleandoc
from validations.overwrite import check_overwrite
from moviepy.editor import VideoFileClip, CompositeVideoClip, concatenate, vfx


def time_symetrize(video):
    return concatenate([video, video.fx(vfx.time_mirror)])


def create_gif(f_input, f_output, f_starttime, f_endtime, f_measure, sway, f_fps, f_overwrite):
    resize = {
        'small': 0.3,
        'medium': 0.6,
        'large': 0.9,
    }

    if sway:
        video = (VideoFileClip(str(f_input))).subclip(
            f_starttime, f_endtime).resize(resize[f_measure]).fx(time_symetrize)

        new_filename = f'sway-{str(f_input.name)}'.replace(
            str(f_input.suffix), '.gif')
    else:
        video = (VideoFileClip(str(f_input))).subclip(
            f_starttime, f_endtime).resize(resize[f_measure])

        new_filename = str(f_input.name).replace(
            str(f_input.suffix), '.gif')

    final_output = f_output.joinpath(new_filename)
    final_file = CompositeVideoClip([video])

    if f_overwrite or check_overwrite(final_output):
        final_file.write_gif(str(final_output), fps=f_fps)

    # video.reader.close()
    # video.audio.reader.close_proc()


if __name__ == '__main__':
    print(cleandoc(f'''
        Make a gif from your videos.
        python editor.py gif -h, for more info
    '''))
