#!/usr/bin/env python
# coding: utf-8

# In[10]:


from PIL import Image, ImageDraw # allows us to draw
import hashlib                   # allows us to compute the has of a given string
import random                    # allows us to generate an offset
import math                      # allows access to log function
import matplotlib                # allows us to get all colors by string


# In[11]:


def actually_draw_square(canvas_mode, canvas_size_in_pixels, canvas_background_color_rgb, rectangle_position, rectangle_fill, rectangle_outline):
    """Draws a square based on input args.
    
    Args:
        canvas_mode (String): The mode of an image defines the type and depth of a pixel in the image. See https://pillow.readthedocs.io/en/3.1.x/handbook/concepts.html#concept-modes for supported modes
        canvas_size_in_pixels (2-tuple): A 2-tuple, containing (width, height) in pixels.
        canvas_background_color_rgb (String): What color to use for the image. Default is black. If given, this should be a single integer or floating point value for single-band modes, and a tuple for multi-band modes (one value per band). When creating RGB images, you can also use color strings as supported by the ImageColor module. If the color is None, the image is not initialised.
        rectangle_position (Tuple of two Tuples): Four points to define the bounding box. Sequence of either 
        rectangle_fill (String): Color to use for the fill.
        rectangle_outline(String): Color to use for the outline.
        
    Returns:
        None
        
    """
    im = Image.new(canvas_mode, canvas_size_in_pixels, canvas_background_color_rgb)
    dr = ImageDraw.Draw(im)

    dr.rectangle(rectangle_position, fill=rectangle_fill, outline=rectangle_outline)

    im.save("square.png")


# In[12]:


def position_from_seed(seed):
    """Pulls position from a seed which is a md5 in hex
    
    Args:
        seed (String): seed md5 in hex
        
    Returns:
        Position (Tuple of two Tuples): Four points to define the bounding box.
    
    """
    random.seed(seed)
    ascii_character_sum = sum(bytearray(seed, "utf8")) # Sums the ASCII values of every character
    offset = random.randint(1, 100)
    start_position = (math.log(ascii_character_sum / 100) + offset, math.log(ascii_character_sum / 100) + offset)
    end_positon = (start_position[0] + 100, start_position[1] + 100)
    square_position = (start_position, end_positon)
    print(square_position)
    
    return square_position


# In[13]:


def color_from_seed(seed):
    """Pulls color from a seed which is a md5 in hex
    
    Args:
        seed (String): seed md5 in hex
        
    Returns:
        color (String): Some color
    
    """
    supported_colors = []
    for name, hex in matplotlib.colors.cnames.items():
        supported_colors.append(hex)
    ascii_character_sum = sum(bytearray(seed, "utf8")) # Sums the ASCII values of every character
    selection = ascii_character_sum % len(supported_colors)
    
    return supported_colors[selection]


# In[14]:


def square_parameters_from_seed(seed):
    """Pulls out square parameters from a seed which is a md5 in hex.
    
    Args:
        seed (String): Input string to be used to generate a seed.
       
    Returns:
        canvas_mode (String): The mode of an image defines the type and depth of a pixel in the image. See https://pillow.readthedocs.io/en/3.1.x/handbook/concepts.html#concept-modes for supported modes
        canvas_size_in_pixels (2-tuple): A 2-tuple, containing (width, height) in pixels.
        canvas_background_color_rgb (String): What color to use for the image. Default is black. If given, this should be a single integer or floating point value for single-band modes, and a tuple for multi-band modes (one value per band). When creating RGB images, you can also use color strings as supported by the ImageColor module. If the color is None, the image is not initialised.
        rectangle_position (Tuple of two Tuples): Four points to define the bounding box.
        rectangle_fill (String): Color to use for the fill.
        rectangle_outline(String): Color to use for the outline.
        
    """
    # canvas
    canvas_mode = "RGB"
    canvas_size_in_pixels = (200, 200)
    canvas_background_color_rgb = (255, 255, 255) # white
    
    # rectangle
    rectangle_position = position_from_seed(seed) # ((0, 0), (10, 10))
    rectangle_fill = color_from_seed(seed)
    rectangle_outline = color_from_seed(seed + str(random.randint(1, 100))) # offset
    
    return canvas_mode, canvas_size_in_pixels, canvas_background_color_rgb, rectangle_position, rectangle_fill, rectangle_outline


# In[15]:


def generate_seed(input):
    """Generates a seed from a given input string.
    
    Args:
        input (String): input string to generate seed from
        
    Returns:
        (String): md5 hash
        
    """
    return hashlib.md5(input.encode("utf8")).hexdigest()


# In[16]:


def draw_square(input):    
    """Draws a square based on the input string.
    
    Args:
        input (String): Input string to be used to generate a seed to draw a square.
    
    Returns: 
        None
        
    """
    seed = generate_seed(input)
    
    canvas_mode, canvas_size_in_pixels, canvas_background_color_rgb, rectangle_position, rectangle_fill, rectangle_outline = square_parameters_from_seed(seed)
        
    actually_draw_square(canvas_mode, canvas_size_in_pixels, canvas_background_color_rgb, rectangle_position, rectangle_fill, rectangle_outline)


# In[29]:


draw_square("Grehg")


# In[30]:


get_ipython().run_cell_magic('html', '', '<img src="square.png">')


# In[ ]:




