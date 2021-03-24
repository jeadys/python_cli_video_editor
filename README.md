# Video editing through CLI

## About
This repo has many functionalities that can be used to edit/manipulate your videos.
Libraries/modules such as [MoviePy](https://github.com/Zulko/moviepy)
and [FFMPEG](https://github.com/FFmpeg/FFmpeg) are being used to get most of the work done.

Feel free to make use of this project!

## prerequisite
* Python v.3+
* MoviePy
* FFMPEG
* PyGame (If you want to see previews)
* ImageMagick (If you want to add text to gifs)

    ### Notes
    Imagemagick is automaticly detected by MoviePy except on Windows systems.
    Navigate to `moviepy/config_defaults.py` and provide the path to the IMAGEMAGICK_BINARY named convert. See example below!

    IMAGEMAGICK_BINARY = `"C:\\Program Files\\ImageMagick_VERSION\\convert.exe"`

## Install
```
$ git clone https://github.com/YassinAO/python_cli_video_editor
$ cd python_cli_video_editor
$ pip install -r requirements.txt 
```

## Usage
```
required arguments:
    -i, --input            absolute path to file [TIP: Drag & drop a file in the terminal to get the path]
                           (e.g.) -i C:\Users\John\Desktop\Intro.mp4

    -f --feature           Task you want to apply on file [options: gif, watermark]
                           (e.g.) -f gif
optional arguments:
    -h, --help             Show this help message and exit

    -o, --output           Absolute path to file [TIP: Drag & drop a file in the terminal to get the path]
                           (e.g.) -o C:\Users\John\Desktop\
                           Default value = output folder within project

    -s --start             starttime of video [give time in seconds]
                           (e.g.) -s 60
                           Default value = 1

    -e --end               endtime of video [give time in seconds]
                           (e.g.) -s 70
                           Default value = 3

    -m --measure           size of the gif and/or watermark [options: small, medium, large]
                           (e.g.) -m large
                           Default value = small

    -p --position          Position of watermark [options: top_left, top_right, bottom_left, bottom_right]
                           (e.g.) -p top_left
                           Default value = bottom_right

    --preview              See preview of edit [no values are needed for this argument]
                           (e.g.) --preview 

```
### Example creating gif
You can leave the -o OR --output argument out of the command to use the default location. Folder named 'output' within this project. 
```
     $ python editor.py -i C:\Users\John\Desktop\Intro.mp4 -o C:\Users\John\Desktop\ -s 6 -e 9 -m large --preview
```

### Example adding watermark
You can leave the -o OR --output argument out of the command to use the default location. Folder named 'output' within this project. 
```
     $ python editor.py -i C:\Users\John\Desktop\Intro.mp4 -o C:\Users\John\Desktop\ -p top_right -m large --preview
```

## Current functionalities
* Add watermark to video [option to choose size & position of watermark]
* Create gif from video  [option to choose size & start/endtime of gif]

## Future functionalities
* A lot...