from heapq import heappush, heappop
from collections import defaultdict
import sys

def huffman_encoding(string):

    if not string:
        return None, None

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

    return encoded_string, encoding_table

def huffman_decoding(encoded_string, encoding_table):
    if not encoded_data or not encoding_table:
        return ""
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

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

# Example usage:
# Encode a string, then decode it
original_string = "AAAAAAABBBCCCCCCCDDEEEEEE"
encoded_string, encoding_table = huffman_encoding(original_string)
decoded_string = huffman_decoding(encoded_string, encoding_table)
print("Original string:", original_string)
print("Encoded string:", encoded_string)
print("Decoded string:", decoded_string)

original_string = None
encoded_string, encoding_table = huffman_encoding(original_string)
decoded_string = huffman_decoding(encoded_string, encoding_table)


original_string = ''
encoded_string, encoding_table = huffman_encoding(original_string)
decoded_string = huffman_decoding(encoded_string, encoding_table)
