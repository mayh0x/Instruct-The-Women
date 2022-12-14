class Carro:
  def __init__(self, placa):
    self.placa = placa
    self._estacionado = False
  
  @property
  def estacionado(self):
    return self._estacionado

  @estacionado.setter
  def estacionado(self, valor):
    self._estacionado = valor

  def estacionar(self):
    if self._estacionado == True: return
    self._estacionado = True
  
  def sair_da_vaga(self):
    if self._estacionado == False: return
    self._estacionado = False

class Moto:
  def __init__(self, placa):
    self.placa = placa
    self._estacionado = False
  
  @property
  def estacionado(self):
    return self._estacionado

  @estacionado.setter
  def estacionado(self, valor):
    self._estacionado = valor

  def estacionar(self):
    if self._estacionado == True: return
    self._estacionado = True
  
  def sair_da_vaga(self):
    if self._estacionado == False: return
    self._estacionado = False

class Vaga:
  def __init__(self, id, tipo):
    self.id = id
    self.tipo = tipo
    self._livre = True
    self.placa = "0000"
  
  @property
  def livre(self):
    return self._livre

  @livre.setter
  def livre(self, valor):
    self._livre = valor

  def ocupar(self, veiculo):
    if self._livre == False: return
    self._livre = False
    self.placa = veiculo.placa
  
  def desocupar(self):
    if self._livre == True: return
    self._livre = True
    self.placa = "0000"

class Estacionamento:
  def __init__(self):
    self.vagas_de_carro = 25
    self.vagas_de_moto = 25
    self.carro_para_vaga = 0
    self.moto_para_vaga = 0
    self.total_vagas_livres_carro = 25
    self.total_vagas_livres_moto = 25

  def estacionar_carro(self, carro, vaga):
    if carro.estacionado == True: return
    if self.total_vagas_livres_carro > 0:
      carro.estacionar()
      vaga.ocupar(carro)
      self.total_vagas_livres_carro -= 1
    else: self.carro_para_vaga += 1

  def estacionar_moto(self, moto, vaga):
    if moto.estacionado == True: return
    if self.total_vagas_livres_moto > 0:
      moto.estacionar()
      vaga.ocupar(moto)
      self.total_vagas_livres_moto -= 1
    else: self.moto_para_vaga += 1

  def remover_carro(self, carro, vaga):
    if carro.estacionado == False: return
    carro.sair_da_vaga()
    vaga.desocupar()
    self.total_vagas_livres_carro += 1

  def remover_moto(self, moto, vaga):
    if moto.estacionado == False: return
    moto.sair_da_vaga()
    vaga.desocupar()
    self.total_vagas_livres_moto += 1
  
  def __str__(self) -> str:
    return f'Total de vagas: 50\nVagas de Carro: {self.vagas_de_carro}\nVagas de Moto: {self.vagas_de_moto}\nVagas livres de carro: {self.total_vagas_livres_carro}\nVagas livres de moto: {self.total_vagas_livres_moto}\nCarros aguardando vaga: {self.carro_para_vaga}\nMotos aguardando vaga: {self.moto_para_vaga}\n'

# Testando

estacionamento = Estacionamento()
print(estacionamento)

carro = Carro('123456')
moto = Moto('123456')
vaga_carro = Vaga(1, 'Carro')
vaga_moto = Vaga(2, 'Moto')

estacionamento.estacionar_carro(carro, vaga_carro)
estacionamento.estacionar_moto(moto, vaga_moto)
print(estacionamento)

estacionamento.remover_carro(carro, vaga_carro)
estacionamento.remover_moto(moto, vaga_moto)
print(estacionamento)