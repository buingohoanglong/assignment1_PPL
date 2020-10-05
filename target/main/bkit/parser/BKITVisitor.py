# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_dcl.
    def visitVar_dcl(self, ctx:BKITParser.Var_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_init.
    def visitVar_init(self, ctx:BKITParser.Var_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var.
    def visitVar(self, ctx:BKITParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_dcl.
    def visitFunc_dcl(self, ctx:BKITParser.Func_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#param_list.
    def visitParam_list(self, ctx:BKITParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#param.
    def visitParam(self, ctx:BKITParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#body.
    def visitBody(self, ctx:BKITParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement_list.
    def visitStatement_list(self, ctx:BKITParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign_stmt.
    def visitAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stmt.
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_stmt.
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_stmt.
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:BKITParser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_stmt.
    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stmt.
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_call.
    def visitFunc_call(self, ctx:BKITParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression.
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        return self.visitChildren(ctx)



del BKITParser