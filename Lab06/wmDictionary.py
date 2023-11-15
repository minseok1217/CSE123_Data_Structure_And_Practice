from bstTree import *


class Record:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __eq__(self, other): return self.word == other.word

    def __ne__(self, other): return self.word != other.word

    def __lt__(self, other): return self.word < other.word

    def __gt__(self, other): return self.word > other.word

    def __str__(self):
        return "{}:{}".format(str(self.word), str(self.meaning))


class Dictionary(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def searchByWord(self, word):
        return self.search(self.root, Record(word, None))

    def searchByMeaning(self, meaning):
        return self.searchMeaning(self.root, meaning)

    def searchMeaning(self, n, meaning):
        ans = []
        if n is not None:
            ans += self.searchMeaning(n.left, meaning)
            if n.data.meaning == meaning:
                ans.append(n.data)
            ans += self.searchMeaning(n.right, meaning)
        return ans

    def runDict(self):
        wdict = Dictionary()
        while True:
            command = input("i-insert, d-delete, p-print, s-search, q-quit -> ")

            if command == 'i':
                word = input(" > word: ").strip()
                meaning = input(" > meaning: ").strip()
                wdict.insert_bst(Record(word, meaning))

            elif command == 'd':
                word = input(" Inter word: ")
                wdict.delete_bst(Record(word, None))

            elif command == 'p':
                print(" Dictionary : ")
                wdict.inOrder(wdict.root)
                print('\n')

            elif command == 's':
                word = input(" > word: ")
                n = wdict.search(wdict.root, Record(word, None))
                if n is not None:
                    print('Record is -->> ', n)
                else:
                    print('The : ' + word + ' is not found')

            elif command == 'q':
                return