import sys

print("SerialActivation - Keygen by b0l0k - Enter your serial number")
userinput = input()

lastedx = 0
lasteax = 0
var28 = 0

for x in range(100):
    
    edx = ord(userinput[0]) + ord(userinput[5])
    eax = ord(userinput[2]) | ord(userinput[6])
    edx = edx ^ eax
    edx = edx & 0x0F
    edx = edx + lastedx
    lastedx = edx

    eax = ord(userinput[1])
    edx = ord(userinput[7])
    eax = eax + edx
    ecx = ord(userinput[8])
    eax += ecx
    eax ^= lastedx
    eax &= 0xF0
    eax += lasteax
    lasteax = eax

eax = lasteax

edx = ord(userinput[3])
ecx = lastedx
ecx &= 1
edx >>= ecx
eax = ord(userinput[8])
eax += lasteax
eax += edx
var28 = eax

eax = lastedx + lasteax + var28
print(eax)
