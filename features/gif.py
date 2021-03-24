from .overwrite import check_overwrite
from moviepy.editor import VideoFileClip, CompositeVideoClip


def create_gif(f_input, f_output, f_starttime, f_endtime, f_measure, f_feature):
    new_filename = str(f_input.name).replace(str(f_input.suffix), '.gif')

    if f_measure == 'small':
        resize = 0.3
    elif f_measure == 'medium':
        resize = 0.6
    elif f_measure == 'large':
        resize = 0.9

    video = (VideoFileClip(str(f_input))).subclip(
        f_starttime, f_endtime).resize(resize)

    final_file = CompositeVideoClip([video])
    final_output = f_output.joinpath(new_filename)

    check_overwrite(final_file, final_output, f_feature, video)


if __name__ == '__main__':
    create_gif()
