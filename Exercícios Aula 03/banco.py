class Banco:
  def __init__(self, nome, telefone, renda, genero):
    self._nome = nome
    self._telefone = telefone
    self._renda = renda
    self._genero = genero
  
  @property
  def nome(self):
    return self._nome

  @property
  def telefone(self):
    return self._telefone

  @property
  def renda(self):
    return self._renda

  @nome.setter
  def nome(self, nome):
    self._nome = nome

  @telefone.setter
  def telefone(self, telefone):
    self._telefone = telefone
  
  @renda.setter
  def renda(self, renda):
    self._renda = renda

# A classe Conta é derivada da classe Banco
# Relação: Conta é uma conta do Banco

class Conta(Banco):
  def __init__(self, nome, telefone, renda, genero):
    super().__init__(nome, telefone, renda, genero)
    self.__saldo = 0

    if self._genero.lower() == 'feminino': self.__cheque_especial = self._renda
    if self._genero.lower() == 'masculino': self.__cheque_especial = 0

  @property
  def genero(self):
    return self._genero

  @property
  def saldo(self):
    return self.__saldo
  
  @property
  def cheque_especial(self):
    return self.__cheque_especial

  @saldo.setter
  def saldo(self, valor):
    self.__saldo = valor

  def saque(self, valor):
    if self._genero.lower() == 'masculino':
      if valor <= self.__saldo:
        self.__saldo -= valor
      else:
        ValueError(f'O valor {valor} solicitado para saque é superior ao saldo atual do cliente.')
    
    if self._genero.lower() == 'feminino':
      if valor <= self.__saldo:
        self.__saldo -= valor
      elif valor >= self.__saldo and (valor <= self.__saldo + self.__cheque_especial if self.__saldo >= 0 else valor <= self.__cheque_especial):
        self.__cheque_especial -= (valor - self.__saldo if self.__saldo >= 0 else valor)
        self.__saldo -= valor
      else:
        ValueError(f'O valor {valor} solicitado para saque é superior ao saldo atual + cheque especial da cliente.')

  def deposito(self, valor):
    if self.__saldo >= 0:
      self.__saldo += valor
    else:
      self.__saldo += valor
      if self._genero.lower() == 'feminino':
        if self.__cheque_especial + valor >= self._renda: self.__cheque_especial = self._renda
        else: self.__cheque_especial += valor
  
  def __str__(self) -> str:
    return f'Conta Banco Delas:\nNome: {self._nome}\nGênero: {self._genero.title()}\nTelefone: {self._telefone}\nRenda: {self._renda}\nSaldo: {self.__saldo}\nCheque Especial: {self.__cheque_especial}\n'

# Testando

cliente1 = Conta('Marayah', '(85) 99999-9999', 1200, 'feminino')
print(cliente1)

cliente1.saque(50)
print(cliente1)
cliente1.deposito(10)
print(cliente1)
cliente1.deposito(50)
print(cliente1)

cliente2 = Conta('Thiago', '(85) 99999-9999', 800, 'masculino')
print(cliente2)

cliente2.saque(50)
print(cliente2)
cliente2.deposito(50)
print(cliente2)
cliente2.saque(40)
print(cliente2)