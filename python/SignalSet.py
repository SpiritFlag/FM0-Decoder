class SignalSet:
  def __init__(self):
    self.train = []
    self.validation = []
    self.test = []

  def concatenate(self, src):
    self.train += src.train
    self.validation += src.validation
    self.test += src.test
