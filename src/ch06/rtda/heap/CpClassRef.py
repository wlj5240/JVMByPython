from ch06.rtda.heap.CpSymRef import SymRef

class ClassRef(SymRef):

    @staticmethod
    def newClassRef(constantPool, classInfo):
        ref = ClassRef()
        ref.cp = constantPool
        ref.className = classInfo.name()
        return ref

