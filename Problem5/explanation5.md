# Code Design:
1. TrieNode:
has two instance variable is_word, children(dictionary)
Insert function:
Simple TrieNode at children[char]

Suffixes function:

iterate over children and the suffixes operation with the children of each child

2. Trie:
Insert function:
It iterates over each char in word, creating a new TrieNode, assigning as node for next iteration
Loop completed, set node.is_word to True

Find function:
We need to iterate over each char in word, get char in node.children, assign children[char] as node for next iteration
If we not prefix is there it returns None
# Time Complexity:
insert and find:
> Both takes O(n), cause 1 iteration per char
suffixes: O(n * m): iterate over children + the suffixes operation with the children of each child
# Space Complexity:
> insert: O(n), the auxiliary space used by the algorithms assigning the node and keep it update while the process is executed
suffixes: O(n * m), results variable will occupy n + m, plus the n * m of the recursive stack
