#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

print("Content-type: text/plain")
print()

form = cgi.FieldStorage()
operands = [int(x) for x in form.getlist('operand')]
print(f"Sum = {sum(operands)}")
