"""
Exercise 5: Take the following Python code that stores a string:
str = 'X-DSPAM-Confidence:0.8475'
Use find and string slicing to extract the portion of the string after the
colon character and then use the float function to convert the extracted
string into a floating point number.
"""

def convert_to_float(string):
    number = float(string)
    return number

sign = 'X-DSPAM-Confidence:0.8475'

#find and string slicing to extract the portion of the string after the colon character (:)
find_colon = sign.find(":")
print("colon is at >{}< position".format(find_colon))
some_number = sign[find_colon +1 : ]
try:
    final_number = convert_to_float(some_number)
    print(final_number)
    print(type(final_number))
except:
    print("Something went wrong")
