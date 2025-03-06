import sys
import logging
logging.basicConfig(level=logging.DEBUG)

from decimal import Decimal, getcontext

getcontext().prec = 50  

calculation = None
choice = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
if choice == '1':
    num_1 = Decimal(input("Wybrałeś dodawanie, podaj pierwszą liczbę: "))
    num_2 = Decimal(input("Podaj drugą liczbę: "))
    calculation = num_1 + num_2
elif choice == '2':
    num_1 = Decimal(input("Wybrałeś odejmowanie, podaj pierwszą liczbę: "))
    num_2 = Decimal(input("Podaj drugą liczbę: "))
    calculation = num_1 - num_2
elif choice == '3':
    num_1 = Decimal(input("Wybrałeś mnożenie, podaj pierwszą liczbę: "))
    num_2 = Decimal(input("Podaj drugą liczbę: "))
    calculation = num_1 * num_2
elif choice == '4':
    num_1 = Decimal(input("Wybrałeś dzielenie, podaj pierwszą liczbę: "))
    num_2 = Decimal(input("Podaj druga liczbę: "))
    calculation = num_1 / num_2

if __name__ == "__main__":
    logging.debug("Wykonuje działanie na następujących liczbach: %.2f %.2f" % (num_1, num_2))
    logging.debug(" Wynik to: %.2f" % calculation)