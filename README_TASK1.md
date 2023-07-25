# Complexity
##Operation 1: Store Dictionary
Time Complexity: O(L * N) where L is the average length of a word in the dictionary. And, N is the total number of words in the dictionary.
Space Complexity: O(L * N)
Each character in the words is stored in a TrieNode in the data structure.

##Operation 2: Find Nearest Words
Time Complexity: O(L * D) where L is the average length of a word. And, D is the depth of the trie traversal (2 in this case for two words before and after the input word).
Space Complexity: O(L * D)
The nearest words and current_word strings are created during the traversal, and each character of the words is stored in the nearest_words list.

##Operation 3: Add Word to Dictionary

Time Complexity: O(L) where L is the length of the word being added.
Space Complexity: O(L)
The word characters are stored in the TrieNode in the data structure.

## Store this dictionary in a suitable data structure.
All operations, including insert, search, and delete, can be supported by Trie in O(n) time, where n is the length of the word to be processed. The ability to print all words in alphabetical order, which is not achievable with hashing, is another benefit of Trie. Trie's drawback is that it takes up a lot of space. Ternary Search Tree can be preferable if space is an issue.

## Operation 2 (Note)
I managed to do DFS. So, it only gets the nearest 4 words after. 
