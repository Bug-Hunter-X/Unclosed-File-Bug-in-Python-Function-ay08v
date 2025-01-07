# Unclosed File Bug in Python Function

This repository demonstrates a common yet subtle error in Python: forgetting to close a file after it's been opened.  Leaving files open can lead to resource exhaustion and potential data corruption, especially in long-running processes or applications handling many files.

The `bug.py` file showcases the problematic code. The solution, found in `bugSolution.py`, correctly uses the `with` statement to ensure the file is automatically closed.