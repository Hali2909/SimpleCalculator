
def calcola(espressione):
    try:
        risultato = eval(espressione)
        return str(risultato)
    except:
        return "errore dell'espressione"
    



