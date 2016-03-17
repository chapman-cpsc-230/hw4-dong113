
def digits (pichu): #takes in a number and counts how many digits it has--including the sign
    pika = 0    
    if pichu == 0: #if the number is zero, it returns a value of one
        pika += 1
        return pika
    else: # if the value is not zero...
        
        while pichu > 1 or pichu < -1: #...it checks whether the number's absolute value is greater than one
            pika +=1 #if it is, the loop has a counter that keeps track of how many times ...
            pichu /= 10. # the number can be divided by ten before the absolute value is less than one
        if pichu < 0: # if it's negative, it'll add one to the counter
            pika += 1
        return pika
        

x = raw_input("enter a number: ")
raichu = int(x)


print digits(raichu)

