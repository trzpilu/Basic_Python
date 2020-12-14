from faker import Faker

fake = Faker("pl_PL")

# deklaracja klasy BaseContact


class BaseContact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def label_length(self):
        return len(self.full_name)

    @property
    def contact_number(self):
        return self.phone

    def contact(self):
        return f"Wybieram numer {self.contact_number} i dzownię do {self.full_name}"


class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, phone, email, position, company, work_phone):
        super().__init__(first_name, last_name, phone, email)
        self.position = position
        self.company = company
        self.work_phone = work_phone

    @property
    def contact_number(self):
        return self.work_phone


def create_contacts(card_type, amount):
    cards = []
    for i in range(amount):
        if card_type == "base":
            cards.append(
                BaseContact(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    phone=fake.phone_number(),
                    email=fake.email(),
                )
            )
        elif card_type == "business":
            cards.append(
                BusinessContact(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    phone=fake.phone_number(),
                    position=fake.job(),
                    company=fake.company(),
                    work_phone=fake.phone_number(),
                    email=fake.email(),
                )
            )
    return cards


if __name__ == "__main__":

    card_type = input("What type of card(s) would you like to make? (Choose business or base) ")
    amount = int(input("How many cards would you like to create? (Choose number) "))

    if card_type == 'base':
        print("Generuję zwykłe kontakty")
        base_cards = create_contacts("base", amount)
        for card in base_cards:
            print("długość labelki: ", card.label_length)
            print(card.contact())
            print()

    elif card_type == 'business':
        print("Generuję kontakty biznesowe")
        business_cards = create_contacts("business", amount)
        for card in business_cards:
            print("długość labelki: ", card.label_length)
            print(card.phone, card.work_phone)
            print(card.contact())
            print()

    else:
            error = f"Error!"
            print(error)
            exit()