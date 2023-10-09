import tkinter as tk
from tkinter import *
import webbrowser
from tkinter import ttk

darkest = '#331D2C'
dark1 = '#2D4356'
dark2 = '#435B66'
pink1 = '#A76F6F'
light1 = '#EAB2A0'
light2 = '#EFE1D1'
yellow = '#FEFFAC'
lightblue = '#F1F0E8'

image_width = 60
image_height = 100

class LIBGUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Library Helper')
        self.root.geometry("1000x800")
        self.root.config(bg=lightblue)
        self.createWidgets()

    def createWidgets(self):



        self.library_image = tk.PhotoImage(file="images/library.png", width=image_width, height=image_height)
        self.library_button = tk.Button(self.root, image=self.library_image, bg=lightblue,command=self.open_library_link, justify="center", borderwidth=0, relief="flat", activebackground=lightblue)
        self.library_button.pack(side="left", padx=5, anchor='nw', pady=10)

        self.profile_image = tk.PhotoImage(file='images/user.png', width=image_width, height=image_height)
        self.profile_button = tk.Button(self.root, image=self.profile_image, bg=lightblue, command=self.open_login_link, justify="center", borderwidth=0, relief="flat", activebackground=lightblue)
        self.profile_button.pack(side="left", padx=5, anchor='nw', pady=10)


        self.show_main_screen()

    def show_main_screen(self):
        if hasattr(self, 'new_arrivals_frame'):
            self.new_arrivals_frame.destroy()
        if hasattr(self, 'book_data_frame'):
            self.book_data_frame.destroy()

        self.main_frame = Frame(self.root, bg=lightblue)
        self.main_frame.pack(expand=True, fill='both')

        main_label = tk.Label(self.main_frame, text='L I B   H E L P', font=('PERPETUA TITLING MT', 60), fg=dark2,
                              bg=lightblue, anchor='center', justify='center')
        main_label.pack(pady=20)

        new_arrivals_button = tk.Button(self.main_frame, text='New Arrivals', font=('Freestyle Script', 30), fg=dark2,
                                        bg=yellow, command=self.show_new_arrivals, relief='ridge')
        book_data_button = tk.Button(self.main_frame, text='Book Data', font=('Freestyle Script', 30), fg=dark2,
                                     bg=yellow, command=self.show_book_data, relief='ridge')

        new_arrivals_button.place(x=540, y=200, width=300, height=50)
        book_data_button.place(x=540, y=260, width=300, height=50)

    def show_new_arrivals(self):
        if hasattr(self, 'main_frame'):
            self.main_frame.destroy()

        self.new_arrivals_frame = Frame(self.root, bg=lightblue)
        self.new_arrivals_frame.pack(expand=True, fill='both')

        newarrival_label = tk.Label(self.new_arrivals_frame, text='N e w   A r r i v a l s', font=('PERPETUA TITLING MT', 55),
                                    fg=dark2,
                                    bg=lightblue, anchor='center', justify='center')
        newarrival_label.pack(pady=10)

        button_frame = Frame(self.new_arrivals_frame, bg=lightblue)
        button_frame.pack(pady=20)

        get_new_arrivals_button = tk.Button(button_frame, text='Get New Arrivals', font=('Freestyle Script', 30),fg=dark2,
                                            bg=yellow, command=self.show_new_arrivals, relief='ridge')
        copy_new_arrivals_button = tk.Button(button_frame, text='Copy New Arrivals', font=('Freestyle Script', 30),fg=dark2,
                                             bg=yellow, command=self.show_new_arrivals, relief='ridge')
        clear_new_arrivals_button = tk.Button(button_frame, text='Clear New Arrivals', font=('Freestyle Script', 30),fg=dark2,
                                              bg=yellow, command=self.show_new_arrivals, relief='ridge')

        get_new_arrivals_button.pack(side=LEFT, padx=5)
        copy_new_arrivals_button.pack(side=LEFT, padx=5)
        clear_new_arrivals_button.pack(side=LEFT, padx=5)

        newarrivals_label = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=('HP Simplified Hans Light', 15),
                                                  bg=dark2, fg=lightblue)
        newarrivals_label.pack()


        self.home_image = tk.PhotoImage(file="images/back.png", width=image_width, height=image_height)
        self.home_button = tk.Button(self.new_arrivals_frame, image=self.home_image, bg=lightblue,
                                     command=self.show_main_screen, justify="center", borderwidth=0, relief="flat",
                                     activebackground=lightblue)
        self.home_button.place(y = 800)



    def show_book_data(self):
        if hasattr(self, 'main_frame'):
            self.main_frame.destroy()

        self.book_data_frame = Frame(self.root, bg=lightblue)
        self.book_data_frame.pack(expand=True, fill='both')

        book_data_label = tk.Label(self.book_data_frame, text='B o o k   D a t a',font=('PERPETUA TITLING MT', 55),
                                    fg=dark2,
                                    bg=lightblue, anchor='center', justify='center')
        book_data_label.pack(pady=10)

        self.home_image = tk.PhotoImage(file="images/back.png", width=image_width, height=image_height)
        self.home_button = tk.Button(self.new_arrivals_frame, image=self.home_image, bg=lightblue,
                                     command=self.show_main_screen, justify="center", borderwidth=0, relief="flat",
                                     activebackground=lightblue)
        self.home_button.pack(pady=20)

    def open_library_link(self):
        webbrowser.open('https://statelibrary.kerala.gov.in/en/sample-page/')

    def open_login_link(self):
        webbrowser.open('http://103.251.43.202:8080/cgi-bin/koha/opac-user.pl')

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = LIBGUI()
    app.run()
