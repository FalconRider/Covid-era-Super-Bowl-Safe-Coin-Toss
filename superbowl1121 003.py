# Copyright 2019 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# FOR AMUSEMENT ONLY - based on antenna model

#Covid Superbowl Test

# SuperBowl is coming in this ers of COVID Pandemic.
# There is a new culture of HANDS FREE   and VIRTUAL everything
# So here is a COIN TOSS with the  True Randomness of QUANTUM.

# Call it and hit the Green Arrow.
# Repeat a few times and see if it is random.
print("The coin is tossed and  it's   . . .")


# Import networkx for graph tools
import networkx as nx

# Import dwave_networkx for d-wave graph tools/functions
import dwave_networkx as dnx

# Import matplotlib.pyplot to draw graphs on screen
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
print("  ")
print ("gonna be  . . ")
print(" ")
# Set the solver we're going to use
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

sampler = EmbeddingComposite(DWaveSampler())

# Create empty graph
G = nx.Graph()

# Add edges to graph - this also adds the nodes
G.add_edges_from([(3, 4),(1,2)])

# Find the maximum independent set, S
S = dnx.maximum_independent_set(G, sampler=sampler, num_reads=10)

# Print the solution for the user
#print('Maximum independent set size found is', len(S))
#print(S)
zz =S[0]
#print (zz, "testing")


if zz ==1:
    print("HEADS")
if zz  == 2:
    print("TAILS")  


print("  ")

# Visualize the results
#k = G.subgraph(S)
#notS = list(set(G.nodes()) - set(S))
#othersubgraph = G.subgraph(notS)
#pos = nx.spring_layout(G)
#plt.figure()

# Save original problem graph
#original_name = "antenna_plot_original.png"
#nx.draw_networkx(G, pos=pos, with_labels=True)
#plt.savefig(original_name, bbox_inches='tight')

# Save solution graph
# Note: red nodes are in the set, blue nodes are not
#solution_name = "antenna_plot_solution.png"
#nx.draw_networkx(k, pos=pos, with_labels=True, node_color='r', font_color='k')
#nx.draw_networkx(othersubgraph, pos=pos, with_labels=True, node_color='b', font_color='w')
#plt.savefig(solution_name, bbox_inches='tight')

#print("Your plots are saved to {} and {}".format(original_name, solution_name))
