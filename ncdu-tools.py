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
    # 执行ncdu命令，-o-将标准输出写入控制台
    res = subprocess.check_output(['ncdu',  path,'-o-'], universal_newlines=True)
    res = res.split('\n')
    res.pop(0)
    res_dict = []
    for i in res:
        tmp = eval('{'+i.split('{')[1].split('}')[0]+'}')
        # 排除目录
        if '/' in tmp['name']:
            continue
        res_dict.append(tmp)
    # 利用大顶堆排序
    end = heapq.nlargest(count,res_dict,key=lambda k: (k.get('asize', 0)))
    click.echo("name    size    path")
    for i in end:
        message = i['name']+'    '+str(i['asize'])+'    '+str(i['ino'])
        click.echo(message)
if __name__ == '__main__':
    find_big_files()