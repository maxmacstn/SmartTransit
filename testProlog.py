from pyswip import Prolog


prolog = Prolog()
prolog.consult("test.pl")



print(list(prolog.query("path(mochit, X)"))[0]["X"])

