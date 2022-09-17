# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:32:15 2020

@author: Slade
"""
#insert random class and variables
import random
nouns = ("man", "bubble", "iguana", "mcDonalds")
verbs = ("ran", "bounced", "cut", "raised")
articles = ("a", "the", "some")
prepositions = ("for", "near", "with")
adjectives = ("smelly", "red", "little", "big", "stupid")
conjunctions = ("and", "but", "because")
def main():
    print(sentence())#prints the sentence

    
def sentence():
    conOption = int(input("would you like 1 or 2 sentences?: ")) #if 2 print conjunction. If 1 don't
    if conOption == 2:
        return nounPhrase() + " " + verbPhrase() + " " + \
        random.choice(conjunctions) + " " + nounPhrase() + \
        " " + verbPhrase()
    elif conOption == 1:
        return nounPhrase() + " " + verbPhrase()
    else:
        print("That is an invalid number.")
def nounPhrase():
    adOption = random.randint(0, 2) #if 1 print adjective. if 2 don't
    if adOption == 1:
        return random.choice(articles) + " " + \
        random.choice(adjectives) + " " + random.choice(nouns)
    else:    
        return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    prepOption = random.randint(0, 2) #if 1 print prepostional phrase, if 2 don't
    if prepOption == 1:        
        return random.choice(verbs) + " " + nounPhrase() + " " + \
        prepositionalPhrase()
    else:
        return random.choice(verbs) + " " + nounPhrase()

def prepositionalPhrase(): 
    return random.choice(prepositions) + " " + nounPhrase()
    
    

    
main()#calls main to start program