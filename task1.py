#Task 1 create a class "Dictionary".
class Dictionary():
    #Init method is created to add atributes to the class.
    def __init__(self):
        #The "entries" attribute ir created which is an empty Python dictionary.
        self.entries = {}
    #The "newentry" function is created for the class, this function is used to create new entries for the dictionary.
    def newentry(self, key, value):
        #If the entry already exists in the dictionary, we do not add anything.
        if key in self.entries:
            print(f"The key '{key}' already exist. Use other key")
        #If the entry does not exist, we add to the dictionary the key and its value
        else:
            self.entries[key] = value
            print(f"Key added: '{key}': '{value}'")
    #The"look" function is created for the class, this function is used to search the value of the key
    def look(self, key):
        return self.entries.get(key, f"Can't find entry for '{key}'.")

#Example
d = Dictionary()
d.newentry('Apple', 'A fruit that grows on trees')
print(d.look('Apple'))
print(d.look('Banana'))