#!/usr/bin/env python2.7

import re
import sys


class DiGraph:
    """
    Class for directed graphs.
    """
    def __init__(self):
        self.node = {}  # dictionary for node attributes
        self.adj = {}   # empty adjacency dict

    def __iter__(self):
        """
        Iterate over the nodes. Use the expression 'for n in G'.
        """
        return iter(self.node)

    def __contains__(self, n):
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

    def __str__(self):
        return self.adj.__str__()

    def add_node(self, n, attr_dict=None, **attr):
        """
        Add a single node n and update node attributes.
        """
        # set up attribute dict
        if attr_dict is None:
            attr_dict = attr
        else:
            try:
                attr_dict.update(attr)
            except AttributeError:
                raise Exception(
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
        # add the edge
        self.adj[u][v] = self.adj[u].get(v, {})


#######################################################
#################### Main #############################
#######################################################

def decipher(word_set, text):
    """
    decipher(word_dict, text) --> deciphered text

    return the deciphered text of encrypted text
    """
    word_dict = {}
    for x in word_set:
        if len(x) in word_dict:
            word_dict.get(len(x)).append(x)
        else:
            word_dict[len(x)] = [x]

    # start to build the graph
    text_words = text.split()
    G = DiGraph()
    start_nodes = []
    end_nodes = []
    i = 0
    for x in map(len, text_words):
        if x not in word_dict:
            raise Exception('Not validated cryptograph')
        curr_nodes = []
        for w in word_dict[x]:
            i += 1
            G.add_node(i, word=w)
            curr_nodes.append(i)
            for j in end_nodes:
                G.add_edge(j, i)
        if not end_nodes:
            start_nodes = curr_nodes
        end_nodes = curr_nodes

    deciphered_text = []
    # find paths
    for x, y in [(x, y) for x in start_nodes for y in end_nodes]:
        p = find_paths(G, x, y, text)
        if p:
            for x in p:
                t = []
                for y in x:
                    t.append(G.node[y].get("word"))
                if t:
                    deciphered_text.append(" ".join(t))
    if deciphered_text:
        return deciphered_text[0]
    else:
        return re.sub(r'\S', '*', text)


def find_paths(graph, start, end, text, path=[]):
    """ Find paths from start to end"""
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    if is_conflicted(graph, path, text):
        return []
    for node in graph[start]:
        if node not in path:
            newpaths = find_paths(graph, node, end, text, path)
            for newpath in newpaths:
                if not is_conflicted(graph, newpath, text):
                    paths.append(newpath)
    return paths


def is_conflicted(graph, path, text):
    test_str = []
    for i in path:
        test_str.append(graph.node[i].get("word"))
    if test_str and _is_conflicted(text.replace(" ", ""), "".join(test_str)):
        return True


def _is_conflicted(str1, str2):
    m = {}
    for x, y in zip(str1, str2):
        if x in m:
            if m[x] != y:
                return True
        else:
            m[x] = y
    return False

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip().replace('\n', '').replace('\r', '')
    n = int(lines[0])
    word_set = set([])
    for x in range(1, n+1):
        word_set.add(lines[x])
    for y in range(n+1, len(lines)):
        print decipher(word_set, lines[y])
