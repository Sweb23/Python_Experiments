import tkinter as tk
from tkinter import filedialog
from PIL import Image

def select_image():
    root = tk.Tk()
    root.withdraw()


    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")]
    )

    if file_path:
        print(f"Selected Image: {file_path}")


        base_image = Image.open("template.png").convert("RGBA")

       
        overlay_image = Image.open(file_path).convert("RGBA")

        # Preserve aspect ratio while fitting into 150x150
        max_size = (150, 150)
        overlay_image.thumbnail(max_size, Image.LANCZOS)  # Resize while keeping aspect ratio

        # Define paste position
        position = (320, 90)

        temp_layer = Image.new("RGBA", base_image.size, (0, 0, 0, 0))
        temp_layer.paste(overlay_image, position, overlay_image)  # Correctly apply transparency mask

        # Composite the images together
        final_image = Image.alpha_composite(base_image, temp_layer)

       
        final_image.show()

        
        save_path = filedialog.asksaveasfilename(
            title="Save Image",
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg"), ("Bitmap Image", "*.bmp")]
        )

        if save_path: 
            final_image.convert("RGB").save(save_path)  
            print(f"Image saved at: {save_path}")
        else:
            print("Save canceled.")

    else:
        print("No file selected.")


select_image()
