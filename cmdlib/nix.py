from subprocess import check_output as run, Popen
from subprocess import *
import os
from re import findall
from config import EXTENSION

"""
def listdir(path):
    REG = '(?P<p>.).*"(?P<n>.+)"\n'
    output = run(('ls', '-lQL', '--group-directories-first', path))
    for type, name in findall(REG, output):
        yield(type, name)
"""

def listdir(path, show_hidden=False):
    REG = '(?P<a>[a-zA-Z\-]+) +(?P<b>[0-9]+) +(?P<c>[^ ]+) +(?P<d>[^ ]+) +(?P<e>[^ ]+) +(?P<f>[^ ]+) +(?P<g>[^ ]+) +(?P<h>[^ ]+) +"(?P<i>.+)"\n'
    output = run(('ls', '-lQLh%s' % ('A' if show_hidden else ''), '--group-directories-first', path))
    return findall(REG, output)

def cp(origin, destin):
    """

    """
    args = ('cp', '-R') + origin + (destin,)
    output = run(args)
    return output



def rm(args):
    output = run(('rm', '-fr') + args)
    return output

def mv(args, dst):
    output = run(('mv', ) + args + (dst, ))
    return output

def create_text_file(filename):
    output = run(('echo', '', '>>', filename))
    return output

def open_with(filename):
    try:
        app = EXTENSION[filename.rsplit('.', 1)[1]]
    except:
        app = EXTENSION['default']
    print '%s %s' % (app, filename)
    Popen([app, filename], shell=False)

def open_with_default(filename):
    app = EXTENSION['default']

    print '%s %s' % (app, filename)
    Popen([app, filename], shell=False)

def call(cmd):
    Popen([cmd], shell=False)

def mkdir(dirname):
    output = run(('mkdir', dirname))
    return output








