#!/usr/bin/env python3
"""
ASCII Image Converter
Converts regular images to ASCII art representation.
"""

import argparse
from PIL import Image
import sys


# ASCII characters from darkest to lightest
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
# Alternative extended set: 
# ASCII_CHARS = ["$", "@", "B", "%", "8", "&", "W", "M", "#", "*", "o", "a", "h", "k", "b", "d", "p", "q", "w", "m", "Z", "O", "0", "Q", "L", "C", "J", "U", "Y", "X", "z", "c", "v", "u", "n", "x", "r", "j", "f", "t", "/", "\\", "|", "(", ")", "1", "{", "}", "[", "]", "?", "-", "_", "+", "~", "<", ">", "i", "!", "l", "I", ";", ":", ",", "\"", "^", "`", "'", ".", " "]


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


def convert_image_to_ascii(image_path, new_width=100):
    """
    Main function to convert image to ASCII art.
    
    Args:
        image_path: Path to the input image
        new_width: Width of the ASCII art in characters
    
    Returns:
        String containing the ASCII art
    """
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error: Unable to open image file '{image_path}'")
        print(f"Details: {e}")
        sys.exit(1)
    
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


def main():
    """Command-line interface for the ASCII image converter."""
    parser = argparse.ArgumentParser(
        description="Convert images to ASCII art",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s input.jpg                    # Display ASCII art in terminal
  %(prog)s input.jpg -o output.txt      # Save to file
  %(prog)s input.jpg -w 150             # Use 150 characters width
  %(prog)s input.jpg -w 80 -o art.txt   # Custom width and save to file
        """
    )
    
    parser.add_argument(
        "image",
        help="Path to the input image file"
    )
    
    parser.add_argument(
        "-w", "--width",
        type=int,
        default=100,
        help="Width of the ASCII art in characters (default: 100)"
    )
    
    parser.add_argument(
        "-o", "--output",
        help="Output file path (if not specified, prints to console)"
    )
    
    args = parser.parse_args()
    
    # Convert image to ASCII
    print(f"Converting '{args.image}' to ASCII art...")
    ascii_art = convert_image_to_ascii(args.image, args.width)
    
    # Output result
    if args.output:
        try:
            with open(args.output, "w") as f:
                f.write(ascii_art)
            print(f"ASCII art saved to '{args.output}'")
        except Exception as e:
            print(f"Error: Unable to write to file '{args.output}'")
            print(f"Details: {e}")
            sys.exit(1)
    else:
        print("\n" + ascii_art)


if __name__ == "__main__":
    main()

