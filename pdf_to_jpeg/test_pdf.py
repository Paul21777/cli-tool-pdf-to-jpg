

import fitz

# Create a simple test PDF
doc = fitz.open()
page = doc.new_page()

# Add some text
page.insert_text((100, 100), "Hello, World!", fontsize=24)
page.insert_text((100, 200), "This is a test PDF for conversion.", fontsize=18)

# Save the PDF
doc.save("test.pdf")
doc.close()

