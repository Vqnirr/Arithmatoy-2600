# Aucun n'import ne doit être fait dans ce fichier


def nombre_entier(n: int) -> str:
	return f"{'S'*n}0"


def S(n: str) -> str:
	return f"S{n}"
	


def addition(a: str, b: str) -> str:
	
	""" 
	a = "" if a == "0" else a[:-1]
	b = "" if b == "0" else b[:-1]

	if a == b == "0":
		return "0" 
	"""

	if a == "0":
		return b

	return S(addition(a[1:], b))
   


def multiplication(n: str, x: str) -> str:

	if n == "0":
		return "0"

	return  addition(multiplication(n[1:], x), x)


def facto_ite(n: int) -> int:
	accum = 1
	for i in range(1, n+1):
		accum *= i
	return accum

def facto_rec(n: int) -> int:
	if n == 0:
		return 1
	return n * facto_rec(n - 1)


def fibo_rec(n: int) -> int:
	if n == 0:
		return 0
	if n == 1:
		return 1
	
	return fibo_rec(n-1) + fibo_rec(n-2)


def fibo_ite(n: int) -> int:

	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		a = 0
		b = 1
		for i in range(n-1):
			tmp = a + b
			a = b
			b = tmp
		return b
			

def golden_phi(n: int) -> int:
	#https://fr.wikipedia.org/wiki/Nombre_d%27or#Suite_de_Fibonacci
	if n == 0:
		return 1
	return 1 + 1/golden_phi(n-1)


def sqrt5(n: int) -> int:
	return n ** (1/5)


def pow(a: float, n: int) -> float:
	if n == 0:
		return 1
	return a * pow(a, n-1)


def pow2(a: float, n: int) -> float:
	result = 1
	for _ in range(n):
		result *= a
	return result 


def pow3(a: float, n: int) -> float:
	if n == 0:
		return 1
	if n % 2 == 0:
		return pow3(a * a, n // 2)
	else:
		return a * pow3(a, n-1)



