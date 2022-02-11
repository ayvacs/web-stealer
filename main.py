import os

# Define colours
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Whitespace
print("")

site = input(bcolors.BOLD + "Enter a website to steal:\n" + bcolors.ENDC + ">> ")

# wget -r --user-agent=Mozilla --page-requisites --convert-links -e robots=off https://cdn.openttd.org
cmd = "wget -r --user-agent=Mozilla --page-requisites --convert-links -e robots=off " + site

print("\n"+cmd)

# Run the command
os.system(cmd)

# Whitespace
print("")