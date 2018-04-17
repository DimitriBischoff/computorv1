#-*- coding: utf-8 -*-

from lib import *
from resolve import *
import sys

def cut(eq):
	i = 0
	j = 0
	exp = "+-"
	tmp = eq.split("=")
	ret = [[], []]

	for index, tab in enumerate(tmp):
		i = 0
		j = 0
		while j < len(tab):
			if tab[j] in exp:
				if i != j:
					ret[index].append(strextract(tab, i, j))
				ret[index].append(tab[j])
				i = j + 1
			j += 1
		ret[index].append(strextract(tab, i, j))
	return ret

def mapeq(eq, func):
	tmp = eq[:]

	for i, a in enumerate(tmp):
		tmp[i] = map(a, func)
	return tmp

def normalise(elem):
	if isnum(elem) and "*" not in elem:
		elem += " * X^0"
	if "X" in elem and " * X" not in elem:
		elem = elem.replace("X", " * X")
	if "X" in elem and "X^" not in elem:
		elem = elem.replace("X", "X^1")
	return elem

def printeq(eq, naturel = False):
	tmp = mapeq(eq, supprfloat)
	tmp = " = ".join([" ".join(tmp[0]), " ".join(tmp[1])])

	if naturel:
		print(replacesup(tmp,
			[" * X^0", " * X^1", " * X^2", " 1X"],
			["", "X", "X²", " X"]))
	else:
		print(tmp)

def calcelem(elem1, elem2, op):
	a = getnum(elem1)
	b = getnum(elem2)
	c = calc(a, b, op)

	return str(round(c, 5)) + elem1[search(elem1, " "):]

def reduce(eq):
	tmp = eq[:]
	deg = powmax(eq)

	for i in range(deg + 1):
		index1 = search(tmp[0], "X^" + str(i))
		index2 = search(tmp[1], "X^" + str(i))
		if index1 >= 0 and index2 >= 0:
			tmp[0][index1] = calcelem(getelem(tmp[0], index1),
				getelem(tmp[1], index2), '-')
			itmp = 1 if index2 - 1 >= 0 else 0
			tmp[1] = slice(tmp[1], index2 - itmp, 1 + itmp)
		elif index2 >= 0:
			signe = "-" if getsigne(tmp[1], index2) == "+" else "+"
			tmp[0].append(signe)
			tmp[0].append(tmp[1][index2])
			del tmp[1][index2]
	tmp = plusmoins(zero(tmp))
	return powmax(tmp), tmp

def zero(eq):
	tmp = eq[:]
	power = powmax(eq)

	for tab in tmp:
		while power == powmax(tmp):
			i = search(tab, "X^" + str(power))
			if i != -1 and getnum(tab[i]) == 0:
				tab[i] = "0"
			power -= 1
		while len(tab) and tab[0] == "+":
			del tab[0]
		i = search(tab, "0", True)
		while i != -1:
			del tab[i]
			if i - 1 >= 0:
				del tab[i - 1]
			i = search(tab, "0", True)
		if not len(tab):
			tab.append("0")
	return tmp

def plusmoins(eq):
	i = 0

	for tab in eq:
		while i < len(tab):
			if i > 0 and len(tab[i]) > 1 and tab[i][0] == '-':
				if tab[i - 1] == "+":
					tab[i] = tab[i][1:]
					tab[i - 1] = "-"
				elif tab[i - 1] == "-":
					tab[i] = tab[i][1:]
					if i - 1 > 0:
						tab[i - 1] = "-"
			i += 1
	return eq

def parse(entree):
	eq = replacesup(entree[1].upper(), [" ", "*"], ["", " * "])

	return mapeq(cut(eq), normalise)

def powmax(eq):
	f = lambda a: int(a[search(a, "^") + 1:])
	exp = "X^"
	tmp = map(findall(eq[0], exp) + findall(eq[1], exp), f)

	return max(tmp) if len(tmp) else 0

def main():
	deg = -1
	resolve = [
		resolve0,
		resolve1,
		resolve2
	]
	entree = sys.argv

	if len(entree) != 2 or "=" not in entree[1]:
		warning("error equation", entree[1:])
		return
	eq = parse(entree)
	printeq(eq)
	deg, eq = reduce(eq)
	title("Reduced form: ")
	printeq(eq)
	title("Polynomial degree: ", deg, '\n')
	if deg >=0 and deg <= 2:
		title("Natural form: ")
		printeq(eq, True)
		resolve[deg](eq)
	elif deg > 2:
		solution("The polynomial degree is stricly greater than 2, I can't solve.")
	else:
		warning("Problem !")

main()
