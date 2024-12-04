#Task 2 Calculate total cost
def get_total(dictionary, keys, tax):
    #A counter is created to accumulate the costs of each item
    cost = 0
    #A 'for' loop is created to go through the list of 'keys' items
    for i in keys:
        #If the item exist in the dictionary, get the cost
        if i in dictionary:
            cost += dictionary.get(i)
        else:
            #If the item doesnt exist in the dictionary, skip the item
            print("Can't find a entry for {i}")
    #Add the tax to the final cost
    cost += cost * tax
    #Print the result
    print(cost)

#Example
costs = {'socks':5, 'shoes': 60, 'sweater':30}
get_total(costs, ['socks', 'shoes'], 0.09)
