list_length([], 0).
list_length([_ | L], N) :-
    list_length(L, N1),
    N is N1 + 1. 

delete_element(_, [], []).    

delete_element(X, [X | L], L) :- !.

delete_element(X, [Y | L], [Y | L1]) :-
    delete_element(X, L, L1).