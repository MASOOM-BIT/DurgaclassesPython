
# Write a Python program that accepts a list of integers and calculates the length and the fifth element.
# Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.

class InputList:
    def __init__(self, number_list):
        self.number_list = number_list

    def list_length(self):
        return len(self.number_list) == 8
        
    def fifth_element(self):
        if self.number_list.count(self.number_list[4]) == 3:
            return True
        else:
            return False

number_list = eval(input('Enter the list: '))
list_obj = InputList(number_list)
if list_obj.list_length() and list_obj.fifth_element():
    print('True')
else:
    print('False')