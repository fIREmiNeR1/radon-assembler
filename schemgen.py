import sys
import mcschematic

args = sys.argv
in_data = open(args[1] + '.txt','r') 
schem = mcschematic.MCSchematic()

in_file = in_data.read()
input = in_file.splitlines()
in_data.close()

for i in range(len(input)):
    input[i] = input[i][::-1]

ss_list = [0,1,2,4,6,8,10,12,14,16,18,20,22,24,26,27]
dir = r'D:\Minecraft\game\config\worldedit\schematics'

def fillBarrel(count):
    ss0 = r'minecraft:barrel'
    if count == 0:
        return ss0
    else:
        # r'minecraft:barrel{Items:[{Slot:1,id:wooden_shovel,Count:1}]}'
        output = ss0 + r'{Items:['
        for i in range(0,count):
            output = output + (r'{Slot:%s,id:wooden_shovel,Count:1},' % i)

        output = output[:-1]
        output = output + r']}'
        return output
    
def bin2ss(data_bin):
    if data_bin == '1000':
        return '1'
    if data_bin == '0100':
        return '2'
    if data_bin == '1100':
        return '3'
    if data_bin == '0010':
        return '4'
    if data_bin == '1010':
        return '5'
    if data_bin == '0110':
        return '6'
    if data_bin == '1110':
        return '7'
    if data_bin == '0001':
        return '8'
    if data_bin == '1001':
        return '9'
    if data_bin == '0101':
        return '10'
    if data_bin == '1101':
        return '11'
    if data_bin == '0011':
        return '12'
    if data_bin == '1011':
        return '13'
    if data_bin == '0111':
        return '14'
    if data_bin == '1111':
        return '15'
    if data_bin == '0000':
        return '0'

def getBarrel(row,col):
    result = input[col][row+8] + input[col+16][row+8] + input[col][row] + input[col+16][row]
    return result



for col in range(0,16):
    for row in range(0,8):
        y = -1-row*2
        z = col*2+2
        ss_here = int(bin2ss(getBarrel(row,col)))
        item = fillBarrel(ss_list[ss_here])
        schem.setBlock((0,y,z), item)
schem.save(dir,"radon_" + args[1],mcschematic.Version.JE_1_18_2)

