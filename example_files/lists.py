#CONCATENATE TWO LISTS
my_list1 = ["a", "b", "c", "d", "e", "f"]
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list1 + number_list)

#CHANGE A SPECIFIC ELEMENT IN A LIST
my_list1 = ["a", "b", "c", "d", "e", "f"]
my_list1[1] = 7
print(my_list1)

#USE INSERT METHOD
my_list1 = ["a", "b", "c", "d", "e", "f"]
my_list1.insert(1, 7)
print(my_list1)

#USE THE REMOVE METHOD
my_list1 = ["a", "b", "c", "d", "e", "f"]
my_list1.remove("d")
print(my_list1)

#EXTRACT THE FIRST 3 CHARACTERS OF AN IP ADDRESS
ip_address = "198.223.xx.xxx"
print(ip_address[0:3])

#EXTRACT THE FIRST 3 CHARACTERS FROM A LIST OF IP ADDRESSES
IP = ["198.223.xx.xxx", "192.168.xx.xxx", "10.0.xx.xxx"]
networks = []
for addresses in IP:
    networks.append(addresses[0:3])

print(networks)