from pathlib import Path
from inspect import cleandoc

from helpers.colors import Color

"""
check_overwrite is used when files are written on the end users machine.
This will check if the file already exists on their machine.

This check can be skipped for all files if the --overwrite argument is passed.
"""


def check_overwrite(final_output):
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
                return True
            elif overwrite.lower() == 'n':
                print(f'{Color.OKGREEN}exiting...{Color.ENDC}')
                return False
            else:
                continue
        else:
            return True


if __name__ == '__main__':
    check_overwrite()
