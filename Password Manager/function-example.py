'''
Function Example
'''

# add two numbers together
def combine_words(word1, word2):
    
    concatenated = word1 + word2  # concatenate the two words provided to the function

    return concatenated # return the concatenated word

first_word = input("What's the first word? ")      # get first word from user
second_word = input("What's the second word? ")    # get second word from user

result = combine_words(first_word, second_word)     # call function and provide user inputs

print("Result:", result)  # display results