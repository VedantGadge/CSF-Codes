def booths_algorithm():
    # Gets Multiplicand
    multiplicand_dec = getInput("Multiplicand")
    # Gets Multiplier
    multiplier_dec = getInput("Multiplier")
    # Converts Multiplicand
    multiplicand_bin = convertDec(multiplicand_dec)
    # Converts Multiplier
    multiplier_bin = convertDec(multiplier_dec)
    # Perform Booth's algorithm
    boothsTriumph(multiplicand_bin, multiplier_bin)
    # Print the final decimal result
    print("Decimal Result: " + str(int(multiplier_dec) * int(multiplicand_dec)))

## Parent function for logical process
def boothsTriumph(mcand, plier):
    # Create full product line for Booth's Algorithm
    print("multiplicand: " + mcand + " multiplier: " + plier)
    product = "00000000" + plier + "0"
    print("Product: " + product)
    # Display product line to user
    print(buildLine(0, mcand, product))
    # Iterate through Booth's Algorithm
    for i in range(1, 9):
        operation = product[len(product) - 2:]
        product = perform_operation(product, mcand, operation)
        print(buildLine(i, mcand, product))
    # Print out the final value in binary and decimal
    product = shift(product)
    product = product[9:17]
    print("Product: " + product)

## Perform the necessary algorithmic operation
def perform_operation(product, mcand, operation):
    if operation == "00" or operation == "11":
        product = shift(product)
        print("No Op")
    elif operation == "01":
        # Product = Product + mcand
        temp = binAdd(product[0:8], mcand)
        product = temp + product[8:]
        product = shift(product)
        print("Add")
    elif operation == "10":
        # Product = Product - mcand
        product = subtraction(product, mcand)
        product = shift(product)
        print("Sub")
    else:
        print("An error occurred when choosing operation: Exiting program")
        exit(0)
    return product

## Perform subtraction operation
def subtraction(product, mcand):
    carry = 0
    prime_product = product[:8]
    final_product = ""
    for i in range(len(prime_product) - 1, -1, -1):
        if mcand[i] == "0" and prime_product[i] == "0":
            final_product = ("1" if carry == 1 else "0") + final_product
        elif mcand[i] == "1" and prime_product[i] == "0":
            final_product = ("0" if carry == 1 else "1") + final_product
            carry = 1
        elif mcand[i] == "0" and prime_product[i] == "1":
            final_product = ("0" if carry == 1 else "1") + final_product
            carry = 0
        elif mcand[i] == "1" and prime_product[i] == "1":
            final_product = ("1" if carry == 1 else "0") + final_product
            carry = 1
        else:
            print("An error occurred during subtraction: Exiting program")
            exit(0)
    return final_product + product[8:]

## Shifts left
def shift(product):
    return "0" + product[:len(product) - 1]

## Adds two binary strings
def binAdd(num, num2):
    product = ""
    carry = "0"
    for i in range(len(num) - 1, -1, -1):
        if carry == "0":
            if num[i] == "0" and num2[i] == "0":
                product = "0" + product
            elif num[i] == "1" and num2[i] == "1":
                product = "0" + product
                carry = "1"
            else:
                product = "1" + product
        else:
            if num[i] == "0" and num2[i] == "0":
                product = "1" + product
                carry = "0"
            elif num[i] == "1" and num2[i] == "1":
                product = "1" + product
                carry = "1"
            else:
                product = "0" + product
                carry = "1"
    return product

## Shows step-by-step process
def buildLine(iteration, mcand, product):
    return f"Step: {iteration} | Multiplicand: {mcand} | Product: {product[:8]} | {product[8:16]} | {product[16]}"

## Converts a decimal number to its binary representation
def convertDec(dec):
    bin_num = twos_complement(int(dec)) if int(dec) < 0 else "{0:b}".format(int(dec))
    return bin_num.zfill(8)

## Handles input and input validation
def getInput(varName):
    while True:
        try:
            boothIn = int(input(f'Please enter your {varName}: '))
            if boothIn > 127 or boothIn < -128:
                print("Absolute value too big, please try again.")
            else:
                return boothIn
        except ValueError:
            print("Invalid input. Please enter an integer.")

## Converts a negative decimal number into two's complement
def twos_complement(value):
    value = (1 << 8) + value if value < 0 else value
    return "{0:b}".format(value)

## CALL MAIN
booths_algorithm()