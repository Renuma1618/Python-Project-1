from helper_functions import *

#-----------------------FILL IN THE FOLDER WHERE YOUR IMAGE EXISTS--------------------------
datafolder = "C:/Users/spj/workspace-python/teaching-material/assgn1code/images/"
imgpath = datafolder + "1.jpg" 
#----------------------------------------STARTER CODE----------------------------------------
# Convert the color image to grayscale and returns the grayscale pixels 
pixel_values = read_colorimg(imgpath)
# The returned pixel values INCLUDE 2 boundary rows and 2 boundary colns. Therefore,
numb_rows = len(pixel_values)-2
numb_colns = len(pixel_values[0])-2
#
#----------------------------------------WRITE YOUR CODE HERE----------------------------------------
# Create a data structure to store updated pixel information
new_pixel_values = [[0 for _ in range(numb_colns)] for i in range(numb_rows)]
# Define the 3 x 3 mask as a tuple of tuples
mask = ((-1,-1,-1), (-1,8,-1), (-1,-1,-1))

# Implement a function to slice a part from the image as a 2D list
def get_slice_2d_list(pixel_values, pos):
    return [pixel_values[i][pos[1]-1:pos[1]+2]for i in range(pos[0]-1,pos[0]+2)]

# Implement a function to flatten a 2D list or a 2D tuple
def flatten(pixels_data):
    return [k for i in pixels_data for k in i ]

# For each of the pixel values, excluding the boundary values
    # Create little local 3x3 box using list slicing
for i in range(1,len(pixel_values)-1):
    for j in range(1,len(pixel_values[0])-1):
        neighbour_pixels = get_slice_2d_list(pixel_values,(i,j))
        neighbour_pixels_flattened = flatten(neighbour_pixels)
        mask_flattened = flatten(mask)
        # Apply the mask
        mult_result = list(map(lambda x,y:x*y, neighbour_pixels_flattened, mask_flattened))
        new_pixel_values[i-1][j-1] = sum(mult_result)      
    # Sum all the multiplied values and set the new pixel value
total = sum(flatten(new_pixel_values))
#        
#----------------------------------------END YOUR CODE HERE----------------------------------------
# Verify your result
verify_result(pixel_values, new_pixel_values, mask)
# View the original image and the edges of the image
view_images(imgpath, new_pixel_values)
