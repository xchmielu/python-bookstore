from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all boks
- 'r' to mark book as read
- 'd' to delete the book
- 'q' to quit

Your choice: """


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            promt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            promt_delete_book()
        else:
            print('Unknown command')

        user_input = input(USER_CHOICE)

def promt_add_book():
    name = input('Book name: ')
    author = input('Author of the book: ')

    database.add_book(name, author)

def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'Yes' if book['read'] else 'No'
        print(f"{book['name']} by {book['author']}, read = {book['read']}")

def prompt_read_book():
    name = input('Enter the book u have read: ')
    database.mark_book_as_read(name)

def promt_delete_book():
    name = input('Enter the of the book you want to delete: ')

menu()



