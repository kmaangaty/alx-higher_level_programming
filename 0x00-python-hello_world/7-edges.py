#!/usr/bin/python3
word = "Holberton"
word_first_3 = f"First 3 letters: {word[:3]}"
word_last_2 = f"Last 2 letters: {word[7:]}"
middle_word = f"Middle word: {word[1:-1]}"
print_line = "\n"
to_print = f"{word_first_3}{print_line}{word_last_2}{print_line}{middle_word}"
print(to_print)
