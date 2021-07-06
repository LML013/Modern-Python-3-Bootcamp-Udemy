'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''


def list_check(items):
    answer = True
    for item in items:
        if type(item) != list:
            answer = False
    pass
    return answer
