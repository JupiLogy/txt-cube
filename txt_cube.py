from rubik_solver import utils
import random
import numpy as np
import sympy.combinatorics.permutations as perm
import sympy.combinatorics.generators   as gens

def lse_scr():
	corners			= random.choice(range(4))
	if corners == 1 or corners == 3:
		permn 		= random.choice(o_6)
	else:
		permn  		= random.choice(a_6)
	flip   			= random.choice(range(4))
	orient 			= random.sample(range(6), flip*2)
	m2 				= random.choice(range(2))
	LSE_pieces 		= np.array([[1, 37], [3, 10], [7, 19], [5, 28], [46, 25], [52, 43]])
	LSE_pieces_new	= LSE_pieces
	for i in orient:
		LSE_pieces_new[i] = perm.Permutation(0,1)(LSE_pieces[i])
	LSE_pieces_new 	= permn(LSE_pieces_new)

	edge_perm_list	= perm.Permutation(53).list()
	for i in range(12):
		edge_perm_list[np.asarray(LSE_pieces).reshape(12)[i]] = np.asarray(LSE_pieces_new).reshape(12)[i]

	scramble_perm = perm.Permutation(11,20,29,38)(6,8,2,0)(18,27,36,9)**corners*perm.Permutation(edge_perm_list)

	cube = scramble_perm(SOLVED_CUBE)
	if m2 == 1:
		cube = M2(cube)
	return(cube)

def generate_moves():
	M2 = DEFAULT_CUBE
	M  = DEFAULT_CUBE
	Mp = DEFAULT_CUBE
	U  = DEFAULT_CUBE
	U2 = DEFAULT_CUBE
	Up = DEFAULT_CUBE

	for cubelet in [1,4,7]:
		M  = M *perm.Permutation(cubelet,	 44-cubelet, cubelet+45, cubelet+18)	# UM -> FM -> DM -> BM

	U = perm.Permutation(53)(0,2,8,6)(1,5,7,3)										#Rotates U face
	for cubelet in [9,10,11]:
		U  = U *perm.Permutation(cubelet,    cubelet+9,  cubelet+18, cubelet+27)	# FU -> LU -> BU -> RU

	M2 = M*M
	Mp = M2*M

	U2 = U*U
	Up = U2*U

	return(M2, M, Mp, U, U2, Up)

def generate_groups():
	a_6	= list(gens.alternating(6))
	o_6 = [x for x in list(gens.symmetric(6)) if x not in a_6]
	return(a_6, o_6)

DEFAULT_CUBE = perm.Permutation(53)
COLOUR_NAMES = ["Y","B","R","G","O","W"]
SOLVED_CUBE = []
for colour in COLOUR_NAMES:
	for cubie in range(9):
		SOLVED_CUBE.append(colour)

a_6, o_6 = generate_groups()
M2, M, Mp, U, U2, Up = generate_moves()