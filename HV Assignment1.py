# Taking inputs in five Different lines
a = int(input('Enter  first Number :'))
b = int(input('Enter second Number :'))
c = int(input('Enter third Number :'))
d = int(input('Enter fourth Number :'))
e = int(input('Enter  fifth Number :'))

x = open('solution1.txt','a') # Opening files in append mode

if ((a<=0)or(b<=0)or(c<=0)or(d<=0)or(e<=0)): #checking for postive numbers2
    print('The entered values are',a,b,c,d,e)
    print('The entered values are',a,b,c,d,e,file=x) # entering into files
    print('Enter Values Higher Than Zero',file=x) # entering into files
    print('Enter Values Higher Than Zero')
else:
    sum = a+b+c+d+e # adding the numbers
    print('The entered values are',a,b,c,d,e)
    print('The entered values are',a,b,c,d,e,file=x) # entering into files
    print('The TOTAL of the five entered numbers is :',sum)
    print('The TOTAL of the five entered numbers is :',sum,file=x) # entering into files

x.close() # closing the file