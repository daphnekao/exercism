import re

class Node:
    #num_variation = 0
    def __init__(self, properties=[], children=[]):
        self.properties = properties
        self.children = children

    def __repr__(self):
        description = """
        Node with the following properties and children:
        Properties: {}
        Children: {}
        """.format(self.properties, self.children)
        return description

    def next(self, variation=1):
        if len(self.children) == 0:
            return None
        else:
            return self.children[variation - 1]


def shave_string(input_string):
    """Shaves off the opening "(;"
    """
    return input_string[2:]

def extract_properties_string(shaved_string):
    # The properties are everything after the initial "(;"" and before either ";" or "(;"
    if "(;" in shaved_string:
        end_of_properties_list = shaved_string.find("(;")
    else:
        end_of_properties_list = shaved_string.find(";")
    properties_string = shaved_string[:end_of_properties_list]
    return properties_string

def parse_properties(properties_string):
    """
    FF[4]C[root]SZ[19] --> [ { "FF": ["4"] }, { "C": ["root"] }, { "SZ": ["19"] } ]
    AB[aa][ab][ba] --> [ { "AB": [aa, ab, ba] } ]
    """
    # Will need to use regular expressions here.
    pass

def parse(input_string):
substring = shave_string(input_string)
properties_string = extract_propert_string(substring)
properties = parse_properties(properties_string)


"""
TO-DO:
- Write a function for extracting the list of children from the string.
- After converting the properties and children into lists of dictionaries,
instantiate a Node with those properties.
- Make sure the code works on empty trees.
- Fill out unit tests.
"""





