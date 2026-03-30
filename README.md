# Image Compressor using Huffman Coding

This project implements lossless image compression using Huffman Coding.

## Features
- Converts image to grayscale
- Builds Huffman tree based on pixel frequency
- Compresses and decompresses images

## Technologies Used
- Python
- PIL (Pillow)
- Heap (priority queue)

## How to Run

1. Install dependency:
   pip install pillow

2. Add an image named `input.png`

3. Run:
   python huffman_image_compressor.py

## Output
- compressed.bin → compressed file
- decompressed.png → reconstructed image
