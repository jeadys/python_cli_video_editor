import sys
import argparse
from pathlib import Path
from inspect import cleandoc

from helpers.colors import Color
from helpers.validator import Validate

"""
argument_parser is used to give the end user the option to run commands from the CLI (command line interface)
The argument_parser exists of a parent parser that has all main arguments that can be used in combination with the subparsers (subcommands)
A subparser (subcommand) exists of their own arguments that can be passed, these can be required or optional.
When a command is ran it executes the feature linked to the subcommand. 
"""


def argument_parser():
    BASE_DIR = Path(__file__).resolve().parent

    parent_parser = argparse.ArgumentParser(
        prog='Python CLI Video Editor', description='An application to modify vids and more, Made By https://github.com/YassinAO/', add_help=False
    )

    """
    These commands can be used with any subcommand.
    'input' is necessary to manipulate the targeted video(s).
    The other ones are optional.
    """
    parent_parser.add_argument('-i', '--input')
    parent_parser.add_argument('-o', '--output')
    parent_parser.add_argument('--overwrite', action='store_true')
    parent_parser.add_argument('-b', '--bulk', action='store_true')
    parent_parser.add_argument('--fps', type=int)

    main_parser = argparse.ArgumentParser()

    """
    'dest' is defined to see which subcommand is being used.
    This is important because it tells the script which feature to execute.
    """
    feature_subparsers = main_parser.add_subparsers(
        help='sub-command help', title='actions', dest='command')

    """
    Some arguments within the subcommand have 'nargs', 'default', 'const' & 'choices' defined.
    
        - 'nargs' is used to specify the amount of arguments expected. '?' indicates 0 or 1.
        - 'default' is used when argument isn't specified.
        - 'const' is used when argument is specified but no value given.
        - 'choices' are the values the end user can choose from.

    'default' or 'const' will be passed as the value depending on the condition.
    This is to avoid missing arguments for the executed feature.
    """

    """
    A subparser (subcommand) has their own arguments.
    The subparser also requires some conditions from the parent_parser,
    so we define this in 'parents' to give it access to the parents arguments such as --input --output.
    """

    # GIF FEATURE
    gif_parser = feature_subparsers.add_parser(
        'gif', parents=[parent_parser])
    gif_parser.add_argument('-s', '--start', nargs='?',
                            default='00:00:05', const='00:00:05')
    gif_parser.add_argument('-e', '--end', nargs='?',
                            default='00:00:10', const='00:00:10')
    gif_parser.add_argument('-m', '--measure', nargs='?',
                            default='small', const='small', choices=['small', 'medium', 'large'])
    gif_parser.add_argument('--sway', action='store_true')

    # WATERMARK FEATURE
    watermark_parser = feature_subparsers.add_parser(
        'watermark', parents=[parent_parser])
    watermark_parser.add_argument('-p', '--position', nargs='?',
                                  default='bottom_right', const='bottom_right', choices=['top_left', 'top_right', 'bottom_left', 'bottom_right'])
    watermark_parser.add_argument('-m', '--measure', nargs='?',
                                  default='small', const='small', choices=['small', 'medium', 'large'])

    # CUT FEATURE
    cut_parser = feature_subparsers.add_parser(
        'cut', parents=[parent_parser])
    cut_parser.add_argument('-p', '--parts', type=int, nargs='?',
                            default=2, const=2)

    # AUDIO FEATURE
    audio_parser = feature_subparsers.add_parser(
        'audio', parents=[parent_parser])
    audio_parser.add_argument('--export', type=str, nargs='?',
                              default='.wav', const='.wav', choices=['.wav', '.mp3'])

    # SNAPSHOT FEATURE
    snapshot_parser = feature_subparsers.add_parser(
        'snapshot', parents=[parent_parser])
    snapshot_parser.add_argument('--interval', type=int, nargs='?',
                                 default=1, const=1)

    args = main_parser.parse_args()
    args_dict = vars(args)

    if args.input is None:
        print(cleandoc(f'''
        {Color.WARNING}missing -i OR --input argument{Color.ENDC}'''))
        sys.exit()
    elif args.command == 'gif' and args.bulk:
        print(cleandoc(f'''
        {Color.WARNING}gif feature doesn't support bulk manipulation.{Color.ENDC}'''))
        sys.exit()
    elif args.output is None:
        args.output = BASE_DIR.joinpath('output', args.command)

    return Validate(**args_dict).check_path()


if __name__ == '__main__':
    argument_parser()
