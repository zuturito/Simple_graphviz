from graphviz import Graph
import sys


def graphic(node_list, tuple_list):
	nodes_to = str(node_list)
	tuple_number = len(tuple_list)
	counter = 0
	print(nodes_to)
	e = Graph('ER', filename='my_file.gv', engine='neato')
	e.attr('node', shape='ellipse')
	for n in node_list:
		e.node(n)
	while counter < tuple_number:
		actual_tuple = tuple(i for i in tuple_list[counter])
		e.edge(str(""+actual_tuple[0]+""),str(""+actual_tuple[1]+""))
		counter+=1
	return e.view()

def func(lst):
    new_lst = []
    for i in lst:
            if type(i) == list or type(i) == tuple: 
                new_lst.extend(func(i))
            else: new_lst.append(i)
    return new_lst
#---------------MAIN----------------------------------------
print("What's your graph? [In format ('x','y'),('y','z')] ")
list_graph = input()
res = list(eval(list_graph))
final_nodes = list(dict.fromkeys(func(res)))
print('Nodes: ' + str(final_nodes))
graphic(final_nodes, res)