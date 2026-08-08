def func(name,loc):
    print(f"Hello {name}")
    print(f"Are you from {loc}")

func("shruthi","karimnagar")
print("---------------------------------")

#now when we change the order of arguements it became complete nonsnse in the compiler
#do be more specific we need to add keyword arguements
func("Karimnagar","Shruthi")
print("----------------------------------")
func(name="shruthi",loc="karimnagar")