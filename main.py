print("")

site = input("Enter a website to steal:\n >> ")

# wget -r --user-agent=Mozilla --page-requisites --convert-links -e robots=off https://cdn.openttd.org
cmd = "wget -r --user-agent=Mozilla --page-requisites --convert-links -e robots=off " + site

print("")
print(cmd)

print("")