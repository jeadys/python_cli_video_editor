import sys
import argparse
from pathlib import Path
from inspect import cleandoc
from validations.validator import Validate
from validations.colors import Color


def argument_parser():
    BASE_DIR = Path(__file__).resolve().parent

    parent_parser = argparse.ArgumentParser(
        prog='Python CLI Video Editor', description='An application to modify vids and more, Made By https://github.com/YassinAO/', add_help=False
    )
    # These commands can be used with any subcommand.
    parent_parser.add_argument('-i', '--input')
    parent_parser.add_argument('-o', '--output')
    parent_parser.add_argument('--overwrite', action='store_true')
    parent_parser.add_argument('--fps', type=int)

    main_parser = argparse.ArgumentParser()

    feature_subparsers = main_parser.add_subparsers(
        help='sub-command help', title='actions', dest='command')  # Dest is defined to see which subcommand is being used.

    gif_parser = feature_subparsers.add_parser(
        'gif', parents=[parent_parser])  # Parent is defined to get access to the parent's commands within this subcommand.
    gif_parser.add_argument('-s', '--start', default='00:00:5')
    gif_parser.add_argument('-e', '--end', default='00:00:10')
    gif_parser.add_argument('-m', '--measure', default='small',
                            help='choices: small, medium, large')
    gif_parser.add_argument('--sway', action='store_true')

    watermark_parser = feature_subparsers.add_parser(
        'watermark', parents=[parent_parser])  # Parent is defined to get access to the parent's commands within this subcommand.
    watermark_parser.add_argument('-p', '--position', default='bottom_right',
                                  help='choices: top_left, top_right, bottom_left, bottom_right')
    watermark_parser.add_argument('-m', '--measure', default='small',
                                  help='choices: small, medium, large')

    cut_parser = feature_subparsers.add_parser(
        'cut', parents=[parent_parser])  # Parent is defined to get access to the parent's commands within this subcommand.
    cut_parser.add_argument('-p', '--parts', type=int, default=2)

    audio_parser = feature_subparsers.add_parser(
        'audio', parents=[parent_parser])
    audio_parser.add_argument('--export', action='store_true')

    args = main_parser.parse_args()
    args_dict = vars(args)

    if args.input is None:
        print(cleandoc(f'''
        {Color.WARNING}missing -i OR --input argument{Color.ENDC}'''))
        sys.exit()
    elif args.output is None:
        args.output = BASE_DIR.joinpath('output', args.command)

    Validate(**args_dict).check_path()


if __name__ == '__main__':
    argument_parser()
