vlans={}
vlans["10"]="HR"
vlans["20"]="IT"
vlans["30"]="Finance"
print(vlans)
while True:
    print("===VLAN Manager===\n")
    print("1. Create vlan:")
    print("2. View vlan: :")
    print("3. Search vlan :")
    print("4. Delete vlan :")
    print("5. Exit :")
    choice =input("Enter Your Choice: ")
    if choice == "1":
        vlan_id =input("Enter vlan id: ")
        vlan_name =input("Enter vlan name: ")
        if vlan_id in vlans:
            print("VLAN already exists") 
        else: 
        # save in Dictionary
            vlans[vlan_id]=vlan_name
        #save in file
            with open("vlan.txt","a") as file:
               file.write(f"{vlan_id} {vlan_name} \n")
               print("Vlan add successfully!: ")
        #view vlan
    elif choice == "2":
        if len(vlans) ==0:
            print("Vlan not Found!: ")
        else:
            print("\n VLAN ID\t VLAN Name")
            print("-" * 25)
        for vlan_id , vlan_name in vlans.items():
            print(vlan_id,vlan_name)
        #search vlan
    elif choice =="3":
        search =input("Enter vlan id: ")
        if search in vlans:
            print("\n VLAN Found!")
            print("VLAN ID:",search)
            print("VLAN Name:", vlans[search])
        else:
            print("Vlans Not Found!")
        #Delete vlan
    elif choice =="4":
        delete=input("Enter Vlan ID to delete: ")
        if delete in vlans:
            del vlans[delete]
            print("VLAN Delete Successful:")
        else:
            print("Vlan Not Found!")
        #Exit
    elif choice =="5":
        print("Thank You for using Vlan Manager:")
        break
    else:
        print("Invalied Choice,Plese Try Again.")