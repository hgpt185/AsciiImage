"""
ASCII Image Converter Utility
Provides functions to convert images to ASCII art.
"""

from PIL import Image
import io


# ASCII characters from darkest to lightest
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def resize_image(image, new_width=100):
    """
    Resize image while maintaining aspect ratio.
    Characters are taller than wide, so we adjust the height accordingly.
    """
    width, height = image.size
    aspect_ratio = height / width
    # Adjust for character height (typically characters are about 2x taller than wide)
    new_height = int(aspect_ratio * new_width * 0.55)
    return image.resize((new_width, new_height))


def grayscale_image(image):
    """Convert image to grayscale."""
    return image.convert("L")


def pixels_to_ascii(image):
    """
    Convert grayscale pixel values to ASCII characters.
    """
    pixels = image.getdata()
    ascii_str = ""
    
    for pixel_value in pixels:
        # Map pixel value (0-255) to ASCII character index
        ascii_str += ASCII_CHARS[pixel_value * len(ASCII_CHARS) // 256]
    
    return ascii_str


def convert_image_to_ascii(image_file, new_width=100):
    """
    Main function to convert image to ASCII art.
    
    Args:
        image_file: File object or path to the input image
        new_width: Width of the ASCII art in characters
    
    Returns:
        String containing the ASCII art
    """
    # Open image
    if isinstance(image_file, str):
        image = Image.open(image_file)
    else:
        # Handle file upload (InMemoryUploadedFile or similar)
        image = Image.open(image_file)
    
    # Convert to grayscale
    image = grayscale_image(image)
    
    # Resize image
    image = resize_image(image, new_width)
    
    # Convert pixels to ASCII
    ascii_str = pixels_to_ascii(image)
    
    # Format into lines
    img_width = image.width
    ascii_lines = []
    for i in range(0, len(ascii_str), img_width):
        ascii_lines.append(ascii_str[i:i+img_width])
    
    return "\n".join(ascii_lines)


