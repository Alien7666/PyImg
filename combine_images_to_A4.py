from PIL import Image
import os

def combine_images_to_A4(folder_path, output_folder_path):
    images = [Image.open(os.path.join(folder_path, img)) for img in os.listdir(folder_path) if img.endswith(('png', 'jpg', 'jpeg'))]
    
    # A4 size at 300 dpi in pixels, adjust if necessary
    a4_size = (2480, 3508)
    
    for i in range(0, len(images), 4):
        # Create a new A4 image with a white background
        a4_image = Image.new('RGB', a4_size, 'white')
        
        # Calculate positions for each image (1 2 on top, 3 4 on bottom)
        positions = [(0, 0), (1240, 0), (0, 1754), (1240, 1754)]
        
        # Paste images into the A4 image
        for j, pos in enumerate(positions):
            if i+j < len(images):
                a4_image.paste(images[i+j], pos)
        
        # Save the combined image
        a4_image.save(os.path.join(output_folder_path, f'combined_{i//4+1}.jpg'))
        print(f'Saved combined image {i//4+1}')

# Example usage
folder_path = 'img'
output_folder_path = 'output'
combine_images_to_A4(folder_path, output_folder_path)
