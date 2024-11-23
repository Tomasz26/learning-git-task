shopping_dict = {
    "warzywniak": ['marchew', 'seler', 'rukola'],
    "piekarnia": ['chleb', 'pączek', 'bułki']
}

i = 0

print("Lista zakupów")

for store, things in shopping_dict.items():
    capitalized_things = [item.capitalize() for item in things]
    print(f"Idę do {store.capitalize()}, kupuję tu następujące rzeczy: {capitalized_things}")