import argparse
from pathlib import Path
from colors import Color
from inspect import cleandoc
from validator import Validation


def main():
    BASE_DIR = Path(__file__).resolve().parent
    OUTPUT_DIR = BASE_DIR.joinpath('output')

    parser = argparse.ArgumentParser(
        prog='Python CLI Video Editor', description='An application to modify vids and more, Made By https://github.com/YassinAO/'
    )

    # Make arguments optional by adding - or -- in front of it.
    parser.add_argument('-i', '--input',
                        metavar=('path/to/file'))

    parser.add_argument('-o', '--output',
                        metavar=('path/to/folder'), default=OUTPUT_DIR)

    parser.add_argument('-s', '--start',
                        metavar=('time in seconds'), type=int, default=1)

    parser.add_argument('-e', '--end',
                        metavar=('time in seconds'), type=int, default=10)

    parser.add_argument('-m', '--measure',
                        metavar=('size of'),
                        choices=['small', 'medium', 'large'], help='choices: [small, medium, large]',
                        default='small')

    parser.add_argument('-p', '--position', metavar=('watermark'),
                        choices=['top_left', 'top_right', 'bottom_left', 'bottom_right'], help='choices: [top_left, top_right, bottom_left, bottom_right]',
                        default='bottom_right')

    parser.add_argument(
        '-f', '--feature', choices=['gif', 'watermark'], help='choices: [gif, watermark]')
    # parser.add_argument('--preview', action='store_true')

    args = parser.parse_args()

    if args.input is None:
        print(cleandoc(f'''
        {Color.WARNING}missing -i OR --input argument
        run -h OR --help for more info{Color.ENDC}
        '''))
    elif args.feature is None:
        print(cleandoc(f'''
        {Color.WARNING}missing -f OR --feature argument
        run -h OR --help for more info{Color.ENDC}
        '''))
    else:
        Validation(args.feature, args.input, args.output, args.start,
                   args.end, args.measure, args.position).check_path()


if __name__ == '__main__':
    main()
