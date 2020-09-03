grammar Hello;
omp : 'hello' ID rule2 | EOF ;         // match keyword hello followed by an identifier
rule2 : 'bye' ID | EOF ;
ID : [a-z]+ ;             // match lower-case identifiers
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines