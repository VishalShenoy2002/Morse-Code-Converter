import sys
letter_to_morse_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'," ":"/"}

morse_to_letter_dict={v:k for k,v in letter_to_morse_dict.items()}

def convertToMorseCode(message:str):
    print("Morse Code:")
    message=message.upper()
    return " ".join(letter_to_morse_dict[char] for char in message)

def convertToNormalMessage(morseCode:str):
    print("Message:")
    return "".join(morse_to_letter_dict[char] for char in morseCode.split(" "))
        

if __name__=="__main__":
    with open('logo.txt','r') as f:
        print(f.read())
        f.close()

    for option in ["[1] Convert Message to Morse Code","[2] Convert Morse Code to Message","[3] Exit"]:
        print(option)
    
    choice=int(input("Enter Option Number:"))
    if choice==1:
        message=input("Enter Message: ")
        code=convertToMorseCode(message)
        print(code)

    elif choice==2:
        code_input=input("Enter Morse Code: ")
        print(convertToNormalMessage(code_input))

    elif choice==3:
        sys.exit(0)

    else:
        print("Wrong Option.")
        sys.exit(0)