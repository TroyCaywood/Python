#This application is used to set a user's default printer and add a network printer. Executable and .dat file should be put in c:\scripts changing directory will break application for now. List of available printers can be customized by editing the printers.dat file in c:\scripts.
#Printers.dat must be formatted with one printer per line pointing to printer network name EX: \\printserver\desktop-printer

import tkinter as tk
import tkinter.ttk as ttk

import win32api
import win32print

with open('c:/scripts/printers.dat') as f:
    lines = f.read().splitlines()
    f.close()


def get_available_printers():
    return lines


def get_available_servprinters():
    return [printer[2] for printer in win32print.EnumPrinters(5)]


# Main PrinterManager class definition

class PrinterManager(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.configure_interface()
        self.create_widgets()

    # Define window size, title, and background color

    def configure_interface(self):
        self.master.title('Printer Manager')
        self.master.geometry('350x280')
        self.master.resizable(False, False)
        self.master.config(background='#626a77')

    # Create default printer text label

    def create_widgets(self):
        self.default_printer_label = tk.Label(self.master, bg='#626a77', fg='white')
        self.default_printer_label.place(x=10, y=12)
        self.update_default_printer_label()

        selected_printer2 = tk.StringVar()
        selected_printer = tk.StringVar()

        # Print server

        print_menu_label = tk.Label(self.master, bg='#626a77', fg='white', text='Available Printers:')
        print_menu_label.place(x=12, y=79)
        printer_choice_menu = ttk.Combobox(self.master, textvariable=selected_printer2, width=35, state='readonly')
        printer_choice_menu['values'] = get_available_printers()
        printer_choice_menu.place(x=12, y=95)

        # Local printers

        print_server_menu = get_available_servprinters()
        print_server_menu_label = tk.Label(self.master, bg='#626a77', fg='white', text='Currently Installed Printers:')
        print_server_menu_label.place(x=12, y=44)
        # List available printers and post command updates list when selection dropdown is clicked

        print_server_menu = ttk.Combobox(self.master, textvariable=selected_printer, width=35, state='readonly',
                                         values=get_available_servprinters(),
                                         postcommand=lambda: print_server_menu.configure(
                                             values=get_available_servprinters()))
        print_server_menu.place(x=12, y=62)

        set_default_printer_button = tk.Button(self.master, text='Set',
                                               command=lambda: self.set_default_printer(selected_printer))
        set_default_printer_button.place(x=285, y=60, width=50)

        add_printer_button = tk.Button(self.master, text='Add', command=lambda: self.add_printer(selected_printer2))
        add_printer_button.place(x=285, y=90, width=50)

        instructions_label = tk.Label(self.master, bg='#626a77', fg='white', justify='left', wraplength=345,
                                      text='INSTRUCTIONS:  To set your default printer, click on the dropdown menu under "Currently installed printers" and select the printer you want to be default. Then click the button that says "Set".')
        instructions_label.place(x=12, y=140)

        instructions2_label = tk.Label(self.master, bg='#626a77', fg='white', justify='left', wraplength=335,
                                       text='TO ADD A PRINTER:  Click on the dropdown below the text that says "Available Printers" and select the printer you want to add. Then click the button that says "Add".')
        instructions2_label.place(x=12, y=210)

    def update_default_printer_label(self):
        default_printer = win32print.GetDefaultPrinter()
        default_printer_text = 'Default printer: {}'.format(default_printer)
        self.default_printer_label.config(text=default_printer_text)

    def set_default_printer(self, printer_name):
        win32print.SetDefaultPrinter(printer_name.get())
        self.update_default_printer_label()

    def add_printer(self, printer_name):
        win32print.AddPrinterConnection(printer_name.get())


if __name__ == '__main__':
    root = tk.Tk()
    PrinterManager(root)
    root.mainloop()
