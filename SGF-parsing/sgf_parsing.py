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


class SGFParser:
    def __init__(self, input_string):
        self.input_string = input_string

    def convert_properties_string_to_list(properties_string)
        # FF[4]C[root]SZ[19] --> [ { "FF": ["4"] }, { "C": ["root"] }, { "SZ": ["19"] } ]
        # AB[aa][ab][ba] --> [ { "AB": [aa, ab, ba] } ]
        properties_as_text = re.finditer("(\w+\[\w+\])", properties_string)
        raw_properties = []
        for prop in properties_as_text:
            raw_properties.append(prop.group(0))
        pattern = re.compile("\[\w+\]")

        parsed_properties = []
        for raw_prop in raw_properties:
            opening_bracket_location = raw_prop.find("[")
            key = raw_prop[:opening_bracket_location]
            value = pattern.search(raw_prop).group(0).strip("[").strip("]")
            parsed_properties.append({ key: value })
        return parsed_properties

    def parse(self):
        # Shave off the opening "(;"
        self.shaved_string = self.input_string[2:]

        # Boolean stating whether the string indicates variant children or not.
        self.variations_exist = False
        if "(;" in self.shaved_string:
            self.variations_exist = True

        # Find the delimiter between the properties list and the children.
        if self.variations_exist:
            self.delimiter_location = self.shaved_string.find("(;")
        else:
            self.delimiter_location = self.shaved_string.find(";")

        # Extract the properties string -- everything before either ";" or "(;"
        self.node_properties_string = self.shaved_string[:self.delimiter_location]

        self.properties = self.convert_properties_string_to_list(self.node_properties_string)

        # Extract the children string.
        if self.variations_exist:
            self.children_string = self.shaved_string[self.delimiter_location:]
        else:
            self.children_string = self.shaved_string[self.delimiter_location + 1:]

        # Convert this string into a list of list of properties.
        children_list = []
        if self.variations_exist:
            raw_children_string = self.children_string[2:].strip("(").strip(")")
        else:
            raw_children_list = raw_children_string.split(";")
            for string in raw_children_list:
                children_list.append(self.convert_properties_string_to_list(string))


        # In the list

example_string = "(;FF[4]C[root]SZ[19];B[aa];W[ab](;B[ae]C[black to play and live])(;B[ag]C[only one eye this way]))"
two_variations_string = "(;A[B](;B[bg])(;B[dh]C[Oops! You can't take this stone.]))"

"""
TO-DO:
- After converting the properties and children into lists of dictionaries,
instantiate a Node with those properties.
- Make sure the code works on empty trees.
- Fill out unit tests.
"""





