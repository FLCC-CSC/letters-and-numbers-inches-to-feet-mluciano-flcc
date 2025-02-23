# FILE NAME - inches_to_feet.py

# NAME: Marcelo Luciano
# DATE: February 17, 2025
# BRIEF DESCRIPTION: Create a function that will convert inches to feet and inches.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience





# BEWARE! You'll need to cast not only the input from the user
# but also maybe the number of feet

########## ENTER YER CODE BELOW THIS LINE ##########
def convert():
    input_inches = int(input("Enter the number of inches: "))
    output = (input_inches // 12, input_inches % 12)
    print("\n" + str(input_inches) + " inches is " + str(output[0]) + " feet, and " + str(output[1]) + " inches")
convert()
########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter the number of inches: 14

14 inches is 1 feet, and 2 inches


'''



'''

Enter the number of inches: 100

100 inches is 8 feet, and 4 inches

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What does it mean to "cast" input from the user?

Casting input from the user means turning the string input into another datatype.

'''
