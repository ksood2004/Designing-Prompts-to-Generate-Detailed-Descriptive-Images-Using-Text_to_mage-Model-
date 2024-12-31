from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


image_path = '/Users/jarvis/pymycod/Samsung_prism/pics_data/text_overlayed/4.jpg'  
img = Image.open(image_path)


img = img.convert('RGB')

def onclick(event):

    if event.xdata is not None and event.ydata is not None:
        x, y = int(event.xdata), int(event.ydata)
        if x < img.width and y < img.height:
            rgb = img.getpixel((x, y))
            print(f'Clicked at ({x}, {y}) - RGB: {rgb}')


fig, ax = plt.subplots()
ax.imshow(mpimg.imread(image_path))
ax.set_title('Click on the image to get RGB values')
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
