#My code
from Graph import Graph
from Huffman import Huffman
from Helper import Helper

#Libs
from collections import defaultdict
import random
import sys
import pprint

def main():
    #filename = sys.argv[1] -> Production
    filename = "graph-text.txt" # -> Dev
    
    g = Helper.readGraph(filename)
    print("The file to be read is {0}".format(filename))
    print("Graph is loaded...")
    k_cores = int(input("Enter the number of cores ")) # The number of cores for each subgraph
    graph_size = len(g) # The number of the Vertices
    
    g1 = Graph(9)
    g1.addEdge(0, 1) 
    g1.addEdge(0, 2) 
    g1.addEdge(1, 2) 
    g1.addEdge(1, 5) 
    g1.addEdge(2, 3) 
    g1.addEdge(2, 4) 
    g1.addEdge(2, 5) 
    g1.addEdge(2, 6) 
    g1.addEdge(3, 4) 
    g1.addEdge(3, 6) 
    g1.addEdge(3, 7) 
    g1.addEdge(4, 6) 
    g1.addEdge(4, 7) 
    g1.addEdge(5, 6) 
    g1.addEdge(5, 8) 
    g1.addEdge(6, 7) 
    g1.addEdge(6, 8) 

    # g2 = Graph(13); 
    # g2.addEdge(0, 1) 
    # g2.addEdge(0, 2) 
    # g2.addEdge(0, 3) 
    # g2.addEdge(1, 4) 
    # g2.addEdge(1, 5) 
    # g2.addEdge(1, 6) 
    # g2.addEdge(2, 7) 
    # g2.addEdge(2, 8) 
    # g2.addEdge(2, 9) 
    # g2.addEdge(3, 10) 
    # g2.addEdge(3, 11) 
    # g2.addEdge(3, 12) 
    # g2.printKCores(k) 
    # for i in range(0, graph_size):
    #     graph.addEdge(i, g[i])

    g1.writeKCores("results.txt", k_cores)

if __name__ == "__main__":
    main()
    