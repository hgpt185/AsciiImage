# ASCII Image Converter

A Python script that converts regular images into ASCII art.

## Features

- Converts any image format (JPEG, PNG, GIF, etc.) to ASCII art
- Customizable output width
- Maintains aspect ratio
- Save to file or display in terminal
- Uses grayscale brightness mapping

## Installation

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic usage (display in terminal):

```bash
python ascii_image.py your_image.jpg
```

### Save to a text file:

```bash
python ascii_image.py your_image.jpg -o output.txt
```

### Customize width (in characters):

```bash
python ascii_image.py your_image.jpg -w 150
```

### Combine options:

```bash
python ascii_image.py your_image.jpg -w 80 -o ascii_art.txt
```

## Command-line Options

- `image` - Path to the input image file (required)
- `-w, --width` - Width of the ASCII art in characters (default: 100)
- `-o, --output` - Output file path (if not specified, prints to console)

## How It Works

1. **Load Image**: Opens the input image using PIL/Pillow
2. **Convert to Grayscale**: Simplifies the image to brightness values
3. **Resize**: Adjusts the image size to match the desired character width
4. **Map to ASCII**: Each pixel's brightness is mapped to an ASCII character (darker pixels get denser characters like '@', lighter pixels get sparse characters like '.')
5. **Output**: The resulting ASCII art is either displayed or saved to a file

## Examples

For best results:
- Use images with good contrast
- Start with a width of 100-150 characters
- For detailed images, use higher width values
- Smaller width values (50-80) work well for simple images or icons

## ASCII Character Set

The script uses the following characters from darkest to lightest:
```
@ # S % ? * + ; : , .
```

## License

Free to use and modify.

