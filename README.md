# Video editing through CLI

## About
This repo has many functionalities that can be used to edit/manipulate your videos.
Libraries/modules such as [MoviePy](https://github.com/Zulko/moviepy)
and [FFMPEG](https://github.com/FFmpeg/FFmpeg) are being used to get most of the work done.

Also interested in image editing? Check out [python_cli_image_editor](https://github.com/YassinAO/python_cli_image_editor)

## Prerequisite
* Python v.3+
* MoviePy
* FFMPEG
* PyGame (If you want to see previews)

## Install
```
$ git clone https://github.com/YassinAO/python_cli_video_editor
$ cd python_cli_video_editor
$ pip install -r requirements.txt 
```

## Usage / Examples
You can leave the -o OR --output argument out of the command to use the default location. Folder named 'output' within this project. 
### create gif

```
     $ python editor.py gif --input C:\Users\John\Desktop\Intro.mp4 --output C:\Users\John\Desktop\ --start 00:00:06 --end 00:00:09 --measure large
```

### add watermark
```
     $ python editor.py watermark --input C:\Users\John\Desktop\Intro.mp4 --output C:\Users\John\Desktop\ --position top_right --measure large
```

### cut video in to parts
```
     $ python editor.py cut --input C:\Users\John\Desktop\Intro.mp4 --output C:\Users\John\Desktop\ --parts 6 
```

### export audio from video
```
     $ python editor.py audio --input C:\Users\John\Desktop\Intro.mp4 --output C:\Users\John\Desktop\ --export 
```

### make video snapshots
```
     $ python editor.py snapshot --input C:\Users\John\Desktop\Intro.mp4 --output C:\Users\John\Desktop\ --interval 10 
```

## Commands
```
The main arguments are used in combination with the subcommands/arguments

required main arguments:
    -i, --input            absolute path to file, tip [drag & drop a file in the terminal to get the path]
                           (e.g.) --input C:\Users\John\Desktop\Intro.mp4

optional main arguments:
    -o, --output           absolute path to folder, tip [drag & drop a folder in the terminal to get the path]
                           (e.g.) --output C:\Users\John\Desktop\
                           default = output folder within project

    -h, --help             show this help message and exit
                           (e.g.) --help

    --overwrite            overwrite existing file with new file [no values needed]
                           (e.g.) --overwrite

    --fps                  set new fps for video
                           (e.g.) --fps 30
    

    --preview              see preview of edit [no values needed]
                           (e.g.) --preview 
    
optional arguments gif subcommand:

    gif                    allows use of the gif feature and the subcommands
                           (e.g.) gif <subcommands>

    -s --start             starttime of video [give time in HH:MM:SS]
                           (e.g.) --start 00:00:10
                           default = 00:00:05

    -e --end               endtime of video [give time in HH:MM:SS]
                           (e.g.) --end 00:00:20
                           default = 00:00:10

    -m --measure           size of the gif, options [small, medium, large]
                           (e.g.) -measure large
                           default = small
    
    --sway                 plays the gif forward then backward [no values needed]
                           (e.g.) --sway


optional arguments watermark subcommand:

    watermark              allows use of the watermark feature and the subcommands
                           watermark <subcommands>

    -p --position          position of watermark, options [top_left, top_right, bottom_left, bottom_right]
                           (e.g.) --position top_left
                           default = bottom_right

    -m --measure           size of the watermark, options [small, medium, large]
                           (e.g.) --measure large
                           default = small                           

optional arguments cut subcommand:

    cut                    allows use of the cut feature and the subcommands
                           cut <subcommands>

    -p --parts             The amount of video parts you want to cut the video in
                           (e.g.) --parts 6
                           default = 2

optional arguments audio subcommand:

    audio                  allows use of the audio feature and the subcommands
                           audio <subcommands>

    --export               export the audio from a video [no values needed]
                           (e.g.) --export

optional arguments snapshot subcommand:

    snapshot               allows use of the snapshot feature and the subcommands
                           snapshot <subcommands>

    --interval             the interval in seconds when you want to make snaphots from the video
                           (e.g.) --interval 10
                           default = 1

```

## Current functionalities
* Add watermark to video [option to choose size & position of watermark]
* Create gif from video  [option to choose size, type & start/endtime of gif]
* Cut video in to multiple parts
* Export audio from video
* Make snapshots from video

## Future functionalities
* A lot...