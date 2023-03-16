Using a Trie data structure storing the children as a hash table, could also use an array/list.

For the class Trie Searching and inserting are both O(m) linear time complexity with m being the length of the word. The TrieNode inserting is constant O(1), returning the suffixes is O(n) linear time.

Space complexity is determined by the number of characters in the alphabet used and worst case scenario of O(n * m * a) where n is the number of keys stored, m the length of a key and a the size of the alphabet or distinct characters used in the keys.
