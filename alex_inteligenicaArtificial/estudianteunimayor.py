from logic import *

# Definir los símbolos lógicos
lluvia = Symbol("lluvia")
BBC = Symbol("BBC")
unimayor = Symbol("unimayor")

# Base de conocimiento (KB) que refleja las condiciones de la diapositiva 359
# 1. Si no llueve, entonces BBC emite su señal
# 2. BBC o unimayor deben ocurrir
# 3. No pueden ocurrir ambas, BBC y unimayor
# 4. Unimayor ocurre
knowledge = And(
    Implication(Not(lluvia), BBC),
    Or(BBC, unimayor),
    Not(And(BBC, unimayor)),
    unimayor
)

# Verificar si la proposición 'lluvia' es verdadera en la base de conocimiento
print(model_check(knowledge, lluvia))