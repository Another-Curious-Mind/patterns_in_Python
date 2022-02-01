n = 5
for i in range(n+1):
    print(i*"*")


n = 5
for i in range(n+1):
    
    print((2*i-1)*"*")

n = 5
for i in range(n+1):
    print(("*"*(i-1))+(i*"*"))




# 1st diamond shape
h = int(input("Enter diamond's height: "))
for x in range(h):
    print(" " * (h - x), "*" * (2*x + 1))   # here space_number = (" " * (h - x) & star_number = "*" * (2x + 1), because:
                                                #if h= 5 then 
                                                # 1st iteration:
                                                # space_number= (5-0)=5 & star_number= (2*0+1)=1
                                                # 2nd iteration:
                                                # space_number= (5-1)=4 & star_number= (2*1+1)=3
                                                # 3rd iteration:
                                                # space_number= (5-2)=3 & star_number= (2*2+1)=5
                                                # and so on
                                                # this portion for upper side of the diamond shape


for x in range(h - 2, -1, -1):          # this portion for lower side of the diamond shape
    ''' 
    Here initial limit of range(h-2), cause till half of the shape the 1st loop runs for h-1 times.
    which is the highest or middle line of the diamond shape.
    & before/after the line number is less then 1 of that middle line number. 
    though that middle line number is (h-1), so that lines after which line comes that will be (h-1-1) equals to (h-2) 
    so 2nd loops initial line number is (h-2)

    # end limit or outer line is -1, cause 2nd loop will run from initial limit to '0'
    # interval is -1, cause every time the loop runs the counter number will decrease value 1 from the init value
    
    '''
    print(" " * (h - x), "*" * (2*x + 1))   # here space_number = " " * (h - x),& star_number = "*" * (2*x + 1)
                                                #if h= 5 then
                                                # 1st iteration:
                                                    # x = h-2 
                                                    #   = 5-2 
                                                    #   = 3
                                                # space_number = (5-3)= 2 & star_number = (2*3+1)=7

                                                # 2nd iteration:
                                                    # h = h-1 
                                                    #   = 5-1 
                                                    #   = 4
                                                    # x = h-2 
                                                    #   = 4-2 
                                                    #   = 2
                                                # space_number = (4-2)= 2 & star_number = (2*2+1)=5

                                            # and so on...




# 2nd diamond shape
h = eval(input("Enter diamond's height: "))     # here for giving eval() method i don't have to declare the input type.It automatically return the integer value in h.& if i don't use this method then i've to declare the input type, cause in python everything the user inputs will be a string.
for x in range(h):
    print(" " * (h - x), "*" * (2*x + 1))

for x in range(h - 2, -1, -1):
    print(" " * (h - x), "*" * (2*x + 1))