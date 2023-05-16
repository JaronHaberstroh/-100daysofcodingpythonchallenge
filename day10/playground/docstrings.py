# Create function
# Create docstring by inserting text with tripple quotes """docstring"""
def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "No valid inputs"
    name = f_name.title() + " "
    name += l_name.title()
    return name

