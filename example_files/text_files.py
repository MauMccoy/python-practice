#OPEN A TEXT FILE AND READ IT
with open('example_files/example.txt', 'r') as file:
    file_text = file.read()
print(file_text) 

#IMPORT FILES IN PYTHON
line = "jrafael,192.168.243.140,4:56:27,True"

with open("example_files/access_log.txt", "a") as file:

    file.write(line)

#NOW READ FILE BACK TO CONFIRM
with open("example_files/access_log.txt", "r") as file:
    contents = file.read()
    print(contents)

#APPEND TO A FILE
with open("example_files/access_log.txt", "a") as file:
    file.write('\n# Este nuevo bloque de comentario explica que la línea fue agregada al archivo usando el modo "a" (append) al manejar archivos en Python. El modo a permite añadir contenido al final del archivo sin borrar')

#OPEN, READ, AND SPLIT A FILE
with open("example_files/login_attempts.txt", "r") as file:
    file_text = file.read()
    print(file_text.split('\n'))

#THE BASICS OF SPLIT()
approved_users = "jrafael,mgarcia,lrodriguez,jmartinez"
print('Before split:', approved_users)
approved_users = approved_users.split(',')
print('After split:', approved_users)

#APPLYING split() TO FILES
with open("example_files/login_attempts.txt", "r") as file:
    access_log = file.read()
access_log = access_log.split('\n')
print(access_log)

#THE BASIS OF JOIN()
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
print("before .join():", approved_users)
approved_users = ",".join(approved_users)
print("after .join():", approved_users)

#APPLYING join() TO FILES
with open("example_files/access_log.txt", "r") as file:
    updates = file.read()
updates = updates.split()
updates = " ".join(updates)
with open("example_files/access_log.txt", "w") as file:
    file.write("this is a test\n")

