


import os
import shutil
from pathlib import Path
import subprocess

def test_pdf_to_jpeg_conversion():
    """Test the PDF to JPEG conversion functionality."""

    # Clean up any existing test files
    if os.path.exists("test.pdf"):
        os.remove("test.pdf")
    if os.path.exists("test_output"):
        shutil.rmtree("test_output")

    # Create test PDF
    import fitz
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((100, 100), "Test PDF for Conversion", fontsize=24)
    doc.save("test.pdf")
    doc.close()

    from cli.main import convert_pdf_to_jpeg

    # Test conversion
    pdf_path = Path("test.pdf")
    output_dir = Path("test_output")

    # This should work without errors
    convert_pdf_to_jpeg(pdf_path, output_dir)

    # Check if output file exists
    output_file = output_dir / "page_1.jpg"
    assert output_file.exists(), f"Output file {output_file} does not exist"

    # Check file size (should be > 0)
    file_size = output_file.stat().st_size
    assert file_size > 0, f"Output file {output_file} is empty"

    print("✓ Conversion test passed!")

if __name__ == "__main__":
    test_pdf_to_jpeg_conversion()

