class Library:

    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def display(self, book):
        print(f"The following Books are in our Library: ")
        for book in self.booklist:
            print(book)

    def lendBook(self,user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender Book Database is Updated. You can take the Book.")
        else:
            print(f"Book is already being in used. {self.lendDict[book]}")

    def addBook(self,book):
        self.booklist.append(book)
        print("Book has been added Successfully!")

    def returnBook(self,book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    Shubham = Library(['Python', 'Java', 'C++', 'Data Structure and Algorithm', 'C', 'Maths'], 'Shubham') 


    print(f"Welcome to {Shubham.name}'s Library.")
    while (True):
        print("Enter the Choice to Continue")
        print('1. Display the List of Books')
        print('2. Lend a Book from Library')
        print('3. Add the Book in Library')
        print('4. Return the Book to Library')    

        user_choice = input()

        if user_choice == '1':
            book = Shubham.booklist
            Shubham.display(book)

        elif user_choice == '2':
            book = input("Enter the Book You want to Lend From Library: ")
            user = input('Enter Your Name: ')
            Shubham.lendBook(user,book)

        elif user_choice == '3':
            book = input("Enter the Book name You want to add in the Lirary: ")
            Shubham.addBook(book)

        elif user_choice == '4':
            book = input('Enter the Book you want to return to the Library: ')
            Shubham.returnBook(book)

        else:
            print('You Choose Invalid Option!\nPlease choose a Valid Option.\n')


        # print('Press (Q) to QUIT and (C) to CONTINUE.\n')
        user_choice1 = ''
        while(user_choice1 != "Q" and user_choice1 != "C"):
            user_choice1 = input('Enter Your Choice to (Q)Quit and (C)Continue to the Library: ')

            if user_choice1 == 'C':
                continue
            
            elif user_choice1 == 'Q':
                exit()
            
            else:
                print('Not a Valid Option')