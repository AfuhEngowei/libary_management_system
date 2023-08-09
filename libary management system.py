import csv
books = []
borrowed_books = {}
users = []
name = input("enter your name      ")
email = input("enter your email address   ")
password = input("enter your password   ")
#function to create new user account
def create_user_account(name, email_address,passaword):
    user = {"name":name , "email_address":email_address, "password":passaword}
    users.append(user)
#function to update user info
def update_info(email,password):
    for user in users:
        if user["email"]== email or user["password"] == password:
            new_email = input("enter your new email address")
            new_password = input("enter your new password")
            user["email"] == new_email
            user["password"] == new_password
            print("new user info is",user)
            return user
        else:
            print("user does not exist in our system")


#function to reset user password
def reset_password():
    for user in users:
        if user["email"] == email:
            new_password = input("enter your new password")
            user["password"] == new_password
            print("your password has been reset. New password is",user)
            return user
        
#function for user authentication and user login
def user_autthentication():
    for user in users:
        if user["email"] == email and user["password"] == password:
            print("user authenticated and loged in")
        else:
            print("user does not exist in our system")


#function to generate report of books 
def report_of_all_books():
    for book in books:
        report = book
        print(report)
        return report

#function to check all books by genre
def reort_of_all_book_by_genre():
    genre = input("enter the genre of your book")
    for book in books:
        if book["genre"] == genre:
            report = book
            print (report)
            return report




                                   
#function to save and load to a file


def save_book(book):
    with open("books.csv","a")as file:
        writer = csv.writer(file)
        writer.writerow(book)
    print(book)
    return True


#add book function           
def  add_book():
    isbn = int(input(" enter the isbn of the book "))
    title = str(input(" enter the name of the book "))
    author = str(input(" enter the name of theauthor of the book "))
    genre = input("enter the genre of your book")
    my_dictionary = {"isbn": isbn, "title":title, "author":author, "genre":genre}
    row = [isbn, title, author, genre]
    books.append(my_dictionary )
    save_book(row)
    print(my_dictionary)
    print("the books added are",books)
    return books
 #delete book function 
def delete_book():
    key =  int(input("enter the isbn of the book"))
    value = str(input("enter the name of the book"))
    for key in books:
        books.remove(key)
        print(books)
        return books
#uodate book function
def update_book():
    isbn = int(input("enter the isbn  of the book"))
    for book in books:
            if book["isbn"] == isbn:
                new_title = input("enter the new title of the book")
                new_author = (input("enter the name of the book"))
                book["title"] = new_title
                book["author"] = new_author
                print("updated book is", book)
                return book
            else:
                continue
 #search book function           
def search_book():
    key_word = input("enter the keyword of the book")
    for book in books:
        if (book['isbn'] == key_word or book["author"] == key_word  or book["title"] == key_word):
            print("bookfound",book)
            return book
        else:
            print("book not found")
 #borrow book function       
def borrow_book():
    name = input("enter your name ")
    for user in users:
        if user["user_name"] == name: 
            info = user_info()
            print(info)
        else:
            print("user does not exist")
    isbn = int(input("enter the isbn of the book you want to borrow  "))
    for book in books:
        if book["isbn"] == isbn:
          print("book found")
          book["borrowed_by"] = name
          books.remove(book)
          print("book deleted",book)
          return borrowed_books
        else:
            print("book not found")
 #return book function           
def return_book():
    isbn = int(input("enter the isbn of the book")) 
    name = input("enter your name")
    for book in books:
        if book["isbn"] == isbn:
            print("book found")
            book["returned by"] = name
            print("books returned =",book)
            return book
        else:
            print("book not found")


        

def load_book():
    with open("books.csv", "r") as file:
        reader = csv.DictReader(file)
        #header = next(reader)
        print("isbn     |       title       |       author      |       genre       |")
        print("________________________________________________________________________")
        for book in reader:
            print(f"{book['isbn']}  |   {book['title']}     |   {book['author']}    |   {book['genre']}   ")
            books.append(book)
    return books

#function to print number of users
def all_users():
    for user in users:
        if user["email"] == email and user["password"] == password:
            report = user
            print("all users in the system are",report)
            return report

    

#menu of options
def main():
    print('What do you want to do: ')
    print("1: Add book")
    print("2: Delete book")
    print("3: Update book")
    print("4: search book")
    print("5: Borrow book")
    print("6: return book")
    print("7: save book")
    print("8: load book")


    while True:
        options = int(input('enter option'))
        if(options == 1):
            add_book()
        elif(options == 2):
            delete_book()
        elif(options == 3):
            update_book()
        elif(options == 4):
            search_book()
        elif(options == 5):
            borrow_book()            
        elif(options == 6):
            return_book()
        elif(options == 7):
            save_book(books)
        elif(options == 8):
            load_book()
        else:
            print('wrong option')
            exit()
#print(" to check all books available")
#print("1: books by genre")
#print("2: all books")
#print("3: number of users")
#while True:
    #option = int(input("enter  your option"))
    #if option == 1:
        #report_of_all_books()
        
    #elif option == 2:
     #   reort_of_all_book_by_genre()
    #elif option == 3:
     #   all_users()
     #else:
        #print("wrong option")
        #exit()



main()