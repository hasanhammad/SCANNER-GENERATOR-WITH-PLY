# SCANNER-GENERATOR-WITH-PLY
PLY - PYTHON


GRAMMAR : 

P ==> D C

D ==> id = (num , num) , D

D ==> id = (num , num);

C ==> {L}

L ==> S ; L L ==> ԑ

S ==> id = (num , num)

S ==> X(id)++

S ==> X(id)--

S ==> Y(id)++

S ==> Y(id)--
