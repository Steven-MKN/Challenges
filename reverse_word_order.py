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