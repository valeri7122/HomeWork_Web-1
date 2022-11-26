from HomeWork import *


if __name__ == "__main__":
    print('Hello. I am your contact-assistant. What should I do with your contacts?')
    book = AddressBook()
    book.load("auto_save")
    commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']
    while True:
        action = input('Type help for list of commands or enter your command\n').strip().lower()
        if action == 'help':
            CreateCommandList(commands).execute()
        elif action == 'view':
            View(book).execute()
        elif action == 'search':
            Search(book).execute()           
        else:
            bot = Bot(book)
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        if action == 'exit':
            break
