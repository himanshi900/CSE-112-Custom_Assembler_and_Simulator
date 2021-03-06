import sys
import os


Lines = []
allLines = []
output = []
from sys import stdin

def instruction_call(arr):
	dic={
	'add': '00000' , 
	'sub': '00001', 
	'mov':'00010',
	'mov1': '00011',
	'ld':'00100',
	'st':'00101', 
	'mul':'00110',
	'div':'00111',
	'rs':'01000', 
	'ls':'01001',
	'xor':'01010',
	'or':'01011',
	'and':'01100',
	'not':'01101',
	'cmp':'01110',
	'jmp':'01111',
	'jlt':'10000',
	'jgt':'10001',
	'je':'10010',
	'hlt':'10011'}

	listr=['R0','R1','R2','R3','R4','R5','R6']
	
    # register can only be one of given r0 to r6 and flags (only mov)..check condn
	if((arr[0]=="add" or arr[0]=="sub" or arr[0]=="mul" or arr[0]=="xor" or arr[0]=="or" or arr[0]=="and" ) and len(arr)==4 and arr[1] in listr and arr[2] in listr and arr[3] in listr ):
		
		a = dic.get(arr[0])
		b = encodeA(arr[1])
		c = encodeA(arr[2])
		d = encodeA(arr[3])
		if(b=='-1' or c=='-1' or d=='-1'):
			#clear()
			err = "Syntax error in line {} ".format(cou)
			print(err)
			exit()
		else:
			out=(a+"00"+b+c+d)
			output.append(out)
	
	elif((arr[0]=="ls" or arr[0]=="rs" or (arr[0]=="mov" and len(arr)==3 and arr[1][0]=='R' and  arr[2][0]=="$")) and len(arr)==3 and arr[1] in listr and arr[2][0]=="$" ):
		#m
		a = dic.get(arr[0])
		b = encodeA(arr[1])
		c=arr[2]
		d = c[1:]
		if(d.isnumeric() == True):
			d = int(d)
		else:
			d = -1
		p=bnr(c)
		if (b == '-1' or c == '-1' or d == '-1'):
			#clear()
			err = "Syntax error in line {} ".format(cou)
			print(err)
			exit()
		if(d<0 or d>255):
			#clear()
			err = "Invalid value line {} ".format(cou)
			print(err)
			exit()
		else:
			out=(a+b+p)
			output.append(out)

	elif(arr[0] == "mov" and len(arr)==3 and arr[1][0]=="R" and arr[2][0]=="R" and arr[1] in listr and arr[2] in listr ):
		 
		#move r1 in flags?
		a = dic.get("mov1")
		b = encodeA(arr[1])
		c = encodeC(arr[2])

		if(b=='-1' or c=='-1'):
			#clear()
			err = "Syntax error in line {} ".format(cou)
			print(err)
			exit()
		else:
			out=(a+"00000"+b+c)
			output.append(out)
	
	elif(arr[0] == "mov" and len(arr)==3 and arr[1][0]=="R" and arr[2]=="FLAGS" and arr[1] in listr ):
		a = dic.get("mov1")
		b = encodeC(arr[1])
		c = encodeC(arr[2])
		if(b=='-1' or c=='-1'):
			#clear()
			err = "Syntax error in line {} ".format(cou)
			print(err)
			exit() 
		else:
			out=(a+"00000"+b+c)
			output.append(out)
	
	elif ((arr[0] == "div" or arr[0] == "not" or arr[0] == "cmp") and len(arr)==3 and arr[1] in listr and arr[2] in listr):
		

		a = dic.get(arr[0])
		b = encodeA(arr[1])
		c = encodeA(arr[2])
		if(a=='-1' or b=='-1' or c=='-1'):
			#clear()
			err = "Syntax error in line {} ".format(cou)
			print(err)
			exit()
		else:
			out=(a+"00000"+b+c)
			output.append(out)
	
	elif ((arr[0] == "ld" or arr[0] == "st") and len(arr)==3):  
		a = dic.get(arr[0])
		b = encodeA(arr[1])
	#c=variable value
		c = variable_value(arr[2])
		if(a==-1 or b==-1):
			#clear()
			err = "Syntax error in line {} ".format(cou)
			print(err)
			exit()
		out=(a+b+c)
		output.append(out)

	elif ((arr[0] == "je" or arr[0] == "jlt" or arr[0]=="jmp" or arr[0]=="jgt") and len(arr)==2 and arr[1] in dictLabel):
		
		a=dic.get(arr[0])
		b=dictLabel.get(arr[1])
		b3=(bin(b))[2:]
		b4=b3.zfill(8)

		##b2=bin(int(str1[1:]))[2:]
		#txt1 = b2.zfill(8)
					
		if(b==-1):
			#clear()
			err = "Syntax error in line {} ".format(cou)
			print(err)
			exit()
		else:
			out=(a+"000"+b4)
			output.append(out)


	elif(arr[0]=="hlt" and len(arr)==1):
		a = dic.get(arr[0])
		out=(a + "00000000000")
		output.append(out)

	elif (arr[0][-1]==':'):
		arr.pop(0)
		instruction_call(arr)
		

	

	else:
		err = "Syntax error in line {} ".format(cou)
		print(err)
		exit()



def bnr(a):
	if a[0] == '$':
		b = a[1:]
		if b.isnumeric() == True:
			c =  bin(int(a[1:]))[2:]
			txt = c.zfill(8)
			return txt
	else: 
		return -1


def variable_value(x):
	a=int(indexHalt)
	if(listVar.count(x) == 1):
		b=listVar.index(x)
		k=a+b+1
		ans=bin(k)[2:]
		ans1=(str(ans)).zfill(8)
		return ans1
	else:
		err = "Wrong variable in line {} ".format(cou)
		print(err)
		exit()

def checkName(a) :
	s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890"
	if (a[0] not in s):
		return False
	else:
		if(len(a) > 1):
			return checkName(a[1:])
		elif(len(a) == 1):
			return True

arr=[]
def encode(a):
	if (a == 'R0'):
		return '000'
	elif (a == 'R1'):
		return '001'
	elif (a == 'R2'):
		return '010'
	elif (a == 'R3'):
		return '011'
	elif a == 'R4':
		return '100'
	elif a == 'R5':
		return '101'
	elif a == 'R6':
		return '110'
	elif a == 'FLAGS':
		return '111'
	elif a[0] == '$':
		b = a[1:]
		if b.isnumeric() == True:
			return bin(int(a[1:]))[2:]  # else error
		else:
			return '-1'
			
	else:
		return '-1'

def encodeC(a):
	if (a == 'R0'):
		return '000'
	elif (a == 'R1'):
		return '001'
	elif (a == 'R2'):
		return '010'
	elif (a == 'R3'):
		return '011'
	elif a == 'R4':
		return '100'
	elif a == 'R5':
		return '101'
	elif a == 'R6':
		return '110'
	elif a == 'FLAGS':
		return '111'
	else:
		return -1

def encodeA(a):
	if (a == 'R0'):
		return '000'
	elif (a == 'R1'):
		return '001'
	elif (a == 'R2'):
		return '010'
	elif (a == 'R3'):
		return '011'
	elif a == 'R4':
		return '100'
	elif a == 'R5':
		return '101'
	elif a == 'R6':
		return '110'
	else:
		return -1

for line in stdin:
	if line == '':
		break
	if line == "\n":
		allLines.append(line)
	else :
		line = line.strip()
		allLines.append(line)
		Lines.append(line)

#print(Lines)
if(len(Lines) > 256):
	cou = 256
	err = "ERROR in line {}: more than 256 instructions".format(cou)
	print(err)
	exit()

count = 0
listVar = []
dictLabel = {}
countVar=0
indexHalt = 0

for line in Lines:
	line = line.strip()
	count+=1
	if line[0:3] == "var":
		aaa = line.split()
		if(len(aaa) == 2 and listVar.count(aaa[1])==0):
			t3 = checkName(aaa[1])
			if(t3 == True):
				listVar.append(aaa[1])
				countVar += 1
				if countVar<count:
					cou = allLines.index(line) + 1
					err = "ERROR in line {}: Variable not declared at the beginning".format(cou)
					print(err)
					exit()
			else:
				cou = allLines.index(line) + 1
				err = "ERROR in line {}: Syntax error".format(cou)
				print(err)
				exit()
		elif len(aaa) == 2 and listVar.count(aaa[1]) != 0:
			#cou = allLines.index(line) + 1
			cou = len(allLines)- allLines[::-1].index(line)
			err = "ERROR in line {}: Variable already defined".format(cou)
			print(err)
			exit()
		elif len(aaa) != 2:
			cou = allLines.index(line) + 1
			err = "ERROR in line {}: Variable not properly defined".format(cou)
			print(err)
			exit()
	elif line[0:3] == "var" and len(line) == 3:
		cou = allLines.index(line) + 1
		err = "ERROR in line {}: Variable not properly defined".format(cou)
		print(err)
		exit()

allHalt = 0
flag2 = False
for line in Lines:
	if("hlt" in line):
		lst = line.split()
		if(len(lst) == 1):
			flag2 = True
			indexHalt = Lines.index(line) - countVar
			allHalt = allLines.index(line) + 1
			break
		elif len(lst) == 2 and lst[1] == "hlt" and lst[0][-1] == ":":
			lst[0] = lst[0][:-1]
			t4 = checkName(lst[0])
			if(t4 == True and lst[0] not in dictLabel.keys() and listVar.count(lst[0]) == 0):
				flag2 = True
				dictLabel[lst[0]] = Lines.index(line) - countVar
				indexHalt = Lines.index(line) - countVar
				allHalt = allLines.index(line) + 1
				break
			else:
				cou = allLines.index(line) + 1
				err = "ERROR in line {}: Syntax error".format(cou)
				print(err)
				exit()
		elif len(lst) == 2 and lst[1] == "hlt" and lst[0][-1] != ":":
			cou = allLines.index(line) + 1
			err = "ERROR in line {}: Syntax error".format(cou)
			print(err)
			exit()

if flag2 == False:
	cou = len(allLines)
	err = "ERROR in line {}: Missing hlt instruction".format(cou)
	print(err)
	exit()

elif flag2 == True and len(Lines) - countVar > indexHalt + 1:
	cou = allHalt 
	err = "ERROR in line {}: wrong declaration for hlt".format(cou)
	print(err)
	exit()


count = 0
"""
count = 0
arr1= Lines[-1]
arr1=arr1.split()
flag1=False
if(arr1[0][-1]==':' and arr1[-1]=='hlt' and arr1[1]=='hlt'):
	flag1 =True
	str1=''
	for e in Lines[-1]:
		str1+=e
	indexHalt = Lines.index(str1) - countVar
	
#print('hello') ###########################################################3
if flag == False:
	#Error message
	cou =  + 1
	err = "ERROR in line {}: Variable not declared at the beginning".format(cou)
	print(err)
	exit()
if Lines.count("hlt") > 1 and flag1==False:
    #check for a hlt b hlt c hlt  d #Lines= len(test_list) - 1 - test_list[::-1].index('e')
	#print('0 or >1') ###########################################################
	cou = len(allLines)- allLines[::-1].index('hlt')
	err = "ERROR in line {}: hlt instruction used more than once".format(cou)
	print(err)
	exit()
if Lines.count("hlt") == 0 and flag1==False:
	cou = len(allLines)
	err = "ERROR in line {}: Missing hlt instruction".format(cou)
	print(err)
	exit()
if(Lines.count("hlt") != 0 ):
	indexHalt = Lines.index("hlt") - countVar 
if len(Lines) - countVar > indexHalt + 1:
	cou =  allLines.index("hlt") + 1
	err = "ERROR in line {}: hlt not being used as the last instruction".format(cou)
	print(err)
	exit()
"""
for line in Lines:
	line = line.strip()
	if line != "hlt" and line[0:3] != "var":
		if line.count(":") == 1 and "hlt" not in line:
			t1 = line.index(":")
			t2 = checkName(line[:t1])
			if(t2 == True and line[:t1] not in dictLabel.keys() and listVar.count(line[:t1]) == 0):
				dictLabel[line[:t1]] = count 
				
				if line.index(":") + 1 == len(line):
					count -= 1
			else:
				if(t2 == True and listVar.count(line[:t1]) == 0 and line[:t1] in dictLabel.keys()):
					cou = allLines.index(line) + 1
					err = "ERROR in line {}: multiple declaration; declared more than once".format(cou)
					print(err)
					exit()
				else:
					cou = allLines.index(line) + 1
					err = "ERROR in line {}: Syntax error".format(cou)
					print(err)
					exit()
			
		if line.count(":") > 1:
			cou = allLines.index(line) + 1
			err = "ERROR in line {}: Syntax error".format(cou)
			print(err)
			exit()
		count += 1



for line in Lines:
	cou = allLines.index(line) + 1
	if line == "\n":
		continue
	elif line[0:3] != "var":
		line = line.strip()
		arr = line.split()
		instruction_call(arr)

for i in output:
	print(i)
