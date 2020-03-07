import numpy
import matplotlib.pylab as plt
from operator import itemgetter


# ColLegManager function inputs are:
#       >>> colours   <dict> - dict connecting molecule types (eg. Chla --> Chla1, Chla2, ...)
#                              with color maps of user's choice
#       >>> legend    <list> - list of molecules names as they are present in density matrix (in correct order)
#       >>> N         <int>  - dimension of density matrix (usually one element longer than legend length
#
# ColLegManager unction returns list of:
#  [0]  >>> order     <list> - list of indexes of molecules names in 'legend' (input) in alphabetical order
#  [1]  >>> paintings <list> - list of RGBA vectors for each molecule name, order of values corresponds to the legend

def ColLegManager(colours=None, legend=None, N=None):
    # If no dict of colours_map or legend has been entered
    if not colours:
        colours = None
    if not legend:
        legend = None

    # Constructing list of indexes for alphabetically ordered molecule names in 'legend'
    if legend != None:
        index_list = list(range(0, N - 1))
        merged_list = []
        ## Creating 2D list of ['position index','molecule name']
        for entry in index_list:
            merged_list.append([index_list[entry], legend[entry]])
        print("Merged_list:        ", merged_list)
        ordered = sorted(merged_list, key=itemgetter(1))
        ## List of position indexes according to alphabetical order
        order = []
        for index in index_list:
            order.append(ordered[index][0])
        print("Order_of_mol_names: ", order)

    cols = []
    if colours != None:
        # Sorting molecules by colours:
        for mol in legend:
            for key in list(colours.keys()):
                if mol.find(colours[key]) != -1:
                    cols.append(key)

        print("Input_legend:       ", legend)
        print("Matched_col_maps:   ", cols)

        # Creating list of different colour shades from selected colour map for each molecule:
        paintings = [0] * len(cols)
        for col in list(colours.keys()):
            numocc = cols.count(col)
            gradient = numpy.linspace(0.2, 1, 2 * numocc + 1)
            i = 0
            for n in range(0, numocc):
                i = cols.index(col, i)
                paintings[i] = plt.get_cmap(col)(1 - gradient[n])
                i = i + 1
    return [order, paintings]
