from Graph import Graph

class Helper:
    
    @staticmethod
    def readGraph(inputFile):
        g = {}
        with open(inputFile) as graph_input:
            for line in graph_input:
                # Split line and convert line parts to integers.
                nodes = [int(x) for x in line.split()]
                if len(nodes) != 2:
                    continue
                # If a node is not already in the graph
                # we must create a new empty list.
                if nodes[0] not in g:
                    g[nodes[0]] = []
                if nodes[1] not in g:
                    g[nodes[1]] = []
                # We need to append the "to" node
                # to the existing list for the "from" node.
                g[nodes[0]].append(nodes[1])
                # And also the other way round.
                g[nodes[1]].append(nodes[0])
        return g

    @staticmethod
    def writeToFile(g,cores, outputfile):
        graph = Graph(len(g))
        graph.writeKCores(outputfile, cores)
