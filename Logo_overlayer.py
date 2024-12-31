import cv2
import numpy as np

seed = 62242
logo = cv2.imread("/Users/jarvis/pymycod/Samsung_prism/pics_data/logo.png", cv2.IMREAD_UNCHANGED)
poster_image = cv2.imread("/Users/jarvis/pymycod/Samsung_prism/new/No_textseed1.png")

if seed == 754324257:
    scale_factor = 0.5
    new_width = int(logo.shape[1] * scale_factor)
    new_height = int(logo.shape[0] * scale_factor)
    logo_resized = cv2.resize(logo, (new_width, new_height), interpolation=cv2.INTER_CUBIC)


    x_offset = 400
    y_offset = 40
elif seed == 53643534:
    scale_factor = 0.5
    new_width = int(logo.shape[1] * scale_factor)
    new_height = int(logo.shape[0] * scale_factor)
    logo_resized = cv2.resize(logo, (new_width, new_height), interpolation=cv2.INTER_CUBIC)


    x_offset = 400
    y_offset = 80
    
elif seed == 882422131:
    scale_factor = 0.5
    new_width = int(logo.shape[1] * scale_factor)
    new_height = int(logo.shape[0] * scale_factor)
    logo_resized = cv2.resize(logo, (new_width, new_height), interpolation=cv2.INTER_CUBIC)


    x_offset = 450
    y_offset = 60
else: 
    scale_factor = 0.5
    new_width = int(logo.shape[1] * scale_factor)
    new_height = int(logo.shape[0] * scale_factor)
    logo_resized = cv2.resize(logo, (new_width, new_height), interpolation=cv2.INTER_CUBIC)


    x_offset = 144
    y_offset = 50

if logo_resized.shape[2] == 4:
    alpha_channel = logo_resized[:, :, 3] / 255.0
    logo_rgb = logo_resized[:, :, :3]
else:
    alpha_channel = np.ones((logo_resized.shape[0], logo_resized.shape[1]), dtype=float)
    logo_rgb = logo_resized


alpha_channel = np.expand_dims(alpha_channel, axis=2)


y1, y2 = y_offset, y_offset + logo_rgb.shape[0]
x1, x2 = x_offset, x_offset + logo_rgb.shape[1]


if y2 > poster_image.shape[0] or x2 > poster_image.shape[1]:
    raise ValueError("The phone image exceeds the dimensions of the poster image at the given offsets.")


for c in range(0, 3):
    poster_image[y1:y2, x1:x2, c] = (
        alpha_channel[:, :, 0] * logo_rgb[:, :, c] + 
        (1.0 - alpha_channel[:, :, 0]) * poster_image[y1:y2, x1:x2, c]
    )

cv2.imwrite(f"/Users/jarvis/pymycod/Samsung_prism/pics_data/logo_overlayed/logo{seed}.jpg", poster_image)
