#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#----------------------------------------------------------------------
#  eliza.py
#
#  a cheezy little Eliza knock-off by Joe Strout
#  with some updates by Jeff Epler
#  hacked into a module and updated by Jez Higgins
#  Minor improvements by changux
#----------------------------------------------------------------------

import re
import random
import time

# Reflections for transforming user input
reflections = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
}

# Classic ELIZA response patterns
psychobabble = [
    [r'I NEED (.*)',
     ["WHY DO YOU NEED {0} ?",
      "WOULD IT REALLY HELP YOU TO GET {0} ?",
      "ARE YOU SURE YOU NEED {0} ?"]],

    [r'YOU ARE (.*)',
     ["WHAT MAKES YOU THINK I AM {0} ?",
      "DO YOU ENJOY THINKING I AM {0} ?",
      "PERHAPS YOU WOULD PREFER IF I WERE NOT {0} ?"]],

    [r'CAN YOU ([^\?]*)\??',
     ["WHAT MAKES YOU THINK I CAN {0} ?",
      "IF I COULD {0}, THEN WHAT ?",
      "WHY DO YOU ASK IF I CAN {0} ?"]],

    [r'WHAT (.*)',
     ["WHY DO YOU ASK ?",
      "DOES THAT QUESTION INTEREST YOU ?",
      "WHAT IS IT THAT YOU REALLY WANT TO KNOW ?"]],

    [r'(.*)',
     ["PLEASE TELL ME MORE.",
      "LET'S CHANGE FOCUS A BIT... TELL ME ABOUT YOUR FAMILY.",
      "CAN YOU ELABORATE ON THAT ?",
      "WHY DO YOU SAY THAT ?"]]
]

def reflect(fragment):
    """Reflects the user's input using predefined reflections."""
    words = fragment.lower().split()
    return ' '.join([reflections.get(word, word) for word in words])

def eliza_response(statement):
    """Generates a response based on user input."""
    statement = statement.upper()
    for pattern, responses in psychobabble:
        match = re.match(pattern, statement)
        if match:
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])
    return "I SEE. PLEASE CONTINUE."

def chat(use_input=True, test_inputs=None):
    """Main ELIZA chat loop. Uses input() if interactive, else uses test_inputs."""
    print("\nWelcome to")
    print(" EEEEEEE  LL      IIII  ZZZZZZ  AAAAAA  ")
    print(" EE       LL       II   ZZ     AA    AA  ")
    print(" EEEEEEE  LL       II    ZZ    AAAAAAAA  ")
    print(" EE       LL       II     ZZ   AA    AA  ")
    print(" EEEEEEE  LLLLLLL IIII ZZZZZZ  AA    AA  ")
    print("\nEliza is a mock Rogerian psychotherapist.")
    print("The original program was described by Joseph Weizenbaum in 1966.")
    print("This implementation is inspired by the original.")
    print("\nELIZA: HELLO. I AM ELIZA. HOW CAN I HELP YOU TODAY?")
    
    if use_input:
        while True:
            try:
                user_input = input("YOU: ")
            except EOFError:
                break
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("ELIZA: GOODBYE. TAKE CARE.")
                break
            time.sleep(1)  # Simulate a slight delay
            print(f"ELIZA: {eliza_response(user_input)}")
    else:
        responses = []
        for user_input in test_inputs or []:
            responses.append(f"YOU: {user_input}")
            if user_input.lower() in ['exit', 'quit', 'bye']:
                responses.append("ELIZA: GOODBYE. TAKE CARE.")
                break
            time.sleep(0.5)
            responses.append(f"ELIZA: {eliza_response(user_input)}")
        return "\n".join(responses)

if __name__ == "__main__":
    chat()
