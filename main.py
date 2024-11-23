shopping_dict = {
    "warzywniak": ['marchew', 'seler', 'rukola'],
    "piekarnia": ['chleb', 'pączek', 'bułki']
}

i = 0

print("Lista zakupów")

for store, things in shopping_dict.items():
    print(f"Idę do {store.capitalize()}, kupuję tu następujące rzeczy: {shopping_dict[store]}")