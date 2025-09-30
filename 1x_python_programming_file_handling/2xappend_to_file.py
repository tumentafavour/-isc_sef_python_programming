"""Appends text to an existing file and saves to a new file."""

def append_to_file(original_file, new_file, new_text):
    """Appends new_text to original_file and writes to new_file."""
    with open(original_file, 'r', encoding='utf-8') as file:
        content = file.read()

    content += f'\n{new_text}\n'

    with open(new_file, 'w', encoding='utf-8') as file:
        file.write(content)


if __name__ == '__main__':
    append_to_file(
        'sample.txt',
        'sample0.txt',
        'Practice writing and appending to files.'
    )
    print("Text appended and saved as sample0.txt.")
