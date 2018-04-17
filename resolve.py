#-*- coding: utf-8 -*-

from lib import *

def getnum(elem):
	if elem is None:
		return 0
	for i in range(len(elem)):
		if elem[i] == " ":
			return float(strextract(elem, 0, i))

def getsigne(tab, index):
	if index - 1 < 0:
		return "+"
	return "-" if tab[index - 1] == "-" else "+"

def getelem(tab, index):
	if index < 0 or index >= len(tab):
		return None
	tmp = getsigne(tab, index) + tab[index]
	if "-+" in tmp or "+-" in tmp:
		return "-" + tab[index][1:]
	elif "--" in tmp or "++" in tmp:
		return "+" + tab[index][1:]
	return tmp

def supprfloat(elem):
	tmp = str(elem)
	exp = ".0"
	i = 0

	while exp in tmp[i:]:
		index = tmp[i:].index(exp)
		if index != -1:
			if (i + index + 2 < len(tmp) and not isnum(tmp[i + index + 2]) or
					i + index + 2 == len(tmp)):
				tmp = slice(tmp, i + index, 2)
			i = i + index + 2
		else:
			break
	return tmp

def resolve0(eq):
	if getnum(eq[0][0]) == getnum(eq[1][0]):
		solution("valid")
	else:
		solution("invalid")

def resolve1(eq):
	num1 = getnum(getelem(eq[0], search(eq[0], "X^0")))
	num2 = getnum(getelem(eq[0], search(eq[0], "X^1")))

	try:
		solution("The solution is:", supprfloat(round(-num1 / num2, 9)))
	except ZeroDivisionError as err:
		warning("error:", err)
	
def resolve2(eq):
	a = getnum(getelem(eq[0], search(eq[0], "X^2")))
	b = getnum(getelem(eq[0], search(eq[0], "X^1")))
	c = getnum(getelem(eq[0], search(eq[0], "X^0")))
	disc = pow(b, 2) - 4 * a * c
	resultat = ""

	try:
		if disc > 0:
			solution("Discriminant is strictly positive, the two solutions are:")
			resultat = [
				round((-b - sqrt(disc, 10)) / (2 * a), 9),
				round((-b + sqrt(disc, 10)) / (2 * a), 9)
			]
		elif disc < 0:
			solution("Discriminant is strictly negative, the two solutions are:")
			rcdisc = round(sqrt(abs(disc), 10), 9)
			if a != 0 and -b == 2 * a:
				resultat = [
					"1 + " + str(rcdisc / (2 * a)) + "i",
					"1 - " + str(rcdisc / (2 * a)) + "i"
				]
			else:
				resultat = [
					join(["(", -b, " + ", rcdisc, "i) / ", 2 * a], ""),
					join(["(", -b, " - ", rcdisc, "i) / ", 2 * a], "")
				]
		else:
			solution("Discriminant is zero, the solution is:")
			resultat = [round(-b / (2 * a), 9)]
		resultat = join(map(resultat, supprfloat), "\n").replace(" 1i", " i")
		print(resultat)
	except ZeroDivisionError as err:
		warning("error:", err)
