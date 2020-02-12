# Group Name : Avishek Pradhan ,Naresh Gurung

# STEP 1
def ConvertToFloatingBinary(num,AfterWhole):

    # separating whole number and Decimal number where
    # split separate the two numbers and put in the list

    WholeNum, DecimalNum = str(num).split(".")

    # converting numbers to string to integer
    # ( note: split is used in string not in integer)

    WholeNum = int(WholeNum)
    DecimalNum= int(DecimalNum)

    # convert whole number to binary and removed (0b) which mean base 2

    Conversion = bin(WholeNum).lstrip("-0b")+"." # it works as Converting whole number to binary and
                                                # removing the characters the nearest left and '.' is added

    # count the n steps after the decimal point

    for r in range (AfterWhole): # execute the counts
        WholeNum, DecimalNum = str((dec_convertor(DecimalNum))*2).split(".") # multiply decimal number by 2
                                                                            # separate the whole number part and decmial part

        DecimalNum = int(DecimalNum) # converting into integer
        Conversion += WholeNum # adding the integer

    return Conversion

# conversion for the value passed as parameter to decimal representation

def dec_convertor(number):

    # divide the whole value by 10 until it becomes less than value 1
    while number > 1:
        number = number / 10
    return number

# check weather sign bit is 1 or 0

# STEP 2
def calculate_sign_bit(num):

    # check the value is negative or positive
    if num <= -1: #select number 1 if the input is negative
        num = 1
    else:
        num = 0 #select the number 0 if the input is postive

    return num #return the number

# STEP 3

def normalize_binary(num):

# Separating whole number and Decimal number where
# Split separate the two numbers and put in the list

    WholeNum, DecimalNum = str(num).split(".")

    WholeNum= int(WholeNum)

    Expo= len(str(WholeNum))# count the total number of input

    E = Expo-1# subtract the number by 1 according to the formula (E-1)

    mantissa = str(WholeNum)[1:] #slice the given whole number
                                  # reads the value from 1 to 6
                                # and adding the number at back of the output not including decimal

    mantissa = mantissa + DecimalNum # adding normalized output and decimal number together

    Result = ("Mantissa:"+str(mantissa) + " Exponent:"+str(E)) #formating the input
    return Result# returns the result

# Step 4
def calculate_exponent_biased(num):

    E = (2 **(8-1)-1) + num #implement the formula of the (2^(n-1)-1)

    exponent_bits = bin(E).lstrip("0b")#converts the given number to binary removing 0b

    return exponent_bits # results the output

#Step 5

def IEEE754_rep(num, Expo,fraction):

    # check the value is negative or positive
    if num < -1: #select the num 1 if the input is negative
        num = 1
    else:
        num = 0 #select the num 0 if the input is negative

    E = (2 ** (8 - 1) - 1) + Expo#implement the formula of the (2^(n-1)-1)
    exponent_bits = bin(E).lstrip("0b")#converts the given number to binary removing 0b

    # Separating whole number and Decimal number where
    # Split separate the two numbers and put in the list
    WholeNum, DecimalNum = str(fraction).split(".")

    Ex = len(str(WholeNum))  # count the numbers and subtract
    Eo = Ex - 1

    man = str(WholeNum)[1:]# reads the value from 1 to 6
                                     # and adding the number at back of the output not including decimal
    mantissa = man + DecimalNum

    Normalization = int(mantissa) * 10**(23-len(mantissa))

    Result = (str(num) + "-" + str(exponent_bits) + "-" + str(Normalization)) #formating the input

    return Result

#Reverese Operation

def IEEE_754_to_float(n):

    ListOfbinary = [str(d) for d in str(n)[2:]]# make the octal number into list

    if ListOfbinary[0] == 1:  # select the num 1 if the input is negative
        n = 1
    else:
        n = 0  # select the num 0 if the input is negative

    fraction =ListOfbinary[1:9]# Seprate the normalization from given fraction
    binary_conversion = ListOfbinary[9:18]

    s = [str(i) for i in fraction]# Convert integer list to string of fraction
    N = str("".join(s))# Join list items using join() of fraction
    Dec = int(N,2)


    b = [str(w) for w in binary_conversion] # Convert or integer list to string for exponent
    F = str("".join(b))# Join list items using join() for exponent

    BiasedExpo = 2 ** (8 -1)-1 # default biasedExpo 127

    Exponet = Dec - BiasedExpo # find the exponent subtracting from the default Exponent

    BinaryConv =str(1) + "." + str(F)# shfiting points and adding in normalization
    result = float(BinaryConv) * (10 ** Exponet) # using Exponential and normalization for the given binary

    WholeNum, DecimalNum = str(result).split(".") # split decimal and whole numbers

    Binary_Whole = str(WholeNum) #separate the whole number
    Decimal_Whole = str(DecimalNum) # seprate the decimal number

    BeforeDecimal = int(Binary_Whole, 2) # change to decimal number

    counter = 1 # counts
    Deci = 0 # add sloution

    for i in Decimal_Whole: # create a loop to multiply after decimal number
        if int(i) != 0: # if i is zero then skip the step and go for another count
            Deci += 1/(2**counter)  #If i is not zero then multiply the number by 1/2(power)
        counter = counter + 1 # add the count if it is zero


    Final = BeforeDecimal + Deci #combining both whole number and decimal number

    return Final



if __name__ == '__main__':

    num = float(input("Input any number: \n"))

    print("\nThe Binary Representation of the number is:", (ConvertToFloatingBinary(num, 3)))

    print("\nThe sign is negative with a sign bit :", calculate_sign_bit(num))

    print("\n"+normalize_binary(1010101.001))

    E = calculate_exponent_biased(6)
    print("\nThe exponent is : 6 and biased exponent is: ", E)

    IEE754 = IEEE754_rep(num, 6, 1010101.001)
    print("\nThe IEEE 754 single precision for 85.125 is :",IEE754)

    print("\nThe float number for the given binary is", IEEE_754_to_float('0001000010101010100100000000000000'))







