# Function
# Library Fuction
#   _Built in function
"""
        _syntax
        _sum()
        _min()
        _max
        _pow()
"""
#   _Module function
"""
        _import moduleName
        direct
        _from moduleName import functionName
        แค่บางตัว
        _from nuduleName import *
        ทั้งหมด 
"""
#   _ฟังก์ชันในโมดูล datetime
"""
        _from datetime import *
        #YYYY-MM-DD
        _.date(YYYY, MM, DD)
        set data to variable
        _.weekday()
            0	Monday
            1	Tuesday
            2	Wednesday
            3	Thursday
            4	Friday
            5	Saturday
            6	Sunday
        _.strftime(%d/%m/%y)
"""
#   _ฟังก์ชันในโมดูล math
"""
        _from math import *
        _from random import *
        _pow()
        _sqrt()
        _abs()
        _ceil()
        ปัดขึ้น
        _floor()
        _round()
        ปัดตาม math
        _sin()
        _cos()
        _tan()
        _randint()
        random 0-9
        _random()
        floating point ตำแหน่งไม่ร้จบ
        
        random * 100(10, 100, 1000, 10000) 
"""
# User defined function
"""
        _def functionName(parameter):
        
            return varValue
            
        can call funtion to value
"""
# ตัวแปร global
"""
        x = 0
        def functionName():
            function can call x
            
            y 
            global z
        outside can't call y
        but outside can call z
"""
# ตัวแปร local
"""
        We y is local
"""
# Argument Parameter
"""
        positional arrgument
            def calmax(parameter):
                pass
            calmax(arrgument)
        variable length arfgument
            def calmax(*parameter):# list ไม่มีจำนวนตายตัว
                pass
            calmax(data1, data2)
            calmax(data1, data2, data5, data4)
"""
# รูปแบบการเขียนฟังก์ชัน
#   _ไม่รับพารามิเตอร์และไม่คืนค่า
"""
        def calwage():
            pass
        use global variable
"""
#   _รับพารามิเตอร์แต่ไม่คืนค่า
"""
        def calwage(h, r):
            pass
        calwage(h, r)
"""
#   _ไม่มีการรับพารามิเตอร์แต่คืนค่า
"""
        def calwage():
            return value
            
        function use global variable
        result = calwage()
"""
#   _มีการรับพารามิเตอร์และมีการคืนค่่า
"""
        def calwage(h, r):
            return value
            
        result = calwage(h, r)
"""
# ฟังก์ชันโมดูล
"""
        ในงานจริงควรทำ File function แยก
        
        _from file_function import *
"""
# Lambda function
"""
    a = lambda x, n: x * n
    a(3, 5)
        x = 3
        n = 5
        
    หรือ ส่งค่า lambda(argument) -> parameter
"""

from _03_control_statement import * # ชื่อ file ไม่ควรใช้ตัวเลข
printf("Hello")