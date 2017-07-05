def FindChar(a, b):
    new = []
    for count in range(0, len(a)):
        if b in a[count]:
            new.append(a[count])
    print new
FindChar(['hello','blue','world','my','name','is','Ausar'], 'o')
