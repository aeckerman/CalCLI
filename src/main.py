import click

@click.group()
def calc():
	'''A simple CLI calculator...'''
	pass

@click.command()
@click.argument('int1')
@click.argument('int2')
def add(int1, int2):
	'''Addition action.'''
	click.echo(int(int1) + int(int2))

@click.command()
@click.argument('int1')
@click.argument('int2')
def sub(int1, int2):
	'''Subtraction action.'''
	click.echo(int(int1) - int(int2))

@click.command()
@click.argument('int1')
@click.argument('int2')
def mul(int1, int2):
	'''Multiplication action.'''
	click.echo(int(int1) * int(int2))

@click.command()
@click.argument('int1')
@click.argument('int2')
def div(int1, int2):
	'''Division action.'''
	click.echo(int(int1) / int(int2))

@click.command()
@click.argument('int1')
@click.argument('int2')
def mod(int1, int2):
	'''Modulus action.'''
	click.echo(int(int1) % int(int2))

calc.add_command(add)
calc.add_command(sub)
calc.add_command(mul)
calc.add_command(div)
calc.add_command(mod)

if __name__ == '__main__':
	calc()