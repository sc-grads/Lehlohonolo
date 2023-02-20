#########################
# Importing Python Modules
#########################

# Importing a module
# Importing two or more modules
# Importing a module as an alias
# Importing just the Response class from requests module from requests
# Importing a class from a module as an alias from requests import Response as res
# Import everything directly from shutil module into the global namespace
# TO BE AVOIDED!

# The block of code below if will be executed only when the script is run directly (not imported in another script)
if __name__ == '__main__':
    print('Running the script directly. Not importing it as a module.')
