# default paramaterlarning ustunik tomonlari
def cost_produc(item, price, count=1):
    total_price = price * count
    return f"{count} {item} cost ${total_price}."


result = cost_produc('Pen', 1.25, 4)
print(result)


# funktsiya yaratilyotganda kalit=qiymat dan o'ng tomonda pozitsion formal paramatr uzatib bo'lmaydi.
# def cost_produc(count=1, item, price):
#     total_price = price * count
#     return f"{count} {item} cost ${total_price}."


