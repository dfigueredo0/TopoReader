import cv2
import numpy as np

def prepocess_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # TODO: Apply image preprocessing techniques
    
    return image

def detect_contours(processed_image):
    # TODO: Detect contour lines
    return

def analyze_contours():
    # TODO: Analyze them each line should be a specific elevation give that number
    # Keep in mind contours characteristics 
    return

def calculate_contour_interval():
    # TODO: Implement calculations
    # find two index contours, determine the difference, count number of contours, divide by said amount. 
    return

def construct_graph():
    # TODO: create a graphical representation of how an analyzed contour area would look like. 
    return


    