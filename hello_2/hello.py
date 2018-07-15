import sys

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = input("Bonvolu diru min vian nomo")
    if name == '': name = 'Gogeta tiam'

print("Saluton", name)
