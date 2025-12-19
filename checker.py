def check_password(password):
  rules={"length":False,
         "upper":False,
         "digit":False,
         "lower":False,
         "special":False}
  special="!@#$%^&*"
  if len(password)>=8:
    rules["length"]=True
  for ch in password:
    if ch.isupper():
      rules["upper"]=True
    elif ch.islower():
      rules["lower"]=True
    elif ch.isdigit():
      rules["digit"]=True
    elif ch in special:
      rules["special"]=True
  score=sum(rules.values())
  return rules,score
def get_strength(score):
  if score<=2:
    return "Weak"
  elif score<=4:
    return "Medium"
  else:
    return "strong"
def suggestion(rules):
  tip=[]
  if not rules["length"]:
    tip.append("use at least 8 characters")
  if not rules["digit"]:
    tip.append("use at least one digit")
  if not rules["lower"]:
    tip.append("use a lower character in your password")
  if not rules["upper"]:
    tip.append(" Add a uppercase letter")
  if not rules["special"]:
    tip.append("use a special character ")
  return tip

password=input("Enter the password -->")
rules,score=check_password(password)
strength =get_strength(score)
print("password check:")
for rule,value in rules.items():
  print(f"{rule.capitalize():8}: {value}")
print("strength of password",strength)
if strength!="strong":
  print(f"suggestions :")
  for i in suggestion(rules):
    print(i)
