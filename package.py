# -*- coding: utf-8 -*-

name = 'sg_python_api'

version = "3.1.1.2"

requires = ['python']

tools = []

build_command = "python {root}/rezbuild.py {install}"


def commands():
    env.PYTHONPATH.append("{root}")


timestamp = 1568257732

format_version = 2
