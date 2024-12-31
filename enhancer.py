# from PIL import Image


# image = Image.open("/Users/jarvis/pymycod/Samsung_prism/pics_data/samsungs24.png_no_bg.png")

# image = image.convert("RGB")
# resized_image = image.resize((300, 350), Image.LANCZOS)


# resized_image.save("/Users/jarvis/pymycod/Samsung_prism/pics_data/enhanced_image.jpg")
import cv2


image = cv2.imread("/Users/jarvis/pymycod/Samsung_prism/pics_data/samsungs24.png_no_bg.png")


resized_image = cv2.resize(image, (300, 350), interpolation=cv2.INTER_CUBIC)

# resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)

cv2.imwrite("/Users/jarvis/pymycod/Samsung_prism/pics_data/enhanced_image.jpg", resized_image)
