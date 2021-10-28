from Components.number import Number
from Components.errors import RTResult

class Interpreter:
    def visit(self, node, context):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node, context)

    def no_visit_method(self, node, context):
        raise Exception(f'No visit_{type(node).__name__} method defined')
    
    def visit_NumberNode(self, node, context):
        res = RTResult()
        return res.success(
            Number(node.token.value).set_context(context).set_pos(node.pos_start, node.pos_end)
        )
    
    def visit_BinOpNode(self, node, context):
        res = RTResult()
        left = res.register(self.visit(node.left_node, context))
        if res.error: return res
        right = res.register(self.visit(node.right_node, context))
        if res.error: return res

        if node.op_token.type == 'PLUS':
            result, error = left.added_to(right)
        elif node.op_token.type == 'MINUS':
            result, error = left.subtracted_by(right)
        elif node.op_token.type == 'MULTIPLY':
            result, error = left.multiplied_by(right)
        elif node.op_token.type == 'DIVIDE':
            result, error = left.divided_by(right)
        elif node.op_token.type == 'MODULO':
            result, error = left.divmod_by(right)

        if error: return res.failure(error)
        else: return res.success(result.set_pos(node.pos_start, node.pos_end))

    def visit_UnaryOpNode(self, node, context):
        res = RTResult()
        number = res.register(self.visit(node.node, context))
        if res.error: return res

        error = None
        if node.op_token.type == 'MINUS':
            number, error = number.multiplied_by(Number(-1))

        if error: return res.failure(error)
        else: return res.success(number.set_pos(node.pos_start, node.pos_end))
