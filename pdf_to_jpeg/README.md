

# PDF to JPEG Converter

A simple CLI tool to convert PDF files to JPEG images using Typer.

## Features

- Convert PDF pages to high-quality JPEG images
- Customizable DPI and quality settings
- Convert specific page ranges
- Easy-to-use command line interface

## Installation

1. Clone this repository
2. Install dependencies using Uv:

```bash
uv sync
```

## Usage

```bash
python -m cli.main convert path/to/input.pdf path/to/output/dir [options]
```

### Options

- `--dpi`, `-d`: Dots per inch for output images (default: 300)
- `--quality`, `-q`: JPEG quality (1-100, default: 85)
- `--first-page`, `-f`: First page to convert (default: 1)
- `--last-page`, `-l`: Last page to convert (default: all pages)

### Example

```bash
python -m cli.main convert document.pdf output_images --dpi 600 --quality 95 --first-page 1 --last-page 5
```

This will convert pages 1-5 of `document.pdf` to JPEG images with 600 DPI and 95% quality, saving them in the `output_images` directory.

## Dependencies

- Typer: For building the CLI
- PyMuPDF: For PDF processing
- Pillow: For image handling

## License

MIT

