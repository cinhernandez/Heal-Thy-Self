from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from db.models import (Base, Artist, Festival)


engine = create_engine('sqlite:///edm.db')
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

    print("Welcome to the EDM Festival Finder!")
    print("Please enter your name to get started:")
    user_name = input(">>> ")
    clear()

    print(f"Welcome {user_name}!")
    print("Please enter your location to get started:")
    user_location = input(">>> ")
    clear()

    print("Choose an option")
    print("111\t=>\tSee all EDM Festivals in your area")
    print("222\t=>\tSee all Artists")
    print("333\t=>\tSee all Accommodations")
    print("444\t=>\tSee all Festivals")
    print("555\t=>\tSee all Festivals with Accommodations")
    print("666\t=>\tSee all Festivals with Artists")
    print("777\t=>\tSee all Festivals with Artists and Accommodations")
    print("888\t=>\tSee all Festivals with Artists and Accommodations in your area")
    print("999\t=>\tSee all Festivals with Artists and Accommodations in your area and their prices")

    user_input = input(">>> ")

    if user_input == "111":
        #clear()
        print("Here are all the Genres:")
        for genre_optiions in session.query(Genre).all():
            print(genre_optiions.name)

    elif user_input == "222":
        clear()
        print("Here are all the Artists:")
        for artists in session.query(Artist).all():
            print(artists.name)
        print("Press any key to exit")
        input(">>> ")
        clear()
    
    # elif user_input == "333":
    #     clear()
    #     print("Here are all the Accommodations:")
    #     for accommadation in session.query(Accommadation).all():
    #         print(accommadation.name)
    #     print("Press any key to exit")
    #     input(">>> ")
    #     clear()

    elif user_input == "444":
        clear()
        print("Here are all the Festivals:")
        for festival in session.query(Festival).all():  
            print(festival.name)    
        print("Press any key to exit")
        input(">>> ")
        clear()

    elif user_input == "555":
        clear()
        print("Here are all the Festivals with Accommodations:")
        for festival in session.query(Festival).all():
            if festival.accommadation:
                print(festival.name)
        print("Press any key to exit")
        input(">>> ")
        clear()

    else:
        print("Invalid input")
        print("Press any key to exit")
        input(">>> ")
        clear()

    print("Thank you for using the EDM Festival Finder!")
    print("Goodbye!")
    print("Press any key to exit")
    input(">>> ")
    clear()

