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

// program
program  : var_dcl* func_dcl+ EOF;

// variable declaration
var_dcl : VAR COLON var_init (COMMA var_init)* SEMI;

var_init : var (ASSIGN_OP (INTLIT | FLOATLIT | STRINGLIT | BOOLEANLIT | ARRAYLIT))?; 

var : ID (LSB INTLIT RSB)*;
// function declaration
func_dcl : FUNCTION COLON ID param_list? body ;

param_list : PARAMETER COLON param (COMMA param)*; 

param : ID (LSB INTLIT RSB)*;

body : BODY COLON statement_list END_BODY DOT;

statement_list : var_dcl* (assign_stmt | if_stmt | for_stmt | while_stmt | do_while_stmt | call_stmt | return_stmt | break_stmt | continue_stmt)*;

// statements
assign_stmt : var ASSIGN_OP expression SEMI;

if_stmt : IF expression THEN statement_list (ELSE_IF expression THEN statement_list)* (ELSE statement_list)? END_IF DOT;

for_stmt : FOR LP ID ASSIGN_OP expression COMMA expression COMMA expression RP DO statement_list END_FOR DOT;

while_stmt : WHILE expression DO statement_list END_WHILE DOT;

do_while_stmt : DO statement_list WHILE expression END_DO DOT;

break_stmt : BREAK SEMI;

continue_stmt : CONTINUE SEMI;

call_stmt : func_call SEMI;

func_call : ID LP (expression (COMMA expression)*)? RP;

return_stmt : RETURN expression? SEMI;

// expression
expression : 
    LP expression RP
    | func_call // function call : assoc none ?????
    | ID (LSB expression RSB)+ // index : ARRAYLIT[expression] ??????
    | <assoc=right> (INT_SUB_OP | FLOAT_SUB_OP) expression  // sign
    | <assoc=right> NEG_OP expression   // logical
    | expression (INT_MUL_OP | FLOAT_MUL_OP | INT_DIV_OP | FLOAT_DIV_OP | INT_REMAINDER_OP) expression // multiplying
    | expression (INT_ADD_OP | FLOAT_ADD_OP | INT_SUB_OP | FLOAT_SUB_OP) expression // adding
    | expression (CONJ_OP | DISJ_OP) expression // logical
    | expression (EQ_OP | INT_NEQ_OP | FLOAT_NEQ_OP | INT_LT_OP | FLOAT_LT_OP | INT_GT_OP | FLOAT_GT_OP | INT_LTE_OP | FLOAT_LTE_OP | INT_GTE_OP | FLOAT_GTE_OP) expression // relational : assoc none ????
    | (ID | INTLIT | FLOATLIT | BOOLEANLIT) ; // operands

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
fragment STR_CHAR : ~['"\n\\] | ('\\' ['bfrnt\\]) | '\'"' ;
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
// Assignment operator
ASSIGN_OP : '=';

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


COMMENT : '**' .*? '**' -> skip;    // ????
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

// Errors
ERROR_CHAR: .;
UNCLOSE_STRING: '"' STR_CHAR*;
ILLEGAL_ESCAPE: '"' STR_CHAR* '\\' ~['bfrnt\\];
UNTERMINATED_COMMENT: '**' .*?; // ?????
