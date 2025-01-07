def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # ... code to process file using f ...
            for line in f:
                # process each line
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
