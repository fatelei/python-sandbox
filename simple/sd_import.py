#!/usr/bin/env python
#-*-coding: utf8-*-

import ast

FORBIDDEN_IMPORT = ['sys', 'os']

class SdImport(ast.NodeVisitor):
    def __init_(self):
        pass

    def visit_Import(self, stmt_import):
        for alias in stmt_import.names:
            if alias.name in FORBIDDEN_IMPORT:
                raise Exception('forbidden')
        super(SdImport, self).generic_visit(stmt_import)

if __name__ == '__main__':
    code = 'import sys'
    tree = ast.parse(code)
    sdimport = SdImport()
    try:
        sdimport.visit_Import(tree.body[0])
    except:
        print "killed by sandbox"
