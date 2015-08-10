#!/usr/bin/env python
# HW05_ex00_logics.py
##############################################################################

def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    i=0
    while i != 1:
        try:
            a = raw_input("Enter an integer: ")
            b = int(a)
        except:
            print "Enter a number"
        else:
            i = 1
            if b % 2 ==0:
                print "The number is an even number"
            else:
                print "he number is odd"
    


def ten_by_ten():
    for i in range(101):
        if i>0:
            if i<10:
                print "",str(i),
                continue
            if(i%10)==0:
                print str(i)+ "\n"
            else:
                print i,
    


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    count = 0
    sum = 0
    a = raw_input("Enter a value: ")
    while(a!= "done"):
        sum+= int(a)
        count+= 1
        a = raw_input("enter another value")
    avg = sum/float(count)    
    print avg        
    pass

##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    find_average()
    ten_by_ten()
    even_odd()
    pass

if __name__ == '__main__':
    main()
