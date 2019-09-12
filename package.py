# -*- coding: utf-8 -*-

name = 'sg_python_api'

version = "3.1.1.0"

requires = ['python']

tools = []

build_command = "python {root}/rezbuild.py {install}"


def commands():
    env.PYTHONPATH.append("{root}")


timestamp = 1568257729

format_version = 2
