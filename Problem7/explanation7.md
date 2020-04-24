# Code Design

1. RouterTrieNode

Have two instance variable children and handler(intially set to Not Found)

Insert function:

simply insert RouterTrieNode at children[char]

2. RouteTrie

Insert function:
Iterate over path and look is the state is present in dictionary on and go inside the dictionary deeply, and put where we don't find state.
And where path end we set the handler.

Find function:
We need to iterate over each state in path, get state in current_state.children, assign current_state.children[char] as node for next iteration
If no path is there it returns Not Found

3. Router
Have instance variable root with value "".

split_path function:

Simply splits with "/" and check for if path end with "/" then ignore this.
It returns the list of states in path

add_handler function:
 Calls split and pass path to RouteTrie

lookup function:
 Simply call the split_path and then check if length of path is 1 it means it is root so, return root handler
 Else call the find function of the RouteTrie.
# Time complexity:

1. RouterTrie

> Insert and find function- **O(n)**

2. Router

> split_path function: **O(n)**
> add_handler: **O(n)** (because it call split as well insert function of RouteTrie O(n+n) results O(n))
> lookup function: **O(n)**


# Space Complexity

1. RouteTrieNode O(1)
2. RouteTrie
> insert: O(n), the auxiliary space used by the algorithms assigning the node and keep it update while the process is executed

3. Router - totally dependent on RouteTrie methods.
> add_handler: O(n) no. of states

> split-O(n) - no. of states
