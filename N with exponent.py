def check_Power(N,k):
    if N <= 0 or k <=0:
        print ("not a valid input")
    else:
        for i in range (1,20):
            s = k**i
            if s == N :
                print(" True ")
                print (k, "power ", i , "is", N)
                break
            elif s> N:
                print ("false")
                break
check_Power(0, 16)
check_Power(1,1)
