import argparse

from utils.get_name_dirs_from_dir import get_name_dirs_from_dir
from utils.get_file_from_dir import get_file_from_dir
from utils.import_file_dynamically import import_module_dynamically


def cli():
    """Herramienta para crear funciones lambda en AWS"""
    parser = argparse.ArgumentParser(description=cli.__doc__)

    names_commands = get_name_dirs_from_dir('commands')
    parser.add_argument(
        'command',
        type=str,
        help='an integer for the accumulator',
    )
    print(names_commands)

    args = parser.parse_args()

    args = vars(args)
    print(args)

    command = args.get('command')

    if not command:
        print('Debe ingresar un comando')
        return

    if command not in names_commands:
        print('El comando ingresado no existe')
        print('Los comandos disponibles son:')
        print(names_commands)
        return
    
    file = get_file_from_dir(f'commands/{command}/main.py')

    Module = import_module_dynamically(file)

    class_executed = Module()
    class_executed.handle()


# Punto de entrada principal
if __name__ == "__main__":
    cli()
