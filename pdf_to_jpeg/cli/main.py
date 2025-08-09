
import typer
from pathlib import Path
import fitz  # PyMuPDF
from PIL import Image
import io

app = typer.Typer()

def convert_pdf_to_jpeg(
    pdf_path: Path,
    output_dir: Path,
    dpi: int = 300,
    quality: int = 85,
    first_page: int = 1,
    last_page: int = None,
):
    """Convert PDF to JPEG images."""
    # Check if PDF file exists
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Determine the range of pages to convert
    if last_page is None or last_page > len(pdf_document):
        last_page = len(pdf_document)

    if first_page < 1 or first_page > last_page:
        raise ValueError("Invalid page range")

    # Convert each page to JPEG
    for page_num in range(first_page - 1, last_page):
        page = pdf_document.load_page(page_num)
        zoom = dpi / 72  # Convert DPI to zoom factor
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)

        # Convert to PIL Image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Save as JPEG
        output_path = output_dir / f"page_{page_num + 1}.jpg"
        img.save(output_path, "JPEG", quality=quality)

    typer.echo(f"Converted {last_page - first_page + 1} pages to JPEG format in {output_dir}")

@app.command()
def convert(
    pdf_path: Path = typer.Argument(..., exists=True, readable=True, help="Path to the PDF file"),
    output_dir: Path = typer.Argument(..., dir_okay=True, writable=True, help="Output directory for JPEG files"),
    dpi: int = typer.Option(300, "--dpi", "-d", help="Dots per inch for output images"),
    quality: int = typer.Option(85, "--quality", "-q", min=1, max=100, help="JPEG quality (1-100)"),
    first_page: int = typer.Option(1, "--first-page", "-f", min=1, help="First page to convert"),
    last_page: int = typer.Option(None, "--last-page", "-l", help="Last page to convert"),
):
    """Convert PDF to JPEG images."""
    convert_pdf_to_jpeg(pdf_path, output_dir, dpi, quality, first_page, last_page)

if __name__ == "__main__":
    app()
