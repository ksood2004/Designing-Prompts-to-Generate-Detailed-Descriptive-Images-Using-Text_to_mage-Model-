import cv2
import numpy as np
from PIL import Image

def extend_image_with_gradient(image_path, output_path, extension_size, direction='left'):

    img = cv2.imread(image_path)
    

    height, width, _ = img.shape
    

    if direction == 'left':
        new_img = np.zeros((height, width + extension_size, 3), dtype=np.uint8)
        new_img[:, extension_size:] = img
        

        for i in range(extension_size):
            alpha = i / extension_size
            new_img[:, i] = (1 - alpha) * img[:, 0] + alpha * img[:, 1]
    
    elif direction == 'right':
        new_img = np.zeros((height, width + extension_size, 3), dtype=np.uint8)
        new_img[:, :width] = img
        

        for i in range(extension_size):
            alpha = i / extension_size
            new_img[:, width + i] = (1 - alpha) * img[:, -1] + alpha * img[:, -2]
    

    cv2.imwrite(output_path, new_img)
    


input_image_path = '/Users/jarvis/pymycod/Samsung_prism/diwali2.jpeg'
output_image_path = '/Users/jarvis/pymycod/Samsung_prism/out.jpg'

extend_image_with_gradient(input_image_path, output_image_path, extension_size=500 , direction='left')