grammar Lambda;

prog            :       stat+;

stat            :       expr NEWLINE?                   # printExpr
                |       ID '=' expr NEWLINE?            # assign
                ;

expr            :       ID                              # variable
                |       INT                             # int
                |       '(' expr ')'                    # parens
                |       METHODNAME '(' exprList? ')'    # methodCall
                ;

exprList        :       expr (',' expr)*                
                ;               

ID              :       '[' .+? ']';
METHODNAME      :       [a-zA-Z]+;
INT             :       [0-9]+ ;
NEWLINE         :       '\r'? '\n';
WS              :       [ \t]+ -> skip;