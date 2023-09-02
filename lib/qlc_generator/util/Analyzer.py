import ast
from lib.qlc_generator.util.AstUtil import AstUtil

class Analyzer(ast.NodeTransformer):
    def __init__(self):
        self.astUtil = AstUtil()
        self.parent = None

    def visit(self, node):
        node.parent = self.parent
        self.parent = node
        node = super().visit(node)
        if isinstance(node, ast.AST):
            self.parent = node.parent
        return node
        
    def visit_FunctionDef(self, node):
        self.astUtil.addFunctionDefNode(node)
        self.generic_visit(node)
        return node

    def visit_For(self, node):
        self.astUtil.addForNode(node)
        self.generic_visit(node)
        return node
    
    def visit_While(self, node):
        self.astUtil.addWhileNode(node)
        self.generic_visit(node)
        return node