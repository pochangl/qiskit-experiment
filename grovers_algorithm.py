import qiskit
from qiskit import QuantumRegister, QuantumCircuit
from operators import add
from utils import print_vector


def oracle(circuit, data, fx):
    circuit.barrier()
    circuit.x(data[0])

    # circuit.cx(data[:2], fx)
    circuit.ccx(data[0], data[1], fx)

    circuit.x(data[0])


def diffusion(circuit, data):
    circuit.barrier()
    circuit.h(data)
    circuit.x(data)

    circuit.cz(data[0], data[1])

    circuit.x(data)
    circuit.h(data)


q = qiskit.QuantumRegister(3)
data, fx = q[:2], q[2]

circuit = qiskit.QuantumCircuit(q)

circuit.x(fx)
circuit.h(q)

oracle(circuit, data, fx)
diffusion(circuit, data)

print_vector(circuit, width=3)
