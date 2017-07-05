def CompareList(list_1,y):
    for i in range(0, len(list_1)):
        if (list_1[i] != y[i]):
            return "The lists are not the same."
    return "The lists are the same"

print CompareList([1,2,5], [1,2,5,6,5])
print CompareList(['celery','carrots','bread','milk'], [1,2,5,6,5])
print CompareList(['celery','carrots','bread','milk'], ['celery','carrots','bread','cream'])
