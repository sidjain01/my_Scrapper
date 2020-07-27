from app import books

USER_CHOICE = '''Enter one of the following:
-'b' to look at the 5 stars books
-'c' to look at the cheapest books
-'n' to just get the next available book on the page
-'q' to quit
'''
book_next = (book for book in books)


def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating, reverse=True)[:10]
    for book in best_books:
        print(book)


def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


def get_next_book():
    print(next(book_next))


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'b':
            print_best_books()
        elif user_input == 'c':
            print_cheapest_books()
        elif user_input == 'n':
            get_next_book()
        else:
            print('Please enter correct input')
        user_input = input(USER_CHOICE)


menu()
