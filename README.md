# Edge Detection using Python

This project demonstrates a basic implementation of edge detection in Python, designed for educational purposes. It applies a 3×3 convolution mask to a grayscale image to identify and highlight edges based on pixel intensity changes.

## 🖼️ Project Overview

Edge detection is a fundamental technique in image processing used to identify significant transitions in pixel intensity. These transitions usually signify boundaries of objects within an image. This project:

- Converts a color image into grayscale
- Applies a 3×3 edge detection mask
- Computes new pixel values by convolving the mask over the image
- Displays the original and edge-detected images

## 🛠️ Tools and Libraries

The project uses basic Python and the following libraries (make sure they are installed):

- `matplotlib`
- `numpy`
- `scikit-image`
- `scipy`

## 📁 Folder Structure
project/
│
├── edgedetect_assgn.py # Main script for edge detection
├── helper_functions.py # Provided utility functions
├── images/
│ └── 1.jpg # Sample input image
└── README.md # Project documentation


## ⚙️ How It Works

1. **Image Reading and Preprocessing**  
   The `read_colorimg()` function converts the input color image to grayscale and adds padding (dummy pixels) around the border to handle convolution near the edges.

2. **Edge Detection Mask**  
   A 3x3 convolution mask is applied over each pixel to detect edges. In this implementation, Mask 2 is used:

[ [-1, -1, -1],
[-1, 8, -1],
[-1, -1, -1] ]


3. **Convolution Operation**  
For each pixel:
- A 3x3 patch is extracted using `get_slice_2d_list()`.
- Both the patch and the mask are flattened using `flatten()`.
- The pixel values are multiplied element-wise with the mask using `map()` and `lambda`.
- The sum of these products determines the new pixel intensity.

4. **Verification and Visualization**  
The result is verified against a reference implementation using `scipy`, and both the original and processed images are displayed using `matplotlib`.

## 🧠 Code Explanation

Key functions and logic:


# Extract 3x3 pixel neighborhood
def get_slice_2d_list(pixel_values, pos):
 return [pixel_values[i][pos[1]-1:pos[1]+2] for i in range(pos[0]-1,pos[0]+2)]

# Flatten 2D list or tuple to 1D
def flatten(pixels_data):
 return [k for i in pixels_data for k in i]

# Apply convolution using mask
for i in range(1, len(pixel_values) - 1):
 for j in range(1, len(pixel_values[0]) - 1):
     patch = get_slice_2d_list(pixel_values, (i, j))
     patch_flat = flatten(patch)
     mask_flat = flatten(mask)
     multiplied = list(map(lambda x, y: x * y, patch_flat, mask_flat))
     new_pixel_values[i - 1][j - 1] = sum(multiplied)

## Expected Output
The program prints “True result” if the output matches the reference result.
Displays two images side by side:
Original grayscale image
Edge-detected image
