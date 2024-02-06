# Use a file to parse and remove blacklisted IP addresses
# Brandon Dawson
# 11/06/2023

# Define a function to update a file which takes two parameters
def update_file(import_file, remove_list):
    #Open the initial contents of the file
    with open(import_file, "r") as file:
        # Create a new variable and read the contents to store data
        ip_addresses = file.read()
        
    # Parse through the data and convert to a list separating using the split method and whitespace
    ip_addresses = ip_addresses.split()
    
    # Create a loop to iterate through the remove list and remove specified contents from IP addresses
    for element in remove_list:
        if element in ip_addresses:
            ip_addresses.remove(element)
            
    # Convert the list back into a string so it can be written to a new file
    ip_addresses = "\n".join(ip_addresses)
    
    # Rewrite the contents of the original file
    with open(import_file, "w") as file:
        file.write(ip_addresses)
           