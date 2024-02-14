from trie import PrefixTree


def main():
    stratagem_trie = PrefixTree()

    stratagem_trie.insert('⇨⇨⇧', 'Orbital Precision Strike')
    stratagem_trie.insert('⇨⇩⇦⇧⇧', 'Orbital Gatling Barrage')

    stratagem_trie.display()


if __name__ == '__main__':
    main()
