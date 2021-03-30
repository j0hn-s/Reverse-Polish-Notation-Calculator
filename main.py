""" To perform calculations please give your expressions as a list of numbers and operations, with single spaces after each element: 

For example '3 4 + =' will return '7', and is equivilent to the expression "3 + 4 =", whilst "3 3 * 4 4 * + =" will return '25', and is equivilent to '(3 * 3) + (4 * 4) =' """

print ("You may now start interacting with the SRPN calculator")


user_stack = []


r_list = [1804289383, 846930886, 1681692777, 1714636915, 1957747793, 424238335, 719885386, 1649760492, 596516649, 1189641421, 1025202362, 1350490027, 783368690, 1102520059, 2044897763, 1967513926, 1365180540, 1540383426, 304089172, 1303455736, 35005211, 521595368]


inc_op = ('+', '-', '*', '/', '%', '=', 'd','^', 'r', ' ') 


# The following section defines the functions implemented in the calculator-

# The function below converts user inputs into integers and ensures calculator returns an integer:
def user_int_in(user_in):
  try:
    return int(user_in)
  except:
    return user_in


# The function below converts user inputs into integers and ensures calculator returns an integer:

def result_range(result):
  max_val = 2147483647
  min_val = -2147483648
  if result >= max_val:
    user_stack[-1] = max_val
    print(max_val)
  elif result <= min_val:
    user_stack[-1] = min_val
    print(min_val)
  else:
    print(result)


# (iii) The following function displays the top of the stack and outputs "stack empty" in instances where the stack contains 0 elements:

def top_stack():
  if user_stack[-1] == '=':
    user_stack.pop(-1)
    try:
      result_range(user_stack[-1])
    except:
      if len(user_stack) == 0:
        print("Erro: Stack Is Empty.")
  

# The function below provides the user with an error message if the input is not included in the list of defined numerical operators or constitutes a non-integer value:

def not_inc_op():         
  for i in range(len(user_stack)):
    if user_stack[i] not in inc_op and type(user_stack[i]) != int and len(user_stack[i]) == 1:
      print(f'Error: Unrecognized Numerical Value: "{user_stack[i]}" ')
      user_stack.pop(i)


# The function below provides the user with an error message if the input is not included in the list of defined alphabetical character-operators, calling on function:  

def not_inc_alph(character):
  if character not in inc_op: 
    print(f'Error: Unrecognized Character: "{character}" ')


# The following function equates d to -2147483648 when the stack is empty and applies maximum/minimum & integer value constraints:

def return_stack():
  if user_stack[-1] == 'd':
    user_stack.pop(-1) 
    if len(user_stack) == 0:
      print(int(-2147483648))
    for i in range(len(user_stack)):
      if type(user_stack[i]) == int:
        result_range(user_stack[i])


#The function below hierarchically selects a given number from list provided in r_list (i.b) and adds it to the defined stack, removing it from r_list in the process:

def select_r_list():
  if user_stack[-1] == 'r':
    user_stack.pop(-1)
    user_stack.append(r_list[0])
    r_list.append(r_list.pop(0))


#The following function handles underflow errors found within the stack and ensures that stack is longer than 1:

def stack_underflow():
  if len(user_stack) ==1:
    print("Error: Stack underflow")
    
    
#The function below ensures that user can return "divide by 0":

def div_zero():
  if user_stack[-1] == 0:
    print("Divide By 0")


# The following function checks the stack to ensure that only results are retained:
def check_stack():
  user_stack.pop(-3)
  user_stack.pop(-2)


#The following section defines the main function contained in the program: the calculator engine/controller. This function calls on a variety of the preceding functions and performs a multitude of calculations. After any given calculation the engine stores the result in the stack, whilst deleting the remaining components of the calculation:

def calc_controller():
  top_stack()
  if user_stack[-1] == '+':
    user_stack.pop(-1)

    try:
      user_stack.append(user_stack[-2] + user_stack[-1])
      check_stack()
    except:
      stack_underflow()
  if user_stack[-1] == '-':
    user_stack.pop(-1)
    
    try:
      user_stack.append(user_stack[-2] - user_stack[-1])
      check_stack()
    except:
      stack_underflow()
  if user_stack[-1] == '*':
    user_stack.pop(-1)
    
    try:
      user_stack.append(user_stack[-2] * user_stack[-1])
      check_stack()
    except:
      stack_underflow()
  if user_stack[-1] == '/':
    user_stack.pop(-1)
    
    try:
      user_stack.append(user_stack[-2] // user_stack[-1])
      check_stack()
    except:
      stack_underflow()
      div_zero()
  if user_stack[-1] == '%':
    user_stack.pop(-1)
    
    try:
      user_stack.append(user_stack[-2] % user_stack[-1])
      check_stack()
    except:
      stack_underflow()
  if user_stack[-1] == '^':
    user_stack.pop(-1)
    
    try:
      user_stack.append(user_stack[-2] ** user_stack[-1])
      check_stack()
    except:
      stack_underflow()


#The function below defines the format allowing horizontal user inputs, when the length of the input string is greater than 1 and an integer, as defined by the compliment of (iv.a):

def num_string_int_inp(user_in):
  if type(user_in) == str and len(user_in) > 1:
    user_in = user_in # Adding flag (§) ensures that user_in does not miss last element of input
    user_stack.pop(-1)
    user_in = user_in + '&'
    
    for i in range(len(user_in)):
      if user_in[i] == '': 
        user_in[i] = '&'
    start = 0 # (a)
    end = 0 # (b)

    for i in range(len(user_in)):
      if user_in[i] in ('+', '-','^', '%','/', '^', '*', ' ','', '&', 'd', 'r', '='): 
        end = i # # Fixes final element- defined by (a)- to pre-defined reference points, constituted by preceding operators (c)
        
        try: 
          user_stack.append(int(user_in[start:end]))
          if user_in[end] not in (' ', '&'):
            user_stack.append(user_in[end])
            calc_controller()
            top_stack()
            return_stack
            select_r_list()
          
        except:
          if user_in[end] not in (' ', '&'):
            user_stack.append(user_in[end])
            calc_controller()
            top_stack()
            return_stack()
            select_r_list()      
                
        start = end + 1 
  else:
    top_stack()
    return_stack()
    select_r_list()
    pass


# The following function combines and processes all operations in the stack, but prohibits inputs with more than 24 elements:

def other_symbols(user_in):
  if type(user_in) == str and len(user_in) > 1:
    for i in range(len(user_in)):
      try:
        int(user_in[i])
      except:
        not_inc_alph(user_in[i])

def stack_elements(user_in):
  if len(user_stack) >= 24:
    print("Error: Stack Overflow.")
    if type(user_stack[-1]) == str:
      other_symbols(user_in)
      num_string_int_inp(user_in)
      not_inc_op()
      calc_controller()
    elif type(user_stack[-1]) == int:    
        user_stack.pop(-1)
    
  else:
    try:
      other_symbols(user_in)
      num_string_int_inp(user_in)
      not_inc_op()
      calc_controller()
    except:
      main()


#The following calls all functions contained within program through function (v), by creatnig an infinite loop which appends user inputs to the stack

def main():
  while True:
    
    user_in = input("")
    user_in = user_int_in(user_in)
    user_stack.append(user_in)
    
    stack_elements(user_in)

main()