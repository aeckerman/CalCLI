import click

@click.command()
@click.argument("eq")
def calc(eq):
	'''A simple CLI calculator...'''
	print(eval(eq))

if __name__ == '__main__':
	calc()