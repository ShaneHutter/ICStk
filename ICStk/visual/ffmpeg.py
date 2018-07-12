#/usr/env/bin python
"""
ICStk.visual.ffmpeg
"""

from ..                 import *
from ..system.datatype  import strConvert
from ..system.shell     import (
        shell       ,
        shellOut    ,
        )
from ..system.system    import isdir
from sys                import (
        exit            ,
        version_info    ,
        )



# Global Constant declaration
DEBUG_MODE  = True
PYTHON3     = 3


FFPROBE_STREAMS_KEY     = "streams"
FFPROBE_FORMAT_KEY      = "format"


# Global variable declaration
python3     = False



# Detect python version
if version_info.major == PYTHON3:
    python3 = True


# Python version specific imports`
if python3:
    # imports for Python 3.x
    pass
else:
    # Imports for Python 2.x
    pass


# Check for ffmpeg, and exit if not installed

# **kwargs is python3 only, as far as I know
if python3:
    def ffmpeg(
            inputFile   = str() ,
            outputFile  = str() ,
            **options           
            ):
        """
            Run ffmpeg command.
        """
        ffmpegCommandStart  = "ffmpeg -i "
        # convert **options key to ffmpge switch string
        '''
            Some options cant be parsed in this way
                clobber = True  is -y
                clobber = Flase is -n
                    use eval() to turn a string True/False into a bool
    
                seekTimeStamp = True    is -seek_timestamp
    
                -discard, -disposition, -reinit_filter, -vn (disable video), -dn (disable data)
                -sn (disable subtitles)
    
                -fix_sub_duration
    
                adding metadata is -metadata string=string
                -map_metadata
                -program title=string st=int, add program to a stream
    
                -timecode hh:mm:ss[:;.]ff
        '''
        parseOptions    = {
                # Pre-file main options
                "framerate"         : "-framerate"              ,
                "startNumber"       : "-start_number"           ,   # Starting frame for png sequence
                "volume"            : "-volume"                 ,   # Normal = 256
                "format"            : "-f"                      ,
                "codec"             : "-c"                      ,
                "preset"            : "-pre"                    ,
                "duration"          : "-t"                      ,   # in seconds
                "stopTime"          : "-to"                     ,
                "startTime"         : "-ss"                     ,
                "startTimeEOF"      : "-sseof"                  ,   # Start time relative to end of file
                "limitSize"         : "-fs"                     ,   # Limit filesize in bytes
                "fileType"          : "-target"                 ,   # vcd, svcd, dvd, dsv, dv50. optional prefixes: pal-, ntsc-, film-
                "audioPad"          : "-apad"                   ,
                "frames"            : "-frames"                 ,   # number of frames in output
                "filterGraph"       : "-filter"                 ,   # set stream filter graph
                "filterScript"      : "-filter_script"          ,
    
                # Video Options
                "videoFrames"       : "-vframes"                ,
                "frameRate"         : "-r"                      ,
                "size"              : "-s"                      ,   # (WxH)
                "aspectRatio"       : "-aspect"                 ,   # 4:3, 16:9
                "bitsPerRawSample"  : "-bits_per_raw_sample"    ,
                "videoCodec"        : "-vcodec"                 ,   # "copy" to copy stream
                "pass"              : "-pass"                   ,   # set pass number
                "videoFilter"       : "-vf"                     ,  # filter graph
                "audioBitrate"      : "-b:a"                    ,
                "videoBitrate"      : "-b:v"                    ,
    
                # Audio options
                "audioFrames"       : "-aframes"                ,
                "audioQuality"      : "-q:a"                    ,
                "sampleRate"        : "-ar"                     ,
                "audioChanels"      : "-ac"                     ,   # Number of audio chanels
                "audioVolume"       : "-vol"                    ,   # 256 is normal
                "audioFilter"       : "-af"                     ,   # filter graph
    
                # Subtitle Options
                "subtitleSize"      : "-s"                      ,   # (WxH)
                "subtitleCodec"     : "-scodec"                 ,
                "subtitleTag"       : "-stag"                   ,   # tag/fourcc
                "subtitleCanvas"    : "-canvas_size"            ,   # (WxH)
                "subtitlePreset"    : "-spre"                   ,
                }

        # Create the options string
        optionsString   = str()
        for option in options:
            if option in parseOptions:
                optionsString += parseOptions[ option ] + " " + options[ option ] + " "
            #elif option in boolOptions
    
        return shell(
                ffmpegCommandStart  +
                inputFile           +
                " "                 +
                optionsString       +
                " "                 +
                outputFile          ,
                )



def info( 
        mediaFile = str()   ,
        ):
    """
        Return a dictionary of data on a media file using ffprobe

        ffprobe -v error -show_format -show_streams file.avi
        
        Output is a dictionary
            {
                "streams":  streams     ,   # A list of dictionaries
                "format":   formatData  ,   # A dictionary of format information
                }
    """
    output          = dict()    # you dont need this return output directly
    
    ffprobeCommand      = "ffprobe -v error -show_format -show_streams "
    ffprobeOutput       = shellOut(
            ffprobeCommand  +
            mediaFile       ,
            )

    streamCount         = 0
    streamStartTag      = "[STREAM]"
    streamEndTag        = "[/STREAM]"
    streams             = list()

    formatStartTag      = "[FORMAT]"
    formatEndTag        = "[/FORMAT]"
    formatData          = dict()

    keyValueDelimiter   =   "="


    for stream in ffprobeOutput.split( streamStartTag ):
        streamData      = dict()
        if stream:
            if formatStartTag in stream:
                # Remove formatData from streamData
                for streamLine in stream.split( 
                        formatStartTag 
                        )[ FIRST_INDEX ].split( NEW_LINE ):
                    if streamLine != streamEndTag and keyValueDelimiter in streamLine:
                        streamData.update(
                                { 
                                    streamLine.split( keyValueDelimiter )[ KEY_INDEX ]      :
                                    strConvert(
                                        streamLine.split( keyValueDelimiter )[ VALUE_INDEX ]  
                                        )                                                   ,
                                    }
                                )
            else:
                for streamLine in stream.split( NEW_LINE ):
                    if streamLine != streamEndTag and keyValueDelimiter in streamLine:
                        streamData.update(
                                { 
                                    streamLine.split( keyValueDelimiter )[ KEY_INDEX ]      :
                                    strConvert(
                                        streamLine.split( keyValueDelimiter )[ VALUE_INDEX ]  
                                        )                                                   ,
                                    }
                                )
            streams.append( streamData )


    for formatLines in ffprobeOutput.split( formatStartTag ):
        if streamStartTag not in formatLines:
            # This index does not contain stream data
            for formatLine in formatLines.split( NEW_LINE ):
                if formatLine != formatEndTag and keyValueDelimiter in formatLine:
                    formatData.update(
                            {
                                formatLine.split( keyValueDelimiter )[ KEY_INDEX ]      :
                                strConvert(
                                    formatLine.split( keyValueDelimiter )[ VALUE_INDEX ]    
                                    )                                                   ,
                                }
                            )

    return {
            FFPROBE_STREAMS_KEY : streams       ,
            FFPROBE_FORMAT_KEY  : formatData    ,
            }




def video2pngSeq(
        videoFile   = str() ,
        outputDir   = None  ,
        ):
    """
        Take a video file and convert it into an uncompressed png sequence.
        Return True/False based on success
    """
    FFPROBE_CODEC_TYPE_KEY  = "codec_type"
    FFPROBE_FRAME_TOTAL_KEY = "nb_frames"
    # Check the frame total in the video file
    videoInfo = info( videoFile )
    for stream in videoInfo[ FFPROBE_STREAMS_KEY ]:
        if FFPROBE_CODEC_TYPE_KEY in stream and stream[ FFPROBE_CODEC_TYPE_KEY ] == "video":
            # This pulls the frame total from the first video stream and breaks
            # May be an issue IF there is a file with two video streams with two different frame totals
            #   this may not be realistic.
            frameTotal  = stream[ FFPROBE_FRAME_TOTAL_KEY ]
            break

    # Setup working dirctory for png seq dump
    DEFAULT_PNG_SEQ_OUTPUT_DIR  = 'pngseq/'
    if not( outputDir ):
        outputDir   = DEFAULT_PNG_SEQ_OUTPUT_DIR

    if not(
            isdir( outputDir )
            ):
        # There is not already an output directory, make one
        shell(
                "mkdir -p " +
                outputDir   ,
                )



    return



'''
def screenCapture(
        output  = str()     ,
        width   = int()     ,
        height  = int()     ,
        x       = 0         ,
        y       = 0         ,
        display = ":0.0"    ,
        ):
    """
        Use ffmpeg to screen capture

        ffmpeg -f x11grab -y -video_size 800x600 -i :22.0 -vframes 1 test.png

        ***ultimately use the ffmpeg call***
    """
    return print(
            "ffmpeg -f x11grab -y -video_size " +
            str( width )                        +
            ","                                 +
            str( height )                       +
            " -i "                              +
            display                             +
            "+"                                 +
            str( x )                            +
            ","                                 +
            str( y )                            +
            " -vframes 1 "                      +
            output                              ,
            )
'''
