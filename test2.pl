/*area(Number,PosX,PosY).*/

area(1,20,80).
area(2,50,30).
area(3,100,100).
area(4,90,70).
area(5,70,50).
area(6,110,50).
area(7,150,90).
area(8,200,90).
area(9,140,60).
area(10,160,20).
area(11,180,60).
area(12,190,20).
area(13,230,70).
area(14,240,30).
area(15,240,20).

/*street(CityA,CityB,Distance).*/
street(1,2,50).
street(1,3,100).
street(1,4,75).
street(1,5,65).
street(2,5,30).
street(3,4,40).
street(3,7,50).
street(4,5,25).
street(4,6,30).
street(4,9,65).
street(4,7,70).
street(5,6,30).
street(6,9,35).
street(6,10,60).
street(7,8,35).
street(7,9,30).
street(8,9,70).
street(8,11,40).
street(8,13,50).
street(9,10,50).
street(9,11,30).
street(10,11,50).
street(10,12,40).
street(11,12,40).
street(11,13,50).
street(11,14,60).
street(12,14,50).
street(13,14,50).

astar(Start,Final,_,Tp, Result):-
      estimation(Start,Final,E),
      astar1([(E,E,0,[Start])],Final,_,Tp, Result).

astar1([(_,_,Tp,[Final|R])|_],Final,[Final|R],Tp, Result):- reverse([Final|R], Result),write('Path = '), write(Result).

astar1([(_,_,P,[X|R1])|R2],Final,C,Tp, Result):-
       findall((NewSum,E1,NP,[Z,X|R1]),(street(X,Z,V),
               not(member(Z,R1)),
               NP is P+V,
               estimation(Z,Final,E1),
               NewSum is E1+NP),L),
        append(R2,L,R3),
        sort(R3,R4),
        astar1(R4,Final,C,Tp, Result).




estimation(C1,C2,Est):-
          area(C1,X1,Y1),area(C2,X2,Y2), DX is X1-X2,DY is Y1-Y2,
                    Est is sqrt(DX*DX+DY*DY).