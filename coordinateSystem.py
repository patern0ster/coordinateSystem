coordx = eval(input("Give the coordinate x: "))
coordy = eval(input("Give the coordinate y: "))
coord=[]
coord.append(coordx)
coord.append(coordy)
coord = tuple(coord)
column = [" "," "," "," ","|"," "," "," "," "]
row =    ["—","—","—","—"," ","—","—","—","—"]
columnwritten=[" "," "," "," ","|"," "," "," "," "]
if coord[1] < 0 or coord[1] >0:
	columnwritten[coord[0]+4]="*"
else:
	row[coord[0]+4]="*"
counter=0
while counter < 9:
	if counter-4 == -coord[1]:
		n=0
		if coord[1]<0 or coord[1]>0:
			while n<9:
				print(columnwritten[n],end="  ")
				n+=1
		else:
			while n<9:
				print(row[n],end="  ")
				n+=1
		print("\n")
	elif counter<4:
		n=0
		while n<9:
			print(column[n],end="  ")
			n+=1
		print("\n")	
	elif counter>4:
		n=0
		while n<9:
			print(column[n],end="  ")
			n+=1
		print("\n")
	else:
		n=0
		while n<9:
			print(row[n],end="  ")
			n+=1
		print("\n")
	counter+=1
if coord[0]==0 and coord[1]==0:
	print("it is the origin of the coordinate system")
elif coord[0]>0 and coord[1]>0:
	print("it is on the first zone")
elif coord[0] <0 and coord[1]>0:
	print("it is on the second zone")
elif coord[0] <0 and coord[1]<0:
	print("it is on the third zone")
elif coord[0] >0 and coord[1] <0:
	print("it is on the forth zone")
elif coord[0] == 0 and coord[1]>0:
	print("it is on the positive y-axis")
elif coord[0] == 0 and coord[1]<0:
	print("it is on the negative y-axis")
elif coord[0]>0 and coord[1] == 0:
	print("it is on the positive x-axis")
elif coord[0]<0 and coord[1] == 0:
	print("it is on the negative x-axis")
