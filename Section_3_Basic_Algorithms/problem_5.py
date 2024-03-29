#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.insert(ch)
            node = node.children[ch]
        node.is_end = True
            

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node if node.is_end else None


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[21]:


class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_end = False
        self.children = {}
    
    def insert(self, ch):
        ## Add a child node in this Trie
        self.children[ch] = TrieNode()
    '''    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        def rec(node, string, strings):
            if node.is_end:
                strings.append("".join(string))
            for ch in node.children:
                string.append(ch)
                rec(node.children[ch], string, strings)
                string.pop()
        strings = []
        rec(self, [], strings)
        return strings
    '''

        # Recursive function that collects the suffix for all complete words
    # below this point
    def suffixes(self, suffix=''):

        suffixes = []

        # Traverse through the children
        for char, node in self.children.items():

            # If the node specifies the end of a word
            if node.is_end:
                suffixes.append(suffix + char)

            # If the node contains more children
            # Add those children to the current suffixes recursively
            if node.children:
                suffixes.extend(node.suffixes(suffix + char))

        return suffixes


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[22]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# In[23]:


'''
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');
'''

# In[ ]:




