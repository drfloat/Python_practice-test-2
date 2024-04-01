def q3(n):
    posty=[]
    negty=[]
    for i in n:
        if i-abs(i) ==0:
            posty.append(i)
        else:
            negty.append(i)
    postysq = [sq ** 2 for sq in posty]
    negtyc3 = [c3 **3 for c3 in negty]
    print(f'Square of Positive Integers: {postysq}')
    print(f'Cube of Negative Integers: {negtyc3}')
    ab=[abs(non) for non in n ]
    print(f'Absoulte Values of All Integers: {ab}')
    ev10=[ev for ev in n if ev>10 and ev%2==0]
    print(f'Even Numbers Greater than 10: {ev10}')



numbers = [5,-8,12,-3,17,0,-10,6]
q3(numbers)
i=9
