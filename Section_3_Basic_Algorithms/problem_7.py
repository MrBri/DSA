# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode(root_handler)

    def insert(self, path_parts, handler):
        node = self.root
        for part in path_parts:
            if part not in node.children:
                node.insert(part)
            node = node.children[part]
        node.handler = handler

    def find(self, path_parts):
        node = self.root
        for part in path_parts:
            if part not in node.children:
                return None
            node = node.children[part]
        return node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = {}
        self.handler = handler

    def insert(self, path_part):
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode()


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler=None):
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        path_parts = self.split_path(path)
        self.route_trie.insert(path_parts, handler)

    def lookup(self, path):
        path_parts = self.split_path(path)
        handler = self.route_trie.find(path_parts)
        if handler is None:
            return self.not_found_handler
        return handler

    def split_path(self, path):
        return [part for part in path.split("/") if part]

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

print("\nCreating new router...\n")
# create the router and add a route
router = Router("main handler", "404 not found") # remove the 'not found handler' if you did not implement this
router.add_handler("/main", "main route")  # add a route
router.add_handler("/about", "about route")  # add a route
router.add_handler("/main/contact", "contact route")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'main handler'
print(router.lookup("/main")) # should print 'main route'
print(router.lookup("/home")) # should print '404 not found' or None if you did not implement one
print(router.lookup("/home/about")) # should print '404 not found' or None if you did not implement one
print(router.lookup("/about/")) # should print 'about route' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print '404 not found' or None if you did not implement one

