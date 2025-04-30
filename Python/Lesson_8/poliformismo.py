from persona2 import Persona
from alieno import Alieno

# Creo oggeto p della classe Persona
p: Persona = Persona("Alessio", "Caico", 29)

# visualizzo informzaioni di p
print(p)

# Creo ET oggetto della classe Alieno
ET: Alieno = Alieno("Andromeda")

# visualizzo le informazioni di ET
print(ET)

# p invoca il suo metodo speak
p.speak()

# ET invoca il suo metodo speak
ET.speak()