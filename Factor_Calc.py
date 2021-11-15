def statement_generator(text, decoration) :
    ends = decoration * 5
    statement = "{} {} {}".format(ends, text, ends)
    
    print()
    print(statement)
    print()

    return ""

def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("Please choose a data type (image / text / integer)")
    print("This program assumes that images are being represented in 24 bit colour (ie:24 bits per pixel). For text, we assume that ascii encoding is being used (8 bits per character).")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit")
    print()
    return ""

def num_check(question):
    valid = False 
    while not valid:

        error = "Please enter an integer that is more than 0"
        "(or equal to) {}".format()

        try:

            response = int(input(question))

            if response >= ():
                num = response
                return response 

            else:
                print(error)
                print()

        except ValueError:
           print(error)

statement_generator("Factors Calculator", "-")

first_time = input("Press <enter> to see the instructions or press any key to continue")

if first_time == "":
    instructions()

keep_going = ""
while keep_going == "":
    comment = ""
    var_to_factor = num_check("Number? ")
    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
        comment = "One is Unity! it only has one factor. Itself :)"

    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)

    if var_to_factor == 1:
        heading = "One is special..."

    else:
        heading = "Factors of {}".format(var_to_factor)

    statement_generator(heading, "*")

    print(factor_list)
    print(comment)
    print()
    keep_going = input("Press <enter> to continue or any key to quit")

    print("Thank you for using the Factors calculator")