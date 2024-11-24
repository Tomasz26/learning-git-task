shopping_dict = {
    "warzywniak": ['marchew', 'seler', 'rukola'],
    "piekarnia": ['chleb', 'pączek', 'bułki'],
    "miesny": ['szynka', 'kielbasa', 'schab']
}

i = 0

print("Lista zakupów")

for store, things in shopping_dict.items():
    capitalized_things = [item.capitalize() for item in things]
    print(f"Idę do {store.capitalize()}, kupuję tu następujące rzeczy: {capitalized_things}")
    i += len(things)

print(f"W sumie kupuję {i} produktów")

for i in range(0, 10):
    print("Mmmm, spam, spam")

print("Serdecznie gorąco pozdrawiam mentora, życzę miłego niedzielnego wieczoru")