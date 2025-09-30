"""Word and character counter for a text file."""

def count_words_and_chars(filename):
    """Counts words and characters in a file."""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        words = content.split()
        return len(words), len(content)


if __name__ == '__main__':
    word_count, char_count = count_words_and_chars('sample.txt')
    print(f'Total words: {word_count}')
    print(f'Total characters: {char_count}')
