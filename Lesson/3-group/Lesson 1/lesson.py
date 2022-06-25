class Products:
    def __init__(self, family:str) -> None:
        self.family = family
        self.products = []
        self.purchased = []
        self.remain = []

    def add(self, name, price, amount=1) -> list:
        self.name = name
        self.price = price
        self.amount = amount
        if not isinstance(self.name, str):
            raise TypeError(f"Iltimos, <class, 'str'> ma'lumot kiriting, {type(product)} emas.")
        
        def add_product():
            self.products.append(self.name)
            return self.products

        return add_product()

    def myprod(self):
    	return f"{self.family}\n {self.products}"


    def purchased(self, product:str) ->list:

    	# print(self.products)
    	
    	if product not in self.products:
            raise ValueError(f"Ro'yxatda '{product}' mahsuloti topilmadi.")
		
		if not isinstance(product, str):
            raise TypeError(f"Iltimos, <class, 'str'> ma'lumot kiriting, {type(product)} emas.")

        def inner_purchased():
            self.products.remove(product)
            self.sold.append(product)
            self.purchased.append(product)
            return self.remain

        return inner_purchased()


sabzavotlar = Products('Sabzavotlar')
sabzavotlar.add('Sabzi', 12345.23)
sabzavotlar.add('Kartoshka', 4532.90)
print(sabzavotlar.purchased('Kartoshka'))
print(sabzavotlar.myprod())