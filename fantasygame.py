##INVENTORY PROGRAM 

def displayInventory(inventory): # SHOWS WHAT'S INSIDE INVENTORY
	print("Inventory: ")
	for k, v in inventory.items():
		print (str(v),k)	
	print (f"Total number of items: {sum(inventory.values())}")

def add_to_inventory(inventory, addedItems): # adds new items to inventory 
	for item in addedItems:
		if item in inventory:
			inventory[item]+=1
		else:
			inventory[item] = 1
	return inventory

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'rope': 1, 'gold coin': 42}
inv = add_to_inventory(inv, dragonLoot)
displayInventory(inv)






