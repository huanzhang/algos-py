class DiGraph:
    """
    Class for directed graphs.
    """
    def __init__(self):
        self.node = {} # dictionary for node attributes
        self.adj = {}  # empty adjacency dict

    def __iter__(self):
        """
        Iterate over the nodes. Use the expression 'for n in G'.
        """
        return iter(self.node)

    def __contains__(self,n):
        """
        Return True if n is a node, False otherwise. Use the expression
        'n in G'.
        """
        try:
            return n in self.node
        except TypeError:
            return False

    def __getitem__(self, n):
        """
        Return a dict of neighbors of node n.  Use the expression 'G[n]'.
        """
        return self.adj[n]

    def add_node(self, n, attr_dict=None, **attr):
        """
        Add a single node n and update node attributes.
        """
        # set up attribute dict
        if attr_dict is None:
            attr_dict=attr
        else:
            try:
                attr_dict.update(attr)
            except AttributeError:
                raise Exception(\
                    "The attr_dict argument must be a dictionary.")
        if n not in self.adj:
            self.adj[n] = {}
            self.node[n] = attr_dict
        else:
            self.node[n].update(attr_dict)

    def add_edge(self, u, v):
        """
        Add an edge between u and v.
        """
        # add nodes
        if u not in self.adj:
            self.adj[u]={}
            self.node[u] = {}
        if v not in self.adj:
            self.adj[v]={}
            self.node[v] = {}
        # add the edge
        datadict=self.adj[u].get(v,{})
        self.adj[u][v]=datadict

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
