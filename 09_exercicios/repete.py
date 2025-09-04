#!/usr/bin/env python3 
"""
Repeat vowels

Write a program that asks the user to enter one or more words and prints
each of the words with their vowels duplicated.

ex:
python repeat_vowel.py
‘Enter a word (or press Enter to exit):’ Python
‘Enter a word (or press Enter to exit):’ Matheus
‘Enter a word (or press Enter to exit):’ <Enter>
Pythoon
Maatheeuus
"""
vowel = ["a","e","i","o","u"]

while True:
    word_list = []
    word = input("Enter a word (or press Enter to exit): ")
    if not word:
        break
    for letter in word:
        if letter in vowel:
            word_list.append(letter *2)
        else:
            word_list.append(letter)
    print("".join(word_list))
