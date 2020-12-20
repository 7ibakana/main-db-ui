import ui 
import database
from menu import Menu
from db import Db, Database

db = Database()

def main():

    while True:
        # what does the user want to do?
        # print menu
        task = input('What task? ') 

        if task == '1':
            add_artist()
        elif task == '2':
            add_artwork()
        elif task == '3':
            delete_artwork()


def create_menu():
    menu = Menu()
    menu.add_option('1', "Add artist", add_artist)
    menu.add_option('2', "Add artwork", add_artwork)
    menu.add_option('3', "Delete artwork", delete_artwork)
    menu.add_option('Q', "Exit", exit_program)
    return menu

def add_artist():
    # get input 
    name = ui.get_non_empty_string('Artist name? ')
    email = ui.get_non_empty_string('Artist email? ')
    email.add_artist(name, email)

def add_artwork():
    artName = ui.get_non_empty_string('\nName of artwork? ')
    artistName = ui.get_non_empty_string('Name of artist? ')
    artistName.add_artwork(artName, artistName) 

def delete_artwork():
    artName = ui.get_non_empty_string('\nArtwork to delete? ')
    artName.delete_artwork(artName)

def exit_program():
    ui.message('Goodbye!')

if __name__ == '__main__':
    main()
