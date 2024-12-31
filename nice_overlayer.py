from PIL import Image, ImageDraw, ImageFilter

def overlay_images(background_image_path, overlay_image_path, output_path):
    # Open background image
    background = Image.open(background_image_path)
    
    # # Upscale background image
    # upscale_factor = 2  # Increase this factor as needed
    # background = background.resize((500,300), Image.ANTIALIAS)
    
    # Open overlay image
    overlay = Image.open(overlay_image_path)

    # Resize overlay image to match background image size
    overlay = overlay.resize((200,250), Image.ANTIALIAS)

    # Create a transparent mask
    mask = Image.new("L", background.size, 0)
    draw = ImageDraw.Draw(mask)

    # Draw gradient on the mask
    draw.rectangle((0, 0, background.width, background.height), fill=255)
    for y in range(int(background.height / 2)):
        alpha = int(255 * (1 - (y / (background.height / 2))))
        draw.rectangle((0, y, background.width, y + 1), fill=alpha)

    # Apply the mask to the overlay
    overlay.putalpha(mask)

    # Composite images
    result = Image.alpha_composite(background.convert("RGBA"), overlay)

    result.save(output_path, format="PNG")

    print("Overlay created successfully!")

if __name__ == "__main__":
    background_image_path = "/Users/jarvis/pymycod/Samsung_prism/new/No_txt754324257.jpg"
    overlay_image_path = "/Users/jarvis/pymycod/Samsung_prism/pics_data/table.png"

    output_path = "/Users/jarvis/pymycod/Samsung_prism/pics_data/result_image.png"

    overlay_images(background_image_path, overlay_image_path, output_path)
