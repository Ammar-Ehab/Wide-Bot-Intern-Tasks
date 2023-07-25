class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class SpellChecker:
    def __init__(self):
        self.root = TrieNode()

    def store_dictionary(self, words):
        for word in words:
            self.add_word_to_trie(word)

    def add_word_to_trie(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def find_nearest_words(self, word):
        def dfs_trie(node, current_word, nearest_words, depth):
            if node.is_end_of_word and current_word != word:
                nearest_words.append(current_word)
            if depth == 0:
                return
            for char, child_node in node.children.items():
                dfs_trie(child_node, current_word + char, nearest_words, depth - 1)

        nearest_words = []
        node = self.root
        for char in word:
            if char not in node.children:
                return nearest_words
            node = node.children[char]

        # Include two words before and after the input word
        for char in node.children:
            dfs_trie(node.children[char], word + char, nearest_words, 2)
        
        nearest_words.sort()  # Sort the nearest words lexicographically
        return nearest_words[:4]

    def add_word_to_dictionary(self, word):
        self.add_word_to_trie(word)


def read_dictionary_from_file(file_path):
    with open(file_path, "r", encoding="latin-1") as file:
        return [line.strip() for line in file.readlines()]


if __name__ == "__main__":
    file_path = r"E:\widebot\input.txt.txt"
    dictionary = read_dictionary_from_file(file_path)

    spell_checker = SpellChecker()
    spell_checker.store_dictionary(dictionary)

    while True:
        print("\n=== Spell Checker ===")
        print("1. Check spelling and find nearest words")
        print("2. Add word to the dictionary")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            word_to_check = input("Enter the word to check: ")
            nearest_words = spell_checker.find_nearest_words(word_to_check)
            if not nearest_words:
                print("The word is not in the dictionay.")
            else:
                print("Nearest words:", nearest_words)
        elif choice == "2":
            new_word = input("Enter the word to add to the dictionary: ")
            spell_checker.add_word_to_dictionary(new_word)
            print("Word added to the dictionary.")
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
