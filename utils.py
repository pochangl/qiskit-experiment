import qiskit
from qiskit import Aer


def print_vector(circuit, width):
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
