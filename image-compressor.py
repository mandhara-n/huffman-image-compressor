from PIL import Image
import heapq
from collections import Counter
import pickle

# ---------------- Huffman Node ----------------
class Node:
    def __init__(self, pixel, freq):
        self.pixel = pixel
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# ---------------- Build Huffman Tree ----------------
def build_huffman_tree(freq_dict):
    heap = []
    for pixel, freq in freq_dict.items():
        heapq.heappush(heap, Node(pixel, freq))

    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)

        merged = Node(None, n1.freq + n2.freq)
        merged.left = n1
        merged.right = n2

        heapq.heappush(heap, merged)

    return heap[0]


# ---------------- Generate Huffman Codes ----------------
def generate_codes(node, code="", codes={}):
    if node is None:
        return

    if node.pixel is not None:
        codes[node.pixel] = code
        return

    generate_codes(node.left, code + "0", codes)
    generate_codes(node.right, code + "1", codes)

    return codes


# ---------------- Compress Image ----------------
def compress_image(image_path):
    img = Image.open(image_path).convert("L")  # Grayscale
    pixels = list(img.getdata())

    freq = Counter(pixels)
    tree = build_huffman_tree(freq)
    codes = generate_codes(tree)

    encoded_data = "".join(codes[p] for p in pixels)

    with open("compressed.bin", "wb") as f:
        pickle.dump((encoded_data, codes, img.size), f)

    print("Image compressed successfully!")
    print("Original size (pixels):", len(pixels))
    print("Compressed size (bits):", len(encoded_data))


# ---------------- Decompress Image ----------------
def decompress_image():
    with open("compressed.bin", "rb") as f:
        encoded_data, codes, size = pickle.load(f)

    reverse_codes = {v: k for k, v in codes.items()}

    decoded_pixels = []
    temp = ""

    for bit in encoded_data:
        temp += bit
        if temp in reverse_codes:
            decoded_pixels.append(reverse_codes[temp])
            temp = ""

    img = Image.new("L", size)
    img.putdata(decoded_pixels)
    img.save("decompressed.png")

    print("Image decompressed successfully!")
    print("Saved as decompressed.png")


# ---------------- Main ----------------
if __name__ == "__main__":
    compress_image("input.png")   # Put your image name here
    decompress_image()