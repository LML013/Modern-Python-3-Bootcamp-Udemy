'''
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
'''


def remove_every_other(items):
    add_i = True
    answer = []
    for i in items:
        if add_i == True:
            answer.append(i)
            add_i = False
        else:
            add_i = True
    return answer
