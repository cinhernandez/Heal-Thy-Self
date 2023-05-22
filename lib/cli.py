from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import time

from helpers import *
from db.models import (Base, Genre_Option, Festival, Add_To_Cart)


engine = create_engine('sqlite:///music_festivals.db')
session = sessionmaker(bind=engine)()

terminal_width = os.get_terminal_size().columns
def clear(): return os.system('tput reset')


if __name__ == '__main__':

    print('𓍊𓋼𓍊𓋼𓍊' * int(terminal_width / 6))
    print('''



██████╗░██╗░░░░░██╗░░░██╗██████╗░  ██████╗░░█████╗░██████╗░████████╗░█████╗░██╗░░░░░
██╔══██╗██║░░░░░██║░░░██║██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║░░░░░
██████╔╝██║░░░░░██║░░░██║██████╔╝  ██████╔╝██║░░██║██████╔╝░░░██║░░░███████║██║░░░░░
██╔═══╝░██║░░░░░██║░░░██║██╔══██╗  ██╔═══╝░██║░░██║██╔══██╗░░░██║░░░██╔══██║██║░░░░░
██║░░░░░███████╗╚██████╔╝██║░░██║  ██║░░░░░╚█████╔╝██║░░██║░░░██║░░░██║░░██║███████╗
╚═╝░░░░░╚══════╝░╚═════╝░╚═╝░░╚═╝  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝
    

    
    
    
    
    ''')
    print('𓍊𓋼𓍊𓋼𓍊' * int(terminal_width / 6))

    print_slowly("Welcome to the EDM Festival Finder!")
    print_slowly("Please enter your name to get started:")
    user_name = input(">>> ")
    clear()

    print_kind_of_slow(f"Welcome {user_name}!")
    print_slowly("Please enter your location to get started:")
    user_location = input(">>> ")
    clear()

    print_slowly("Here is a list of all the genres:")
    genre_options = session.query(Genre_Option)
    create_genre_options_table(genre_options)
    

    genre_option = None
    while not genre_option:
        genre_option_id = input('Please enter the ID of the genre you wish to look at: ')
        genre_option = session.query(Genre_Option).filter(Genre_Option.id == genre_option_id).one_or_none()
    
    if genre_option:
        clear()
        print_slowly(f"Genre selected: {genre_option.genre}")
        festivals = get_festivals_by_genre(genre_option)
    if festivals:
        print_slowly(f"Here are the festival events for the genre '{genre_option.genre}':")
        create_festivals_table(festivals)
    else:
        print("No festival events found for the selected genre.")


    print_slowly("Return to the main menu? => [exit] or [add] to add festival tickets")
    user_input = input(">>> ")
    if user_input == "exit":
        clear()
    elif user_input == "add":
        # Get the selected genre option
        genre_option = None
        while not genre_option:
            genre_option_id = input('Please enter the ID of the genre you wish to look at: ')
            genre_option = session.query(Genre_Option).filter(Genre_Option.id == genre_option_id).one_or_none()

        if genre_option:
            clear()
            print_slowly(f"Genre selected: {genre_option.genre}")
            festivals = get_festivals_by_genre(genre_option)
            if festivals:
                print_slowly(f"Here are the festival events for the genre '{genre_option.genre}':")
                create_festivals_table(festivals)
                add_to_cart = fill_cart(session, genre_option)  # Add festival tickets to the cart
                if add_to_cart:
                    show_cart(add_to_cart)  # Display the updated cart contents
            else:
                print("No festival events found for the selected genre.")
    else:
        print("Thank you for using Festival Finder.")



    

#not sure where it will go
        
    #  print(f"Here are all the festivals that are {genre_option.genre}:")
    # festivals = session.query(Festival).filter(Festival.genres.any(Genre_Option.id == genre_option.id))
    # for festival in festivals:
    #     print(festival.name)
    # print("Please enter the name of the festival you wish to attend:")
    # festival_name = input(">>> ")
    # clear()
    # festival = session.query(Festival).filter(Festival.name == festival_name).one_or_none()
    # if not festival:
    #     print('Invalid festival name. Please try again.')
    # else:
    #     print(f"Here is the festival you selected: {festival.name}")
    #     print(f"Here is the location of the festival: {festival.location}")
    #     print(f"Here is the date of the festival: {festival.date}")
    #     print(f"Here is the price of the festival: {festival.price}")
    #     print(f"Here is the genre of the festival: {genre_option.genre}")
    #     print("Would you like to add this festival to your cart?")
    #     user_input = input(">>> ")
    #     if user_input == "yes":
    #         fill_cart(user_name, festival_name, festival.price)
    #         print("Here is your cart:")
    #         show_cart(user_name)
    #         print("Would you like to remove this festival from your cart?")
    #         user_input = input(">>> ")
    #         if user_input == "yes":
    #             remove_from_cart(user_name, festival_name)
    #             print("Here is your cart:")
    #             show_cart(user_name)
    #         else:
    #             print("Here is your cart:")
    #             show_cart(user_name)
    #     else:
    #         print("Here is your cart:")
    #         show_cart(user_name)
    # print("Would you like to checkout?")
    # user_input = input(">>> ")
    # if user_input == "yes":
    #     collect_payment(user_name)
    #     print("Thank you for using the EDM Festival Finder!")
    # else:
    #     print("Thank you for using the EDM Festival Finder!")