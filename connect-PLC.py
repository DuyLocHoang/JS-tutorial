# from asyncio import FastChildWatcher

"""
Connect with PLC to send and reiceive data
"""

import socket

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def socket_connect(host,port):
    print(host,port)
    soc.connect((host,port))
    
def ONDEVICE():
    datatest = "ST RM15000\x0D"

    print(datatest.encode("UTF-8"))
    soc.sendall("ST RM15000\x0D".encode("UTF-8"))
    soc.sendall(b'\x53\x54\x20\x4D\x52\x31\x35\x30\x30\x30\x0D')
    data = soc.recv(1024)
    print(data)
    data = data.decode("UTF-8")
    print(data)
    kq = str(data)
    # print(kq)
    if 'OK' in kq:
        return True
    else:
        return False

def OFFDEVICE():
    # soc.sendall("RS RM15000\x0D".encode("UTF-8"))
    soc.sendall(b'\x52\x53\x20\x4D\x52\x31\x35\x30\x30\x30\x0D')
    data = soc.recv(1024)
    print(data)
    kq = str(data)
    print(kq)
    if 'OK' in kq:
        return True
    else:
        return False

def readdata(data):
    a = 'RD '
    c = '\x0D'
    d = a + data + c
    datasend = d.encode("UTF-8")
    soc.sendall(datasend)
    data = soc.recv(1024)
    datadeco = data.decode("UTF-8")
    data1 = int(datadeco)

    return data1



def writedata(register, data):
    a = 'WR '
    b = ' '
    c = '\x0D'
    d = a+ register + b + str(data) + c
    datasend  = d.encode("UTF-8")
    soc.sendall(datasend)
    datares = soc.recv(1024)
    print(datares)

#Write data
def writedatatest(register, data):
    a = 'WR '
    b = ' '
    c = '\x0D'
    d = a+ register + b + str(data) + c
    datasend  = d.encode("UTF-8")
    print(datasend)
    soc.sendall(datasend)
    datares = soc.recv(1024)
    print(datares)

def readdatatest(data):
    a = 'RD '
    c = '\x0D'
    d = a+ data +c
    datasend = d.encode("UTF-8")
    print(datasend)
    soc.sendall(datasend)
    data = soc.recv(1024)
    datadeco = data.decode("UTF-8")
    data1 = int(datadeco)

    return data1

socket_connect("192.168.0.10",8501)
print("Connected")
# print(readdata('DM0'))
writedata("DM1.U",2000)
# writedata("RM15001",1)
# writedatatest('DM2000.U',2000) 
# print(readdatatest('DM2000')) 
# writedatatest("RM15001",1)
# print(readdata("RM15000"))

# if(ONDEVICE() == True):
#     print('MR15000 OFF')
# if(OFFDEVICE() == True):
#     print('MR15000')