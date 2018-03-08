import string
import analisi_testo_mod4_tupple as gramm
#############################################costanti
tup_articoli=gramm.tup_articoli
tup_pronomi=gramm.tup_pronomi
tup_congiunzioni=gramm.tup_congiunzioni
tup_dim=gramm.tup_dim
tup_preposizioni=gramm.tup_preposizioni
tup_ausiliari=gramm.tup_ausiliari
tup_avverbi=gramm.tup_avverbi
tup_dialoghi=gramm.tup_dialoghi
tup=gramm.tup
############################################# VARIABILI -
seq_reale=list() # sequenza reale del libro
seq_parola=list()# sequenza solo delle parole
seq_histogram=dict() # dizionario frequenza:[parole,..] nel testo
array_freq=[]# chiavi per frequenza decrescente
d = dict()# dizionario chiave "parola": n freq presente nel testo
seq_parola_apostrofi=list()
seq_righe=[]#restituisce una lista di indici riferiti all ultimo elemento della linea
numero_linea=0

def inizializza_le_sequenze(fl_source): 
    fl=open(fl_source)
    crea_liste(fl)
    fl.close()


def crea_liste(fl):
    global numero_linea 
    numero_linea=1
    for line in fl:
        crea_reale(line)
        crea_parola(line)
        numero_linea+=1
    crea_histogramma(seq_parola)

 
def crea_reale(line):        
    global seq_reale
    global seq_righe
    line=elabora_linea_apostrofi(line)         
    seq_reale.extend(line.split())
    seq_righe.append(len(seq_reale)-1)
    
def crea_parola(linea):
    punct=string.punctuation+"“”“"
    
    for i in linea[:-4] :
        #linea=linea
        linea=elabora_linea_apostrofi(linea)
        #
        if i in punct:  
            linea=linea.replace(i,"")
    linea.lower()
    global seq_parola  
    seq_parola.extend(linea.split() )

def elabora_linea_apostrofi(linea):
    tupp=gramm.tup_articoli+gramm.tup_preposizioni
    if "'" in linea or "’" in linea:
                  
        linea=linea.replace("’","’ ")
        linea=linea.replace("'","’ ")
        #print (linea)  
        return linea            
    return linea  
                                                                  

def crea_histogramma(array):
    global d        

    for c in array:
        d[c.lower()]=d.get(c.lower(),0)+1
    invert_dictionary_crowcut(d)


def invert_dictionary_crowcut(d):
    global seq_histogram, array_freq
    for k, v in d.items():
        seq_histogram.setdefault(v, []).append(k) 
    array_freq=[]
    for k in seq_histogram:
        array_freq.append(k)
    array_freq.sort(reverse=True)
    return array_freq 
