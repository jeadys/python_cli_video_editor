from inspect import cleandoc


def class_info(my_class):
    method_list = [attribute for attribute in dir(my_class) if callable(
        getattr(my_class, attribute)) and attribute.startswith('__') is False]

    for method in method_list:
        print(method)

    help_command = f'python editor.py {my_class.lower()} -h, fore more info'
    description = {
        'Validate':
        '''
            Validating user input before executing feature.
        ''',

        'Audio':
        f'''
            Export audio from video.
            {help_command}
        ''',

        'Cut':
        f'''
            Cut video into multiple parts.
            {help_command}
        ''',

        'Gif':
        f'''
            Make a gif from your videos.
            {help_command}
        ''',

        'Snapshot':
        f'''
            Take snapshots of video on interval.
            {help_command}
        ''',

        'Watermark':
        f'''
            Add a watermark to your videos.
            {help_command}
        ''',
    }

    print(cleandoc(description[my_class]))
