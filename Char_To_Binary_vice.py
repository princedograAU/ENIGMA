__author__ = 'Prince Dogra'

def ret_Byte(str):

    final_str = ''
    binaryList = []
    for i in range(len(str)):
        final_str = ''
        temp = '{:08b}'.format(int(ord(str[i])))
        final_str += temp
        binaryList.append(final_str)

    return (binaryList)


def ret_Int(bList):

    intList = []
    for i in range(len(bList)):
        intList.append(int(bList[i],2))

    return (intList)

def ret_char(iList):
    charString = ''.join(map(chr,iList))

    return (charString)


enc_code = input("Enter any String")
binaryListData = ret_Byte(enc_code)
print(binaryListData)
integerList = ret_Int(binaryListData)
print(ret_char(integerList))
