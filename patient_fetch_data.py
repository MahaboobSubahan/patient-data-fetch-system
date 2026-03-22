while True:
  uid=input("enter the patient id (1-10): ")
  if not uid.isdigit():
    print("enter numbers only")
    continue
  if not 1<=int(uid)<=10:
    print("enter values between(1-10)")
    continue
  url=f"http://jsonplaceholder.typicode.com/users/{uid}"
  response=requests.get(url)
  if response.status_code==200:
    data=response.json()
    out=input("click 1 :name,2: email,3:full details")
    if out=="1":
      print("Name:" , data["name"])
    elif out=="2":
      print("email:" , data["email"])
    elif out=="3":
      print("\n-------Patient Details -------")
      print("Name:",data["name"])
      print("Email:",data["email"])
      print("City:",data["address"]["city"])
      print("Company:", data["company"]["name"])
    else:
      print("enter valid credentials")
  else:
    print("enter values between(1-10)")
  cont=input("do you want to continue?(yes/no)")
  if cont.lower()!="yes":
      break