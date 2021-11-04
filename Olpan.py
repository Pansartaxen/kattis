def find_all_indexes(string, subString):
    end = False
    indexString = ''
    start = 0
    while end == False:
        try:
            index = string.index(subString, start)
            start = index + 1
            indexString = indexString + str(index) + ','
        except:
            end = True
    return(f"'{indexString[0:-1]}'")

print(find_all_indexes("There's unlimited juice? This party is gonna be off the hook. Oh, I'm sorry, I forgot... your wife is dead!.",'.'))