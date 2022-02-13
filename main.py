import os

# Whitespace
print("")

site = input("\033[1mEnter a website to steal:\n\033[0m >> ")
cmd = "wget -nc -r --user-agent=Mozilla --page-requisites -e robots=off " + site

# Run the command
print("")
os.system(cmd)

# Whitespace
print("")