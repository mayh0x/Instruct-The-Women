# Definicao da classe

class Carro:
  def __init__(self, cor, modelo):
    self.ligado = False
    self.cor = cor
    self.modelo = modelo
    self.velocidade = 0
    self.velocidade_min = 0
    self.velocidade_max = 200
  
  def ligar(self):
    self.ligado = True

  def desligar(self):
    self.ligado = False
    self.velocidade = 0

  def acelerar(self):
    if self.ligado == False: return
    if self.velocidade < self.velocidade_max:
      self.velocidade += 1

  def desacelerar(self):
    if self.ligado == False: return
    if self.velocidade > self.velocidade_min:
      self.velocidade -= 1

  def __str__(self) -> str:
    return f'Carro ligado? {self.ligado}\nModelo: {self.modelo}\nCor: {self.cor}\nVelocidade: {self.velocidade}\n'

# Criando instancias da class Carro

carro1 = Carro('Branco', 'Fusca')
carro2 = Carro('Prata', 'Corolla')

# Criando funções baseadas nos métodos das classes

def andar(carro, quantidade):
  if carro.ligado == False: return 'Carro desligado, nao eh possivel andar'
  carro.ligar()
  for _ in range(quantidade):
    if carro.velocidade + quantidade > carro.velocidade_max: 
      carro.velocidade = carro.velocidade_max
      break
    else: carro.acelerar()

def parar(carro, quantidade):
  if carro.ligado == False: return 'Carro desligado, nao eh preciso parar'
  for _ in range(quantidade):
    if carro.velocidade - quantidade < carro.velocidade_min: 
      carro.velocidade = carro.velocidade_min 
      break
    else: carro.desacelerar()

# Testando

carro1.ligar()

andar(carro1, 60)
andar(carro1, 40)
andar(carro2, 30)

print('Velocidades após andar:', carro1.velocidade, carro2.velocidade)

print('Carro 1:', carro1)
print('Carro 2:', carro2)