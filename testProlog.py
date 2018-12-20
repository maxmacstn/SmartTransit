from pyswip import Prolog

prolog = Prolog()
prolog.consult("train_path.pl")



# print(list(prolog.query("path(mochit, X)")))
# q = prolog.query("astar(1, 10, X,Y,Z)")

# print(list(q)[0])
result = list(prolog.query("astar( arl_ramkhamhaeng, mrt_blue_khlong_toei, X,Y,Z)"))[0]['Z']
resultList = []
for r in result:
    resultList.append(str(r))

print(resultList)

# resultList =  str( list(prolog.query("astar(arl_makkasan, arl_ramkhamhaeng, X,Y,Z)"))[0]['Z'] )
# print( str(  list(prolog.query(""))  )  )
# print(list( prolog.query("dist(arl_makkasan, arl_ramkhamhaeng, X)")))

# astar = Functor("astar", 1)
# arl_makkasan = Variable()
# arl_ramkhamhaeng = Variable()
# X = Variable()
# Y = Variable()
# soln = Query(astar(arl_makkasan,arl_ramkhamhaeng,X,Y))
#
# while soln.nextSolution():
#    b64 = Y.get_value()
# Board_pl = "b("
# for i in range (0, 64):
#     Board_pl += (str(b64.args[i]) + ",")
# Board_pl += (str(b64.args[63]) + ")")
# print(Board_pl)