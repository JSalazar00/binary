# Name:    binary_conversions.py
# Date:    Feburary 6, 2023
# Author:  Justin Salazar
# Purpose: Purpose of this progran is to convert a whole number into a binary number.
#
# Instructions:
#
#   Write a program that will take in a decimal number and will return a string with the binary 
#   equivalent. Make sure your binary number is at least 4 bits. You are highly recommended to 
#   use the "divide by 2" method to convert the number to binary.
#
# Tip: Think about what you can use to store all the remainders.

# dec_to_bin
#   num     - decimal number to be converted to binary
#   returns - the binary conversion of the decimal number
import math

numb = 0
list = [0,0,0,0,0,0,0]
div = 128
numb2 = 0
convNum = " "
def get_num_dec():
        global numb
        numb = input("Enter a number: ")

        
def dec_to_bin(num):
        convNum = " "
        div = 128
        numb2 = 0
        while num != 0:
                if int(num)%div == int(num)-div:
                        list[numb2] = "1"
                        num = int(num)-div
                div = div/2
                numb2 += 1
                if div == .5:
                        break
        for i in list:
                convNum += div
        print(convNum)
        

def bin_to_dec_(num):
        convNum = 0
        div = 0
        numb2 = len(str(num))-1
        while num != 0:
            

get_num_dec()
()
        

                
                        
        

	print("DELETE this print statement and write your code here.")
  
	# Make sure your return the binary number!


# Define and code the other procedures listed in the Required Procedures section of the lab document below.
