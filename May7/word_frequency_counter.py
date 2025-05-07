from collections import Counter

def count_word_frequency(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()
            words = text.split()
            word_count = Counter(words)
            for word, count in word_count.items():
                print(f"{word}: {count}")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print("An unexpected error occurred:", e)

# Example usage
file_name = input("Enter the filename to read: ")
count_word_frequency(file_name)
