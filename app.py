import tkinter as tk
from tkinter import *
import tkinter.messagebox as messagebox
import pyperclip
import requests
from bs4 import BeautifulSoup


class LIBGUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Library Helper')
        self.root.geometry("700x800")

        # Create a main frame to contain all widgets
        self.main_frame = Frame(self.root)
        self.main_frame.pack(pady=20)

        def extractNewArrivals(url):
            print("Extracting new arrivals... ")
            temp = ''
            response = requests.get(url)
            response_cnt = response.content
            soup = BeautifulSoup(response_cnt, 'html.parser')

            td = soup.find_all('td')

            for i in td:
                text = i.text.strip()
                if text:
                    temp += str(text) + '\n'

            with open("new_arrivals.txt", "a", encoding="utf-8") as file:
                arrival_data = temp
                file.write(arrival_data)

            return temp

        def getNewArrivals():
            url = 'https://statelibrary.kerala.gov.in/en/new-arrivals/'
            if not url:
                messagebox.showinfo("Error", "Please enter a valid URL.")
                return

                # Modify the URL to the book details page
            try:

                new_arrivals = extractNewArrivals(url)
                if new_arrivals:
                    messagebox.showinfo("New Arrivals", new_arrivals)
                else:
                    messagebox.showinfo("New Arrivals", "No New Arrivals Found")
            except Exception as e:
                messagebox.showinfo("Error", f"Error: {e}")

        def openNewArrivals():
            try:
                with open('new_arrivals.txt', 'r', encoding='utf-8') as file:
                    file_contents = file.read()
                messagebox.showinfo("New Arrivals", file_contents)
            except Exception as e:
                print(f"Error opening 'new_arrivals.txt': {e}")

        def copyNewArrivals():
            try:
                with open('new_arrivals.txt', 'r', encoding='utf-8') as file:
                    file_contents = file.read()

                # Copy the file contents to the clipboard
                pyperclip.copy(file_contents)

                messagebox.showinfo("New Arrivals", "Contents copied to clipboard")
            except Exception as e:
                print(f"Error copying 'new_arrivals.txt': {e}")

        def extractBookData(url):
            print("Extracting book details... ")
            temp = ''
            response = requests.get(url)
            response_cnt = response.content
            soup = BeautifulSoup(response_cnt, 'html.parser')

            h1 = soup.find('h1')
            h1_text = h1.get_text(strip=True)
            if h1_text:
                temp += '\n' + 'Name & Author - ' + h1_text + '\n'

            td = soup.find_all('td')
            labels = ['Item Type', 'Library', 'Language', 'Call Number', 'Status', 'Date Due', 'Barcode']
            for i in range(len(labels)):
                text = td[i].text.strip() if i < len(td) else ''  # Avoid index out of range error
                if text:
                    if labels[i] == 'Call Number':
                        text = text.replace('(Browse shelf(Opens below))', '').strip()
                    temp += f'{labels[i]} - {text}\n'

            with open("saved_books.txt", "a", encoding="utf-8") as file:
                file.write(temp)
                file.write('-' * 50)
            return temp

        def getBookDetails():
            url = self.entry.get()
            if not url:
                messagebox.showinfo("Error", "Please enter a valid URL.")
                return

                # Modify the URL to the book details page
            try:

                book_data = extractBookData(url)
                if book_data:
                    messagebox.showinfo("Book Details", book_data)
                else:
                    messagebox.showinfo("Book Details", "No book details found.")
            except Exception as e:
                messagebox.showinfo("Error", f"Error: {e}")

        def openSavedBooks():
            try:
                with open('saved_books.txt', 'r', encoding='utf-8') as file:
                    file_contents = file.read()
                messagebox.showinfo("Saved Books Data ", file_contents)
            except Exception as e:
                print(f"Error opening 'saved_books.txt': {e}")

        def copySavedBooks():
            try:
                with open('saved_books.txt', 'r', encoding='utf-8') as file:
                    file_contents = file.read()

                # Copy the file contents to the clipboard
                pyperclip.copy(file_contents)

                messagebox.showinfo("Saved Data", "Contents copied to clipboard")
            except Exception as e:
                print(f"Error copying 'saved_books.txt': {e}")

        def clearNewArrivals():
            try:
                with open('new_arrivals.txt', 'w') as file:
                    pass
                messagebox.showinfo("New Arrivals", "Contents cleared")
            except Exception as e:
                print(f"Error clearing file 'new_arrivals.txt': {e}")

        def clearSavedBooks():
            try:
                with open('saved_books.txt', 'w') as file:
                    pass
                messagebox.showinfo("Saved Books", "Contents cleared")
            except Exception as e:
                print(f"Error clearing file 'saved_books.txt': {e}")

        # Create a label for the title
        self.label = Label(self.main_frame, text="State Central Library TVM - Helper", font=('Mistral', 25, 'bold'))
        self.label.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

        # Create a button to get new arrivals
        self.get_arrivals_button = Button(self.main_frame, text="Get New Arrivals", command=getNewArrivals)
        self.get_arrivals_button.grid(row=1, column=0, padx=20, pady=20)

        # A button to open new arrivals
        self.open_arrivals_button = Button(self.main_frame, text="Open New Arrivals", command=openNewArrivals)
        self.open_arrivals_button.grid(row=1, column=1, padx=20, pady=20)

        # A button to copy new arrivals
        self.copy_arrivals_button = Button(self.main_frame, text="Copy New Arrivals", command=copyNewArrivals)
        self.copy_arrivals_button.grid(row=1, column=2, padx=20, pady=20)

        # clear new arrivals button

        self.clear_arrivals_button = Button(self.main_frame, text="Clear New Arrivals", command=clearNewArrivals)
        self.clear_arrivals_button.grid(row=1, column=3, padx=20, pady=20)

        # label

        self.book_label = Label(self.main_frame, text=' Enter Book Url - ', width=15)
        self.book_label.grid(row=2, column=0, padx=20, pady=10)

        # text box to get the Url
        self.entry = Entry(self.main_frame, width=40)
        self.entry.grid(row=2, column=1, padx=20, pady=10, columnspan=8)

        # A button to copy new arrivals
        self.get_books_button = Button(self.main_frame, text="Get Book Details ", command=getBookDetails)
        self.get_books_button.grid(row=3, column=0, padx=20, pady=20)

        # Create a button to open saved books
        self.open_books_button = Button(self.main_frame, text="Open Saved Books", command=openSavedBooks)
        self.open_books_button.grid(row=3, column=1, padx=20, pady=20)

        # A button to copy saved books
        self.copy_books_button = Button(self.main_frame, text="Copy Saved Books", command=copySavedBooks)
        self.copy_books_button.grid(row=3, column=2, padx=20, pady=20)

        # clear saved books
        self.clear_books_button = Button(self.main_frame, text="Clear Saved Books", command=clearSavedBooks)
        self.clear_books_button.grid(row=3, column=3, padx=20, pady=20)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = LIBGUI()
    app.run()
