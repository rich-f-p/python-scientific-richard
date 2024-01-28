def arithmetic_arranger(problems,solve=False):
  arranged_problems = ""
  # send error if more than 5 problems
  if len(problems) >5:
    return "Error: Too many problems."

  # send error if operator is not + or -
  for problem in problems:
    if "+" not in problem and "-" not in problem:
      return "Error: Operator must be '+' or '-'."

  # send error if numbers are not digits
  for problem in problems:
    for char in problem:
      if char != "+" and char != "-" and char != " ":
        if char.isdigit() is not True:
          return "Error: Numbers must only contain digits."

  # send error if numbers are more than 4 digits
  for problem in problems:
    problem = problem.split()
    for num in problem:
      if len(num) > 4:
        return "Error: Numbers cannot be more than four digits."
  
  seperated_problems = []
  # split problems into lists
  for problem in problems:
    problem = problem.split()
    seperated_problems.append(problem)

  for string in seperated_problems:
    max_length=0
    spot = 0
    if len(string[0])>len(string[2]):
      max_length = len(string[0]) +2
    else:
      max_length = len(string[2]) +2
      spot = 2
      
    # create spacers
    for i in range(len(string)):
      if 0 == i:
        string[0]= " "*(max_length-len(string[i])) +string[i]
      elif 2 == i:
        string[2]= " "*((max_length-1)-len(string[i])) +string[i]
    string.append("-"*(max_length))
    # solve problems if solve is true
    if solve:
      if string[1] == "+":
        add = int(string[0])+int(string[2])
        add = str(add)
        string.append(" "*((max_length-len(add)))+add)
      else:
        sub = int(string[0])-int(string[2])
        sub = str(sub)
        string.append(' '*((max_length-len(sub)))+sub)

  set_order = []
  # create new list with the correct order
  for row in range(len(seperated_problems[0])):
    sort = []
    for col in range(len(seperated_problems)):
      if row == 1:
        sort.append(seperated_problems[col][row]+seperated_problems[col][row+1])
      elif row !=2:
        sort.append(seperated_problems[col][row])
    if sort !=[]:
      set_order.append(sort)
  # add correct format to arranged_problems
  for row in range(len(set_order)):
    for col in range(len(set_order[0])):
      if col == 0:
        arranged_problems += set_order[row][col]
      else:
        arranged_problems += "    "+set_order[row][col]
    if row != len(set_order)-1:
      arranged_problems += '\n'
  print(arranged_problems)
  
  return arranged_problems