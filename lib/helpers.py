from db.models import (Base, Festival, Add_To_Cart, Genre_Option)
import time

YES = ['y', 'ye', 'yes']
NO = ['n', 'no']

def print_slowly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def print_kind_of_slow(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.10)
    print()

def create_genre_options_table(genre_options):
    print('♪♫♪' * 13)
    print(f'|ID  |GENRE{" " * 39}')
    print('=' * 40)
    for genre in genre_options:
        id_spaces = 4 - len(str(genre.id))
        genre_spaces = 43 - len(genre.genre)
        print(f'=>  {genre.id}{" " * id_spaces}|{genre.genre}{" " * genre_spaces}')
    print('♪♫♪' * 13)



def create_festivals_table(festivals):
    print('𓍊𓋼𓍊𓋼𓍊' * 25)
    print(f'    {"ID":<5}|{"Festival Name":<30}|{"Date":<25}|{"Location":<20}|{"Price ($)":<10}')
    print('=' * 110)
    for festival in festivals:
        print(f' => {festival.id:<5}|{festival.name:<30}|{festival.date:<25}|{festival.location:<20}|$ {festival.price:<10}')
    print('𓍊𓋼𓍊𓋼𓍊' * 25)

def get_festivals_by_genre(genre_option):
    return genre_option.festivals if genre_option else []


def fill_cart(session, genre_option):
    add_to_cart = Add_To_Cart()
    festival_id = input('Please enter the ID of the festival you want to add to your cart: ')
    while festival_id:
        festival = session.query(Festival).filter(Festival.id == festival_id).first()
        if festival:
            add_to_cart.festivals.append(festival)
            print('Festival added to cart.\n')
        else:
            festival_id = input('Please enter a valid festival ID: ')
            continue

        yes_no = None
        while yes_no not in YES + NO:
            yes_no = input('Would you like to add another festival to your cart? (Y/n) ')
            if yes_no.lower() in YES:
                festival_id = input('Please enter the ID of the next festival: ')
            elif yes_no.lower() in NO:
                festival_id = None
            else:
                return add_to_cart



def show_cart(add_to_cart):
    print('-' * 50)
    print(f'|ID  |NAME{" " * 29}|PRICE{" " * 4}|')
    print('-' * 50)
    for festival in sorted(add_to_cart.festivals, key=lambda f: f.id):
        id_spaces = 4 - len(str(festival.id))
        name_spaces = 33 - len(festival.name)
        price_spaces = 8 - len(str(festival.price))
        output_string = f'|{festival.id}{" " * id_spaces}|' + \
            f'{festival.name}{" " * name_spaces}|' + \
            f'${festival.price}{" " * price_spaces}|'
        print(output_string)
    cart_total = sum([f.price for f in add_to_cart.festivals])
    total_spaces = 8 - len(str(cart_total))
    print(f'|{" " * 5}TOTAL{" " * 28}|${cart_total}{" " * total_spaces}|')
    print('-' * 50)

def remove_from_cart(session, add_to_cart):
    yes_no = input('Would you like to remove any festivals from your cart? (Y/n) ')
    while yes_no in YES:
        festival_id = input('Please enter the ID of the festival you would like to remove: ')
        festival = session.query(Festival).filter(Festival.id == festival_id).first()
        if festival in add_to_cart.festivals:
            add_to_cart.festivals.remove(festival)
            print('Festival removed from cart.')
        else:
            print('Festival not found.')
        print('Here are the festivals in your cart:')
        show_cart(add_to_cart)
        yes_no = input('Would you like to remove another festival from your cart? (Y/n) ')
        
def collect_payment(cart_total):
    paid = False
    while not paid:
        payment_method = input('Will you be paying with cash or card? ')
        if payment_method.lower() == 'card':
            print('Processing...\n')
            paid = True
        elif payment_method.lower() == 'cash':
            payment = input('How much will you be paying with today? ')
            try:
                payment = float(payment)
                change = payment - cart_total
                print(f'Your change is ${change:.2f}\n')
                paid = True
            except:
                print('Please enter a valid number.')
        else:
            print('Please select a valid payment method.')