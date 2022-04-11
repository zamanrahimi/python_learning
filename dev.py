import sys
  
# sys.path.insert(0, './pages')
sys.path.append('./pages')
  
#sub_page is sub_page.py which has add() and sub() functions
from sub_page import *
  
# calling odd_even function
add(3,5)
sub(10,5)