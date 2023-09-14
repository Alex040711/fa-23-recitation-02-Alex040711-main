from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(10, 1, 2) == 18
	assert simple_work_calc(20, 2, 2) == 92
	assert simple_work_calc(30, 3, 2) == 300


def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 131
	assert work_calc(20, 1, 2, lambda n: n*n) == 3150
	assert work_calc(30, 3, 2, lambda n: n) == 58350
	assert work_calc(10, 1, 2, lambda n: n) == 65
	assert work_calc(30, 1, 2, lambda n: n*n) == 12570
	assert work_calc(20, 2, 2,lambda n: 1) == 2621
