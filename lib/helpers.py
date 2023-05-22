from db.models import (Base, Festival, Add_To_Cart, Genre_Option)

def create_genre_options_table(genre_options):
    print('-' * 50)
    print(f'|ID  |GENRE{" " * 39}|')
    print('-' * 50)
    for genre in genre_options:
        id_spaces = 4 - len(str(genre_options.id))
        genre_spaces = 43 - len(genre_options.genre)
        print(f'|{genre_options.id}{" " * id_spaces}|{genre_options.genre}{" " * name_spaces}|')
    print('-' * 50)