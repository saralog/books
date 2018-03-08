
import analisi_testo_mod1_automatismi as arrayz
import analisi_testo_mod2_cerca as cerca
import analisi_testo_mod3_osserva as osserva
import analisi_testo_mod4_tupple as tup

import analisi_testo_ricerche as ric

#  chiamata per l inizzializazione del testo in formato *txt, verra creata una mappatura del testo

arrayz.inizializza_le_sequenze("inserisci_qui_file_testo.txt")
default=len(arrayz.seq_histogram)
titolo_testo="Inserisci qui il nome del testo "
# PRIMA SCHEDA ANALISI  fornisce una visione generale del testo
print("TESTO ANALIZZATO : ",titolo_testo)
print("\nnumero parole totali: ",len(arrayz.seq_parola))
print("\nnumero parole nuove : ",len(arrayz.d))

print("OSSERVAZIONI\n")
print("\nEcco l elenco delle prime 10 parole più frequenti\n")
q=osserva.hist_ad_esclusione(arrayz.seq_histogram,1,default)
osserva.parole_piu_frequenti(10,q)
print("\npuoi filtrare l'istogramma eliminando le particelle grammaticali più comuni\n")
ric.filtra_frequenze(30)
print("\npuoi selezionare l'istogramma solo per alcune parole nel testo\n")
ric.selezione()

print("RICERCHE\n")
print("\npuoi ricercare una parola specifica\n")
ric.x_parola()
print("\npuoi selezionare solo le parole che condividono una radice")
ric.x_radice_parola()











