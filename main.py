import os, shutil, zipfile

if not os.path.isdir("mods"):
    os.mkdir("mods")

def create_gamepath():
    if not os.path.isfile("gamepath.txt"):
        print("No gamepath.txt found. Please enter the path to your game folder:")
        gamepath = input()
        with open("gamepath.txt", "w") as f:
            f.write(gamepath)
            f.close()

# detect if game path is valid
if os.path.isfile("gamepath.txt"):
    with open("gamepath.txt", "r") as f:
        gamepath = f.read()
        if not os.path.isdir(gamepath):
            os.remove("gamepath.txt")
            create_gamepath()
            f.close()
        

print(f"Installed mods: {[i for i in os.listdir('mods')]}")


gamepath = open("gamepath.txt", "r").read()

def install_mod(mod: str):
    # Get mod name
    modname = input("Name of mod: ")
    # Copy game folder to mod folder
    print("Copying game folder...")
    shutil.copytree(gamepath, f"mods/{modname}/")
    print("Copying mod files...")
    with zipfile.ZipFile(mod, "r") as z:
        z.extractall(f"mods/{modname}/")

# Main loop
while True:
    choice = input("Do you want to install a mod? (y/n) ")
    if choice == "y" or choice == "yes":
        mod = input("Enter mod path (zip file): ")
        install_mod(mod)
    elif choice == "n" or choice == "no":
        break