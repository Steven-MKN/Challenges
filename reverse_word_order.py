#Write a program (using functions!) that asks the user for a long string containing multiple words. 
#Print back to the user the same string, except with the words in backwards order. 
#For example, say I type the string:
#
#  My name is Michele
#Then I would see the string:
#
#  Michele is name My
#shown back to me.

def reverse_sentence(sentence: str):
    aList = sentence.split(" ")
    aList.reverse()
    new_sentence = ""
    for w in aList:
        new_sentence += w
        new_sentence += ' '
    return new_sentence

user_sentence = input('Enter your sentence: ')
print('Your sentence in reverse is: ' + reverse_sentence(user_sentence))
