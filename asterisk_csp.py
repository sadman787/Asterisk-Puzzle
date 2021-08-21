#Look for #IMPLEMENT tags in this file.
'''
All models need to return a CSP object, and a list of lists of Variable objects 
representing the board. The returned list of lists is used to access the 
solution. 

For example, after these three lines of code

    csp, var_array = asterisk_csp_model_1(board)
    solver = BT(csp)
    solver.bt_search(prop_FC, var_ord)

var_array[0][0].get_assigned_value() should be the correct value in the top left
cell of the asterisk puzzle.

1. asterisk_csp_model_1 (worth 20/100 marks)
    - A model of an Asterisk grid built using only 
      binary not-equal constraints

2. asterisk_csp_model_2 (worth 20/100 marks)
    - A model of an Asterisk grid built using only 9-ary 
      all-different constraints

'''
from cspbase import *
import itertools

def asterisk_csp_model_1(ast_grid):
    ##IMPLEMENT
    

def asterisk_csp_model_2(ast_grid):
    ##IMPLEMENT 
    
