import inquirer
import boto3


def create_lambda(nombre, path, runtime, arquitectura):
    questions = [
        inquirer.Text('name', message="Ingrese el nombre de la función lambda"),
        inquirer.Text('path', message="Ingrese el path de la función lambda"),
        inquirer.List('runtime',
                      message="Seleccione la versión de Python",
                      choices=['Python 3.10 (recomendado)', 'Python 3.9', 'Python 3.8'],
                      carousel=True
                      ),
        inquirer.List('architecture',
                      message="Seleccione la arquitectura",
                      choices=['x86_64', 'arm64'],
                      carousel=True
                      ),
    ]

    answers = inquirer.prompt(questions)
    print(answers)
