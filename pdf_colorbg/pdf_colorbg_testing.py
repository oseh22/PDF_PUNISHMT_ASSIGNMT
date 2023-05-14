import subprocess
from reportlab.pdfgen import canvas

# Get user input for text, filename, and path
Title = input("Enter file title: ")
text = input("Enter the text to convert to PDF: ")
filename = input("Enter the filename for the PDF (without extension): ")
path = input("Enter the path to save the PDF file ")

# If path is not specified, use current directory
if not path:
    path = "."

# Add the .pdf extension to the filename
filename = filename + ".pdf"

# Create a new PDF file
pdf = canvas.Canvas(f"{path}/{filename}")

# Set the font and font size of the header
pdf.setFont("Helvetica", 18)

# Set the background color for the header section (red)
pdf.setFillColorRGB(255, 0, 0)
pdf.rect(0, pdf._pagesize[1] - 60, pdf._pagesize[0], 60, fill=True)


# Set the background color for the body section (green)
pdf.setFillColorRGB(0, 255, 0)
pdf.setFont("Helvetica", 12)
pdf.rect(0, 0, pdf._pagesize[0], pdf._pagesize[1] - 60, fill=True)


# Align the title to the center
pdf.setFillColorRGB(255, 255, 0)
pdf.drawCentredString(pdf._pagesize[0] / 2, pdf._pagesize[1] - 40, Title)

# Write the text body
pdf.setFillColorRGB(0, 0, 0)
pdf.drawString(10, 750, text) # 10 for the width while 750 is for the text height

# Save the PDF file
pdf.save()

# Open the PDF file with the default PDF viewer
subprocess.Popen([filename], shell=True, cwd=path)

print(f"PDF file saved as {path}/{filename}")
