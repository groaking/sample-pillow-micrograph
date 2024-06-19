# Install Python Pillow using:
# python -m pip install pillow

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import pandas as pd

# Open the data table (in CSV format)
dt = pd.read_csv('data_table.csv')

# Select which table column to print out
dt = dt['Oxs_TimeDriver::Simulation time']

# The directory where all micrographs (mg) are stored
mg_folder = 'all_micrographs'

# Enlist the list of micrographs (mg) filename
mg_list = os.listdir(mg_folder)

# The directory where all images will be saved
output_folder = 'generated_images'

# Assumption: the number of data table row is equal to the number of micrographs
# i.e., N (number of table row and micrographs) = 10
N = 10

# Iterating through every data table row and micrographs
for i in range(N):

    # Open the background image to overlay
    img = Image.open('background.png')
    
    # Open the N-th micrograph and shrink the size
    micrograph = Image.open(f'{mg_folder}/{mg_list[i]}').reduce(1)
    
    # Pasting the micrograph into the original background
    x_pos = 250
    y_pos = 600
    img.paste(micrograph, (x_pos, y_pos))
    
    # Overlay with text
    # Adjust color by changing fill=(R, G, B)
    x_pos = 600
    y_pos = 700
    text = 'Simulation Time of OOMMF = ' + str(dt[i])
    # Adjust font type and font size
    font = ImageFont.truetype('font_roboto/robotocondensed-regular.ttf', 40)
    method = ImageDraw.Draw(img)
    method.text((x_pos, y_pos), text, fill=(0, 0, 0), font=font)
    
    # Saving the image
    img.save(f'{output_folder}/{i}.png')
    
    # Preventing memory leak (not necessary, but worth a try)
    del img, method, micrograph
    
    # Logging
    print(f'Generated image for data table row number: {i}')
