#Shiran Guo Homework 8
import math
import pandas as pd
import fractions
import decimal

# '√' is the square root symbol
outputFileFloderName = '' # Put your file path here

#Define the function to calculate the key values for further calculation
def coordnateCalculator(A,B,C,D,E,R):
    if D != 0:
        NewA = (math.pow(C,2)+math.pow(D,2))/math.pow(D,2)
        NewB = 2*(C*E-A*math.pow(D,2)+B*C*D)/math.pow(D,2)
        NewC = math.pow(A,2)+math.pow(B,2)+(math.pow(E,2)+2*B*D*E)/math.pow(D,2)-math.pow(R,2)
        Delta = math.pow(NewB,2)-4*NewA*NewC
    else:
        NewA = 1
        NewB = -2*B
        NewC = ((math.pow(E,2)+A*C*E))/math.pow(C,2)+math.pow(A,2)+math.pow(B,2)-math.pow(R,2)     
        Delta = math.pow(NewB,2)-4*NewA*NewC   
    return NewA,NewB,Delta

#Define the function to simplify number under root sign
def simplifyRootSign(Number):
    RangeNumber = int(math.pow(Number,0.5)+1)
    NumberList = []
    for i in range(1,RangeNumber):
        NumberList.append(i)
    NumberList.reverse()
    for n in NumberList:
        TestNumber = Number / math.pow(n,2)
        if TestNumber == int(TestNumber):
            TestNumber = int(TestNumber)
            break
        else:
            continue
    return n,TestNumber

#Define the function to simplify fraction
def simplifyFraction(Denominator,NumeratorA=0,NumeratorB=0):
    Denominator = fractions.Fraction(decimal.Decimal(str(Denominator)))
    NumeratorA = fractions.Fraction(decimal.Decimal(str(NumeratorA)))
    NumeratorB = fractions.Fraction(decimal.Decimal(str(NumeratorB)))
    FirstNumerator, FirstDenominator, SecondNumerator, SecondDenominator = NumeratorA, Denominator, NumeratorB, Denominator
    FirstNumber = NumeratorA/Denominator
    FirstNumerator = FirstNumber.numerator
    FirstDenominator = FirstNumber.denominator
    SecondNumber = NumeratorB/Denominator
    SecondNumerator = SecondNumber.numerator
    SecondDenominator = SecondNumber.denominator
    return FirstNumerator,FirstDenominator,SecondNumerator,SecondDenominator

#Prepare the output dictionary and lists for pandas
outputDic = {}
circleList = []
straightLineList = []
dot1List = []
dot2List = []
resultList = []
    
#Creat a loop that allows user to keep calculating
answerList = ['n','N']
answer = 'yes'
while answer not in answerList:
    
    #Prevent input errors from the user
    identifier = 'n'
    while identifier != 'y':
        #Get the circle equation
        print('Please enter the values for the circle equation (X-a)^2+(Y-b)^2=r^2')
        a = input('a = ?\n>>')
        b = input('b = ?\n>>')
        r = input('r = ?\n>>')
        
        #Get the straight line equation
        print('Please enter the values for the straight line equation cX+dY+e=0')
        c = input('c = ?\n>>')
        d = input('d = ?\n>>')
        e = input('e = ?\n>>')
                    
        #Define the equations for circle and straight line
        circle = '(X-'+a+')^2+(Y-'+b+')^2='+r+'^2'
        straightLine = c+'X+'+d+'Y+'+e+'=0'
        
        try:
            #Prepare the variables for calculation
            a = float(a)#Possible error happening line starts here
            b = float(b)
            c = float(c)
            d = float(d)
            e = float(e)
            r = float(r)
            #Calculate and assign the key values for further calculation
            coordnateCalculator(a,b,c,d,e,r)#Possible error happening line ends here
            identifier = 'y'
        except:
            print('Oops, something went wrong, please try again.')
        
    #Get the key values to calculate
    newA = coordnateCalculator(a,b,c,d,e,r)[0]
    newB = coordnateCalculator(a,b,c,d,e,r)[1]
    delta = coordnateCalculator(a,b,c,d,e,r)[2]
    
    #Distinguish the number of intersection point(s)
    if delta < 0 :
        #Define output
        dot1 = 'none'
        dot2 = 'none'
        result = 'There is no intersection point between '+circle+' and '+ straightLine
    elif delta == 0:
        #Calculate the coordnate
        if d == 0:
            #y = -newB/2*newA
            numerator = simplifyFraction(2*newA,newB)[0]
            denominator = simplifyFraction(2*newA,newB)[1]
            if denominator != 1:
                y = str(-numerator)+'/'+str(denominator)
            elif numerator == 0:
                y = str(0)
            else:
                y = str(-numerator)
            #x=-e/c
            numerator = simplifyFraction(c,e)[0]
            denominator = simplifyFraction(c,e)[1]
            if denominator != 1:
                x = str(-numerator)+'/'+str(denominator)
            elif numerator == 0:
                x = str(0)
            else:
                x = str(-numerator)
        elif c == 0:
            #x = -newB/2*newA
            numerator = simplifyFraction(2*newA,newB)[0]
            denominator = simplifyFraction(2*newA,newB)[1]
            if denominator != 1:
                x = str(-numerator)+'/'+str(denominator)
            elif numerator == 0:
                x = str(0)
            else:
                x = str(-numerator)
            #y = -e/d
            numerator = simplifyFraction(d,e)[0]
            denominator = simplifyFraction(d,e)[1]
            if denominator != 1:
                y = str(-numerator)+'/'+str(denominator)
            elif numerator == 0:
                y = str(0)
            else:
                y = str(-numerator)
        else:
            #x = -newB/2*newA
            numerator = simplifyFraction(2*newA,newB)[0]
            denominator = simplifyFraction(2*newA,newB)[1]
            if denominator != 1:
                x = str(-numerator)+'/'+str(denominator)
            elif numerator == 0:
                x = str(0)
            else:
                x = str(-numerator)
            #y = -(c*x-e)/d
            numeratorA = simplifyFraction(d,c*numerator/denominator,e)[0]
            denominatorA = simplifyFraction(d,c*numerator/denominator,e)[1]
            numeratorB = simplifyFraction(d,c*numerator/denominator,e)[2]
            denominatorB = simplifyFraction(d,c*numerator/denominator,e)[3]
            if numeratorA == 0:
                if numeratorB == 0:
                    y = str(0)
                elif denominatorB == 1:
                    y = str(numeratorB)
                else:
                    y = str(numeratorB)+'/'+str(denominatorB)
            elif denominatorA == 1:
                if numeratorB == 0:
                    y = str(-numeratorA)
                elif denominatorB == 1:
                    y = str(-numeratorA+numeratorB)
                else:
                    y = str(-numeratorA)+'-'+str(numeratorB)+'/'+str(denominatorB)
            else:
                if numeratorB == 0:
                    y = str(-numeratorA)+'/'+str(denominatorA)
                elif denominatorB == 1:
                    y = str(-numeratorA)+'/'+str(denominatorA)+'-'+str(numeratorB)
                else:
                    y = str(-numeratorA)+'/'+str(denominatorA)+'-'+str(numeratorB)+'/'+str(denominatorB)
        #define outputline
        dot1 = [x,y]
        dot2 = 'none'
        coordnateLine = 'A'+str(dot1)
        result = 'There is only one intersection point between '+circle+' and '+ straightLine+' . The coordnate of it is:\n'+coordnateLine
    else:
        #Calculate the coordnate
        if math.pow(delta,.5) == int(math.pow(delta,.5)):
            newDelta = math.pow(delta,.5)
            if d == 0:
                #y1 = (-newB+math.pow(delta,.5))/(2*newA)
                #y2 = (-newB-math.pow(delta,.5))/(2*newA)
                numeratorA = simplifyFraction(2*newA,newB,newDelta)[0]
                denominatorA = simplifyFraction(2*newA,newB,newDelta)[1]
                numeratorB = simplifyFraction(2*newA,newB,newDelta)[2]
                denominatorB = simplifyFraction(2*newA,newB,newDelta)[3]
                if numeratorA == 0:
                    if denominatorB == 1:
                        y1 = str(numeratorB)
                        y2 = str(-numeratorB)
                    else:
                        y1 = str(numeratorB)+'/'+str(denominatorB)
                        y2 = str(-numeratorB)+'/'+str(denominatorB)
                elif denominatorA == 1:
                    if denominatorB == 1:
                        y1 = str(-numeratorA+numeratorB)
                        y2 = str(-numeratorA-numeratorB)
                    else:
                        y1 = str(-numeratorA)+'+'+str(numeratorB)+'/'+str(denominatorB)
                        y2 = str(-numeratorA)+'-'+str(numeratorB)+'/'+str(denominatorB)
                else:
                    if denominatorB == 1:
                        y1 = str(-numeratorA)+'/'+str(denominatorA)+'+'+str(numeratorB)
                        y2 = str(-numeratorA)+'/'+str(denominatorA)+'-'+str(numeratorB)
                    else:
                        y1 = str(-numeratorA)+'/'+str(denominatorA)+'+'+str(numeratorB)+'/'+str(denominatorB)
                        y2 = str(-numeratorA)+'/'+str(denominatorA)+'-'+str(numeratorB)+'/'+str(denominatorB)
                #x1 = -(e/c)
                #x2 = -(e/c)
                numerator = simplifyFraction(c,e)[0]
                denominator = simplifyFraction(c,e)[1]
                if denominator != 1:
                    x1 = str(-numerator)+'/'+str(denominator)
                    x2 = str(-numerator)+'/'+str(denominator)
                elif numerator == 0:
                    x1 = str(0)
                    x2 = str(0)
                else:
                    x1 = str(-numerator)
                    x2 = str(-numerator)
            elif c == 0:
                #x1 = (-newB+math.pow(delta,.5))/(2*newA)
                #x2 = (-newB-math.pow(delta,.5))/(2*newA)
                numeratorA = simplifyFraction(2*newA,newB,newDelta)[0]
                denominatorA = simplifyFraction(2*newA,newB,newDelta)[1]
                numeratorB = simplifyFraction(2*newA,newB,newDelta)[2]
                denominatorB = simplifyFraction(2*newA,newB,newDelta)[3]
                if numeratorA == 0:
                    if denominatorB == 1:
                        x1 = str(numeratorB)
                        x2 = str(-numeratorB)
                    else:
                        x1 = str(numeratorB)+'/'+str(denominatorB)
                        x2 = str(-numeratorB)+'/'+str(denominatorB)
                elif denominatorA == 1:
                    if denominatorB == 1:
                        x1 = str(-numeratorA+numeratorB)
                        x2 = str(-numeratorA-numeratorB)
                    else:
                        x1 = str(-numeratorA)+'+'+str(numeratorB)+'/'+str(denominatorB)
                        x2 = str(-numeratorA)+'-'+str(numeratorB)+'/'+str(denominatorB)
                else:
                    if denominatorB == 1:
                        x1 = str(-numeratorA)+'/'+str(denominatorA)+'+'+str(numeratorB)
                        x2 = str(-numeratorA)+'/'+str(denominatorA)+'-'+str(numeratorB)
                    else:
                        x1 = str(-numeratorA)+'/'+str(denominatorA)+'+'+str(numeratorB)+'/'+str(denominatorB)
                        x2 = str(-numeratorA)+'/'+str(denominatorA)+'-'+str(numeratorB)+'/'+str(denominatorB)
                #y1 = -(e/d)
                #y2 = -(e/d)
                numerator = simplifyFraction(d,e)[0]
                denominator = simplifyFraction(d,e)[1]
                if denominator != 1:
                    y1 = str(-numerator)+'/'+str(denominator)
                    y2 = str(-numerator)+'/'+str(denominator)
                elif numerator == 0:
                    y1 = str(0)
                    y2 = str(0)
                else:
                    y1 = str(-numerator)
                    y2 = str(-numerator)
            else:
                #x1 = (-newB+math.pow(delta,.5))/(2*newA)
                #x2 = (-newB-math.pow(delta,.5))/(2*newA)
                numeratorA = simplifyFraction(2*newA,newB,newDelta)[0]
                denominatorA = simplifyFraction(2*newA,newB,newDelta)[1]
                numeratorB = simplifyFraction(2*newA,newB,newDelta)[2]
                denominatorB = simplifyFraction(2*newA,newB,newDelta)[3]
                if numeratorA == 0:
                    if denominatorB == 1:
                        x1 = str(numeratorB)
                        x2 = str(-numeratorB)
                    else:
                        x1 = str(numeratorB)+'/'+str(denominatorB)
                        x2 = str(-numeratorB)+'/'+str(denominatorB)
                elif denominatorA == 1:
                    if denominatorB == 1:
                        x1 = str(-numeratorA+numeratorB)
                        x2 = str(-numeratorA-numeratorB)
                    else:
                        x1 = str(-numeratorA)+'+'+str(numeratorB)+'/'+str(denominatorB)
                        x2 = str(-numeratorA)+'-'+str(numeratorB)+'/'+str(denominatorB)
                else:
                    if denominatorB == 1:
                        x1 = str(-numeratorA)+'/'+str(denominatorA)+'+'+str(numeratorB)
                        x2 = str(-numeratorA)+'/'+str(denominatorA)+'-'+str(numeratorB)
                    else:
                        x1 = str(-numeratorA)+'/'+str(denominatorA)+'+'+str(numeratorB)+'/'+str(denominatorB)
                        x2 = str(-numeratorA)+'/'+str(denominatorA)+'-'+str(numeratorB)+'/'+str(denominatorB)
                #y1 = -(c*x1-e)/d
                numeratorA1 = simplifyFraction(d*denominatorA*denominatorB,e*denominatorA*denominatorB,c*(numeratorB*denominatorA+numeratorA*denominatorB))[0]
                denominatorA1 = simplifyFraction(d*denominatorA*denominatorB,e*denominatorA*denominatorB,c*(numeratorB*denominatorA+numeratorA*denominatorB))[1]
                numeratorB1 = simplifyFraction(d*denominatorA*denominatorB,e*denominatorA*denominatorB,c*(numeratorB*denominatorA+numeratorA*denominatorB))[2]
                denominatorB1 = simplifyFraction(d*denominatorA*denominatorB,e*denominatorA*denominatorB,c*(numeratorB*denominatorA+numeratorA*denominatorB))[3]
                if numeratorA1 == 0:
                    if numeratorB1 == 0:
                        y1 = str(0)
                    elif denominatorB1 == 1:
                        y1 = str(-numeratorB1)
                    else:
                        y1 = str(-numeratorB1)+'/'+str(denominatorB1)
                elif denominatorA1 == 1:
                    if numeratorB1 == 0:
                        y1 = str(-numeratorA1)
                    elif denominatorB1 == 1:
                        y1 = str(-numeratorA1+numeratorB1)
                    else:
                        y1 = str(-numeratorA1)+'-'+str(numeratorB1)+'/'+str(denominatorB1)
                else:
                    if numeratorB1 == 0:
                        y1 = str(-numeratorA1)+'/'+str(denominatorA1)
                    elif denominatorB == 1:
                        y1 = str(-numeratorA1)+'/'+str(denominatorA1)+'-'+str(numeratorB1)
                    else:
                        y1 = str(-numeratorA1)+'/'+str(denominatorA1)+'-'+str(numeratorB1)+'/'+str(denominatorB1)
                #y2 = -(c*x2-e)/d
                numeratorA2 = simplifyFraction(d*denominatorA*denominatorB,c*(numeratorB*denominatorA-numeratorA*denominatorB),e*denominatorA*denominatorB)[0]
                denominatorA2 = simplifyFraction(d*denominatorA*denominatorB,c*(numeratorB*denominatorA-numeratorA*denominatorB),e*denominatorA*denominatorB)[1]
                numeratorB2 = simplifyFraction(d*denominatorA*denominatorB,c*(numeratorB*denominatorA-numeratorA*denominatorB),e*denominatorA*denominatorB)[2]
                denominatorB2 = simplifyFraction(d*denominatorA*denominatorB,c*(numeratorB*denominatorA-numeratorA*denominatorB),e*denominatorA*denominatorB)[3]
                if numeratorA2 == 0:
                    if numeratorB2 == 0:
                        y2 = str(0)
                    elif denominatorB2 == 1:
                        y2 = str(numeratorB2)
                    else:
                        y2 = str(numeratorB2)+'/'+str(denominatorB2)
                elif denominatorA2 == 1:
                    if numeratorB2 == 0:
                        y2 = str(numeratorA2)
                    elif denominatorB2 == 1:
                        y2 = str(numeratorA2+numeratorB2)
                    else:
                        y2 = str(numeratorA2)+'-'+str(numeratorB2)+'/'+str(denominatorB2)
                else:
                    if numeratorB2 == 0:
                        y2 = str(numeratorA2)+'/'+str(denominatorA2)
                    elif denominatorB2 == 1:
                        y2 = str(numeratorA2)+'/'+str(denominatorA2)+'-'+str(numeratorB2)
                    else:
                        y2 = str(numeratorA2)+'/'+str(denominatorA2)+'-'+str(numeratorB2)+'/'+str(denominatorB2)
        else:
            newDelta = simplifyRootSign(int(delta))[0]
            extraNumber = '√'+str(simplifyRootSign(int(delta))[1])
            if d == 0:
                #y1 = (-newB+math.pow(delta,.5))/(2*newA)
                #y2 = (-newB-math.pow(delta,.5))/(2*newA)
                numeratorA = simplifyFraction(2*newA,newB,newDelta)[0]
                denominatorA = simplifyFraction(2*newA,newB,newDelta)[1]
                numeratorB = simplifyFraction(2*newA,newB,newDelta)[2]
                denominatorB = simplifyFraction(2*newA,newB,newDelta)[3]
                if numeratorA == 0:
                    if denominatorB == 1:
                        y1 = str(numeratorB)+extraNumber
                        y2 = str(-numeratorB)+extraNumber
                    else:
                        y1 = str(numeratorB)+extraNumber+'/'+str(denominatorB)
                        y2 = str(-numeratorB)+extraNumber+'/'+str(denominatorB)
                elif denominatorA == 1:
                    if denominatorB == 1:
                        y1 = str(-numeratorA)+'+'+str(numeratorB)+extraNumber
                        y2 = str(-numeratorA)+'-'+str(numeratorB)+extraNumber
                    else:
                        y1 = str(-numeratorA)+'+'+str(numeratorB)+extraNumber+'/'+str(denominatorB)
                        y2 = str(-numeratorA)+'-'+str(numeratorB)+extraNumber+'/'+str(denominatorB)
                else:
                    if denominatorB == 1:
                        y1 = str(-numeratorA)+'/'+str(denominatorA)+'+'+str(numeratorB)+extraNumber
                        y2 = str(-numeratorA)+'/'+str(denominatorA)+'-'+str(numeratorB)+extraNumber
                    else:
                        y1 = str(-numeratorA)+'/'+str(denominatorA)+'+'+str(numeratorB)+extraNumber+'/'+str(denominatorB)
                        y2 = str(-numeratorA)+'/'+str(denominatorA)+'-'+str(numeratorB)+extraNumber+'/'+str(denominatorB)
                #x1 = -(e/c)
                #x2 = -(e/c)
                numerator = simplifyFraction(c,e)[0]
                denominator = simplifyFraction(c,e)[1]
                if denominator != 1:
                    x1 = str(-numerator)+'/'+str(denominator)
                    x2 = str(-numerator)+'/'+str(denominator)
                elif numerator == 0:
                    x1 = str(0)
                    x2 = str(0)
                else:
                    x1 = str(-numerator)
                    x2 = str(-numerator)
            elif c == 0:
                #x1 = (-newB+math.pow(delta,.5))/(2*newA)
                #x2 = (-newB-math.pow(delta,.5))/(2*newA)
                numeratorA = simplifyFraction(2*newA,newB,newDelta)[0]
                denominatorA = simplifyFraction(2*newA,newB,newDelta)[1]
                numeratorB = simplifyFraction(2*newA,newB,newDelta)[2]
                denominatorB = simplifyFraction(2*newA,newB,newDelta)[3]
                if numeratorA == 0:
                    if denominatorB == 1:
                        x1 = str(numeratorB)+extraNumber
                        x2 = str(-numeratorB)+extraNumber
                    else:
                        x1 = str(numeratorB)+extraNumber+'/'+str(denominatorB)
                        x2 = str(-numeratorB)+extraNumber+'/'+str(denominatorB)
                elif denominatorA == 1:
                    if denominatorB == 1:
                        x1 = str(-numeratorA)+'+'+str(numeratorB)+extraNumber
                        x2 = str(-numeratorA)+'-'+str(numeratorB)+extraNumber
                    else:
                        x1 = str(-numeratorA)+'+'+str(numeratorB)+extraNumber+'/'+str(denominatorB)
                        x2 = str(-numeratorA)+'-'+str(numeratorB)+extraNumber+'/'+str(denominatorB)
                else:
                    if denominatorB == 1:
                        x1 = str(-numeratorA)+'/'+str(denominatorA)+'+'+str(numeratorB)+extraNumber
                        x2 = str(-numeratorA)+'/'+str(denominatorA)+'-'+str(numeratorB)+extraNumber
                    else:
                        x1 = str(-numeratorA)+'/'+str(denominatorA)+'+'+str(numeratorB)+extraNumber+'/'+str(denominatorB)
                        x2 = str(-numeratorA)+'/'+str(denominatorA)+'-'+str(numeratorB)+extraNumber+'/'+str(denominatorB)
                #y1 = -(e/d)
                #y2 = -(e/d)
                numerator = simplifyFraction(d,e)[0]
                denominator = simplifyFraction(d,e)[1]
                if denominator != 1:
                    y1 = str(-numerator)+'/'+str(denominator)
                    y2 = str(-numerator)+'/'+str(denominator)
                elif numerator == 0:
                    y1 = str(0)
                    y2 = str(0)
                else:
                    y1 = str(-numerator)
                    y2 = str(-numerator)
            else:
                #x1 = (-newB+math.pow(delta,.5))/(2*newA)
                #x2 = (-newB-math.pow(delta,.5))/(2*newA)
                numeratorA = simplifyFraction(2*newA,newB,newDelta)[0]
                denominatorA = simplifyFraction(2*newA,newB,newDelta)[1]
                numeratorB = simplifyFraction(2*newA,newB,newDelta)[2]
                denominatorB = simplifyFraction(2*newA,newB,newDelta)[3]
                if numeratorA == 0:
                    if denominatorB == 1:
                        x1 = str(numeratorB)+extraNumber
                        x2 = str(-numeratorB)+extraNumber
                    else:
                        x1 = str(numeratorB)+extraNumber+'/'+str(denominatorB)
                        x2 = str(-numeratorB)+extraNumber+'/'+str(denominatorB)
                elif denominatorA == 1:
                    if denominatorB == 1:
                        x1 = str(-numeratorA)+'+'+str(numeratorB)+extraNumber
                        x2 = str(-numeratorA)+'-'+str(numeratorB)+extraNumber
                    else:
                        x1 = str(-numeratorA)+'+'+str(numeratorB)+extraNumber+'/'+str(denominatorB)
                        x2 = str(-numeratorA)+'-'+str(numeratorB)+extraNumber+'/'+str(denominatorB)
                else:
                    if denominatorB == 1:
                        x1 = str(-numeratorA)+'/'+str(denominatorA)+'+'+str(numeratorB)+extraNumber
                        x2 = str(-numeratorA)+'/'+str(denominatorA)+'-'+str(numeratorB)+extraNumber
                    else:
                        x1 = str(-numeratorA)+'/'+str(denominatorA)+'+'+str(numeratorB)+extraNumber+'/'+str(denominatorB)
                        x2 = str(-numeratorA)+'/'+str(denominatorA)+'-'+str(numeratorB)+extraNumber+'/'+str(denominatorB)
                #y1 = -(c*x1-e)/d
                numeratorA1 = simplifyFraction(d*denominatorA*denominatorB,denominatorB*(c*numeratorA+e*denominatorA),c*denominatorA*numeratorB)[0]
                denominatorA1 = simplifyFraction(d*denominatorA*denominatorB,denominatorB*(c*numeratorA+e*denominatorA),c*denominatorA*numeratorB)[1]
                numeratorB1 = simplifyFraction(d*denominatorA*denominatorB,denominatorB*(c*numeratorA+e*denominatorA),c*denominatorA*numeratorB)[2]
                denominatorB1 = simplifyFraction(d*denominatorA*denominatorB,denominatorB*(c*numeratorA+e*denominatorA),c*denominatorA*numeratorB)[3]
                if numeratorA1 == 0:
                    if numeratorB1 == 0:
                        y1 = str(0)
                    elif denominatorB1 == 1:
                        y1 = str(-numeratorB1)+extraNumber
                    else:
                        y1 = str(-numeratorB1)+extraNumber+'/'+str(denominatorB1)
                elif denominatorA1 == 1:
                    if numeratorB1 == 0:
                        y1 = str(-numeratorA1)
                    elif denominatorB1 == 1:
                        y1 = str(-numeratorA1)+'+'+str(numeratorB1)+extraNumber
                    else:
                        y1 = str(-numeratorA1)+'-'+str(numeratorB1)+extraNumber+'/'+str(denominatorB1)
                else:
                    if numeratorB1 == 0:
                        y1 = str(-numeratorA1)+'/'+str(denominatorA1)
                    elif denominatorB == 1:
                        y1 = str(-numeratorA1)+'/'+str(denominatorA1)+'-'+str(numeratorB1)+extraNumber
                    else:
                        y1 = str(-numeratorA1)+'/'+str(denominatorA1)+'-'+str(numeratorB1)+extraNumber+'/'+str(denominatorB1)
                #y2 = -(c*x1-e)/d
                numeratorA2 = simplifyFraction(d*denominatorA*denominatorB,c*denominatorA*numeratorB,denominatorB*(c*numeratorA+e*denominatorA))[0]
                denominatorA2 = simplifyFraction(d*denominatorA*denominatorB,c*denominatorA*numeratorB,denominatorB*(c*numeratorA+e*denominatorA))[1]
                numeratorB2 = simplifyFraction(d*denominatorA*denominatorB,c*denominatorA*numeratorB,denominatorB*(c*numeratorA+e*denominatorA))[2]
                denominatorB2 = simplifyFraction(d*denominatorA*denominatorB,c*denominatorA*numeratorB,denominatorB*(c*numeratorA+e*denominatorA))[3]
                if numeratorA2 == 0:
                    if numeratorB2 == 0:
                        y2 = str(0)
                    elif denominatorB2 == 1:
                        y2 = str(numeratorB2)
                    else:
                        y2 = str(numeratorB2)+'/'+str(denominatorB2)
                elif denominatorA2 == 1:
                    if numeratorB2 == 0:
                        y2 = str(numeratorA2)+extraNumber
                    elif denominatorB2 == 1:
                        y2 = str(numeratorA2)+extraNumber+'+'+str(numeratorB2)
                    else:
                        y2 = str(numeratorA2)+extraNumber+'-'+str(numeratorB2)+'/'+str(denominatorB2)
                else:
                    if numeratorB2 == 0:
                        y2 = str(numeratorA2)+extraNumber+'/'+str(denominatorA2)
                    elif denominatorB2 == 1:
                        y2 = str(numeratorA2)+extraNumber+'/'+str(denominatorA2)+'-'+str(numeratorB2)
                    else:
                        y2 = str(numeratorA2)+extraNumber+'/'+str(denominatorA2)+'-'+str(numeratorB2)+'/'+str(denominatorB2)
        #Define outputline
        dot1 = [x1,y1]
        dot2 = [x2,y2]
        coordnateLine = 'A1'+str(dot1)+'\nA2'+str(dot2)
        result = 'There are two intersection points between '+circle+' and '+ straightLine+' . The coordnates of them are:\n'+coordnateLine
    
    #Print the result
    print(result)
    print('--------------------------------------------')
    
    #Add values to output lists
    circleList.append(circle)
    straightLineList.append(straightLine)
    dot1List.append(dot1)
    dot2List.append(dot2)
    resultList.append(result)
    
        
    #Ask the user whether he want to keep calculating
    answer = input('Do you want to keep calculating? Press n to exit:\n>>')
    
#Prepare for the final output dictionary
outputDic['circle'] = circleList
outputDic['straight line'] = straightLineList
outputDic['dot1'] = dot1List
outputDic['dot2'] = dot2List

#Creat data frame and save it to a csv. file
outputDf = pd.DataFrame(outputDic)
outputDf.to_csv(outputFileFloderName+'\\results.csv', index = False)

#Write results in txt file:
outputFileName = outputFileFloderName+'\\results.txt'
with open(outputFileName, 'w', encoding='utf-8') as oF:
    for r in resultList:
        oF.write(r+'\n\n')

#Tell the user where the result files have been stored
print('All the results have been stored at',outputFileFloderName)

