#Even Fibonacci numbers
def fibSeq(n):
    allFib= []
    evenFib =[]
    f1,f2 = 0,1
    if(n < 1):
        return
    for x in range(1,n):
        allFib.append(f2)
        next = f1 + f2
        f1 = f2
        f2 = next
    for even in allFib:
        if(even % 2 == 0 ):
            evenFib.append(even)

    print(allFib)
    print(evenFib)

fibSeq(10)






