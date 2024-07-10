mkdir directory
touch notmine
chmod 111 notmine
# NotADirectoryError:
python -c 'import zundaerror; import os; os.rmdir("notmine")'
# IsADirectoryError:
python -c 'import zundaerror; import os; os.remove("directory")'
# PermissionError:
python -c 'import zundaerror; open("notmine")'
# FileNotFoundError:
python -c 'import zundaerror; open("hhhh")'
# NameError:
python -c 'import zundaerror; print(hhhh)'
# IndexError:
python -c 'import zundaerror; print("hhhh"[8])'
# ZeroDivisionError:
python -c 'import zundaerror; 8/0'
# AssertionError:
python -c 'import zundaerror; assert False'
# AttributeError:
python -c 'import zundaerror; zundaerror.hoge'
# ModuleNotFoundError:
python -c 'import zundaerror; import hoge'
# KeyError:
python -c 'import zundaerror; {}["hoge"]'
# RecursionError:
python -c '''import zundaerror
def rec(x):
    rec(4)
rec(4)
'''
# TypeError:
python -c '''import zundaerror
def rec(x):
    pass
rec()
'''
# FileExistsError:
python -c '''import zundaerror; import os; os.mkfifo("directory")'''
rm -r directory
chmod 777 notmine
rm notmine

####################
# Errors which is hard to test
####################
# ProcessLookupError:
# TimeoutError:
# InterruptedError:
# ConnectionRefusedError:
# ConnectionAbortedError:
# BrokenPipeError:
# ChildProcessError:
# BlockingIOError:
# UnicodeEncodeError:
# UnicodeDecodeError:
# UnboundLocalError:
# OverflowError:
# ArithmeticError:
# EOFError:
# ImportError:
# KeyboardInterrupt:
# MemoryError:
# BufferError:
# LookupError:
# OSError:
# ReferenceError:
# RuntimeError:
# IndentationError:
# TabError:
# SystemError:
# SyntaxError:

