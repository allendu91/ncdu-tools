# ncdu-tools.py
import click
import os
import subprocess
import heapq

@click.command()
@click.option('--count', default=1, help='Number of files.')
@click.option('--path', default=os.getcwd, help='The person to greet.')
def find_big_files(count, path):
    """Simple program that using ncdu to find big files"""
    if not os.path.isdir(path):
        click.echo('Path is illega!!')
        return
    x = subprocess.check_output(['ncdu',  path,'-o-'])
    click.echo(x)
if __name__ == '__main__':
    find_big_files()