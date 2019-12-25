from tkinter import *

x_window = Tk()
output_text = StringVar()
check_space = IntVar()
txt_plain_text = Entry(x_window, width=35, font=10)
txt_key = Entry(x_window, width=20, font=10)

ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
      'x', 'y', 'z']
matrix_full = [[0] * len(ls) for i in range(len(ls))]


# to make the matrix of full vignere
def make_full_vignere_matrix(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            matrix[row][column] = ls[(row + column) % 26]


# Encryption
def encryption(message, key):
    print(message, key)
    cipher_text = ""
    i_key = 0

    for i in range(len(message)):
        if message[i] == ' ':
            continue
        else:
            cipher_text += matrix_full[ls.index(message[i])][ls.index(key[i_key % len(key)])]
            i_key += 1

    output_text.set("Cipher text : " + cipher_text)
    print("Cipher text : ", cipher_text)


# decryption
def decryption(message, key):
    print(message, key)
    plain_text = ""
    i_key = 0

    for i in range(len(message)):
        for row in range(len(matrix_full)):
            if matrix_full[row][ls.index(key[i_key % len(key)])] == message[i]:
                plain_text += ls[row]
                i_key += 1
                break

    output_text.set("Cipher text : " + plain_text)
    print("plain text : ", plain_text)


def click_btn1():
    encryption(str(txt_plain_text.get()).lower(), str(txt_key.get()).lower())


def click_btn2():
    decryption(str(txt_plain_text.get()).lower(), str(txt_key.get()).lower())


def main():
    make_full_vignere_matrix(matrix_full)

    # frame window
    x_window.configure(background="black")
    x_window.title("Full Vignere")
    x_window.geometry("500x300")

    # labels
    lbl_txt1 = Label(x_window, text="Text : ", padx=5, pady=5, bg="black", fg="white")
    lbl_txt2 = Label(x_window, textvariable=output_text, padx=5, pady=5, font=10, bg="black", fg="white")
    lbl_key = Label(x_window, text="Key : ", padx=5, pady=5, bg="black", fg="white")
    lbl_txt1.place(x=10, y=10)
    lbl_key.place(x=10, y=50)

    # text
    txt_plain_text.focus()
    txt_plain_text.place(x=60, y=15)
    txt_key.place(x=60, y=55)

    # Button and check button
    btn_encrypt = Button(x_window, text="Encrypt", padx=5, pady=5, command=click_btn1, bg="gray", fg="white",
                         activebackground="black", activeforeground="white")
    btn_decrypt = Button(x_window, text="Decrypt", padx=5, pady=5, command=click_btn2, bg="gray", fg="white",
                         activebackground="black", activeforeground="white")

    btn_encrypt.place(x=100, y=110)
    btn_decrypt.place(x=250, y=110)

    lbl_txt2.place(x=60, y=160)
    x_window.mainloop()


if __name__ == '__main__': main()
