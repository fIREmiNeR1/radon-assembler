import sys
import converts as sf

args = sys.argv
input_filename = args[1]
output_filename = args[2]

input_file = open(input_filename, 'r')
input_file_data = input_file.read()
input = input_file_data.splitlines()
input_file.close()

def save_out(data):
    output_file  = open(output_filename, "w")
    out_data =[]
    for i in data:
        out_data.append(i)
    while len(out_data) < 32:
        out_data.append('0000000000000000')
    for i in out_data:
        output_file.write(i + '\n')

asmdata = []

# 1-full op, 2-imm, 3-jmpe, 4-jmp
# 5-branch, 6-dest, 7-1op, 8-noop

def assemble(code):
    for i in code:
        parts = i.split()
        result = sf.get_opcode(parts[0])
        group = sf.get_group(parts[0])
        print(group)
        if group == '1':
            result = result + sf.decode_reg(parts[1]) + sf.decode_reg(parts[2]) + sf.decode_reg(parts[3]) + '00'
        if group == '2':
            result = result + sf.decode_reg(parts[1]) + sf.getNum8(parts[2])
            print('IMM!')
        if group == '3':
            result = result + sf.decode_page(parts[1]) + sf.getNum5(parts[2])
        if group == '4':
            result = result + '000000' + sf.getNum5(parts[2])
        if group == '5':
            result = result + sf.get_flag(parts[1]) + '000' + sf.getNum5(parts[2])
        if group == '6':
            result = result + sf.decode_reg(parts[1]) + '00000000'
        if group == '7':
            result = result + '000000' + sf.decode_reg(parts[1]) + '00'
        if group == '8':
            result = result + '00000000000'
        asmdata.append(result)

assemble(input)
save_out(asmdata)


