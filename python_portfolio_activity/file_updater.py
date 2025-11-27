# Your task is to create an algorithm that uses Python code to check whether the allow list 
# contains any IP addresses identified on the remove list. If so, you should remove 
# those IP addresses from the file containing the allow list.
import_file = "allow_list.txt"

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

#READ THE CONTENTS OF THE import_file INTO A LIST
with open(import_file, 'r') as file:
    ip_addresses = file.read()
    print(ip_addresses)
    # Split the string into a list of IP addresses
    ip_addresses = ip_addresses.split()

#ITERATE THROUGH THE remove_list AND CHECK IF ANY ELEMENTS EXIST IN THE ip_addresses LIST
for element in ip_addresses:
    if element in remove_list:
        #REMOVE THE ELEMENT FROM THE ip_addresses LIST
        ip_addresses.remove(element)

#CONVERT THE ip_addresses LIST BACK TO A STRING
ip_addresses = " ".join(ip_addresses)

#WRITE THE UPDATED ip_addresses LIST BACK TO THE import_file
with open(import_file, 'w') as file:
    file.write(ip_addresses)
   
#PRINT THE UPDATED CONTENTS OF THE import_file
with open(import_file, 'r') as file:
    text = file.read()

print(text)