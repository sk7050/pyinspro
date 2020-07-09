import time
def prime(x):
	if(~x==-2):
		return 0
	else:
		return 1
def Truth_Table_t0_Display(Truth_Table):
	a1,b1,c1,d1,e1,f1,g1=Truth_Table
	a=g=d=" --"
	e=c=f=b="|"
	if a1==0:
		a=""
	if g1==0:
		g=""
	if b1==0:
		b=" "
	if e1==0:
		e=" "
	if c1==0:
		c=" "
	if f1==0:
		f=" "
	if d1==0:
		d=""
	element=(a,f+"  "+b,g,e+"  "+c,d)
	return element

	


def seven_segment(A,B,C,D):
	a=(A|C|(B &D)|(prime(B) & prime(D)))
	b=(prime(B)|(prime(C) & prime(D))|(C & D))
	c=(B|prime(C)|D)
	d=((prime(B) & prime(D))|(C & prime(D))|(B & prime(C) & D)|(prime(B) & C)|A)
	e=((prime(B) & prime(D))|(C & prime(D)))
	f=(A|(prime(C) & prime(D))|(B & prime(C))|(B & prime(D)))
	g=(A|(B & prime(C))|(prime(B) & C)|(C & prime(D)))
	return a,b,c,d,e,f,g
	
def Dec_to_B(n):
	BI= "{0:04b}".format(n)
	A=int(BI[0])
	B=int(BI[1])
	C=int(BI[2])
	D=int(BI[3])
	
	Truth_Table=seven_segment(A,B,C,D)
	display_paramiter=Truth_Table_t0_Display(Truth_Table)
	return display_paramiter

for n in range(10):
	time.sleep(1)
	for i in Dec_to_B(int(n)):
		print(i)






