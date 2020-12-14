import logging
logging.basicConfig(level = logging.INFO, format='%(message)s')

operation = int(input("Podaj działanie, posługując się liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))

if (operation >= 1 and operation <= 4):
    a = int(input("Podaj składnik 1. "))
    b = int(input("Podaj składnik 2. "))
    
    if operation == 1:
        result = a + b
        logging.info(f"Dodaję {a} i {b}")
    
    elif operation == 2:
        result = a - b
        logging.info(f"Odejmuję {b} od {a}")  
    
    elif operation == 3:
        result = a * b
        logging.info(f"Mnożę {a} i {b}")
    
    elif operation == 4:
        result = a / b
        logging.info(f"Dzielę {a} przez {b}")
    
    print(f"Wynik to {result}")

else:
    result = f"{operation} is not an option. Please choose options [1 - 4]"
    print(result)
