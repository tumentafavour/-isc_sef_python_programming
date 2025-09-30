# ISC SEF Python Programming

This repository contains solutions to Python programming exercises focused on **file handling**

## Folder Structure

* `1x_python_programming_file_handling/`

  * `README.md`: Explains the approach for each exercise.
  * `0xlog_analyzer.py`: Counts occurrences of `[INFO]`, `[ERROR]`, and `[WARNING]` in a log file.
  * `1xword_counter.py`: Counts total words and characters in a text file.
  * `2xappend_to_file.py`: Appends new text to an existing file and saves the result in a new file.
  * `logs.txt`: Input file for the log analyzer.
  * `sample.txt`: Input file for word counter and append exercises.

## Requirements

* Python 3.7+
* Pylint (for linting)

## Linting

Each script has been checked with `pylint` and scores **10.0/10.0**.

To run the linting :

```bash
pylint 0xlog_analyzer.py
pylint 1xword_counter.py
pylint 2xappend_to_file.py
```
