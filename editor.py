import argparse
from pathlib import Path
from inspect import cleandoc
from moviepy.editor import VideoFileClip


def main():
    BASE_DIR = Path(__file__).resolve().parent
    OUTPUT_DIR = BASE_DIR.joinpath('output')

    parser = argparse.ArgumentParser(
        prog='Python CLI Video Editor', description='An application to modify your videos!'
    )

    # Make arguments optional by adding - or -- in front of it.
    parser.add_argument('-i', '--input',
                        metavar=('path/to/file'))

    parser.add_argument('-o', '--output',
                        metavar=('path/to/folder'), default=OUTPUT_DIR)

    parser.add_argument('-s', '--start',
                        metavar=('time in seconds'), type=int, default=1)

    parser.add_argument('-e', '--end',
                        metavar=('time in seconds'), type=int, default=3)

    parser.add_argument('-m', '--measure',
                        metavar=('size of'),
                        choices='[small, normal, large]', help='choices: [small, normal, large]',
                        default='small')

    parser.add_argument('-p', '--position', metavar=('watermark'),
                        choices=['top_left, top_right, bottom_left, bottom_right'], help='choices: [top_left, top_right, bottom_left, bottom_right]',
                        default='bottom_right')

    args = parser.parse_args()

    if args.input is None:
        print(f'missing -i OR --input argument')
    else:
        pass


def check_time():
    pass


def check_position():
    pass


def check_measurement():
    pass


def check_extension():
    pass


def check_path():
    pass


if __name__ == '__main__':
    main()
