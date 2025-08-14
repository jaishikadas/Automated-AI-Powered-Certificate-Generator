import pandas as pd
from PIL import Image, ImageDraw
import os

# Load CSV
df = pd.read_csv("sample_recipients.csv")

# Template image file name
template_file = "certificate.png"

# Output directory
output_dir = "certificates"
os.makedirs(output_dir, exist_ok=True)

# Coordinates (adjust based on your template)
name_pos = (520, 380)
course_pos = (330, 460)
date_pos = (330, 500)

# Generate certificates
for index, row in df.iterrows():
    name = str(row['Name'])
    course = str(row['Course'])
    date = str(row['Date'])

    # Load template
    cert = Image.open(template_file)
    draw = ImageDraw.Draw(cert)

    # Use default font
    draw.text(name_pos, name, fill="white")
    draw.text(course_pos, course, fill="white")
    draw.text(date_pos, date, fill="white")

    # Save as PDF
    filename = os.path.join(output_dir, f"{name.replace(' ', '_')}.pdf")
    cert.convert('RGB').save(filename, "PDF")
    print(f"Saved: {filename}")

import shutil
shutil.make_archive("certificates_bundle", 'zip', "certificates")
files.download("certificates_bundle.zip")

