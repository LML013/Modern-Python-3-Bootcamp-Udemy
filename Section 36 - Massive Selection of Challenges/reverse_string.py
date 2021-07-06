'''
reverse_string('awesome') # 'emosewa'
reverse_string('Colt') # 'tloC'
reverse_string('Elie') # 'eilE'
'''

# add whatever parameters you deem necessary - good luck!


def reverse_string(word):
    # implement your function here
    arr = []
    drow = ""
    for char in word:
        arr.append(char)
    for char in reversed(arr):
        drow += char
    print(drow)
    pass
    return drow
