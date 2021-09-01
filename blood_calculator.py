def interface():
    keep_running = True
    print("My Program")
    print("Options")
    print("1 - Analysis")
    print("9 - Quit")
    while keep_running:
        choice = input("Enter your choice: ")
        if choice == '9':
            keep_running = False
        elif choice == '1':
            driver_HDL()
    print(choice)
    return choice

def hdl_input():
    hdl_value = int(input(("Enter HDL Value: ")))
    return hdl_value

def check_HDL(HDL_value):
    if HDL_value >= 60:
        out = "Normal"
    elif 40 <= HDL_value < 60:
        out = "Borderline Low"
    else:
        out = "Low"
    return out

def driver_HDL():
    hdl_value = hdl_input()
    hdlCheck = check_HDL(hdl_value)
    outputResults(hdl_value,hdlCheck)


def outputResults(valueHDL,outCheckHDL):
    print("Patient's HDL is " +str(valueHDL) + " which is "  +outCheckHDL)

interface()