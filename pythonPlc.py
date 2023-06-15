


'''
*******************************************************************************************************************************************************+
*******************************************************************************************************************************************************+
*******************************************************************************************************************************************************+
*******************************************************************************************************************************************************+
*******************************************************************************************************************************************************+
CONNECTION TO PLC
'''




# Importing Packages
import snap7                
from snap7.util import *
from snap7.types import *   
import random
import time




# Reading Tags's Values in PL
def ReadDataBlock(plc, data_block_number, byte, bit, size, data_type):
    """e
    plc
    data-block(int): number of Data Block; DB1, DB2, ...  
    byte(int): in case of 2.0, byte is 2.
    bit(int): in case of 2.0,bit is 0.
    size(int): The size of the db data to read                                            

    """     
    result = plc.db_read(data_block_number, byte, size)
    if data_type == S7WLBit:
        return get_bool(result, 0, bit)
    elif data_type == S7WLByte or data_type == S7WLWord:
        return get_int(result, 0)
    elif data_type == S7WLReal:
        return get_real(result, 0)
    elif data_type == S7WLDWord:
        return get_word(result, 0)              
    else:
        return None



# Writting on tags of PLC
def WriteDataBlock(plc, data_block_number, byte, bit, size, data_type, value):
    """
    plc
    data-block(int): number of Data Block; DB1, DB2, ...
    byte(int): in case of 2.0, byte is 2.
    bit(int): in case of 2.0,bit is 0.
    size(int): The size of the db data to read   
    value: value to be written    
    """
    result = plc.db_read(data_block_number, byte, size)       
    if data_type == S7WLBit:
        set_bool(result, 0, bit, value)    # set value to the result
    elif data_type == S7WLByte or data_type == S7WLWord:
        set_int(result, 0, value)
    elif data_type == S7WLReal:
        set_real(result, 0, value)
    elif data_type == S7WLDWord:
        set_dword(result, 0 ,value)
    plc.db_write(data_block_number, byte, result)    # writting to specific data location the inserted value



def canc_tutto(plc):
    
    j = 14
    numero = []

    while j < 212:

        WriteDataBlock(plc, 2, j, 0, 2, S7WLByte, -1)
        numero.append(ReadDataBlock(plc, 3, j, 0, 2, S7WLByte))
        j += 2

    print(numero)




def count_iteraction(duration, plc):

    start_time = time.time()
    end_time = start_time + duration

   
    """l = 0

    while l < 300:

        numero[l] = 0
        l += 1"""
    y = 0 
    numero = []
    
    while time.time() < end_time:


        j = 14


        while j < 212:

            numero.append(ReadDataBlock(plc, 3, j, 0, 2, S7WLByte))

            j += 2
            
            print("Cliclo 1 Lettura")

        j = 14

        while j < 212:

            WriteDataBlock(plc, 2, j, 0, 2, S7WLByte, numero[y])

            y += 1
            j += 2



            print("Ciclo 2 Scrittura")


    return numero



# ... Altre operazioni sul client PLC ...



plc = snap7.client.Client()      
plc.connect('192.168.0.1', 0, 0)  

canc_tutto(plc)

num = count_iteraction(10, plc)

print(len(num))
print(num)

#WriteDataBlock(plc, 2, 200, 0, 2, S7WLByte, -1)
#print(ReadDataBlock(plc, 3, 200, 0, 2, S7WLByte))

# Stampa 



      # 192.168.0.1 is the ip_address of the plc            EXIT