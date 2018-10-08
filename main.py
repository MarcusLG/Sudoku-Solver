import numpy as np
import time
import curses

def array_input_2():
	in_array=[]
	in_row=[]
	str_input=[]
	for i in range(0,9):
		current_row=i+1
		current_row=str(current_row)
		text=str("x["+current_row+"]:\t")
		str_input=str(input(text))
		str_input=list(str_input)
		for j in range(0,9):
			if str_input[j]=='-':
				in_row.append(0)
			else:
				in_row.append(int(str_input[j]))
		in_array.append(in_row)
		in_row=[]
	return in_array

def array_input():
	print("Enter the puzzle horizontally then vertically:\n")
	input_array=[]
	input_row=[]
	for j in range(0,9):
		for i in range(0,9):
			input_row.append(int(input()))
		input_array.append(input_row)
		input_row=[]
	input_array=np.array(input_array)
	return input_array

def mapping(array_temp):
	for j in range(0,9):
		for i in range(0,9):
			if array_temp[j][i]!=0:
				array_temp[j][i]=1
	return array_temp

def counting(array_temp):
	for j in range(0,9):
		for i in range(0,9):
			array_temp[j][i]=0
	return array_temp

def checking_loc(array,y_point,x_point):
	tok_h=1#1-correct row
	tok_v=1#1-correct column
	tok_s=1#1-correct square
	x_s=int(np.floor(x_point)/3)
	y_s=int(np.floor(y_point)/3)
	for i in range(0,9):
		if array[y_point,x_point]==array[y_point,i] and i!=x_point:
			tok_h=0
	for i in range(0,9):
		if array[y_point,x_point]==array[i,x_point] and i!=y_point:
			tok_v=0
	for j in range(0,3):
		for i in range(0,3):
			if (y_s*3+j)!=y_point and (x_s*3+i)!=x_point:
				if array[y_point,x_point]==array[(y_s*3+j),(x_s*3+i)]:
					tok_s=0
	tok=[tok_v,tok_h,tok_s]
	return tok

def checking(array):
	tok=1	#1-correctly arranged array
	sum_h=np.sum(array,axis=1)
	sum_v=np.sum(array,axis=0)
	for i in range(0,9):
		if sum_h[i]!=45 or sum_v[i]!=45:
			tok=0
	return tok

def back_tracking(array_map,y_point,x_point):
	for i in range(1,x_point+1):
		if array_map[y_point,x_point-i]==0:
			previous_x=x_point-i
			previous_y=y_point
			tok_tracking=[previous_y,previous_x]
			return tok_tracking
	for j in range(y_point-1,-1,-1):
		for i in range(8,-1,-1):
			if array_map[j][i]==0:
				previous_x=i
				previous_y=j
				tok_tracking=[previous_y,previous_x]
				return tok_tracking	


def main(array_main,array_mapping, array_counting,start_time):
	i=0
	j=0
	global steps_taken
	steps_taken=0
	steps=steps_taken
	tok_main=0
	working_array=array_main
	while j<9:
		while i<9:
			if array_mapping[j][i]==0:
				tok_main=0
				while(tok_main!=3):
					#screen.refresh()
					#time_elapsed=int(np.floor(time.time()-start_time))
					#print(working_array, end="\n\r", flush="True")
					#print("\nSystem run time (sec):")
					#print(time_elapsed, end="\n\r", flush="True")
					array_counting[j][i]+=1
					working_array[j][i]=array_counting[j][i]
					steps_taken=steps_taken+1
					tok_main=np.sum(np.array(checking_loc(working_array,j,i)))
					if array_counting[j][i]>9:
						array_counting[j][i]=0
						working_array[j][i]=0	#resetting current working box
						ji=back_tracking(array_mapping,j,i)
						j=ji[0]
						i=ji[1]-1
						break
			i+=1
		j+=1
		i=0
	return working_array

array=array_input_2()
array=np.array(array)
array_map=mapping(np.array(array))
array_counter=counting(np.array(array))

#main sorting programme
screen = curses.initscr()
start_time=time.time()
result=main(array,array_map,array_counter,start_time)
stop_time=time.time()

screen.refresh()
print("The solution is:\n",end="\r", flush="True")
print(result)

time_elapsed=float(np.floor(stop_time-start_time))
print("\nTotal time elapsed:\t")
print(time_elapsed," seconds")

print("\nTotal number of steps taken:")
print(steps_taken," steps")
