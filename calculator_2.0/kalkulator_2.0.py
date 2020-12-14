# KALKULATOR_2.PY
# ================

# Importy
# ================
import logging
logging.basicConfig(level = logging.INFO, format='%(message)s')

# Definicje
# ===============

# my_vars: pobiera i zwraca 'a' i 'b'
def my_vars():  
    a = int(input("Podaj składnik 1. "))
    b = int(input("Podaj składnik 2. "))
    return a, b

# add: zwraca wynik dodawania
def add(a, b):
    result = a + b
    return result

# subtract: zwraca wynik odejmowania
def subtract(a,b):
    result = a - b
    return result

# multiply: zwraca wynik mnożenia
def multiply(a,b):
    result = a * b
    return result

# divide: zwraca wynik dzielenia
def divide(a,b):  
    result = a / b
    return result

# print_result: Drukuje każdy wynik    
def print_result(result):
    print(f"Wynik to {result}")

#  error: Drukuje że wybrana opcja jest niewłaściwa i sugeruje zakres opcji od 1 - 4.
def error(choose):
    result_error = f"{choose} is not an option. Please choose options [1 - 4]"
    print(result_error)



# Użycia
# ===============    
choose = int(input("Podaj działanie, posługując się liczbą:" + 
    "1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))

if (choose >=1 and choose <=4):
    
    a, b = my_vars()                        # 0.1 Aktywujemy my_vars by pobrać i zwrócić a i b
    
    if choose == 1:                         # 1.1 Jeśli wybierzemy '1'
        logging.info(f"Dodaję {a} i {b}")   # 1.2 Logujemy operację
        add(a, b)                           # 1.3 Aktywujemy add(a,b), by zalogować operację i otrzymać wynik
        result = add(a, b)                  # 1.4 Zapisujemy 'result'
        print_result(result)                # 1.5 Aktywujemy print_result(result), by wydrukowć wynik.

    elif choose == 2:                       # 2.1 Jeśłi wybierzemy '2'
        logging.info(f"Odejmuję {b} od {a}")# 2.2 Logujemy operację
        subtract(a, b)                      # 2.3 Aktywujemy subtract(a,b), by zalogować operację i otrzymać wynik
        result = subtract(a, b)             # 2.4 Zapisujemy 'result'
        print_result(result)                # 2.5 Aktywujemy print_result(result), by wydrukowć wynik.
                                            # itp. itd. ...
    elif choose == 3:                       # 3.1 ...
        logging.info(f"Mnożę {a} i {b}")
        multiply(a, b)
        result = multiply(a, b)
        print_result(result)
            
    elif choose == 4:                        # 4.1 ...
        logging.info(f"Dzielę {a} przez {b}")
        divide(a, b)
        result = divide(a, b)
        print_result(result)
                    
else:                        # 5.1 W przypadku wybrania złej opcji poza [1 - 4] 
    error(choose)            # 5.2 Drukujemy wiadomość o błędzie.