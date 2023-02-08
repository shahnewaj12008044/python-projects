'''
at previous solutions the program cant convert float like 1. something oor 

greater than that...now this would come with the solution to this problem'''
num = input("enter a number: ")
count=0
result=''
resultf= ''
if '.' in num:
    num = float(num)
    if  int(num) > 0:
        num1 = int(num)
        num2 = float(num)-num1
        
        while num1 > 0:
            result= str(num1%2)+result
            num1 = num1//2
            count+=1
        while num2 != 0:
            num2 =num2*2
            s_num =str(num2)
            resultf =resultf +s_num[0]
            num2 = num2 - int(num2)
            count+=1
        print('the binary form of your number is '+result+'.'+resultf)
    else:
        
        while num !=0:
            num =num*2
            s_num =str(num)
            resultf =resultf +s_num[0]
            num = num - int(num)
            count+=1
            print('remainder:'+str(num))
        print('the binary form of num is '+'0.'+resultf)
        print(count)

        
else:
    num = int(num)
    
    if num == 0:
        result='0'
    else:
        while num > 0:
            result= str(num%2)+result
            num = num//2
            count+=1
    print("the binary form of num is",result )
    print(count)
    '''
    after learning function i'll try it with function
    '''