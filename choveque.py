import random

class Ambiente():
    def __init__(self):
        self.estado = {'A': random.choice(['cheio', 'vazio']), 'C': random.choice(['cheio','vazio']), 'D': random.choice(['cheio','vazio'])}

    def percepcao(self, agente):
        return (agente.localizacao, self.estado[agente.localizacao])

    def localdefault(self):
        return random.choice(['A', 'C', 'D'])

    def executarAccao(self, accao, agente):
        if accao == 'encher':
            agente.desempenho += 10
            self.estado[agente.localizacao] = "cheio"
            self.moverHorario(agente)
        elif accao == 'mover':
            self.moverHorario(agente)

    def moverHorario(self, agente):
        if agente.localizacao == 'A':
            agente.localizacao = 'C'
        elif agente.localizacao == 'C':
            agente.localizacao = 'D'
        elif agente.localizacao == 'D':
            agente.localizacao = 'A'

class Agente():
    def __init__(self, modelo):
        self.desempenho = 0
        self.modelo = modelo
        self.localizacao = modelo.localdefault()

    def programa(self, percepcao):
        localizacao, estado = percepcao
        if estado == 'vazio':
            return 'encher'
        else:
            return 'mover'

amb = Ambiente()


agente = Agente(amb)

for _ in range(3):
    percep = amb.percepcao(agente)
    print("Percepção :", percep)
    acao = agente.programa(percep)
    amb.executarAccao(acao, agente)
    print("Ação executar:", acao)
    print("Estado atual do ambiente:", amb.estado)
    print("Nova localização :", agente.localizacao)
    print()
