from math import *
def compoundinterest(p,r,t):
	result=p*(pow(1+(r/100),t))
	ci=result-p
	return ci
p=eval(input("enter the principal amount"))
r=eval(input("enter the rate of interest"))
t=eval(input("enter the no of years"))
print("the coupound interest",compoundinterest(p,r,t))
