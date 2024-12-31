import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Load the image using OpenCV
image_path = '/Users/jarvis/pymycod/Samsung_prism/pics_data/text_overlayed/3.jpg'
image = cv2.imread(image_path)

# Convert the image to RGB (OpenCV loads images in BGR format)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to PIL Image
image_pil = Image.fromarray(image_rgb)

# Create a drawing context
draw = ImageDraw.Draw(image_pil)

# Load a TrueType or OpenType font file
font_path = '/Users/jarvis/pymycod/Samsung_prism/komika-poster/KOMIKAX_.ttf'  # e.g., 'arial.ttf'
font_size = 30
font = ImageFont.truetype(font_path, font_size)

# Define the JSON data
json_data = {
    "Offer Provider": [""],
    "Offer Amount": [""],
    "Offer Type": [""],
    "Description": ["Get upto 12,500 off *"]
}

# Define the text color (R, G, B) for black
text_color = (237, 54, 136) # Black

# Define the starting position
start_x, start_y = 100, 200
line_spacing = 50 # Adjust spacing between lines
max_width = image_pil.width - start_x - 20  # 20 pixels padding from the right edge

# Function to wrap text
def wrap_text(text, font, max_width):
    lines = []
    words = text.split()
    while words:
        line = ''
        while words and draw.textsize(line + words[0], font=font)[0] <= max_width:
            line += (words.pop(0) + ' ')
        lines.append(line)
    return lines

# Iterate through each offer and draw it on the image
current_y = start_y
for i in range(len(json_data["Offer Provider"])):
    full_text = f'{json_data["Offer Provider"][i]}  {json_data["Offer Amount"][i]}  {json_data["Offer Type"][i]} {json_data["Description"][i]}'
    lines = wrap_text(full_text, font, max_width)
    for line in lines:
        draw.text((start_x, current_y), line, font=font, fill=text_color)
        current_y += line_spacing

# Convert back to OpenCV image
image_with_text = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)

# Save the image
output_path = '/Users/jarvis/pymycod/Samsung_prism/pics_data/text_overlayed/4.jpg'
cv2.imwrite(output_path, image_with_text)

print(f"Image saved to {output_path}")
# import cv2
# from PIL import Image, ImageDraw, ImageFont
# import numpy as np
# import colorsys

# # Load the image using OpenCV
# image_path = '/Users/jarvis/pymycod/Samsung_prism/pics_data/logo_overlayed/logo754324257.jpg'
# image = cv2.imread(image_path)

# # Convert the image to RGB (OpenCV loads images in BGR format)
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# # Convert to PIL Image
# image_pil = Image.fromarray(image_rgb)

# # Create a drawing context
# draw = ImageDraw.Draw(image_pil)

# # Load TrueType or OpenType font file
# font_path = '/Users/jarvis/pymycod/Samsung_prism/impact/Impacted.ttf'
# large_font_size = 60
# small_font_size = 30
# large_font = ImageFont.truetype(font_path, large_font_size)
# small_font = ImageFont.truetype(font_path, small_font_size)

# # JSON data
# json_data = {
#     "Offer Provider": ["Flipkart", "Flipkart UPI", "Flipkart Axis Bank", "HDFC Bank"],
#     "Offer Amount": [12.650, 3249.75, 749.95, 1000],
#     "Offer Type": ["Exchange", "UPI", "card", "credit card"],
#     "Description": ["Buy with Exchange up to 12,650 off", "25% Instant Discount for 1st Flipkart Order", "Cashback on Flipkart Axis Bank Card", "1000 Off On HDFC Bank Credit Non EMI, Credit and Debit Card EMI Transactions"]
# }

# # Split the data into two groups
# half_index = len(json_data["Description"]) // 2

# large_texts = json_data["Description"][:half_index]
# small_texts = json_data["Description"][half_index:]

# # Define starting positions
# large_text_position = (394, 173)
# small_text_position = (450, 450)

# # Function to calculate luminance of a color
# def calculate_luminance(color):
#     r, g, b = color
#     return 0.2126*r + 0.7152*g + 0.0722*b

# # Function to get a contrasting text color
# def get_contrasting_color(image, position, size=(10, 10)):
#     x, y = position
#     region = image[max(y, 0):min(y+size[1], image.shape[0]), max(x, 0):min(x+size[0], image.shape[1])]
#     avg_color = np.mean(region, axis=(0, 1))
#     luminance = calculate_luminance(avg_color)
    
#     if luminance > 128:
#         contrasting_color = (0, 0, 0)  # Dark text for light background
#     else:
#         contrasting_color = (255, 255, 255)  # Light text for dark background
    
#     # Generate aesthetic colors that are fully visible
#     h, l, s = colorsys.rgb_to_hls(contrasting_color[0]/255.0, contrasting_color[1]/255.0, contrasting_color[2]/255.0)
#     aesthetic_colors = []
#     for i in range(6):
#         new_hue = (h + i * 0.1) % 1.0
#         r, g, b = colorsys.hls_to_rgb(new_hue, l, s)
#         aesthetic_colors.append((int(r * 255), int(g * 255), int(b * 255)))
#     return aesthetic_colors

# # Function to draw text with wrapping and cycling through aesthetic colors
# def draw_wrapped_text(draw, text, position, font, max_width, colors):
#     x, y = position
#     lines = []
#     words = text.split()
#     while words:
#         line = ''
#         while words and draw.textsize(line + words[0], font=font)[0] <= max_width:
#             line += (words.pop(0) + ' ')
#         lines.append(line)
    
#     color_index = 0
#     for line in lines:
#         draw.text((x, y), line, font=font, fill=colors[color_index % len(colors)])
#         y += font.getsize(line)[1]
#         color_index += 1

# # Draw large texts
# current_y = large_text_position[1]
# colors = get_contrasting_color(image, large_text_position)
# for text in large_texts:
#     draw_wrapped_text(draw, text, (large_text_position[0], current_y), large_font, image_pil.width - large_text_position[0], colors)
#     current_y += large_font.getsize(text)[1] * 2  # Move to next line with some spacing

# # Draw small texts
# current_y = small_text_position[1]
# colors = get_contrasting_color(image, small_text_position)
# for text in small_texts:
#     draw_wrapped_text(draw, text, (small_text_position[0], current_y), small_font, image_pil.width - small_text_position[0], colors)
#     current_y += small_font.getsize(text)[1] * 2  # Move to next line with some spacing

# # Convert back to OpenCV image
# image_with_text = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)

# # Save the image
# output_path = '/Users/jarvis/pymycod/Samsung_prism/pics_data/text_overlayed/1.jpg'
# cv2.imwrite(output_path, image_with_text)

# print(f"Image saved to {output_path}")
