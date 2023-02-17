from heapq import heappush, heappop
from collections import defaultdict

def encode(string):

    freq = defaultdict(int) # Count frequency, regular dict doesn't set a default without .get
    for c in string:
        freq[c] += 1

    heap = []
    for c, f in freq.items(): # Priority queue representing the huffman nodes
        heappush(heap, [f, [c, ""]])

    # Merge the two trees with the smallest frequencies until there is only one tree
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # Extract the encoding table from the completed Huffman tree
    encoding_table = dict(heappop(heap)[1:])

    # Encode the original string using the encoding table
    encoded_string = ''.join(encoding_table[c] for c in string)

    return encoding_table, encoded_string

def decode(encoding_table, encoded_string):
    # Invert the encoding table to get the decoding table
    decoding_table = {v: k for k, v in encoding_table.items()}

    # Decode the encoded string using the decoding table
    current_code = ''
    decoded_string = ''
    for bit in encoded_string:
        current_code += bit
        if current_code in decoding_table:
            decoded_string += decoding_table[current_code]
            current_code = ''

    return decoded_string

# Example usage:
# Encode a string, then decode it
original_string = "AAAAAAABBBCCCCCCCDDEEEEEE"
encoding_table, encoded_string = encode(original_string)
decoded_string = decode(encoding_table, encoded_string)
print("Original string:", original_string)
print("Encoded string:", encoded_string)
print("Decoded string:", decoded_string)

