# CS1026a 2023
# Assignment 02
# Jackson Blackman
# 251344173
# Jblackm8
# 2023-09-19
# This program will act as a library in which you can add, borrow, return, and list all the books you have added.

# list of all books that are within the library system ['unborrowed'/'borrowed', 'ISBN', 'Title', 'Author',
# 'Edition', [previous readers]]
allBooks = [
    ['unborrowed', '9780596007126', "The Earth Inside Out", "Mike B", 2, ['Ali']],
    ['unborrowed', '9780134494166', "The Human Body", "Dave R", 1, []],
    ['unborrowed', '9780321125217', "Human on Earth", "Jordan P", 1, ['David', 'b1', 'user123']]
]


def searchBook(search, borrower_name):
    # booksfound is used to keep track of if the users input generated an output or not.
    booksfound = False
    # Checks if the user is utilizing a * search
    if search[-1] == "*":
        for x in range(len(allBooks)):
            # finds if any of the book titles contains the search
            if search[:-1].lower() in str(allBooks[x][2]).lower():
                print('-"' + allBooks[x][2] + '" is', allBooks[x][0])
                # If a book is found and is unborrowed it will be borrowed
                if allBooks[x][0] == 'unborrowed':
                    allBooks[x][0] = allBooks[x][0].replace('unborrowed', 'borrowed')
                    allBooks[x][5].append(borrower_name)
                # sets book found to true as books have been found
                booksfound = True

    # Checks if the user is utilizing a % search
    elif search[-1] == "%":
        for x in range(len(allBooks)):
            # finds if any of the book titles starts with the search
            if str(allBooks[x][2]).lower().startswith(search[:-1].lower()):
                print('-"' + allBooks[x][2] + '" is', allBooks[x][0])
                # If a book is found and is unborrowed it will be borrowed
                if allBooks[x][0] == 'unborrowed':
                    allBooks[x][0] = allBooks[x][0].replace('unborrowed', 'borrowed')
                    allBooks[x][5].append(borrower_name)
                # sets book found to true as books have been found
                booksfound = True

    else:
        for x in range(len(allBooks)):
            # finds if any of the book titles is an exact match to the search
            if search.lower() == str(allBooks[x][2]).lower():
                print('-"' + allBooks[x][2] + '" is', allBooks[x][0])
                # If a book is found and is unborrowed it will be borrowed
                if allBooks[x][0] == 'unborrowed':
                    allBooks[x][0] = allBooks[x][0].replace('unborrowed', 'borrowed')
                    allBooks[x][5].append(borrower_name)
                # sets book found to true as books have been found
                booksfound = True

    # If no books are ever found through any of these methods then it will say no books found.
    if booksfound == False:
        print("No books found!")
    print("")


def listBooks():
    # Simple function that just prints if the book is available or not, title, edition, isbn, and author name
    for x in range(len(allBooks)):
        print("---------------")
        if allBooks[x][0] == 'unborrowed':
            print('[Available]')
        else:
            print('[Unavailable]')
        print(allBooks[x][2], "-", allBooks[x][3])
        print("E:", allBooks[x][4], "ISBN:", allBooks[x][1])
        print("Borrowed by:", allBooks[x][5])
    print('')


def isbnChecker(isbn):
    total = 0
    x = 0
    # If isbn is not = 13 then it is invalid
    if len(str(isbn)) != 13:
        return False
    else:
        for num in range(0, 13):
            # every even numer is *1 then added to total
            if num % 2 == 0 or num == 0:
                total = total + int(str(isbn)[x])
                x += 1
            else:
                # every odd num is *3 then added to total
                odd_num = int(str(isbn)[x]) * 3
                total = total + odd_num
                x += 1

        # check if total is devisable by 10, if it is then isbn is valid, if not, not valid
        if total % 10 == 0:
            return True
        else:
            return False


def addBook():
    # This will add the book name, checks for * and %
    placeholder1 = True
    while placeholder1 is True:
        book_name = str(input("Book name> "))
        if "*" in book_name or "%" in book_name:
            print("invalid book name!")
        else:
            placeholder1 = False

    # Author name has no conditions
    author_name = input("Author name> ")

    # Edition must be an int
    placeholder3 = True
    while placeholder3 is True:
        edition = input("Edition> ")
        if not edition.isnumeric():
            print("Must be an integer")
        else:
            placeholder3 = False
            edition = int(edition)

    # This will add the ISBN num and check if it is valid
    placeholder2 = True
    while placeholder2 is True:
        isbn = (input("ISBN> "))
        if not isbn.isdigit():
            print("Invalid ISBN!")
        elif isbnChecker(isbn) is True:
            placeholder2 = False
        else:
            print("Invalid ISBN!")

    # Finally adds all the gathered information into the allBooks list
    new_book = ['unborrowed', isbn, book_name, author_name, edition, []]
    allBooks.append(new_book)
    print("A new book is added successfully.\n")


def borrowBook():
    # Asks for the borrowers name then the search term and uses the search to find their books
    borrower_name = input("Enter the borrower name> ")
    search = input("Search term> ")
    searchBook(search, borrower_name)


def returnBook():
    placeholder2 = True
    booksfound2 = False

    # This will add the ISBN num and check if it is valid
    while placeholder2 is True:
        isbn = (input("ISBN> "))
        if not isbn.isdigit():
            print("Invalid ISBN!")
        elif isbnChecker(isbn) is True:
            placeholder2 = False
        else:
            print("Invalid ISBN!")

    # Checks if the given ISBN correlates to a book within the library then changes borrowed to unborrowed
    for x in range(len(allBooks)):
        if isbn == allBooks[x][1]:
            allBooks[x][0] = allBooks[x][0].replace('borrowed', 'unborrowed')
            booksfound2 = True
            print('-"' + allBooks[x][2] + '" is returned\n')

    # If books found is false then there are no books matching the given ISBN
    if booksfound2 == False:
        print('No book is found in the borrowed books list!')


def printMenu():
    # While true to keep this repeating
    while True:
        # gives user options
        print("####################")
        print("1: (A)dd a new book.")
        print("2: Bo(r)row books.")
        print("3: Re(t)urn a book.")
        print("4: (L)ist all books.")
        print("5: E(x)it.")
        print("####################\n")
        # users option
        choosenInput = str(input("Your selection> ")).lower()
        # Brings up the correct menu for whatever option the user selected.
        if choosenInput == "1" or choosenInput == "a":
            addBook()
            break
        elif choosenInput == "2" or choosenInput == "r":
            borrowBook()
        elif choosenInput == "3" or choosenInput == "t":
            returnBook()
        elif choosenInput == "4" or choosenInput == "l":
            listBooks()
        elif choosenInput == "5" or choosenInput == "x":
            print("$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
            listBooks()
            exit()
        else:
            print("Wrong selection! Please select a valid option.\n")
            continue


def start():
    # while true to keep print menu repeating
    while True:
        printMenu()


# Start program
start()