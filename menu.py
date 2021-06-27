# ALL BOOKS - Done
# BORROW BOOKS
# SEARCH BOOKS - Done
# ADD BOOKS - Done
# RESERVE BOOKS
def menu():
    print("----MENU----") 
    print("""1. ALL BOOKS
2. BORROW BOOKS
3. SEARCH BOOKS
4. ADD BOOKS
5. RESERVE BOOKS""")
    option = int(input('Enter Option -> '))
    while option != 0:
        if option == 1:
            from showBook import showBook
            showBook()
            # print('ShowBOOK')
        elif option == 3:
            print("---SEARCH---")
            print("""1. SEARCH BY TITLE\n2. SEARCH BY AUTHOR\n3. SEARCH BY YEAR\n0. BACK""")
            option2 = int(input('Enter Option -> '))
            while option2 != 0:
                if option2 == 1:
                    from searchBook import searchByTitle
                    searchByTitle()
                elif option2 == 2:
                    from searchBook import searchByAuthor
                    searchByAuthor()
                elif option2 == 3:
                    from searchBook import searchByYear
                    searchByYear()
                
        elif option == 5:
            from addBook import add_to_db
            add_to_db()
        menu()
if __name__ == "__main__":
    menu()
