global krediti, win_bhip
import tkinter as tk


krediti = 0
spin_value = 100

#win = 250*spin_value
win_bhip = False

#fast = False

import random
import time


global beseda, izzrebana_beseda, izzrebana1, izzrebana2, izzrebana3, izzrebana4


def igraj2():
    #Za test#
    global beseda, win_bhip
    win_bhip = True
    beseda = 'BHIP'
    return (beseda)

def igraj():
    global krediti, rezultat, beseda, win_bhip
    win_bhip = True
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
            #win_bhip = True
            print ('Pa saj je win')
##            print ('''
##            P L A T I N U M   B H I P ! ! !
##            ''')
##            time.sleep(2)
##            print ('BIG WIN ' % (win))
    if beseda[0:4] != 'BHIP':
        win_bhip = False
    if beseda[0:4] == 'BHIP':
        win_bhip = True

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



izzrebana_beseda = 'Zavrti in poglej, ali je BHIP zlata jama'
  

def osvezi_prikaz_besede():
    global win_bhip
    time.sleep(0.5)
    if win_bhip == True:
        slot_izpis['text'] = 'WIN WIN WIN'
    elif win_bhip == False:
        motivacija = random.choice('abc')
        if motivacija == 'a':
            slot_izpis['text'] = 'Še malo se potrudi za novo zvezdico'
        elif motivacija == 'b':
            slot_izpis['text'] = 'Samo še 1835€ vloži pa bojo letele pare'
        elif motivacija == 'c':
            slot_izpis['text'] = 'Srečo imaš, da si ob pravem času na pravem mestu'

izzrebana1 = 'X'
izzrebana2 = 'X'
izzrebana3 = 'X'
izzrebana4 = 'X'

    
def osvezi_prikaz1():
    #time.sleep(0.5)
    prva_crka['text'] = str(izzrebana1)

def osvezi_prikaz2():
    #time.sleep(0.5)
    druga_crka['text'] = str(izzrebana2)

def osvezi_prikaz3():
    #time.sleep(0.5)
    tretja_crka['text'] = str(izzrebana3)

def osvezi_prikaz4():
    #time.sleep(0.5)
    cetrta_crka['text'] = str(izzrebana4)
       


def osvezi_prikaz_kreditov():
    krediti_izpis['text'] = str(prikaz_kreditov)

prikaz_kreditov = krediti


#########################

#zapis_vrednost_stave = 0

def vredn_stave10():
    global spin_value
    spin_value = 10
    osvezi_vrednost_stave()

def vredn_stave20():
    global spin_value
    spin_value = 20
    osvezi_vrednost_stave()

def vredn_stave50():
    global spin_value
    spin_value = 50
    osvezi_vrednost_stave()

def vredn_stave100():
    global spin_value
    spin_value = 100
    osvezi_vrednost_stave()



def osvezi_vrednost_stave():
    koliko_vrednost['text'] = str(spin_value)


    
        
#zapis_vrednost_stave = spin_value


def potrdi_dodatek_kreditov():
    global zapis_dodatek_kreditov, krediti, prikaz_kreditov
    krediti += zapis_dodatek_kreditov
    zapis_dodatek_kreditov = 0
    prikaz_kreditov = krediti
    osvezi_prikaz_dodatka_kreditov()
    osvezi_prikaz_kreditov()




def nov_spin():
    #program_tk()
    global izzrebana_beseda, prikaz_kreditov, krediti, beseda
    global izzrebana1, izzrebana2, izzrebana3, izzrebana4
    igraj()

    izzrebana_beseda = beseda

    izzrebana1 = beseda[0]
    izzrebana2 = beseda[1]
    izzrebana3 = beseda[2]
    izzrebana4 = beseda[3]
    
    prikaz_kreditov = krediti
    osvezi_prikaz_besede()

    osvezi_prikaz1()
    osvezi_prikaz2()
    osvezi_prikaz3()
    osvezi_prikaz4()
    
    osvezi_prikaz_kreditov()



    

okno = tk.Tk()
okno.geometry('500x550')
okno.title('b:hip zlata jama')
okno.configure(bg = 'cornflowerblue')

naslov = tk.Frame(okno)
naslov.pack()

preglednost0 = tk.Label(okno, bg = 'cornflowerblue')
preglednost0.pack()

naslov_dod_kreditov = tk.Frame(okno)
naslov_dod_kreditov.pack()

dodajanje_kreditov = tk.Frame(okno)
dodajanje_kreditov.pack()

koliko_dodatka_kreditov = tk.Label(okno, font = ("TkDefaultFont", 13), bg = 'cornflowerblue', fg = 'gold')
koliko_dodatka_kreditov.pack()
osvezi_prikaz_dodatka_kreditov()

potrdi_dod_kreditov = tk.Frame(okno)
potrdi_dod_kreditov.pack()

preglednost1 = tk.Label(okno, bg = 'cornflowerblue')
preglednost1.pack()

preglednost2 = tk.Label(okno, bg = 'cornflowerblue')
preglednost2.pack()


slot_izpis = tk.Label(okno, font = ("TkDefaultFont", 15), fg = 'white', bg = 'cornflowerblue')
slot_izpis.pack()
osvezi_prikaz_besede()


slot_izpis_posebej = tk.Frame(okno)
slot_izpis_posebej.pack()

prva_crka = tk.Label(slot_izpis_posebej, font = ("TkDefaultFont", 23), fg = 'gold', bg = "gray1")
prva_crka.pack(side=tk.LEFT)
osvezi_prikaz1()

druga_crka = tk.Label(slot_izpis_posebej, font = ("TkDefaultFont", 23), fg = 'gold', bg = "gray1")
druga_crka.pack(side=tk.LEFT)
osvezi_prikaz2()

tretja_crka = tk.Label(slot_izpis_posebej, font = ("TkDefaultFont", 23), fg = 'gold', bg = "gray1")
tretja_crka.pack(side=tk.LEFT)
osvezi_prikaz3()

cetrta_crka = tk.Label(slot_izpis_posebej, font = ("TkDefaultFont", 23), fg = 'gold', bg = "gray1")
cetrta_crka.pack(side=tk.LEFT)
osvezi_prikaz4()



zavrti_slot = tk.Frame(okno)
zavrti_slot.pack()

preglednost4 = tk.Label(okno, bg = 'cornflowerblue')
preglednost4.pack()

naslov_krediti = tk.Frame(okno)
naslov_krediti.pack()

krediti_izpis = tk.Label(okno, font = ("TkDefaultFont", 16), fg = 'gold', bg = 'cornflowerblue')
krediti_izpis.pack()
osvezi_prikaz_kreditov()


preglednost5 = tk.Label(okno, bg = 'cornflowerblue')
preglednost5.pack()

preglednost6 = tk.Label(okno, bg = 'cornflowerblue')
preglednost6.pack()




naslov_nastavi_vrednost = tk.Frame(okno)
naslov_nastavi_vrednost.pack()

gumbi_vrednost = tk.Frame(okno)
gumbi_vrednost.pack()

koliko_vrednost = tk.Label(okno, font = ("TkDefaultFont", 13), bg = 'cornflowerblue', fg = 'gold')
koliko_vrednost.pack()
osvezi_vrednost_stave()





###

zapis_naslova = tk.Label(naslov, font = ("TkDefaultFont", 27), text = "b:hip zlata jama", bg= 'cornflowerblue', fg = 'gold').pack()

zapis_naslova_dod_kreditov = tk.Label(naslov_dod_kreditov, font = ("TkDefaultFont", 12), text = "Dodajanje kreditov:", fg = 'white', bg = 'cornflowerblue').pack()


dodatnih_10 = tk.Button(dodajanje_kreditov, font = ("TkDefaultFont", 11), fg = 'white', bg = 'RoyalBlue4', text = "+10", command=zapis_dod_10).grid(row=0, column=0)
dodatnih_100 = tk.Button(dodajanje_kreditov, font = ("TkDefaultFont", 11), fg = 'white', bg = 'RoyalBlue4', text = "+100", command=zapis_dod_100).grid(row=0, column=1)
dodatnih_1000 = tk.Button(dodajanje_kreditov, font = ("TkDefaultFont", 11), fg = 'white', bg = 'RoyalBlue4', text = "+1000", command=zapis_dod_1000).grid(row=0, column=2)
dodatnih_reset = tk.Button(dodajanje_kreditov, font = ("TkDefaultFont", 11), fg = 'white', bg = 'RoyalBlue4', text = "RESET", command=zapis_dod_reset).grid(row=0, column=3)

potrdi_dodajanje = tk.Button(potrdi_dod_kreditov, font = ("TkDefaultFont", 11), text = "Potrdi", bg = 'Royalblue4', fg = 'white', command=potrdi_dodatek_kreditov).pack()

zavrti_slot_gumb = tk.Button(zavrti_slot, font = ("TkDefaultFont", 16), text = "ZAVRTI", bg = 'gold',command=nov_spin).pack()

zapis_naslova_krediti = tk.Label(naslov_krediti, font = ("TkDefaultFont", 16), fg = 'white', bg = 'cornflowerblue', text = "Krediti:").pack()

zapis_naslova_nastavi_vrednost = tk.Label(naslov_nastavi_vrednost, font = ("TkDefaultFont", 12), text = "Vrednost stave:", fg = 'white', bg = 'cornflowerblue').pack()

vrednost_10 = tk.Button(gumbi_vrednost, font = ("TkDefaultFont", 11), fg = 'white', bg = 'RoyalBlue4', text = "10", command = vredn_stave10).grid(row=0, column=0)
vrednost_20 = tk.Button(gumbi_vrednost, font = ("TkDefaultFont", 11), fg = 'white', bg = 'RoyalBlue4', text = "20", command = vredn_stave20).grid(row=0, column=1)
vrednost_50 = tk.Button(gumbi_vrednost, font = ("TkDefaultFont", 11), fg = 'white', bg = 'RoyalBlue4', text = "50", command = vredn_stave50).grid(row=0, column=2)
vrednost_100 = tk.Button(gumbi_vrednost, font = ("TkDefaultFont", 11), fg = 'white', bg = 'RoyalBlue4', text = "100", command = vredn_stave100).grid(row=0, column=3)




#mainloop()

#multiplay(10)
