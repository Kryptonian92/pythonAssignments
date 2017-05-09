def TypeList(x):
    _int = 0
    _str = 0
    sum = 0
    newString = ''
    for i in range(0,len(x)):
        if type(x[i]) == str:
            newString = newString + " " + x[i]
            _str += 1
        elif type(x[i]) == int or float:
            sum += x[i]
            _int += 1

    if _int > 0 and _str > 0:
        print "You have entered a mixed type of array"
        print "Sum:", sum
        print "String:", newString
    elif _int > 0:
        print "You have entered an array of integer type"
        print sum
    else:
        print "You have entered a string array"
        print newString

TypeList(['magical unicorns', 19, 'hello', 98.98, 'world'])
TypeList([2,3,1,7,4,12])
#
#
# def mixed_data(str):
#     string_list = ['magical unicorns',19,'hello',98.98,'world']
#     for element in string_list:
#         if isinstance(element, (int, str, float)):
#             print 'The array you entered is of mixed type'
#         else:
#             print 'Fail'
# # print 'Outside of the function'
# string_list = ['magical unicorns',19,'hello',98.98,'world']
# for element in string_list:
#     if isinstance(element, (int, str, float)):
#         print 'The array you entered is of mixed type'
#     else:
#         print 'Fail'
# #
# # string_list = ['magical unicorns',19,'hello',98.98,'world']
# # for element in string_list:
# #     if isinstance(element, (int, str, float)):
# #         print "The array you entered is of mixed type"
