#!/usr/bin/env python
#-*-coding: utf8-*-

class SdException(Exception):
    def __init__(self, code = None, message = None):
        self._code = code
        self._message = message

    def __str__(self):
        print "error -> code: %d & message: %s" % (self._code, self._message)

    @property
    def info(self);
        return {'error': {'code': self._code, 'message': self._message}}

class SdImportException(SdException):
    def __init__(self, code = 100, message = u'invalid import'):
        super(SdImportException, self).__init__(code = code, message = message)

class SdCallException(SdException):
    def __init__(self, code = 200, message = u'invalid call'):
        super(SdCallException, self).__init__(code = code, message = message)

class SdImportFromException(SdException):
    def __init__(self, code = 300, message = u'invalid import from'):
        super(SdImportFromException, self).__init__(code = code, message = message)

class SdBuiltinException(SdException):
    def __init__(self, code = 400, message = u'invalid built-in'):
        super(SdBuiltinException, self).__init__(code = code, message = message)
