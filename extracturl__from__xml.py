# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import csv

# XML file path
filename = " "
output_csv = "/content/extracted_urls.csv"

# Parse the XML file
tree = ET.parse(filename)
root = tree.getroot()

# Extract URLs from <loc> tags under <url> elements
urls = [url.find('{*}loc').text for url in root.findall('.//{*}url') if url.find('{*}loc') is not None]

# Save output to a CSV file
with open(output_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["URL"])
    for url in urls:
        writer.writerow([url])

print(f"Extracted URLs saved to {output_csv}")
