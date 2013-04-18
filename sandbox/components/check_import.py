#!/usr/bin/python
#-*-coding: utf8-*-

import ast

import config

def check_import(self, node_import):
    for name in node_import.names:
        if name.name in config.DENY_MODULES:

