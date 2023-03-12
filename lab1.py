from tkinter import *
from tkinter import messagebox


def main():
    start = input("Запустити програму в консолі?\n").capitalize()

    if start == "Так":
        start_terminal()
    elif start == "Ні":
        start_form()

def btn_click():
    age = age_input.get()
    sex = sex_input.get()

    if age.isdigit() and sex.isalpha():
        age = int(age)
        if age < 0 and age > 120:
            messagebox.showerror(message='Введіть коректний вік від 0 до 120')
        else:
            if age == 0:
                messagebox.showinfo(message='Спочатку народися!')
            if sex == 'ч':
                if age > 0 and age <= 10:
                    messagebox.showinfo(message='Веселися, насолоджуйся життям!')
                elif age > 10 and age <= 21:
                    messagebox.showinfo(message='У тебе почався тяжкий період, постарайся вижити!')
                elif age > 21 and age <= 35:
                    messagebox.showinfo(message='Ти вижив, займайся саморозвитком!')
                elif age > 35 and age <= 50:
                    messagebox.showinfo(message='Ти прожив вже половину життя, так і продовжуй!')
                elif age > 50 and age <= 80:
                    messagebox.showinfo(message='Ти крутий, якщо дожив!')
                elif age > 80 and age <= 120:
                    messagebox.showinfo(message='Чемпіон!')
            elif sex == 'ж':
                if age > 0 and age <= 10:
                    messagebox.showinfo(message='Залишайся ж такою веселою, як є!')
                elif age > 10 and age <= 21:
                    messagebox.showinfo(message='У тебе почався тяжкий період, постарайся вижити!')
                elif age > 21 and age <= 35:
                    messagebox.showinfo(message='Спробуй пожити для себе!')
                elif age > 35 and age <= 50:
                    messagebox.showinfo(message='Ти прожила вже половину життя, так і продовжуй!')
                elif age > 50 and age <= 80:
                    messagebox.showinfo(message='Ти крута, якщо дожила!')
                elif age > 80 and age <= 120:
                    messagebox.showinfo(message='Чемпіонка!')
    else:
        messagebox.showerror(message='Введіть дані')

def start_form():
    root = Tk()

    root['bg'] = '#b9d2fa'
    root.title("Age advice")
    root.resizable(width=FALSE, height=FALSE)

    canvas = Canvas(root, height=250, width=450)
    canvas.pack()

    title_b = Label(canvas, text='Заповність поля', font=35)
    title_b.place(rely=0.025, relx=0.33)

    #create work frame
    frame = Frame(root, bg='#afc8f0')
    frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

    global age_input, sex_input

    # create age field
    title = Label(frame, text='Вік:', font=23, bg='#afc8f0')
    title.place(relx=0.05, rely=0.15)

    age_input = Entry(frame, bg='white', font=20, width=22)
    age_input.place(relx=0.1731, rely=0.157)

    # create age field
    title = Label(frame, text='Стать:', font=25, width=6, bg='#afc8f0')
    title.place(relx=0.05, rely=0.45)

    sex_input = Entry(frame, bg='white', font=20, width=19)
    sex_input.place(relx=0.281, rely=0.457)

    #create button
    btn = Button(frame, text='Жмяк', command=btn_click, height=2, width=8)
    btn.place(rely=0.7, relx=0.43)

    #work my form
    root.mainloop()

def start_terminal():
    age = input("Введіть ваш вік: \n")
    sex = input("Вкажіть вашу стать: \n")

    if age.isdigit() and sex.isalpha():
        age = int(age)
        if age < 0 and age > 120:
            print('Введіть коректний вік від 0 до 120')
        else:
            if age == 0:
                print('Спочатку народися!')
            if sex == 'ч':
                if age > 0 and age <= 10:
                    print('Веселися, насолоджуйся життям!')
                elif age > 10 and age <= 21:
                    print('У тебе почався тяжкий період, постарайся вижити!')
                elif age > 21 and age <= 35:
                    print('Ти вижив, займайся саморозвитком!')
                elif age > 35 and age <= 50:
                    print('Ти прожив вже половину життя, так і продовжуй!')
                elif age > 50 and age <= 80:
                    print('Ти крутий, якщо дожив!')
                elif age > 80 and age <= 120:
                    print('Чемпіон!')
            elif sex == 'ж':
                if age > 0 and age <= 10:
                    print('Залишайся ж такою веселою, як є!')
                elif age > 10 and age <= 21:
                    print('У тебе почався тяжкий період, постарайся вижити!')
                elif age > 21 and age <= 35:
                    print('Спробуй пожити для себе!')
                elif age > 35 and age <= 50:
                    print('Ти прожила вже половину життя, так і продовжуй!')
                elif age > 50 and age <= 80:
                    print('Ти крута, якщо дожила!')
                elif age > 80 and age <= 120:
                    print('Чемпіонка!')
    else:
        print('Введіть дані')


if __name__ == "__main__":
    main()