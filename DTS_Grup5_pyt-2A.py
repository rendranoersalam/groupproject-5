from tkinter import *
from random import choice

'''
Tugas Grup 5 PYT-2A
Generate random color dengan tampilan antarmuka Tkinter
'''


def create_color():
    ''' Fungsi ini untuk akan menggunakan function choice dari modul random untuk
    mengambil data acak dari list karakter dan angka yang sudah ditentukan, 
    untuk menghasilkan hexa color code yang akan dijadikan sebagai background
    '''
    hexa_code   = ['A','B','C','D','E','F','F','0','1','2','3','4','5','6','7','8','9']

    # generate random number and character
    color_hexa_1     = '#'+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)
    color_hexa_2     = '#'+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)
    color_hexa_3     = '#'+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)+choice(hexa_code)

    color_one.configure(background=color_hexa_1)
    color_two.configure(background=color_hexa_2)
    color_three.configure(background=color_hexa_3)
    color_one_hexa_code.delete(0, 7)
    color_one_hexa_code.insert(0, color_hexa_1)
    color_two_hexa_code.delete(0, 7)
    color_two_hexa_code.insert(0, color_hexa_2)
    color_three_hexa_code.delete(0, 7)
    color_three_hexa_code.insert(0, color_hexa_3)

    # create RGB Color code
    rgb1 = [int(color_hexa_1[1:3], 16),int(color_hexa_1[3:5], 16),int(color_hexa_1[5:7], 16)]
    rgb2 = [int(color_hexa_2[1:3], 16),int(color_hexa_2[3:5], 16),int(color_hexa_2[5:7], 16)]
    rgb3 = [int(color_hexa_3[1:3], 16),int(color_hexa_3[3:5], 16),int(color_hexa_3[5:7], 16)]
    color_one_rgb_code.delete(0, len(color_one_rgb_code.get()))
    color_one_rgb_code.insert(0, rgb1)
    color_two_rgb_code.delete(0, len(color_two_rgb_code.get()))
    color_two_rgb_code.insert(0, rgb2)
    color_three_rgb_code.delete(0, len(color_three_rgb_code.get()))
    color_three_rgb_code.insert(0, rgb3)

# create the main windows to show the GUI
main_window             = Tk()
main_window.geometry    = ('600 x 350')
main_window.resizable   = (False, False)
main_window.title('Generate Random Color')
main_window.background  = '#FFFFFF'

# tkinter widgets
heading_title = Label(main_window, text='Generate Random Color', font=('', 14, 'bold'))
heading_color = Label(main_window, text='COLOR', font=('', 12, 'bold'))
heading_rgb = Label(main_window, text='RGB', font=('', 12, 'bold'))
heading_hexa = Label(main_window, text='HEXA', font=('', 12, 'bold'))
color_one = Label(main_window, background='#FF0000', width=40, height=2)
color_two = Label(main_window, background='#00FF00', width=40, height=2)
color_three = Label(main_window, background='#0000FF', width=40, height=2)
color_one_rgb_code = Entry(main_window)
color_one_hexa_code = Entry(main_window)
color_two_rgb_code = Entry(main_window)
color_two_hexa_code = Entry(main_window)
color_three_rgb_code = Entry(main_window)
color_three_hexa_code = Entry(main_window)
generate_button = Button(main_window, text='GENERATE', font=('', 14, 'bold'), background='#232323', foreground='#FFFFFF', width=23, command=create_color)
footer = Label(main_window, text='Grup 5 PYT-2A')

# grid position
heading_title.grid(row=0, column=0, columnspan=3, pady=20)
heading_color.grid(row=1, column=0)
heading_rgb.grid(row=1, column=1)
heading_hexa.grid(row=1, column=2)
color_one.grid(row=2, column=0, pady=5, padx=5)
color_two.grid(row=3, column=0, pady=5)
color_three.grid(row=4, column=0, pady=5)
color_one_rgb_code.grid(row=2, column=1, padx=10)
color_one_hexa_code.grid(row=2, column=2, padx=10)
color_two_rgb_code.grid(row=3, column=1, padx=10)
color_two_hexa_code.grid(row=3, column=2, padx=10)
color_three_rgb_code.grid(row=4, column=1, padx=10)
color_three_hexa_code.grid(row=4, column=2, padx=10)
generate_button.grid(row=5, column=0)
footer.grid(row=6, column=0, columnspan=3, pady=20)

#run the mainloop
main_window.mainloop()


