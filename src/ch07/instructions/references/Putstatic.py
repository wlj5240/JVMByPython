from ch07.instructions.base.Instruction import Index16Instruction

class PUT_STATIC(Index16Instruction):
    def execute(self, frame):
        from ch07.instructions.base.ClassInitLogic import ClassInitLogic


        currentMethod = frame.method
        currentClass = currentMethod.getClass()
        cp = currentClass.constantPool
        fieldRef = cp.getConstant(self.index)
        field = fieldRef.resolveField()
        clazz = field.getClass()

        if not clazz.initStarted:
            frame.revertNextPC()
            ClassInitLogic.initClass(frame.thread, clazz)
            return

        if not field.isStatic():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")
        if field.isFinal():
            if currentClass != clazz or currentMethod.name != "<clinit>":
                raise RuntimeError("java.lang.IllegalAccessError")

        descriptor = field.descriptor
        slotId = field.slotId
        slots = clazz.staticVars
        stack = frame.operandStack

        if descriptor[0] in {"Z", "B", "C", "S", "I", "F", "J", "D"}:
            slots.set_numeric(slotId, stack.pop_numeric())
        elif descriptor[0] == "L":
            slots.set_ref(slotId, stack.pop_ref())
