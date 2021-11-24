#Fibonocci calculator app


print("\n Welcome to Bosco's fibonacci calculator app\n")
def fibonacci(n):
    n = int(n)

    def fibon(a,b,n,result):
        c = a+b
        result.append(c)
        if c < n:
            fibon(b,c,n,result)
        return result

    return fibon(0,1,n,[])

print(fibonacci(input("Enter the number of of fibonacci calculator length: ")))

