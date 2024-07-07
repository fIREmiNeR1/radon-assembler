def get_opcode(opc):
    if opc == 'ADD':
        return '10000'
    if opc == 'ADDC':
        return '11101'
    if opc == 'SUB':
        return '01000'
    if opc == 'AND':
        return '11000'
    if opc == 'NAND':
        return '00100'
    if opc == 'OR':
        return '10100'
    if opc == 'NOR':
        return '01100'
    if opc == 'XNOR':
        return '00010'
    if opc == 'IMM':
        return '10010'
    if opc == 'JMP':
        return '01010'
    if opc == 'PJMP':
        return '00111'
    if opc == 'BRC':
        return '11010'
    if opc == 'PLOD':
        return '00110'
    if opc == 'PLWT':
        return '11111'
    if opc == 'PSTR':
        return '10110'
    if opc == 'PUSH':
        return '11110'
    if opc == 'PULL':
        return '00001'
    if opc == 'MLOD':
        return '11001'
    if opc == 'MSTR':
        return '00101'
    if opc == 'PSWP':
        return '10101'
    if opc == 'POI':
        return '01101'
    if opc == 'HALT':
        return '00011'
    if opc == 'NOP':
        return '00000'
    

# 1-full op, 2-imm, 3-jmpe, 4-jmp
# 5-branch, 6-dest, 7-1op, 8-noop
    
def get_group(opc):
    if opc == 'ADD':
        return '1'
    if opc == 'ADDC':
        return '1'
    if opc == 'SUB':
        return '1'
    if opc == 'AND':
        return '1'
    if opc == 'NAND':
        return '1'
    if opc == 'OR':
        return '1'
    if opc == 'NOR':
        return '1'
    if opc == 'XNOR':
        return '1'
    if opc == 'IMM':
        return '2'
    if opc == 'JMP':
        return '3'
    if opc == 'PJMP':
        return '4'
    if opc == 'BRC':
        return '5'
    if opc == 'PLOD':
        return '6'
    if opc == 'PLWT':
        return '6'
    if opc == 'PSTR':
        return '7'
    if opc == 'PUSH':
        return '70'
    if opc == 'PULL':
        return '6'
    if opc == 'MLOD':
        return '6'
    if opc == 'MSTR':
        return '7'
    if opc == 'PSWP':
        return '8'
    if opc == 'POI':
        return '7'
    if opc == 'HALT':
        return '8'
    if opc == 'NOP':
        return '8'
    

def decode_reg(input):
    if input == 'r0':
        return '000'
    if input == 'r1':
        return '100'
    if input == 'r2':
        return '010'
    if input == 'r3':
        return '110'
    if input == 'r4':
        return '001'
    if input == 'r5':
        return '101'
    if input == 'r6':
        return '011'
    if input == 'r7':
        return '111'
    
def get_flag(input):
    if input == 'zero':
        return '100'
    if input == 'nzero':
        return '110'
    if input == 'carry':
        return '101'
    if input == 'ncarry':
        return '111'
    
def getNum8(num):
    if num[0] == 'b':
        res = num.lstrip('b')
    if num[0] == '#':
        res = int(num.lstrip('#'))
        res =  str('{:08b}'.format(res))
    return res[::-1]

def getNum5(num):
    if num[0] == 'b':
        res = num.lstrip('b')
    if num[0] == '#':
        res = int(num.lstrip('#'))
        res =  str('{:05b}'.format(res))
    return res[::-1]

def decode_page(page):
    res = int(page.lstrip('p'))
    res =  str('{:05b}'.format(res))
    return res[::-1]
