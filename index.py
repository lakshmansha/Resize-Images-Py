from PIL import Image
import requests
import io

def generate_resized_images(image_url):
    sizes = [
        {"name": "thumbnail", "size": (100, 100)},
        {"name": "small", "size": (300, 300)},
        {"name": "medium", "size": (600, 600)},
        {"name": "large", "size": (1200, 1200)}
    ]

    response = requests.get(image_url)
    image = Image.open(io.BytesIO(response.content))

    for size in sizes:
        resized_image = image.copy()
        resized_image.thumbnail(size["size"])
        resized_image.save(f"./resized/{get_file_name(size, image_url)}")
        print(f"Resized image saved as {get_file_name(size, image_url)}")

def get_file_name(size , image_url):
    # Extract the file name from the URL
    file_name = image_url.split('/')[-1]
    # Append the size before the file name
    return f"{size['name']}_{file_name}"

# Example usage
image_url = "https://genericlazhstrg.blob.core.windows.net/testimages/pexels-pixabay-60597.jpg"
generate_resized_images(image_url)
