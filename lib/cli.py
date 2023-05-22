from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

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

    print("Welcome to the EDM Festival Finder!")
    print("Please enter your name to get started:")
    user_name = input(">>> ")
    clear()

    print(f"Welcome {user_name}!")
    print("Please enter your location to get started:")
    user_location = input(">>> ")
    clear()

    print("Here is a list of all the genres:")
    genre_options = session.query(Genre_Option)
    create_genre_options_table(genre_options)
    

    genre_option = None
    while not genre_option:
        genre_option_id = input('Please enter the ID of the genre you wish to look at: ')
        genre_option = session.query(Genre_Option).filter(Genre_Option.id == genre_option_id).one_or_none()
    
   
