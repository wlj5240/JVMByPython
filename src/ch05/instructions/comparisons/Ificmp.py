from ch05.instructions.base.Instruction import BranchInstruction
from ch05.instructions.base.BranchLogic import BranchLogic

def _icmpPop(frame):
    stack = frame.operandStack
    val2 = stack.pop_numeric()
    val1 = stack.pop_numeric()
    return val1, val2

class IF_ICMPEQ(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 == val2:
            BranchLogic.branch(frame, self.offset)

class IF_ICMPNE(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 != val2:
            BranchLogic.branch(frame, self.offset)

class IF_ICMPLT(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 < val2:
            BranchLogic.branch(frame, self.offset)

class IF_ICMPLE(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 <= val2:
            BranchLogic.branch(frame, self.offset)

class IF_ICMPGT(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 > val2:
            BranchLogic.branch(frame, self.offset)

class IF_ICMPGE(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 >= val2:
            BranchLogic.branch(frame, self.offset)