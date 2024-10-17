# Sequence, Set and Dictionary Date Type
# String
#   _การเข้าถึง
"""
        _str[index]

        _str[start:stop:step]
        stop: n+1
        step: n+1

        for data in _str:
"""
#   _การเชื่อมต่อ และการทำซ้ำ
"""
        +
        ,
        *
"""
#   _การดำเนินการ
"""
    _Comparison Operator & ASCII
    "aA" = 97+65
"""
#   _ฟังก์ชัน
"""
        _.count(" ", start, stop)
        _.len(str)
        _.capitalize()
        _.lower()
        _.upper()
        _.swapcase() swap lower upper
        _.strip() del space font and back
        _.find("x", start, stop)
        stop: n+1
        not find return -1
        _.replace(msg1, msg2)
        _.join(str)
        list string ขั้น _.
        _.ljust(n, "x")
        justifly content width n
        _.rjust(n, "x")
        _.isdigit
        check number on string
"""
# List[] and Tuple()
#   _การเข้าถึงv
"""
        list_or_tuple[index]
        
        list_or_tuple[start:stop:step]
        
        for data in list_or_tuple:
        #just name
"""
#   _ฟังก์ชัน
"""
        _.count(data)
        _.len(list_or_tuple)
        _.index(data)
        _.append(data)
        _.remove(data)
        _.pop(index)
        _clear(list_or_tuple)
        
        # if with list_or_tuple
        if studentid in passtuple
"""
# Set
"""
        Con't use index
        
        for data in sets:
"""
#   _ฟังก์ชัน
"""
        _.union(set2)
        _.intersection(set2)
        _.difference(set2)
        _.add(data)
        _.remove(data)
        _.clear()
        
"""
# Dictionary {(key:value), ...}
#   _การเข้าถึง
"""
        for i in dict:
        i: key
        dict[key]: value
"""
#   _ฟังก์ชัน
"""
        _.len(dict)
        _.keys()
        _.values()
        _.items()
        _.get(key)
        :return value
        _.update(dict2)
        ต่อตูด
        _.pop(key)
        _.clear()
"""

dict = {"keya":12, "keyb":15, "keyc":18}
for i in dict:
    print(i, dict[i])

print(dict.keys())
print(dict.values())
print(dict.items())
print(dict)