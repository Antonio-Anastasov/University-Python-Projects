searched_book = input()
searched_book_counter = 0

while True:
    book = input()

    if book == searched_book:
        print(f'You checked {searched_book_counter} books and found it.')
        break

    if book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {searched_book_counter} books.')
        break

    searched_book_counter += 1