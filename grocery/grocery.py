def main():
    groceries = []
    get_groceries(groceries)

    #iterate through the grocery list
    for each in range(len(groceries)):
        #if list is not empty, procced.
        if len(groceries) >= 1:
            number = 0
            each = groceries[0]
        #if the list is empty, break. All done.
        else:
            break
        #iterate through the list: if any of the words match, count the total and delete the words
        while each in groceries:
            number += 1
            groceries.remove(each)
            #if there's no more matching words, print the total next to the word
            if each not in groceries:
                print(number, each)

def get_groceries(groceries):
    try:
        while True:
            item = input().upper()
            groceries.append(item)
    except EOFError:
        return [groceries]





main()
