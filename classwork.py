# 1.
num= int(input("Enter a number: "))

def even_odd():
        "'to find odd or even'"
        if num%2==0:
            return "even number" #to return even number
        else:
            return "odd number"

def pos_neg():
    "'to find positive or negative'"
    if num>0:
         return "positive number"
    else:
         return "negative number"

def square():
     "'to find square'"
     return num*num

def cube():
     "'to find cube'"
     return num*num*num

def main():
     even_or_odd= even_odd()
     pos_or_neg= pos_neg()
     square_num= square()
     cube_num= cube()
     print(even_or_odd)
     print(pos_or_neg)
     print(square_num)
     print(cube_num)

main()
