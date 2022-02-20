# Import Libraries
from augly.image import *
from pprint import pprint
#from random_words import RandomWords

# Custom Modules
from ProAug.param import Param
from ProAug.augParam import AugParam
from ProAug.augSeq import AugSeq
from ProAug.augOperator import AugOperator
from ProAug.rangeParam import *

# Define Empty auglist with empty dictionary
Augs = AugSeq()

# Define all possible Augmentation Operators
blurOpr = AugOperator( "blur", blur, 1.0, AugParam().add(
									Param("radius", 0.0, ContRange(0.0, 100.0))))

brightnessOpr = AugOperator( "brightness", brightness, 1.0, AugParam().add(
        						Param("factor", 1.0, ContRange(-255.0, 255.0))))

aspectRatioOpr = AugOperator( "change_aspect_ratio", change_aspect_ratio, 1.0,
							AugParam().add(
								Param("ratio", 1.0, ContRange(0.0, 100.0))))

clipImageOpr = AugOperator( "clip_image_size", clip_image_size, 1.0,AugParam().add(
            					Param("min_resolution", 0, ContRange(0, 10000)),
            					Param("max_resolution", 10000, ContRange(10000,90000))))

colorJitterOpr = AugOperator( "color_jitter", color_jitter, 1.0, AugParam().add(
            					Param("brightness_factor", 1.0, ContRange(-255.0, 255)),
            					Param("contrast_factor", 1.0, ContRange(-255.0, 255.0)),
            					Param("saturation_factor", 1.0, ContRange(-255.0, 255.0))))

contrastOpr = AugOperator( "contrast", contrast, 1.0, AugParam().add(
        					Param("factor", 1.0, ContRange(0.0, 255.0))))

# convert_color NOT IMPLEMENTED
cropOpr = AugOperator( "crop", crop, 1.0, AugParam().add(
    					Param("x1", 0.25, ContRange(0.0, 0.5)),
    					Param("y1", 0.25, ContRange(0.0, 0.5)),
    					Param("x2", 0.25, ContRange(0.5, 1.0)),
    					Param("y2", 0.75, ContRange(0.5, 1.0))))

encodingQualityOpr = AugOperator( "encoding_quality", encoding_quality, 1.0, AugParam().add(
        							Param("quality", 50, ContRange(0, 100))))

grayscaleOpr = AugOperator( "grayscale", grayscale, 1.0, AugParam().add(
									Param("mode", "luminosity", EnumRange(
										"luminosity", "average"))))

hFlipOpr = AugOperator( "hflip", hflip, 1.0 )

memeFormatOpr = AugOperator( "meme_format", meme_format, 1.0, AugParam().add(
									Param("text", "LOL", StrRange(1, 7)),
									Param("opacity", 1.0, ContRange(0.0, 1.0)),
									Param("caption_height", 250, DiscreteRange(10, 300))))

opacityOpr = AugOperator("opacity", opacity, 1.0, AugParam().add(
							Param("level", 1.0, ContRange(0.2, 1.0))))

# >>> overlay_image(opacity, emoji_size, x_pos, y_pos) NOT IMPLEMENTED
# >>> overlay_image(opacity, overlay_size, x_pos, y_pos, overlay) NOT IMPLEMENTED
# >>> overlay_onto_background_image(background_image, opacity, overlay_size, x_pos,
# y_pos, scale_bg)
# >>> overlay_onto_screenshot()
# >>> overlay_stripes(line_width, line_color, line_angle, line_density, line_type,
# line opacity)
# >>> overlay_text(text, font_size, opacity, color, x_pos, y_pos)
# >>> pad(w_factor, h_factor, color)
#
# Define AugObj list that will contain s of all Augmentation Operator Objects
AugObj = [
            blurOpr,
            brightnessOpr,
            aspectRatioOpr,
            clipImageOpr,
            colorJitterOpr,
            contrastOpr,
            cropOpr,
            encodingQualityOpr,
			grayscaleOpr,
            hFlipOpr,
			memeFormatOpr,
			opacityOpr
        ]

Augs.add_AugObj_List(AugObj)