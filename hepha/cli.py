import click

@click.group()
def cli():
    """
    Hepha-CLI (abreviatura de Hephaestus Command Line Interface),
    inspirado en Hephaestus, el legendario dios griego de la forja
    y el fuego, es una herramienta para simplificar y optimizar su
    interacción con AWS CLI v2. 
    """
    pass

@click.command()
def create_api():
    """Crea una nueva API Gateway."""
    click.echo("Creando API Gateway...")

@click.command()
def modify_api():
    """Modifica una API Gateway existente."""
    click.echo("Modificando API Gateway...")

@click.command()
def create_websocket_api():
    """Crea una nueva WebSocket API Gateway."""
    click.echo("Creando WebSocket API Gateway...")

@click.command()
def modify_websocket_api():
    """Modifica una WebSocket API Gateway existente."""
    click.echo("Modificando WebSocket API Gateway...")

# Agrega los comandos al grupo cli
cli.add_command(create_api)
cli.add_command(modify_api)
cli.add_command(create_websocket_api)
cli.add_command(modify_websocket_api)

# Punto de entrada principal
if __name__ == "__main__":
    cli()
