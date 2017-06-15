def find_missing(a, b):
#checks if 'a' and 'b' are empty lists
    if a == [] and b == []:
        return 0
#checks if 'a' is equal to 'b'
    elif a == b:
        return 0
#checks the missing number, i.e the number in 'b' and not 'a'
    else:
        for i in b:
            if i not in a:
                return i
