#None is flag value, is okay to use for finding smallest and laggest
smallest = None
print('Before')
for value in [9,234,234,1,23,5,6] :
#first trigger, assign first value to the loop
#is and is not operators, can be used in logical expressions, similar to but
#strong than ==
    if smallest is None :
        smallest = value
#started the loop
    elif value < smallest :
        smallest = value
    print(smallest,value)
print("After",smallest)
