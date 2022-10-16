from collections import UserDict
from datetime import datetime


class Field:
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if len(value) > 9:
            self.__value = value   
        else:
            print('Enter correct data')

class Name(Field):
    def __init__(self, value):
        self.value1 = value

class Phone(Field):
    def __init__(self):
        self.__value = None

class Birthday(Field):
    def __init__(self):
        self.__value = None

class Record(Field):
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        p = Phone()
        p.value = phone
        self.phones.append(p)
  
    def remove_phone(self, remove_phone):
        for phone in self.phones:
            if phone.value == remove_phone:
                self.phones.remove(phone)
                return f'The phone {remove_phone} has been removed'
            
    def change_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.add_phone(new_phone)
                self.phones.remove(phone)
                return f'The phone {old_phone} has been changed to {new_phone}'

    def add_birthday(self, date):
        b = Birthday()
        b.value = date
        self.birthday = b.value

    def days_to_birthday(self):
        birthday_list = self.birthday.split('.')
        birthday_date = datetime(year=int(birthday_list[0]), 
        month=int(birthday_list[1]), day=int(birthday_list[2])).date()
        current_date = datetime.now().date()
        return birthday_date - current_date                 
   
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value1] = record
        
    def show_record(self, name):
        self.list = []
        for el in self.data[name].phones:
            self.list.append(el.value)

    index = 0
    def __next__(self):
        self.list = []
        self.dict = {}
        self.list_value = []
        for key, value in self.data.items():
            for el in value.phones:
                self.list_value.append(el.value)
            self.dict.update({key:self.list_value})
            self.list.append(self.dict)
            
        if self.index >= len(self.list):
            self.index = 0
        element = self.list[self.index:self.index+self.N]
        self.index += self.N
        return element

    def __iter__(self):
        return self

    def iterator(self, N=3):
        self.N = N
        for i in self:
            return i       
        

address =  AddressBook()   

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)    
        except KeyError:
            print('Enter user name:')
        except ValueError:
            print('Enter correct type:')
        except IndexError:
            print('Give me name and phone please:')
    return wrapper

@input_error
def add(func_arg):
    record = Record(func_arg[0])
    record.add_phone(func_arg[1])
    address.add_record(record)
    return 'A new contact has been added'

@input_error
def add_phone(func_arg):
    addphone = address.data[func_arg[0]]
    addphone.add_phone(func_arg[1])
    return 'A new phone has been added'     

@input_error
def add_birthday(func_arg):
    addbirthday = address.data[func_arg[0]]
    addbirthday.add_birthday(func_arg[1])
    return f'The birthday {func_arg[1]} has been added'

@input_error
def days_to_birthday(func_arg):
    birthday = address.data[func_arg[0]]
    return f'The days to birthday are: {birthday.days_to_birthday()}'

@input_error
def change(func_arg):
    change = address.data[func_arg[0]]
    change.change_phone(func_arg[1], func_arg[2])
    return f'The phone: {func_arg[1]} has been changes to {func_arg[2]}'

@input_error
def remove(func_arg):
    remove = address.data[func_arg[0]]
    remove.remove_phone(func_arg[1])
    return f'The phone: {func_arg[1]} has been removed'

@input_error
def phone(func_arg):
    address.show_record(func_arg[0])
    return f'The contact "{func_arg[0]}" has phones: {address.list}'

@input_error
def iterator(func_arg):
    return address.iterator(int(func_arg[0]))

@input_error
def hello(_=None):
    return 'How can I help you?'
    
@input_error
def exit(_=None):
    return 'Good bye!'  

commands = {
'add':add,
'addphone':add_phone,
'good bye':exit,
'close':exit,
'exit':exit,
'hello':hello,
'show':iterator,
'change':change,
'phone':phone,
'remove':remove,
'addbirthday':add_birthday,
'days':days_to_birthday
}

def main():
    while True:

        print('Enter command:')
        
        input_string = input().lower()

        if input_string.split()[0] in commands and len(input_string.split()) > 1:
            print(commands[input_string.split()[0]](input_string.split()[1:]))
            
        elif input_string in commands:
            print(commands[input_string](input_string))
            
            if commands[input_string](input_string) == "Good bye!":
                break


if __name__ == '__main__':
    main() 