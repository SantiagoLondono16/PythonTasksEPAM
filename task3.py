#Task 3 Create nuew words
def create_word(words):
    #An empty string is created to concatenate the selected letters
    new_word = ""
    #A 'for' loop is created to go through the list of 'words'
    for i in range(len(words)):
        #Each time there is a new iteration, the next letter of the new world is searched for.
        new_word += words[i][i]
    #Print the result
    print(new_word)

#Example
create_word(['yoda', 'best', 'has'])
