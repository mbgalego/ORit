import pyperclip


def get_data_to_OR_from_CLI():
    input_data = input("Past data to 'OR' it: \n>")
    
    while True:
        input_line = input()
        if input_line != "":
            input_data = input_data + "\n" + input_line
        else:
            break
    
    return input_data

def get_data_to_OR():
    option = ""
    while True:
        option = input("Get from clipboard (y/n)?: ")
        if option == "y":
            input_data = pyperclip.paste()
            break
        elif option == "n":
            input_data = get_data_to_OR_from_CLI()
            break
    
    return input_data
        


data_to_OR = get_data_to_OR()
data_devide_by_lines = data_to_OR.count("\n")
data_devided_by_spaces = data_to_OR.count(" ")


data_to_OR_list = []

if data_devide_by_lines > 1 and data_devided_by_spaces > 0:
    print("Input has wrong format!\nPast data seperated by lines or spaces only!")
    while True:
        input("\nPress ENTER to quit.")
        break
    quit()
else:    
    if data_devide_by_lines > 1:   # data devided by lines
        data_to_OR_list = data_to_OR.splitlines()
    elif data_devided_by_spaces > 0:  # data devided by spaces
        data_to_OR_list = data_to_OR.split(" ")

data_to_OR_list_len = len(data_to_OR_list)

# since we adding an 'or' between each string
#  we will infact double de size of the list
for i in range(1, data_to_OR_list_len*2-1,2):
    data_to_OR_list.insert(i," or ")
    
# convert the list to a string
ouput_with_OR = ''.join(data_to_OR_list)
ouput_with_OR = ouput_with_OR.replace("\n","")

# send output to clipboard
pyperclip.copy(ouput_with_OR)
print(f"Output {data_to_OR_list_len} items:\n----- \n{ouput_with_OR}\n----- \nAlso sent to clipboard!")

while True:
    input("\nPress ENTER to quit.")
    break

