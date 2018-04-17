#-*- coding: utf-8 -*-

def abs(a):
	return -a if a < 0 else a

def calc(a, b, op):
	if (isnum(a) and isnum(b) and isoperator(op)):
		return {
			"+": lambda a, b: float(a) + float(b),
			"-": lambda a, b: float(a) - float(b),
			"*": lambda a, b: float(a) * float(b),
			"/": lambda a, b: float(a) / float(b),
			"^": lambda a, b: pow(float(a), float(b))
		}[op](a, b)
	return None

def debug(*args):
	print(color(str(args), "white"))
	pause()

def defloat(a):
	return a if isfloat(a) else int(a)

def findall(tab, r):
	i = 0
	tmp = []

	i = search(tab, r)
	while (i != -1):
		tmp.append(tab[i])
		tab = tab[i + 1:]
		i = search(tab, r)
	return tmp

def isnum(n):
	return ((type(n) is int) or (type(n) is float)
			or (type(n) is str and n.isnumeric()))

def isfloat(a):
	return a - int(a) != 0

def isoperator(op):
	return op in "^/*+-"

def join(tab, sep):
	tmp = ""

	for i, e in enumerate(tab):
		tmp += str(e) + (str(sep) if i < len(tab) - 1 else "")
	return tmp

def map(tab, f):
	tmp = []

	for a in tab:
		tmp.append(f(a))
	return tmp

def pause():
	return
	# input("PAUSE...")

def pow(a, b):
	c = a;

	if not b:
		return 1
	for i in range(int(b - 1)):
		c = c * a
	return c

def removeall(list, rm):
	while rm in list:
		list.remove(rm)
	return list

def replacesup(s, a, b):
	tmp = s

	for i, ra in enumerate(a):
		tmp = tmp.replace(ra, b[i])
	return tmp
	
def round(a, n = 0):
	neg = -1 if a < 0 else 1
	a = abs(a)
	b = int(a * pow(10, n + 1)) % 10
	c = a + (1 / pow(10, n) if b >= 5 else 0)

	return trunc(c, n) * neg

def search(tab, n, equal = False):
	for i in range(len(tab)):
		if equal:
			if n == tab[i]:
				return i
		else:
			if n in tab[i]:
				return i
	return -1

def sqrt(a, p = 1):
	i = 1.0
	j = 0
	while j <= p:
		step = 1 / pow(10, j)
		while (i + step) * (i + step) < a:
			i = i + step
		if i * i == a:
			return i
		j = j + 1
	return trunc(i, p)

def slice(tab, i, j):
	return tab[:i] + tab[i + j:]

def strextract(s, a, b):
	tmp = ""

	while a < b:
		tmp = tmp + s[a]
		a = a + 1
	return tmp

def trunc(a, n = 0):
	mult = pow(10, n)

	return float(int(a * mult) / mult)

def color(text, color):
	c = {
		"white"		: "1m",
		"red"		: "31m",
		"green"		: "32m",
		"yellow"	: "33m",
		"blue"		: "34m",
		"purple"	: "35m",
		"cyan"		: "36m",
		"grey"		: "37m"
	}
	return "\033[" + c[color] + text + "\033[0m"

def title(text, *params):
	print(color(text, "cyan"), *params, end="", sep="")

def solution(text, *params):
	print(color(text, "yellow"), *params, end="\n", sep="\n")

def warning(text, *params):
	print(color(text, "red"), *params, end="\n", sep=" ")






















