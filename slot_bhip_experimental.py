global krediti
import tkinter as tk


krediti = 0
spin_value = 100

win = 250*spin_value

#fast = False

import random
import time

#verj_b = 0.25
#verj_h = 0.25
#verj_i = 0.25
#verj_p = 0.25

global beseda, izzrebana_beseda

def igraj2():
    global beseda
    beseda = 'BHIP'
    return (beseda)

def igraj():
    global krediti, rezultat, beseda
    krediti -= spin_value
    simbol = 'X'
    beseda = ''
    for i in range(2):
        #time.sleep(0.75)
        nakljucni_simbol = random.choice('BHIP')
        beseda += nakljucni_simbol
        #print (beseda)

    if beseda[0:2] != 'BH':
        for i in range(2):
            #time.sleep(0.33)
            nakljucni_simbol = random.choice('BHIP')
            beseda += nakljucni_simbol
            #print (beseda)
            
    elif beseda[0:2] == 'BH':
        #print ('''
        #Ni pristopnih stroškov!
        #''')
        #time.sleep(5)
        nakljucni_simbol = random.choice('BHIP')
        beseda += nakljucni_simbol
        #print (beseda)
        #if beseda[0:3] == 'BHI':
            #print ('''
        #Samo še 1835€ plačaj, pa bojo letele pare!
            #''')
            #time.sleep(6)
        #else:
            #time.sleep(0.33)
        
        nakljucni_simbol = random.choice('BHIP')
        beseda += nakljucni_simbol
##        print (beseda)
        if beseda[0:4] == 'BHIP':
            krediti += 250*spin_value
            print ('Pa saj je win')
##            print ('''
##            P L A T I N U M   B H I P ! ! !
##            ''')
##            time.sleep(2)
##            print ('BIG WIN ' % (win))

    #print ('''
#Krediti:''')
    #print (int(krediti))
    #print ('')    
    #print (beseda)
    return (beseda)
    return (krediti)

def multiplay(n):
    for i in range(n):
        #time.sleep(1.5)
        play()


#def program_tk():
#    global beseda, izzrebana_beseda
#    #beseda_tk = beseda
#    #krediti_tk = krediti
#    igraj()
#    izzrebana_beseda = beseda

#def osvezi_prikaz_dodatka_kreditov():
#    koliko_dodatka_kreditov['text'] = str(zapis_dodatek_kreditov)
    
zapis_dodatek_kreditov = 0

def zapis_dod_10():
    global zapis_dodatek_kreditov
    zapis_dodatek_kreditov += 10
    osvezi_prikaz_dodatka_kreditov()

def zapis_dod_100():
    global zapis_dodatek_kreditov
    zapis_dodatek_kreditov += 100
    osvezi_prikaz_dodatka_kreditov()

def zapis_dod_1000():
    global zapis_dodatek_kreditov
    zapis_dodatek_kreditov += 1000
    osvezi_prikaz_dodatka_kreditov()

def zapis_dod_reset():
    global zapis_dodatek_kreditov
    zapis_dodatek_kreditov = 0
    osvezi_prikaz_dodatka_kreditov()

def osvezi_prikaz_dodatka_kreditov():
    koliko_dodatka_kreditov['text'] = str(zapis_dodatek_kreditov)

def potrdi_dodatek_kreditov():
    global zapis_dodatek_kreditov, krediti, prikaz_kreditov
    krediti += zapis_dodatek_kreditov
    zapis_dodatek_kreditov = 0
    prikaz_kreditov = krediti
    osvezi_prikaz_dodatka_kreditov()
    osvezi_prikaz_kreditov()



#def program_tk():
#    global izzrebana_beseda, krediti, beseda
#    igraj()
#    izzrebana_beseda = beseda
#    prikaz_kreditov = krediti

izzrebana_beseda = 'Zavrti in poglej, ali je BHIP zlata jama'
##delna_beseda2 ='abc'
  

def osvezi_prikaz_besede():
    #global izzrebana_beseda, prikaz_izzrebane_besede
    #nov_spin()
    #izzrebana_beseda = beseda
    #global delna_beseda2, delna_beseda3, delno
##    if delno == True:
##        time.sleep(2)      
##    elif delno == False:
##        time.sleep(0.5)
##    slot_izpis['text'] = str(izzrebana_beseda)
    time.sleep(0.5)
    slot_izpis['text'] = str(izzrebana_beseda)
    

##def osvezi_prikaz_besede_2():
##    #global izzrebana_beseda, prikaz_izzrebane_besede
##    #nov_spin()
##    #izzrebana_beseda = beseda
##    global delna_beseda2, delna_beseda3, delno
##    if delno == True:
##        time.sleep(0.5)      
##        slot_izpis2['text'] = str(delna_beseda2)
##    elif delno == False:
##        slot_izpis2['text'] = 'Žal'
        
        
    
'''
def nastavi število autoplay
'''

def osvezi_prikaz_kreditov():
    krediti_izpis['text'] = str(prikaz_kreditov)

prikaz_kreditov = krediti

##delno = False
##delna_beseda2 = ''
##delna_beseda3 = ''

# TESTIRANJE ZA POČASEN PRIKAZ
##def nov_spin():
##    #program_tk()
##    global izzrebana_beseda, prikaz_kreditov, krediti, beseda
##    global delno, delna_beseda2, delna_beseda3
##    igraj()
##    if beseda[0:2] != 'BH': #tale if stavek je modifikacija test
##        delno = False
##        izzrebana_beseda = beseda
##        prikaz_kreditov = krediti
##        osvezi_prikaz_besede()
##        osvezi_prikaz_kreditov()
##    elif beseda[0:2] == 'BH':
##        prikaz_kreditov = krediti
##        izzrebana_beseda = beseda
##        delno = True
##        delna_beseda2 = izzrebana_beseda[0:2]
##        delna_beseda3 = izzrebana_beseda[0:3]
##        osvezi_prikaz_besede()
##        osvezi_prikaz_besede2()
##        #time.sleep(1)
##        #osvezi_prikaz_besede()
##        osvezi_prikaz_kreditov()
##    delno = False
        

# BACKUP NOV_SPIN
def nov_spin():
    #program_tk()
    global izzrebana_beseda, prikaz_kreditov, krediti, beseda
    igraj()

    izzrebana_beseda = beseda
    prikaz_kreditov = krediti
    osvezi_prikaz_besede()
    osvezi_prikaz_kreditov()



    

okno = tk.Tk()
okno.geometry('400x400')

naslov = tk.Frame(okno)
naslov.pack()

preglednost0 = tk.Label(okno)
preglednost0.pack()

naslov_dod_kreditov = tk.Frame(okno)
naslov_dod_kreditov.pack()

dodajanje_kreditov = tk.Frame(okno)
dodajanje_kreditov.pack()

koliko_dodatka_kreditov = tk.Label(okno, font = ("TkDefaultFont", 12), bg = "white")
koliko_dodatka_kreditov.pack()
osvezi_prikaz_dodatka_kreditov()

potrdi_dod_kreditov = tk.Frame(okno)
potrdi_dod_kreditov.pack()

preglednost1 = tk.Label(okno)
preglednost1.pack()

preglednost2 = tk.Label(okno)
preglednost2.pack()

preglednost3 = tk.Label(okno)
preglednost3.pack()

slot_izpis = tk.Label(okno, font = ("TkDefaultFont", 16), bg = "white")
slot_izpis.pack()
osvezi_prikaz_besede()

##slot_izpis2 = tk.Label(okno, font = ("TkDefaultFont", 16), bg = "white")
##slot_izpis2.pack()
##osvezi_prikaz_besede2()

zavrti_slot = tk.Frame(okno)
zavrti_slot.pack()

preglednost4 = tk.Label(okno)
preglednost4.pack()

naslov_krediti = tk.Frame(okno)
naslov_krediti.pack()

krediti_izpis = tk.Label(okno, font = ("TkDefaultFont", 14), bg = "white")
krediti_izpis.pack()
osvezi_prikaz_kreditov()


###

zapis_naslova = tk.Label(naslov, font = ("TkDefaultFont", 13), text = "b:hip slot 2020").pack()

zapis_naslova_dod_kreditov = tk.Label(naslov_dod_kreditov, font = ("TkDefaultFont", 13), text = "Dodajanje kreditov:").pack()


dodatnih_10 = tk.Button(dodajanje_kreditov, font = ("TkDefaultFont", 11), text = "+10", command=zapis_dod_10).grid(row=0, column=0)
dodatnih_100 = tk.Button(dodajanje_kreditov, font = ("TkDefaultFont", 11), text = "+100", command=zapis_dod_100).grid(row=0, column=1)
dodatnih_1000 = tk.Button(dodajanje_kreditov, font = ("TkDefaultFont", 11), text = "+1000", command=zapis_dod_1000).grid(row=0, column=2)
dodatnih_reset = tk.Button(dodajanje_kreditov, font = ("TkDefaultFont", 11), text = "RESET", command=zapis_dod_reset).grid(row=0, column=3)

potrdi_dodajanje = tk.Button(potrdi_dod_kreditov, font = ("TkDefaultFont", 11), text = "Potrdi", command=potrdi_dodatek_kreditov).pack()

zavrti_slot_gumb = tk.Button(zavrti_slot, font = ("TkDefaultFont", 11), text = "ZAVRTI", command=nov_spin).pack()

zapis_naslova_krediti = tk.Label(naslov_krediti, font = ("TkDefaultFont", 13), text = "Krediti:").pack()
