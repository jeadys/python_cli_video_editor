from validations.overwrite import check_overwrite


def create_snapshot(video, f_input, f_output, video_duration, f_interval, f_overwrite):
    for interval in range(0, video_duration, f_interval):
        new_filename = f'snapshot-{interval}-{str(f_input.name)}'.replace(
            str(f_input.suffix), '.jpg')
        final_output = f_output.joinpath(new_filename)

        if f_overwrite or check_overwrite(final_output):
            video.save_frame(f'{final_output}', t=interval)
