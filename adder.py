import qiskit
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import Aer
from operators import add


def print_result(circuit, width):
    backend = Aer.get_backend('statevector_simulator')
    result = qiskit.execute(circuit, backend=backend).result()
    print(circuit)
    vector = result.get_statevector()
    for index, value in enumerate(vector):
        if value:
            result = list('0' * width)
            data = '{0:b}'.format(index)
            data = list(data)
            data.reverse()

            for pos, char in enumerate(data):
                result[pos] = char
            result.reverse()
            print(''.join(result), value)


q = qiskit.QuantumRegister(4)
a, b, s, c = q

circuit = qiskit.QuantumCircuit(q)
circuit.h([a, b])
add(circuit, a, b, s, c)

print_result(circuit, width=4)
