
list_len([],0).
list_len([H|T],N):- list_len(T, N1), N is N1 + 1.

reverse_list([H|T], A, R):- reverse_list(T,[H|A], R).
reverse_list([],A,A).

revList(L,R):- reverse_list(L,[],R).

path(mochit, saphankwai).
path(mochit, max).



