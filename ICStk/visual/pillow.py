#/usr/env/bin python
"""
ICStk.visual.pillow
"""



'''
mode notes:

    1 (1-bit pixels, black and white, stored with one pixel per byte)
    L (8-bit pixels, black and white)
    P (8-bit pixels, mapped to any other mode using a colour palette)
    RGB (3x8-bit pixels, true colour)
    RGBA (4x8-bit pixels, true colour with transparency mask)
    CMYK (4x8-bit pixels, colour separation)
    YCbCr (3x8-bit pixels, colour video format)
    I (32-bit signed integer pixels)
    F (32-bit floating point pixels)

'''


from ..         import *
from glob       import glob
from colorsys   import *
from sys        import (
        exit            ,
        version_info    ,
        )


## CONSTANTS, Put in all or root __init___
MAX_BYTE_VALUE      = 255
MAX_BYTE_MODULUS    = 256
X_INDEX             = 0
Y_INDEX             = 1


### Put these in the __init__ for .art
## Color value indexes
RGB_RED_INDEX           = RGBA_RED_INDEX    = 0
RGB_GREEN_INDEX         = RGBA_GREEN_INDEX  = 1
RGB_BLUE_INDEX          = RGBA_BLUE_INDEX   = 2
RGBA_ALPHA_INDEX        = 3
RGB_RED_LIMIT           = RGB_GREEN_LIMIT   = RGB_BLUE_LIMIT    = MAX_BYTE_VALUE
RGBA_RED_LIMIT          = RGBA_GREEN_LIMIT  = RGBA_BLUE_LIMIT   = RGBA_ALPHA_LIMIT  = MAX_BYTE_VALUE
HSV_HUE_INDEX           = 0
HSV_SATURATION_INDEX    = 1
HSV_VALUE_INDEX         = 2
HSV_HUE_CYCLE           = HSV_VALUE_CYCLE   = 1
HSV_SATURATION_LIMIT    = HSV_VALUE_LIMIT   = 1
MODE_RGB_LENGTH         = 3
MODE_RGBA_LENGTH        = 4
GRAYSCALE_MODE          = "L"


# Try to import PIL files, store tru if the module exists
try:
    from PIL.Image      import open as imgOpen
    from PIL.Image      import new  as imgNew
    from PIL.ImageChops import *
    pillowInstalled = True
except:
    pillowInstalled = False



# Detect python version
python3     = False
if version_info.major == PYTHON3:
    python3 = True



# Python version specific imports`
if python3:
    # imports for Python 3.x
    pass
else:
    # Imports for Python 2.x
    pass



def frameList(
        title           = str() ,
        extension       = 'png' ,
        startingFrame   = 0     ,
        endingFrame     = None  ,
        ):
    """
        Creates a list of frame sequences in a directory.
    """
    return sorted(
            glob(
                title       +
                '*.'        +
                extension   ,
                )
            )



## Colorsys
'''
    rgb_to_hsv()
        takes 3 values 0 to 255 for red green and blue, converts to hsv

        hsv is Hue, saturation, value.
            Hue is the color wheel, its value is a float betwen 0 and 1
            Sautarion is color intesity, 0.0 to 1.0
            Value is lightness, 0 to 255

            Use modulus to keep values within range

            the idea behind rgb2hsv and hsv2rgb is to beable to convert color values back and
            forth directly using the output of each function.
                Each function recieves a tuple of values, and outputs a tuple of values

                there may be issue in the future with RGBa converstions
'''
def rgb2hsv( 
        rgb = tuple()   ,
        ):
    """
        A wrapper for rgb_to_hsv where the input is a tuple of integers
        representing RGB values, and the output is a tuple of floats
        between 0.0 and 1.0 that represent a HSV value.
    """
    if len( rgb ) == MODE_RGB_LENGTH:
        red, green, blue        = rgb
    if len( rgb ) == MODE_RGBA_LENGTH:
        red, green, blue, alpha = rgb


    
    #  Prevent color value from exceeding limit
    if red > RGB_RED_LIMIT:
        red = RGB_RED_LIMIT
    if green > RGB_GREEN_LIMIT:
        green = RGB_GREEN_LIMIT
    if blue > RGB_BLUE_LIMIT:
        BLUE = RGB_BLUE_LIMIT

    # Return converted output
    return (
            rgb_to_hsv(
                red                                     ,
                green                                   ,
                blue                                    ,
                )[ HSV_HUE_INDEX ]  ,
            rgb_to_hsv(
                red     ,
                green   ,
                blue    ,
                )[ HSV_SATURATION_INDEX ]               ,
            rgb_to_hsv(
                red     ,
                green   ,
                blue    ,
                )[ HSV_VALUE_INDEX ] / MAX_BYTE_VALUE   ,
            )




def hsv2rgb(
        hsv = tuple()   ,
        ):
    """
        A wrapper for hsv_to_rgb, where the input for value is 
        a tupple of floating points and the output is an 
        RGB tupple of ints ranging from 0 to 255
    """
    hue , saturation , value = hsv

    # Cycle hue value, and limit saturation and value
    hue = hue % HSV_HUE_CYCLE
    if saturation > HSV_SATURATION_LIMIT:
        saturation  = HSV_SATURATION_LIMIT
    if value > HSV_VALUE_LIMIT:
        value       = HSV_VALUE_LIMIT

    return (
            int(
                hsv_to_rgb(
                    hue         ,
                    saturation  ,
                    value       ,
                    )[ RGB_RED_INDEX ] * MAX_BYTE_VALUE     ,
                )   ,
            int(
                hsv_to_rgb(
                    hue         ,
                    saturation  ,
                    value       ,
                    )[ RGB_GREEN_INDEX ] * MAX_BYTE_VALUE   ,
                )   ,
            int(
                hsv_to_rgb(
                    hue         ,
                    saturation  ,
                    value       ,
                    )[ RGB_BLUE_INDEX ] * MAX_BYTE_VALUE    ,
                )   ,
            )



## PIL
if pillowInstalled:
    """
        These methods are available if the pillow module is installed
    """
    

    ### Replace reduntant operations in the followinf methods, with these methods
    def sameMode(
            mainImage       ,
            secondaryImage  ,
            ):
        """
            Convert the secondary image to be the same type as the main image.
            Return the converted seconday image
        """
        return


    def sameSize(
            mainImage       ,
            secondaryImage  ,
            ):
        """
            Transform the secondary image to equal the size of the main image.
            Return the resized secondaryimage.
        """
        return
    


    # --- Pixel Methods -----------------------------------
    def huePixel(
            basePixel   = (
                int()   , int() , int() ,
                )   ,
            layerPixel  = (
                int()   , int() , int() ,
                )   ,
            ):
        """
            Cycles the Hue value of the basePixel base on the value of layerPixel
        """
        if len( basePixel ) == MODE_RGB_LENGTH:
            return hsv2rgb(
                    (
                        # Hue ( base hue + layer value )
                        rgb2hsv( basePixel )[ HSV_HUE_INDEX ]           +
                        rgb2hsv( layerPixel)[ HSV_VALUE_INDEX ]         ,

                        # Saturation ( base )
                        rgb2hsv( basePixel )[ HSV_SATURATION_INDEX ]    ,
                    
                        # Value ( base )
                        rgb2hsv( basePixel )[ HSV_VALUE_INDEX ]         ,
                        )       ,
                    )
        else:
            rgba = list(
                    hsv2rgb(
                        (
                            # Hue ( base hue + layer value )
                            rgb2hsv( basePixel )[ HSV_HUE_INDEX ]           +
                            rgb2hsv( layerPixel)[ HSV_VALUE_INDEX ]         ,
                            
                            # Saturation ( base )
                            rgb2hsv( basePixel )[ HSV_SATURATION_INDEX ]    ,
                    
                            # Value ( base )
                            rgb2hsv( basePixel )[ HSV_VALUE_INDEX ]         , 
                            )       ,
                        )
                    )
            rgba.append( 
                    basePixel[ RGBA_ALPHA_INDEX ] 
                    )
            return tuple( rgba )


    def lightCycle(
            basePixel   = (
                int()   , int() , int() ,
                )                   ,
            cycleValue  = float()   ,
            cycleMax    = float()   ,
            ):
        """
            Take RGB tupple, a cycle value, and a cycleTotal.
            Convert RGB to HSV, add cycle value to V, modulus max value of V
            Conver new HSV back to RGB
            Return RGB tuple

            rgb2hsv returns a float for value.
            newValue =  ( value + ( cycleValue / cycleMax ) ) % HSV_VALUE_CYCLE


            The value and max arguments are for video frame progress for the cycle
            Max is how many frames occur between cycles.
            Value is the current frame.
        """
        return hsv2rgb(
                (
                    rgb2hsv( basePixel )[ HSV_HUE_INDEX ]           ,
                    rgb2hsv( basePixel )[ HSV_SATURATION_INDEX ]    ,
                    ( 
                        rgb2hsv( basePixel )[ HSV_VALUE_INDEX ] + 
                        ( cycleValue / cycleMax )
                        )
                    % HSV_VALUE_CYCLE
                    )
                )



# ---- Layer Methods ------------------------------------------------------
    def alphaMask(
            base        = str() ,
            layer       = str() ,
            mask        = str() ,
            output      = str() ,
            outputDir   = None  ,
            extension   = 'png' ,
            ):
        """
            Take two image files and a layer mask.
            Convert layer file and mask file to the same size as base.
            Ensure that layer and base are RGBa or RGB, and the same.
            Ensure that mask is greyscale.
            Apply the mask to the layer over the base, and save output.
        """
        success = bool()
        with imgOpen( base ) as imgBase , imgOpen( layer ) as imgLayer , imgOpen( mask ) as imgMask:
            
            ## Ensure layer and base are the same mode and size, and mask is also the same size
            if imgBase.mode != imgLayer.mode:
                # Convert layer mode to base mode
                imgLayer = imgLayer.convert( imgBase.mode )

            if imgBase.size != imgLayer.size:
                # Rescale layer to match base
                imgLayer = imgLayer.resize( imgBase.size )

            if imgBase.size != imgMask.size:
                # Rescale mask to match base
                imgMask = imgMask.resize( imgBase.size )
            
            if outputDir:
                try:
                    composite(
                            imgBase                 ,
                            imgLayer                ,
                            imgMask.convert( GRAYSCALE_MODE )  ,
                            ).save( 
                                    outputDir   +
                                    '/'         +
                                    output      + 
                                    "."         +
                                    extension   ,
                                    )
                    success = True
                except:
                    success = False
            else:
                try:
                    composite(
                            imgBase                 ,
                            imgLayer                ,
                            imgMask.convert( 'L' )  ,
                            ).save( 
                                    output      + 
                                    "."         +
                                    extension   ,
                                    )
                    success = True
                except:
                    success = False
        return success



    def differenceLayer(
            base        = str() ,
            layer       = str() ,
            output      = str() ,
            outputDir   = None  ,
            extension   = 'png' ,
            ):
        """
            Take two image files.
            Convert the layer to the same size as base.
            Ensure that layer and base are same type (RGB, or RGBa).
            Difference layer base and layer, and save output.
        """
        success = bool()
        with imgOpen( base ) as imgBase , imgOpen( layer ) as imgLayer:

            ## Ensure layer and base are the same mode and size
            if imgBase.mode != imgLayer.mode:
                # Convert layer mode to base mode
                imgLayer = imgLayer.convert( imgBase.mode )

            if imgBase.size != imgLayer.size:
                # Rescale layer to match base
                imgLayer = imgLayer.resize( imgBase.size )

            ## Apply effect and save image
            if outputDir:
                try:
                    difference(
                            imgBase                 ,
                            imgLayer                ,
                            ).save( 
                                    outputDir   +
                                    '/'         +
                                    output      + 
                                    "."         +
                                    extension   ,
                                    )
                    success = True
                except:
                    success = False
            else:
                try:
                    difference(
                            imgBase                 ,
                            imgLayer                ,
                            ).save( 
                                    output      + 
                                    "."         +
                                    extension   ,
                                    )
                    return True
                except:
                    return False



    def hueLayer(
            base        = str() ,
            layer       = str() ,
            output      = str() ,
            outputDir   = None  ,
            extension   = 'png' ,
            ):
        """
            Create a hue layer effect.
        
                Convert layer to same size as base, and greyscale

                Create a new image the same size and mode as base.

                Iterate through each pixel in base, and corrisponding pixel in layer.
                Take the pixel value of layer, and add it to hue of base (modulus 1),
                then draw the RGB value to the new output image.
                Also, apply alpha layer of base to output image if base mode
                is RBGa.
        """
        with imgOpen( base ) as imgBase , imgOpen( layer ) as imgLayer, imgNew( 
                imgBase.mode    ,
                imgBase.size    ,
                ) as imgOutput:

            ## Ensure layer and base are the same mode and size
            if imgBase.mode != imgLayer.mode:
                # Convert layer mode to base mode
                imgLayer = imgLayer.convert( imgBase.mode )

            if imgBase.size != imgLayer.size:
                # Rescale layer to match base
                imgLayer = imgLayer.resize( imgBase.size )


            # Iterate through the base layers pixels
            #       Look at numpy, and other ways to do this efficiently
            for imgX in range( imgBase.size[ X_INDEX ] ):
                for imgY in range( imgBase.size[ Y_INDEX ] ):

                    # Grab base pixel RGB values at ( imgX , imgY ) and convert to HSV
                    if len( imgBase.mode ) == MODE_RGB_LENGTH:
                        
                        imgOutput.putpixel(
                                # Image pixel position
                                ( imgX , imgY )                 ,

                                # Image pixel RGB
                                huePixel(
                                    imgBase.getpixel(
                                        ( imgX , imgY ) ,
                                        )                   ,
                                    imgLayer.getpixel(
                                        ( imgX , imgY ) ,
                                        )                   ,
                                    )                           ,
                                )
                        
                    elif len( imgBase.mode ) == MODE_RGBA_LENGTH:
                        imgOutput.putpixel(
                                # Image pixel position
                                ( imgX , imgY )                 ,

                                # Image pixel RGB
                                huePixel(
                                    imgBase.getpixel(
                                        ( imgX , imgY ) ,
                                        )                   ,
                                    imgLayer.getpixel(
                                        ( imgX , imgY ) ,
                                        )                   ,
                                    )                           ,
                                )
                        
                    elif len( imgBase.mode ) == MODE_RGBA_LENGTH:
                        pass
                        # RGBA image, also write alpha layer from base
                    else:
                        # Wrong base image type, return False 
                        #   consider better result for error logging in scripts that
                        #   call this module
                        return False

                    # Grab layer HSV[ value ] value at ( imgX , imgY )

                    # Write an RGB value at (imgX , imgY ) to output.
                    # output HSV[ hue ] =  base HSV[ hue ] + layer[ value ]
                    # convert output HSV to RGB and write pixel


            try:
                imgOutput.save(
                        output      +
                        "."         +
                        extension   ,
                        )
                return True
            except:
                return False


# ----- Frame Methods -------------------------------------------------
    '''
        These methods apply pixels functions to images, and do not involve layering images
        Instead they take a current video frame number as a key on how the effect is applied
    '''

    def frameLightCycle(
            base        = str() ,
            frame       = int() ,
            cycle       = int() ,
            output      = str() ,
            extension   = 'png' ,
            forceGray   = True  ,
            ):
        """
            Take an image, a frame number, and a cycle value.

            cycle the light value of pixels in the frame based on the frame number.
            The cycle value indicates how many frames before the light cycle come full circle
            
            Return True if a new frame is saved.

            MODIFY ARGUMENTS BASED ON PREVIOUS FRAME FUNCTIONS
                i.e.
                    output information
        """
        # Load the Images
        with imgOpen( base ) as imgBase, imgNew(
                imgBase.mode    ,
                imgBase.size    ,
                ) as imgOutput:

            # Iterate through base pixels and light cycle based on a ratio of frame to cycle
            for imgX in range( imgBase.size[ X_INDEX ] ):
                for imgY in range( imgBase.size[ Y_INDEX ] ):

                    if forceGray:
                        # MAX_BYTE_VALUE    ,   MAX_BYTE_MODULUS
                        imgBase     = imgBase.convert( GRAYSCALE_MODE )
                        imgOutput   = imgOutput.convert( GRAYSCALE_MODE ) 
                        imgOutput.putpixel(
                        #print( frame , cycle , ( frame / cycle ) * MAX_BYTE_VALUE ,
                                ( imgX , imgY ) ,
                                int(
                                    imgBase.getpixel(
                                        ( imgX , imgY ) ,
                                        )               +
                                    (
                                        ( frame / cycle )   *
                                        MAX_BYTE_VALUE 
                                        )
                                    ) % MAX_BYTE_MODULUS    ,
                                )

                    else:
                        imgOutput.putpixel(
                                # Pixel position
                                ( imgX , imgY ) ,
                                lightCycle(
                                    imgBase.getpixel(
                                        ( imgX , imgY ) ,
                                        )   ,
                                    frame   ,
                                    cycle   ,
                                    )           ,
                                )

            # Save the new image
            try:
                imgOutput.save(
                        output              +
                        "."                 +
                        extension           ,
                        compress_level  = 0 ,
                        )
                return True
            except:
                return False

        return False
