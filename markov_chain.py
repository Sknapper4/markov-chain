import random


# Map list is here to make creating the graph easier
map_list = {
    'a': ['b', 'd'],
    'b': ['a', 'c', 'e'],
    'c': ['b', 'f'],
    'd': ['a', 'e'],
    'e': ['b', 'd', 'f', 'g'],
    'f': ['c', 'e', 'h'],
    'g': ['e', 'h'],
    'h': ['f', 'g']
}


# This matrix represents the move choice probability of the bug
# that is crawling the graph
th = 1 / 3
M = [
    [0, .5, 0, .5, 0, 0, 0, 0],
    [th, 0, th, 0, th, 0, 0, 0],
    [0, .5, 0, 0, 0, .5, 0, 0],
    [.5, 0, 0, 0, .5, 0, 0, 0],
    [0, .25, 0, .25, 0, .25, .25, 0],
    [0, 0, th, 0, th, 0, 0, th],
    [0, 0, 0, 0, .5, 0, 0, .5],
    [0, 0, 0, 0, 0, .5, .5, 0]
]

# This value represents how many different vertices we want our bug to visit each time we crawl the graph
nodes_to_visit = 10000

# random.seed ensure we get consistent results when running the program
random.seed(97)


# The Node class makes creating and crawling the graph easier
class Node:

    def __init__(self, value):
        self.value = value
        self.connected_nodes = []


# The Graph class lets us order and group our logic
class Graph:

    def __init__(self):
        self.nodes = {}
        self.vector = []

    def __str__(self):
        """
            The 'to string' function lets us print out our graph
            in a pretty way
        :return: Our string
        """
        string = ''
        for k, v in graph.nodes.items():  # this prints the number of times each node was visited
            string += k.value + ' - ' + str(v) + '\n'
        return string

    def traverse_graph_with_markov_chain(self):
        """
            We 'crawl' the graph and add one to each vertex(node) we visit.
            This gives us the total number of times we visited each vertex.
            That value is stored in the node class
        """
        new_node = next(iter(self.nodes))           # sets the first node as the starting vertex
        for x in range(nodes_to_visit):             # we want to visit this many nodes
            # we select a new node value to visit from the list of connected nodes
            new_node_value = random.choice(new_node.connected_nodes)
            for node in self.nodes:                 # we find the selected node in the list of nodes
                if node.value == new_node_value:    # if that node is the node we are looking for
                    new_node = node                 # set the new node as that node and start over
                    break
            self.nodes[new_node] += 1               # add 1 to the number of times that node has been visited

    def avg_out_visits(self):
        """
            Here we divide each value by the number of total vertices(nodes)
                we visited, giving us the probability of each vertex being visited.
        """
        for k, v in self.nodes.items():
            self.nodes[k] = v / nodes_to_visit

    def define_graph(self):
        """
            This function creates the graph using the map_list we defined at the top of
                the file. We create a node, define which other nodes that node is connected to, and
                then initialize the amount of times that node has been visited to one.
        """
        for k, v in map_list.items():       # iterate through items in the map
            temp_node = Node(value=k)       # create a new node based on the value in the map
            temp_node.connected_nodes = v   # define what other nodes we are connected too
            self.nodes[temp_node] = 0       # set the initial value of times we visited the vertex to 0

    def get_avg_visits(self, num_iters=100):
        """
            This function traverses the graph num_iters times and averages out those visits to give us
                our probability. We then assign that value to each node and create our eigenvector.
        :param num_iters: The number of times we want to traverse our graph
        """
        for x in range(num_iters):
            self.traverse_graph_with_markov_chain()
        self.avg_out_visits()
        for k, v in self.nodes.items():
            self.nodes[k] = round(v / num_iters, ndigits=2)
            self.vector.append(round(v / num_iters, ndigits=2))

    def check_vector(self):
        """
            This function checks if the vector that we created is an eigenvector of the
                matrix representation of the graph.
        :return: True if the vectors are equal, False otherwise
        """
        new_vector = []
        for x in range(len(M)):
            temp_val = 0
            for i, val in enumerate(self.vector):
                temp_val += val * M[i][x]
            new_vector.append(round(temp_val, ndigits=2))
        return new_vector == self.vector


if __name__ == '__main__':
    """
        This is called when we call the file from our terminal. We create the graph,
            define the nodes on the graph, average everything out, print the graph and vector, 
            and finally we check if the vector is correct.
    """
    graph = Graph()
    graph.define_graph()
    graph.get_avg_visits()
    print(graph)
    is_eigenvector = graph.check_vector()
    if is_eigenvector:
        print(f'The vector - {graph.vector}, \nis an Eigenvector of our matrix.')
    else:
        print(f'The vector - {graph.vector}, \nis not an Eigenvector of our matrix for Eigenvalue 1.')
