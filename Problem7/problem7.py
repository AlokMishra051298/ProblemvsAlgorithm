# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouterTrieNode()
    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_state = self.root
        for state in path:
            if state not in current_state.children:
                current_state.insert(state)
            current_state = current_state.children[state]
        current_state.handler= handler
    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_state = self.root
        for state in path:
            if not current_state.children.get(state):
                return "Not found"
            current_state=current_state.children[state]
        return current_state.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouterTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = "Not found"
    def insert(self, path):
        # Insert the node as before
        self.children[path]= RouterTrieNode()

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, route_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = RouteTrie()
        self.root.insert("", route_handler)
        #self.root.handler = route_handler
    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path = self.split_path(path)
        self.root.insert(path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path = self.split_path(path)
        if len(path)==1:
            return self.root.root.handler
        return self.root.find(path)

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if len(path)==1:
            return [""]
        path=path.split("/")
        if (path[-1] is ""):
            return path[:-1]
        return path

print("____________________TEST CASE1_________________")

router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")

print(router.lookup("")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # Not found

print("____________________TEST CASE2_________________")

router1 = Router("root handler") # remove the 'not found handler' if you did not implement this
router1.add_handler("/home/about/me", "about me handler")
router1.add_handler("/home/about/team", "about my team handler")
router1.add_handler("/home/", "home handler")

print(router1.lookup("/")) # should print 'root handler'
print(router1.lookup("/home")) # should print 'home handler'
print(router1.lookup("/home/about"))# Not found
print(router1.lookup("/home/about/team")) # should print 'about my team handler' or None if you did not handle trailing slashes
print(router1.lookup("/home/about/me")) # about me handler
