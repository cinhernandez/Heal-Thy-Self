from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from db.models import (Base, Artist, Accommadation, Festival)


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
