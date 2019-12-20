#!/usr/bin/env python3
#
# Number Guessing Game!

def prompt(num):
    # Use this function to ask the user about a guess.
    # This function returns 'H', 'L', or 'C'.
    print(f"My guess: {num}")
    inp = ""
    while inp.upper() not in ['H', 'L', 'C']:
        inp = input(f"Is {num} too (H)igh, too (L)ow, or (C)orrect? ")
    return inp.upper()


def play(max):
    print(f"Think of a number from 1 to {max}.")
    num = input("When you're ready, press Enter.")
    while (prompt(num) != "C"):
	    num = input("press Enter.");
		
    print(f"Yes, it's {num}");
	
play(1000)
