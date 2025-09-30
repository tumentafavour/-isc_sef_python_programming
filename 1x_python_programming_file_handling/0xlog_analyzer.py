"""Log analyzer script to count log levels in a file."""

def count_log_levels(filename):
    """Counts [INFO], [ERROR], and [WARNING] in a log file."""
    counts = {'INFO': 0, 'ERROR': 0, 'WARNING': 0}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            for level in counts:
                if f'[{level}]' in line:
                    counts[level] += 1
    return counts


if __name__ == '__main__':
    log_counts = count_log_levels('logs.txt')
    print(f'Output: {log_counts}')
