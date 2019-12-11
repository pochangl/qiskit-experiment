import qiskit
from qiskit import QuantumRegister, QuantumCircuit
from operators import add
from utils import print_vector


q = qiskit.QuantumRegister(4)
a, b, s, c = q

circuit = qiskit.QuantumCircuit(q)
circuit.h([a, b])
add(circuit, a, b, s, c)

print_vector(circuit, width=4)
