A Trie data structure using hash tables to store children instead of list/arrays.

For the RouteTrie O(m) time complexity for both insert and find with m being the number of path parts. Insert for the RouteTrieNode is constant O(1). the class Router using the find and insert from RouteTrie with additional split_path function that simplifies to linear O(m) time complexity.

Space complexity depends on the number of routes n, length of routes m, and a being the distinct routes O(n * m * a).
