# cerca parola precisa()
import analisi_testo_mod2_cerca as cerca
import analisi_testo_mod3_osserva as osserva
import analisi_testo_mod1_automatismi as arrayz

def x_parola():
    parola=input("cerca parola precisa: ")
    frasi_ric1=[]
    if parola!="":
        ric1=cerca.array_ricorrenze_parola(parola)
        if len(ric1)!=0:
        
        # * opzione stampa
            vuoi_stampa=input("vuoi stampare le frasi in cui è inserita? digita s ed invia")
            if vuoi_stampa=="s":
                print()
                frasi_ric1=cerca.estrapola_frase(ric1)
                cerca.print_frasi(frasi_ric1)
            return frasi_ric1
        else:
            print("parola non trovata")
            x_parola()
    else:
        print("Non hai digitato alcuna parola")
        x_parola()

def x_radice_parola():
    parola=input("cerca radice di un parola (almeno 3 lettere): ")
    frasi_ric1=[]
    if parola!="" and len(parola)>=3:
        ric1=cerca.parole_simili(parola)
        if len(ric1)!=0:
        
        # * opzione stampa
            vuoi_stampa=input("vuoi stampare le frasi in cui è inserita? digita s ed invia")
            if vuoi_stampa=="s":
                print()
                frasi_ric1=cerca.estrapola_frase(ric1)
                cerca.print_frasi(frasi_ric1)
            return frasi_ric1
        else:
            print("parola non trovata")
            x_parola()
    else:
        print("Non hai digitato alcuna parola")
        x_radice_parola()

def filtra_frequenze(n):
    default=len(arrayz.seq_histogram)
    c1=osserva.filtri_tup()
    lista_filtrata=osserva.hist_ad_esclusione(arrayz.seq_histogram,1,default,c1)
    osserva.parole_piu_frequenti(n,lista_filtrata)
    print()

def selezione():
    c=cerca.filtri_per_selezione_tup()
    arr=osserva.frequenza_selezione_filtro(c)
    vuoi_stampa=input("vuoi stampare le frasi in cui è inserita? digita s ed invia")
    if vuoi_stampa=="s":
        s=osserva.parole_filtrate_nel_testo(arr)
        cerca.print_frasi(s)
    print()







