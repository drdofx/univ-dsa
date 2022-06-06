from anytree import Node, RenderTree
from anytree.exporter import DotExporter

A = Node("A")
B = Node("B", parent=A)
C = Node("C", parent=A)
D = Node("D", parent=A)

E = Node("E", parent=B)
F = Node("F", parent=B)
G = Node("G", parent=B)
H = Node("H", parent=C)
I = Node("I", parent=C)
J = Node("J", parent=D)
K = Node("K", parent=D)
L = Node("L", parent=D)
M = Node("M", parent=D)

N = Node("N", parent=E)
O = Node("O", parent=E)
P = Node("P", parent=L)
Q = Node("Q", parent=L)

DotExporter(A).to_picture("tree.png")