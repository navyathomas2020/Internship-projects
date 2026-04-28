items = ["pen", "book", "bag", "pencil", "box"]
prices = {"pen": 10, "book": 50, "bag": 300, "pencil": 5, "box": 120}

print("Items and Prices:")
for item in items:
    print(item, ":", prices.get(item))

prices["book"]=100
print(prices)

items.remove("bag")
print(items)

max_item = max(prices,key=prices.get)
print("\nMost expensive item:", max_item, ":", prices[max_item])

total = sum(prices.values())
print("\nTotal price of all items:", total)

print("\n items with prices greater than 100")
for item in prices:
    if prices[item] > 100:
        print(item, ":", prices[item])

search = "bag"
if search in prices:
    print("\nPrice of", search, "is:", prices[search])
else:
    print("\nItem not found")

