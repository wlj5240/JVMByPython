#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: ConstantPool.py
@time: 2019/9/16 17:25
@desc: 运行时常量池，主要存放两类信息：字面量和符号引用，字面量包括整数、浮点数和字符串字面量；
符号引用包括类符号引用、字段符号引用、方法符号引用和接口符号引用。
"""


class ConstantPool:
    def __init__(self, clazz, consts):
        self._class = clazz
        self.consts = consts

    from classfile.ConstantPool import ConstantPool

    # 把class文件中的常量池转换成运行时常量池
    @staticmethod
    def new_constant_pool(clazz, cfConstantPool: ConstantPool):
        from classfile.CpNumeric import ConstantDoubleInfo, ConstantLongInfo, ConstantFloatInfo, ConstantIntegerInfo
        from classfile.ConstantStringInfo import ConstantStringInfo
        from classfile.ConstantClassInfo import ConstantClassInfo
        from classfile.ConstantMemberRefInfo import ConstantFieldRefInfo, ConstantMethodRefInfo, \
            ConstantInterfaceMethodRefInfo
        from rtda.heap.CpClassRef import ClassRef
        from rtda.heap.CpFieldRef import FieldRef
        from rtda.heap.CpMethodRef import MethodRef
        from rtda.heap.CpInterfaceMethodRef import InterfaceMethodRef

        cp_count = len(cfConstantPool.cp)
        consts = [None for i in range(cp_count)]
        rt_constant_pool = ConstantPool(clazz, consts)

        for i in range(1, cp_count):
            cp_info = cfConstantPool.cp[i]
            if isinstance(cp_info, ConstantIntegerInfo):
                consts[i] = cp_info.val
            elif isinstance(cp_info, ConstantFloatInfo):
                consts[i] = cp_info.val
            elif isinstance(cp_info, ConstantLongInfo):
                consts[i] = cp_info.val
            elif isinstance(cp_info, ConstantDoubleInfo):
                consts[i] = cp_info.val
            elif isinstance(cp_info, ConstantStringInfo):
                consts[i] = str(cp_info)
            elif isinstance(cp_info, ConstantClassInfo):
                consts[i] = ClassRef(rt_constant_pool, cp_info)
            elif isinstance(cp_info, ConstantFieldRefInfo):
                consts[i] = FieldRef(rt_constant_pool, cp_info)
            elif isinstance(cp_info, ConstantMethodRefInfo):
                consts[i] = MethodRef(rt_constant_pool, cp_info)
            elif isinstance(cp_info, ConstantInterfaceMethodRefInfo):
                consts[i] = InterfaceMethodRef(rt_constant_pool, cp_info)

        # rt_constant_pool.consts = consts
        return rt_constant_pool

    def get_class(self):
        return self._class

    # 根据索引返回常量
    def get_constant(self, index):
        c = self.consts[index]
        if c:
            return c
        else:
            raise RuntimeError("No constants at index {0}".format(index))
