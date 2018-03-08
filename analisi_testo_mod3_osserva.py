import analisi_testo_mod1_automatismi as arrayz
import analisi_testo_mod2_cerca as osserva
import string

def hist_ad_esclusione(seq,limite_min_freq,prime_tot_freq,*args):
    lista_filtrata=[]
    parole_non=()
    for it in range(0,len(args)):
        parole_non=parole_non+args[it]                           
    
    for i in range(0,prime_tot_freq):
        if arrayz.array_freq[i]>=int(limite_min_freq):  
            B=False
            c=arrayz.seq_histogram[arrayz.array_freq[i]]        
            for num in range(0,len(c)):                                                
                if c[num] in parole_non:                
                    B=True
                    continue
                else:                
                    B=False
                    break            
            if B:                        
                continue
            else:
                for it in c:
                    if it not in parole_non:
                        lista_filtrata.append(it)
                        #print("n° ",arrayz.array_freq[i],"'",it,"'")
    return lista_filtrata
################################################# costruisci tuple per filtri

def filtri_tup():
    
    tup_filtri=()    
    list_filtri=[]
    risp=input("...filtra la ricerca togli gli\n---1 articoli\n---2 pronomi personali\n---3 preposizioni\n---4 congiunxione\n---5 pronomi dimostrativi\n---6 verbi ausiliari\n---7 avverbi\n---8 virgolette e dialoghi\n...digita il numero per ogni tipo di filtro si voglia applicare : \n...")
    #filtri=[]
    filtri=tuple(risp)
    print(filtri)
    for  item in filtri:
        if item=="1":
            list_filtri.append(arrayz.tup_articoli)
        elif item=="2":
            list_filtri.append(arrayz.tup_pronomi)
        elif item=="3":
            list_filtri.append(arrayz.tup_preposizioni)
        elif item=="4":
            list_filtri.append(arrayz.tup_congiunzioni)
        elif item=="5":
            list_filtri.append(arrayz.tup_dim)
        elif item=="6":
            list_filtri.append(arrayz.tup_ausiliari)
        elif item=="7":
            list_filtri.append(arrayz.tup_avverbi)
        elif item=="8":
            list_filtri.append(arrayz.tup_dialoghi)
    tup_filtri1=tuple(list_filtri)
    tup_filtri=tuple(tup_filtri1)
    tup=()
    for it in list_filtri:
        tup=tup+it
    
    return tup


def parole_piu_frequenti(numero,iterabile):
    for i in range(0,numero):
        
        print("n° ",arrayz.d[iterabile[i]],"'",iterabile[i],"'")


def frequenza_selezione_filtro(tup_filtro):
    array_item=[]
    for item ,v in arrayz.d.items():
        if item in tup_filtro:
            print("n°",v,"'",item,"'")
            array_item.append(item)
    
    return array_item
 
      
def parole_filtrate_nel_testo(array_item): 
    elenco_totale_frasi=[]
    for item in array_item:
        posizioni=osserva.array_ricorrenze_parola(item) 
        elenco_frasi=osserva.estrapola_frase(posizioni)
        elenco_totale_frasi.extend(elenco_frasi)
       
    return elenco_totale_frasi   
    

