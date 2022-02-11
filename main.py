import os

# Whitespace
print("")

site = input("\033[1mEnter a website to steal:\n\033[0m >> ")

# wget -r --user-agent=Mozilla --page-requisites --convert-links -e robots=off https://cdn.openttd.org
cmd = "wget -r --user-agent=Mozilla --page-requisites --convert-links -e robots=off " + site

# Run the command
os.system(cmd)

# Whitespace
print("")