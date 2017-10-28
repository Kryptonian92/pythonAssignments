a,b,c = 1,2,3

def change_values(a,c):
    global b
    print(a,b,c) #what gets printed?
    a,b,c = 0,0,0

def main():
    global a
    a=-1
    change_values(c,a)
    print(a,b,c) #what gets printed?

main()

