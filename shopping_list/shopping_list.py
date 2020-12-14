print("Lista zakupów")
zakupy_dict = {
    "piekarnia": ["chleb", "bagietka", "sernik"],
    "warzywniak": ["ogórki", "papryka", "rzodkiewki"],
    "delikatesy": ["szynka", "halva", "gnocci"]
    }
for sklep, rzeczy in zakupy_dict.items():
    lista_zakupów = f"Idę do {sklep.capitalize()}, kupuję tam {rzeczy[0].capitalize()}, {rzeczy[1].capitalize()} i {rzeczy[2].capitalize()}."
    print(lista_zakupów)
    count = sum(len(rzeczy) for rzeczy in zakupy_dict.values())
total = f"W sumie kupuję {count} produktów."
print(total)