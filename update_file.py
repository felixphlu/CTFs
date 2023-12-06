"""
In this project, assume I am a security analyst for a healthcare company tasked with regularly updating a file that
identifies employees who can access restricted content such as patient records. Employees that can access are restricted
based on their IP address. There is an allow list for IP addresses permitted to view this restricted information.
There is also a remove list that identifies which employees must be removed from this list. I will create an algorithm
using Python to check whether the allow list contains any IP addresses identified in the remove list and then remove
those IP addresses from the file in the allow list.
"""


# First I define the function as update_file which takes two parameters : the file with valid IP addresses
# and the remove_list which is a list of IP addresses to remove that should have no access.
def update_file(import_file, remove_list):
    """Use with statement to close the file after having it read and save it into variable ip_addresses. This opens the
    file from the argument file used in import_file and reads it.
    """
    with open(import_file, "r") as file:
        ip_addresses = file.read()
    # Turn the string file into a list in order to loop through its elements easily with split method.
    ip_addresses = ip_addresses.split()
    for element in ip_addresses:
        # If the IP address fromm the file matches an IP address in the remove_list, then remove it from the list.
        if element in remove_list:
            ip_addresses.remove(element)
    # Turn the list back into a string format in order to write it back into the original file.
    ip_addresses = " ".join(ip_addresses)

    with open(import_file, "w") as file:
        file.write(ip_addresses)

# Calling the function and using a fabricated list of IP addresses to remove.
update_file("allow_list.txt", ["192.168.25.60", "192.168.140.01", "192.168.203.198"])

with open("allow_list.txt", "r") as file:
    text = file.read()

# Check the file of allowed IP addresses
print(text)
"""
The IP addresses used are fabricated for the purpose of this project.
In summary, I created an algorithm that removes IP addresses from a file of approved IP addresses.
The algorithm allowed me to open the file, converting it to a string for reading and then converting it to a list to go
through in order to remove all the IP addresses from the list. I then converted the list back into the string format it
was originally in using .join() method so I could write it over to the file with the revised list of IP addresses.
"""