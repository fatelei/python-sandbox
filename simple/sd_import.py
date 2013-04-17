#!/usr/bin/env python
#-*-coding: utf8-*-

import ast
import sys

FORBIDDEN_IMPORT = ['sys', 'os']

class SdImport(ast.NodeVisitor):
    def __init_(self):
        pass

    def visit_Import(self, stmts):
        for stmt in stmts:
            if isinstance(stmt, ast.Import):
                for alias in stmt.names:
                    if alias.name in FORBIDDEN_IMPORT:
                        raise Exception('forbidden')
            super(SdImport, self).generic_visit(stmt)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "usage %s filename" % sys.argv[0]
    else:
        filename = sys.argv[1]
        suffix = filename.split(".")[1]
        if suffix != 'py':
            print "%s is not a python file" % filename
        else:
            try:
                f = file(filename, 'r')
                data = f.read()
                f.close()
                tree = ast.parse(data)
                try:
                    sdimport = SdImport()
                    sdimport.visit_Import(tree.body)
                    exec(data)
                except:
                    print "Not allowed exec"
            except IOError:
                print 'file is not exists'
