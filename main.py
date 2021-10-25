from PyDictionary import PyDictionary
import sys
import os

def define(word=''):
    dict = PyDictionary()
    os.system('cls')
    

    if len(sys.argv) > 1:
        word = sys.argv[1]
        meaning = dict.meaning(word)
        os.system('cls')
        print(word.title() +':\n')
        print(meaning)
        print('\n')
        
        flag = 0
        while flag == 0:
            word = input('Enter a word to be defined: ')
            if word == '':
                flag = 1
                continue
            if len(word.strip()) > 0:
                os.system('cls')
                meaning = dict.meaning(word)
                
                print(word.title() + '\n')
                print(meaning)
                print('\n')
        
    if len(sys.argv) <= 1:
        if len(word) > 0:
            meaning = dict.meaning(word)
            return meaning
            
        if len(word) == 0:
            flag = 0
            word = input("Enter a word to be defined: ")
            if word == '':
                flag = 1
            while flag == 0:
                meaning = dict.meaning(word)
                print(word.title() + ':\n')
                print(meaning)
                print('\n')
                
                word = input('Enter a word to be define: ')
                if word == '':
                    flag = 1
                    continue
        
if __name__ == "__main__":
    define()
