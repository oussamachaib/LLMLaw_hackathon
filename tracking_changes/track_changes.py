#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 15:24:09 2024

@author: oussamachaib
"""

from docx import Document
import zipfile
from lxml import etree

def extract_tracked_changes(docx_path):
    # Unzip the .docx file to access its XML contents
    with zipfile.ZipFile(docx_path, 'r') as docx:
        xml_content = docx.read('word/document.xml')
    
    # Parse the XML content
    tree = etree.fromstring(xml_content)

    # Define namespaces
    namespaces = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
    }

    # Extract inserted text
    insertions = tree.xpath('//w:ins//w:t', namespaces=namespaces)
    inserted_text = [insertion.text for insertion in insertions]

    # Extract deleted text
    deletions = tree.xpath('//w:del//w:t', namespaces=namespaces)
    deleted_text = [deletion.text for deletion in deletions]

    return inserted_text, deleted_text

# Path to your .docx file
docx_path = 'NDA1.docx'

# Extract tracked changes
inserted_text, deleted_text = extract_tracked_changes(docx_path)

# Print the extracted changes
print("Inserted Text:")
for text in inserted_text:
    print(text)

print("\nDeleted Text:")
for text in deleted_text:
    print(text)



