# import tkinter as tk
# from datetime import datetime
# window = tk.Tk()
# window.title("Hello world!")
# dates = datetime.now()
# hello = tk.Label(text=str(dates.day) + "-Mart",
#                  foreground='white',
#                  background='black')
# hello1 = tk.Label(text='Footer',
#                   foreground='white',
#                   background='black')
# my_data = ['Python Course', 'Django prjects', 'Udemy', 'GeekForGeeks']
# hello.pack(ipady=20, ipadx=120, padx=10, pady=10, side='top')
# for data in my_data:
#     data1 = tk.Label(text=data,
#                      foreground='white',
#                      background='black')
#     data1.pack(ipady=20, ipadx=120, padx=10, pady=10)
#
# hello1.pack(ipady=20, ipadx=120, padx=10, pady=10, side='bottom')
#
# window.mainloop()

# Label
# title
# pack
# mainloop
# Tk()

class Products:
    def __init__(self, family: str) -> None:
        self.family = family
        self.name = None
        self.price = None
        self.amount = None
        self.products = []
        self.purchased = []
        self.remain = []

    def add(self, name, price, amount=1) -> list:
        self.name = name
        self.price = price
        self.amount = amount
        if not isinstance(self.name, str):
            raise TypeError(f"Iltimos, <class, 'str'> ma'lumot kiriting, {type(self.name)} emas.")

        def add_product():
            self.products.append(self.name)
            return self.products

        return add_product()

    def myproduct(self):
        return f"Xarid qilinmagan: {self.products}"

    def mypurchased(self, product: str) -> str:
        if product not in self.products:
            raise ValueError(f"Ro'yxatda '{product}' mahsuloti topilmadi.")

        if not isinstance(product, str):
            raise TypeError(f"Iltimos, <class, 'str'> ma'lumot kiriting, {type(product)} emas.")

        def inner_purchased():
            self.products.remove(product)
            self.remain.append(product)
            self.purchased.append(product)
            return f"Xarid qilindan: {self.remain}"

        return inner_purchased()


sabzavotlar = Products('Sabzavotlar')
sabzavotlar.add('Sabzi', 12345.23)
sabzavotlar.add('Kartoshka', 4532.90)
print(sabzavotlar.mypurchased('Kartoshka'))
print(sabzavotlar.myproduct())
