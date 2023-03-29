import random
import time

class TrisRoom:
  #Campi
  codiceStanza
  timestamp
  giocatori=[] 
  spettatori=[] 
  
  #Metodi
  def __init__(self, host):
    self.giocatori.push(host)
    self.timestamp=time.timestamp()
    self.codiceStanza=self.createCode()
    
  static self createCode():
    #idea:generare un codice tramite conversione in alfanumerico di un numero random/ o del timestamp 
    flag=true #true fin quando il codice non è valido 
    rnd=time.timestamp()
    while(flag):
      
      code=convertB16(rnd) 
     #check sui dati in tabella activeRoom 
      flag=activeRoom.checkCode()
      
      
      
class ActiveRoom:
  active=[] #array di oggetti TrisRoom 
      
  def checkCode():
  #restituisce true se il codice è presente un tavella
  #false altrimenti
  
