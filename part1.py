if __name__ == '__main__':
    pi = 0
    n = 4
    d = 1
    n_terms  = int(input("Enter how many terms to calculate: "))
    for i in range(1,n_terms):
        a = 2*(i%2)-1
        pi = pi + (a*n/d)
        d = d + 2
    print(pi)
    
                   