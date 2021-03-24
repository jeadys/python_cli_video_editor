from pathlib import Path
from inspect import cleandoc
from colors import Color


def check_overwrite(final_file, final_output, f_feature, video):
    print(cleandoc(f'''
    {Color.HEADER}OVERWRITE CHECK{Color.ENDC}
    name        (file)       {final_output.name}
    dir         (folder)     {final_output}   
    '''))

    while True:
        if final_output.is_file():
            overwrite = input(
                f'{Color.WARNING}{final_output.name} already exists in this directory. Overwrite ?{Color.ENDC} [y/N] ')
            if overwrite.lower() == 'y':
                if f_feature == 'gif':
                    final_file.write_gif(str(final_output))
                elif f_feature == 'watermark':
                    final_file.write_videofile(str(final_output))
                print(
                    f'{Color.OKGREEN}{final_output.name} has been overwritten{Color.ENDC}')
                break
            elif overwrite.lower() == 'n':
                print(f'{Color.OKGREEN}exiting...{Color.ENDC}')
                break
            else:
                continue
        else:
            if f_feature == 'gif':
                final_file.write_gif(str(final_output))
            elif f_feature == 'watermark':
                final_file.write_videofile(str(final_output))
            break

    video.reader.close()
    video.audio.reader.close_proc()
