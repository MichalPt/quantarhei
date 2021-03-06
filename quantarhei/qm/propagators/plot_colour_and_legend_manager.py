import numpy as np
from collections import Counter
import matplotlib.pylab as plt

'''
ColLegManager function inputs are:
      >>> colours   <dict> - dict connecting molecule types (e.g. Chla --> Chla1, Chla2, ...)
                             with color maps of user's choice (e.g. 'Reds', 'Blues', ...)
      >>> legend    <list> - list of molecules names as they are present in density matrix (in correct order)
      >>> N         <int>  - dimension of density matrix (usually one element longer than legend length

ColLegManager unction returns list of:
 [0]  >>> order     <list> - list of molecule names' indexes in 'legend' (input) in alphabetical order
 [1]  >>> paintings <list> - list of RGBA vectors for each molecule name, order of values corresponds to the legend
'''


def ColLegManager(colours=None, legend=None, N=None):
    # If no dict of colours_map or legend or N has been entered
    if not colours:
        colours = None
    if not legend:
        legend = None
    if not N:
        N = len(legend) + 1

    # Constructing list of indexes for alphabetically ordered molecule names in 'legend'
    if legend is not None:
        order = np.argsort(legend)
        print("Order_of_mol_names: ", list(order))

    def ColMatcher(*names):
        for name in names:
            if mol.find(name) != -1:
                cols.append(key)
        return cols

    cols = []
    if colours is not None:
        # Sorting molecules by colours:
        for mol in legend:
            for key in list(colours.keys()):
                cmap = colours[key]
                if isinstance(cmap, (list, tuple)):
                    ColMatcher(*cmap)
                else:
                    ColMatcher(cmap)

        print("Input_legend:       ", legend)
        print("Matched_col_maps:   ", cols)

        # Creating list of different colour shades from selected colour map for each molecule:
        paintings = [0] * len(cols)

        # Matching different shades from selected colour map for each molecule, the gradient respects the alphabetical
        # order of the molecules' names (first molecule is always the darkest, the shade gets lighter with each next)
        q = 0
        num_of_col = len(Counter(cols).keys())
        for num in range(0, num_of_col):
            clr = cols[order[q]]
            numocc = cols.count(clr)
            gradient = np.linspace(0.2, 1, 2 * numocc + 1)
            for i in range(0, numocc):
                loc = order[i + q]
                paintings[loc] = plt.get_cmap(clr)(1 - gradient[i])
            q = q + numocc

    # Default setting - gradient of colours of preset colour map
    if colours is None:
        paintings = [0] * N
        gradient = np.linspace(0.2, 1, N)
        j = 0
        for o in order:
            paintings[o] = plt.get_cmap('inferno_r')(1 - gradient[j])
            j = j + 1

    return [order, paintings]
