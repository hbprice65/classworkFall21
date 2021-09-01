def interface():
    keep_running = True
    print("My Program")
    print("Options")
    print("1 - Analysis HDL")
    print("2 - Analysis LDL")
    print("9 - Quit")
    while keep_running:
        choice = input("Enter your choice: ")
        if choice == '9':
            keep_running = False
        elif choice == '1':
            driver_HDL()
        elif choice == '2':
            driver_LDL()
    print(choice)
    return choice

def hdl_input():
    hdl_value = int(input(("Enter HDL Value: ")))
    return hdl_value

def ldl_input():
    ldl_value = int(input(("Enter LDL Value: ")))
    return ldl_value

def check_HDL(HDL_value):
    if HDL_value >= 60:
        out = "Normal"
    elif 40 <= HDL_value < 60:
        out = "Borderline Low"
    else:
        out = "Low"
    return out

def check_LDL(LDL_value):
    if LDL_value < 130 :
        out = "Normal"
    elif 130 <= LDL_value <= 159:
        out = "borderline high"
    elif 160 <= LDL_value <= 189:
        out = "high"
    else:
        out = "very high"
    return out

def driver_HDL():
    hdl_value = hdl_input()
    hdlCheck = check_HDL(hdl_value)
    outputResults(hdl_value,hdlCheck,"HDL")

def driver_LDL():
    ldl_value = ldl_input()
    ldlCheck = check_LDL(ldl_value)
    outputResults(ldl_value,ldlCheck,"LDL")


def outputResults(valueHDL,outCheckHDL,resultType):
    print("Patient's " + resultType + " is " +str(valueHDL) + " which is "  +outCheckHDL)

interface()