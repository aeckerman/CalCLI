import os

print ("Setup initiated!")
version = input("What is your Python version (example: 2, 3): ")
print ("")

os.system("pip"+str(version)+" install Click")
os.system("echo 'alias calc=\"python"+str(version)+" ~/CalCLI/src/main.py\"' >> .bash_profile")

print( "")
print ("Setup complete!")
