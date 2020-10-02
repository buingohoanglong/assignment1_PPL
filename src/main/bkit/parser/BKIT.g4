grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

program  : VAR COLON ID SEMI EOF ;

// Identifiers
ID: [a-z][a-zA-Z0-9_]* ;

// Literals
// Integers
INTLIT : BASE10 | BASE16 | BASE8;
fragment BASE10 : '0' | [1-9][0-9]*;
fragment BASE8 : '0' [oO] [1-7][0-7]*;
fragment BASE16 : '0' [xX] [1-9A-F] [0-9A-F]*;
// Floats
fragment DIGIT : [0-9];
fragment INT_PART : DIGIT+;
fragment DECIMAL_PART : DOT DIGIT*;
fragment EXPONENT_PART : [eE] [+-]? DIGIT+;
FLOATLIT : INT_PART (DECIMAL_PART | EXPONENT_PART | DECIMAL_PART EXPONENT_PART);
// Boolean
BOOLEANLIT : 'True' | 'False';
// String   ??????????
STRINGLIT : '"' STR_CHAR* '"'; 
fragment STR_CHAR : ~['"\b\f\r\n\t\\] | ('\\' ['bfrt\\]) | '\'"' ;
// Array
ARRAYLIT : LCB (LITERAL (COMMA LITERAL)*)? RCB;
fragment LITERAL : INTLIT | FLOATLIT | BOOLEANLIT | ARRAYLIT;

// Keywords
BODY : 'Body';
ELSE : 'Else';
END_FOR : 'EndFor';
IF : 'If';
VAR : 'Var';
END_DO : 'EndDo';
BREAK : 'Break';
ELSE_IF : 'ElseIf';
END_WHILE : 'EndWhile';
PARAMETER : 'Parameter';
WHILE : 'While';
CONTINUE : 'Continue';
END_BODY : 'EndBody';
FOR : 'For';
RETURN : 'Return';
OPERATORS : 'Operators';
DO : 'Do';
END_IF : 'EndIf';
FUNCTION: 'Function';
THEN : 'Then';

// Operators
// Arithmetic operators
INT_SUB_OP : '-';
FLOAT_SUB_OP : '-.';
INT_ADD_OP : '+';
FLOAT_ADD_OP : '+.';
INT_MUL_OP : '*';
FLOAT_MUL_OP : '*.';
INT_DIV_OP : '\\';
FLOAT_DIV_OP : '\\.';
INT_REMAINDER_OP : '%';
// Boolean operators
NEG_OP : '!';
CONJ_OP : '&&';
DISJ_OP : '||';
// Relational operators
EQ_OP : '==';
INT_NEQ_OP : '!=';
INT_LT_OP : '<';
INT_GT_OP : '>';
INT_LTE_OP : '<=';
INT_GTE_OP : '>=';
FLOAT_NEQ_OP : '=/=';
FLOAT_LT_OP : '<.';
FLOAT_GT_OP : '>.';
FLOAT_LTE_OP : '<=.';
FLOAT_GTE_OP : '>=.';

// Separators
LP : '(';
RP : ')';
LSB : '[';
RSB : ']';
LCB : '{';
RCB : '}';
COLON: ':' ;
SEMI: ';' ;
COMMA : ',';
DOT : '.';



WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;