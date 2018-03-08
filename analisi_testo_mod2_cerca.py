import analisi_testo_mod1_automatismi as arrayz
import analisi_testo_mod3_osserva as osserva
import analisi_testo_mod4_tupple as gramm
import string
def freq_parola_in_dict(parola):
    #global d
    for k,v in arrayz.d.items():
        if k==parola:
            print("la parola è presente :",v," volte nel testo")
            return True
            
    print("la parola non c'è")

def array_ricorrenze_parola(parola):

    
    punct=string.punctuation+"“”"
    ricorrenze=[]#array di posizioni
    index=0
    
    if parola in arrayz.d:                
        for i in range(index,len(arrayz.seq_reale)):        
            item= arrayz.seq_reale[i].lower()
                         
            if item==parola or item[:-1]==parola:
                               
                ricorrenze.append(i)
                continue    
    else:
        print("parola non presente")  
    print("'",parola,"' presente : ", len(ricorrenze)," volte")        
    return ricorrenze  

def estrapola_frase(array_posizioni):
    
    array_frasi=[]
    for i in range(0,len(array_posizioni)):
        posizione=array_posizioni[i]
        num_riga=estrai_riga(posizione)
        posizione_finale,posiione_iniziale,an,inn=0,0,1,-1        
        A,I=True, True 

        while A:
            if posizione+an<=len(arrayz.seq_reale):
                parola=arrayz.seq_reale[posizione+an]

                if "." in parola or "?"in parola or"!"in parola:

                    posizione_finale=posizione+an
                    A=False
                an+=1
            else:
                A=False
        while I:
            if posizione+an>=0:
                parola=arrayz.seq_reale[posizione+inn]

                if "." in parola or "?"in parola or"!"in parola:

                    posizione_iniziale=posizione+inn
                    I=False
                inn-=1
            else:
                B=False
        frase=[]
        frase=arrayz.seq_reale[posizione_iniziale+1:posizione_finale+1]

        stringa_frase=""        
        for par in frase:
            stringa_frase=stringa_frase+" "+str(par)  

        array_frasi.append((stringa_frase," riga"+str(num_riga)))
    return array_frasi






def estrai_riga(posizione):
    
    for it in arrayz.seq_righe[1:-1]:
        
        if posizione>it and posizione<=arrayz.seq_righe[arrayz.seq_righe.index(it)+1]:

            return arrayz.seq_righe.index(it)+1+1

        elif posizione<it and posizione>=arrayz.seq_righe[arrayz.seq_righe.index(it)-1]: 
            

            return arrayz.seq_righe.index(it)-1-1
         

def print_frasi(array_frasi):
    c=array_frasi

    for n in range(0,len(c)-1):
        s=c[n]
        
        #print (ss[:-7])
        if c[n][0] not in c[n+1:][0] and c is not None:
            print()
            print(c[n][0]+c[n][1])
    print()    
    print (c[len(c)-1][0]+ c[len(c)-1][1])
        
    

def parole_simili(parola):
    tuple_ricorrenza_parole_simili=tuple()
    for k,v in arrayz.d.items():
        if parola==k[0:len(parola)]:
            c=array_ricorrenze_parola(k)
            tuple_ricorrenza_parole_simili=tuple_ricorrenza_parole_simili+tuple(c)
            #print(v," volte nel testo")
            
            #print()
            continue
            #return True"'",k,
    return tuple_ricorrenza_parole_simili  
        #print("la parola non c'è")

def filtri_per_selezione_tup():

    tup_filtri=()    
    list_filtri=[]
    risp=input("...frequenza e posizione di\n---1 articoli\n---2 pronomi personali\n---3 preposizioni\n---4 avverbio dubitativo\n---5 congiunxione conclusive\n---6 congiunxione avversative\n---7 congiunzione disgiuntiva\n---8 congiunzione causale\n...digita il numero per ogni tipo di filtro si voglia applicare : \n...")
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
            list_filtri.append(gramm.tup_avv_dubbio)
        elif item=="5":
            list_filtri.append(gramm.tup_cong_conclus)
        elif item=="6":
            list_filtri.append(gramm.tup_cong_avvers)
        elif item=="7":
            list_filtri.append(gramm.tup_cong_disg)
        elif item=="8":
            list_filtri.append(gramm.tup_cong_causal)
    tup_filtri1=tuple(list_filtri)
    tup_filtri=tuple(tup_filtri1)
    tup=()
    for it in list_filtri:
        tup=tup+it
    
    return tup
     


