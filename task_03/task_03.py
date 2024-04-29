import sys
from pathlib import Path
from colorama import Fore, Style

path = Path(sys.argv[1])


# builds a folder tree of the provided path
def structure_visualisation(path_to_folder, space=0):
    try:
        for item in path_to_folder.iterdir():
            if item.is_dir():
                print(f"{'  ' * space}\U0001f4c1 " + Fore.CYAN + f"{item.name}" + Style.RESET_ALL)
                structure_visualisation(item, space+1)
            elif item.is_file():
                print(Fore.GREEN + f"{'  ' * space}\U0001f4dc {item.name}")
    except (FileNotFoundError, PermissionError)as error:
        print(error)


if __name__ == '__main__':
    structure_visualisation(path)
