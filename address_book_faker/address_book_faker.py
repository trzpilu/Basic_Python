from faker import Faker
import operator

fake = Faker()

card_list = []


# Create BookAddress objects with first and last names, company, job title, and email.

class BookAdress:
    def __init__(self, first_name, last_name, company, job, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.job = job
        self.email = email

    def __str__(self):
        return f'{self.first_name, self.last_name, self.company, self.job, self.email}'
    
    def __repr__(self):
        return 'BookAddress(first_name: %s, last_name: %s, company: %s, job: %s, email: %s)' % (self.first_name, self.last_name, self.company, self.job, self.email)
    
    def contact(self):
        return f"Kontaktuj się z: {self.first_name} {self.last_name}, na stanowisku: {self.job}, e-mail: {self.email}"

    @property
    def count_letters(self):
        return sum([len(self.first_name), len(self.last_name), 1])

class BaseContact(BookAdress):
    def __init__(self, tel_priv, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.phone_number = tel_priv
    
    def contact(self):
        return f"Wybieram prywatny numer {self.phone_number} i dzwoniuę do {self.first_name} {self.last_name}."
    
    @property
    def label_length(self):
        return sum([len(self.first_name), len(self.last_name)])

class BusinessContact(BookAdress):
    def __init__(self, tel_pub, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.phone_number = tel_pub
    
    def contact(self):
        return f"Wybieram numer {self.phone_number} i dzwoniuę do {self.first_name} {self.last_name}."
    
    @property
    def label_length(self):
        return sum([len(self.first_name), len(self.last_name)])

def create_contacts():
    my_type = input("type:")
    copies = int(input("copies:"))

    if my_type == "base":
        for contact in range(copies):
            contact = BaseContact(
                first_name=fake.first_name(), last_name=fake.last_name(),
                company=fake.company(), job=fake.job(), email=fake.email(),
                tel_priv=fake.phone_number()
                )
            card_list.append(contact)
            print() 
            print((contact))
            print(contact.contact())

    elif my_type == "business":
        for contact in range(copies):
            contact = BusinessContact(
                first_name=fake.first_name(), 
                last_name=fake.last_name(),
                company=fake.company(), 
                job=fake.job(), 
                email=fake.email(),
                tel_pub=fake.phone_number()
                )
            card_list.append(contact)
            print()
            print((contact))
            print(contact.contact())
            return card_list
    
    elif my_type == "by_first":
        for contact in range(copies):
            card = BookAdress(
                first_name = fake.first_name(), 
                last_name = fake.last_name(), 
                company = fake.company(), 
                job = fake.job(), 
                email = fake.email()
                )
            card_list.append(card)
        print("List sorted by first name:")
        by_first = sorted(card_list, key=operator.attrgetter('first_name'))
        card_list = by_first
        print(card_list)
        return card_list

    elif my_type == "by_last":
        for contact in range(copies):
            card = BookAdress(
                first_name = fake.first_name(), 
                last_name = fake.last_name(), 
                company = fake.company(), 
                job = fake.job(), 
                email = fake.email()
                )
            card_list.append(card)
        print("List sorted by last name:")
        by_last = sorted(card_list, key=operator.attrgetter('last_name'))
        card_list = by_last
        print(card_list)
        return card_list

    elif my_type == "by_email":
        for contact in range(copies):
            card = BookAdress(
                first_name = fake.first_name(), 
                last_name = fake.last_name(), 
                company = fake.company(), 
                job = fake.job(), 
                email = fake.email()
                )
            card_list.append(card)
        print("List sorted by email:")
        by_email = sorted(card_list, key=operator.attrgetter('email'))
        card_list = by_email
        print(card_list)
        return card_list

if __name__ == "__main__":
    create_contacts()