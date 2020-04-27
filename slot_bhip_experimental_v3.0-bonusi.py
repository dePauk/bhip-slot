global krediti, win_bhip
import tkinter as tk
import random
import time

krediti = 0
spin_value = 100
free_spini = 0
multi = 1
se_koliko_multi_1_5 = 0
se_koliko_twoway = 0

twoway = 0

win_bhip = False

'''
BBBB ' 10 free spinov x2 multi
'''


global beseda, izzrebana_beseda, izzrebana1, izzrebana2, izzrebana3, izzrebana4


def igraj2():
    #Za test#
    global beseda, win_bhip
    win_bhip = True
    beseda = 'BHIP'
    return (beseda)


def igraj():
    global krediti, rezultat, beseda, win_bhip, free_spini, spin_value
    global multi, se_koliko_multi_1_5, se_koliko_twoway
    
    win_bhip = True

    
    simbol = 'X'
    beseda = ''
    
    for i in range(4):
        nakljucni_simbol = random.choice('BHIP')
        beseda += nakljucni_simbol
    #beseda = 'PPPP'

    if beseda[0:4] == 'BHIP':
        krediti += 200*spin_value*multi
        win_bhip = True
        #print ('Pa saj je win')
        
    if beseda[0:4] == 'BBBB':
        free_spini += 10
        multi = 1.5
        se_koliko_multi_1_5 = 10

    if beseda[0:4] == 'HHHH':
        free_spini += 15
        multi = 1

    if beseda[0:4] == 'IIII':
        free_spini += 10
        multi = 1

    if beseda[0:4] == 'PPPP':
        se_koliko_twoway += 10
        multi = 1

    elif beseda[0:4] == 'PIHB' and se_koliko_twoway > 0:
        krediti += 200*spin_value*multi
        win_bhip = True
        #print ('Pa saj je win')
        
    
        
    else:
        win_bhip = False
        

    if free_spini == 0:
        krediti -= spin_value
    elif free_spini > 0:
        pass

    if free_spini > 0:
        free_spini -=1
    elif free_spini == 0:
        pass

    if se_koliko_multi_1_5 > 0:
        se_koliko_multi_1_5 -=1

    if se_koliko_multi_1_5 > 0:
        multi = 1.5
    elif se_koliko_multi_1_5 == 0:
        multi = 1

    if se_koliko_twoway >0:
        se_koliko_twoway -= 1
        
        

    return (beseda)
    return (krediti)

def multiplay(n):
    for i in range(n):
        igraj()


    
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
        motivacija = random.choice('abcdefghijklmnopqrstuvwxyz1234567890')
        if motivacija == 'a':
            slot_izpis['text'] = 'Še malo se potrudi za novo zvezdico'
        elif motivacija == 'b':
            slot_izpis['text'] = 'Samo še 1835€ vloži, pa bojo letele pare'
        elif motivacija == 'c':
            slot_izpis['text'] = 'Srečo imaš, da si ob pravem času na pravem mestu'
        elif motivacija == 'd':
            slot_izpis['text'] = 'A bi res raje pobiral flaše za 0,50 kn?'
        elif motivacija == 'e':
            slot_izpis['text'] = 'Vem, da bi rad z nami potoval na Tajsko'
        elif motivacija == 'f':
            slot_izpis['text'] = 'Dej, da ti pokažem razliko med piramido pa tem'
        elif motivacija == 'g':
            slot_izpis['text'] = 'Vem, da rad poješ, ampak dvomim, da ti bo s petjem uspelo'
        elif motivacija == 'h':
            slot_izpis['text'] = 'Če si mislu prit sem zarad punc, žal ne bo šlo'
        elif motivacija == 'i':
            slot_izpis['text'] = 'Sposodi si od par kolegov po 100€, pa bo dovolj'
        elif motivacija == 'j':
            slot_izpis['text'] = 'Mamo velik produktov, ampak za erektilno disfunkcijo pa žal ne'
        elif motivacija == 'k':
            slot_izpis['text'] = 'INDIGOOOO TE NAHAJPA'
        elif motivacija == 'l':
            slot_izpis['text'] = 'Tale tip je pa Lamborghinija dubu na eventu'
        elif motivacija == 'm':
            slot_izpis['text'] = 'Če boš pridn, boš meu tut ti lahko tako uro'
        elif motivacija == 'n':
            slot_izpis['text'] = 'Mislim, da tale Vili tut preveč piše, ne samo govori'
        elif motivacija == 'o':
            slot_izpis['text'] = 'Bolš, da se ne vmeša moj mož'
        elif motivacija == 'p':
            slot_izpis['text'] = 'Pozdrav v Srbijo'
        elif motivacija == 'q':
            slot_izpis['text'] = 'Ne jem bureka'
        elif motivacija == 'r':
            slot_izpis['text'] = 'Čau bau Aneja'
        elif motivacija == 's':
            slot_izpis['text'] = 'A se kej kavsa na teh zabavah?'
        elif motivacija == 't':
            slot_izpis['text'] = 'Deny prosim ne it v to'
        elif motivacija == 'u':
            slot_izpis['text'] = 'Vredu bo Ana, se slišimo, ja super, adijo'
        elif motivacija == 'v':
            slot_izpis['text'] = 'Nobenega vložka ne rabiš za začet'
        elif motivacija == 'w':
            slot_izpis['text'] = 'Boljši smo kot Lifepharm'
        elif motivacija == 'x':
            slot_izpis['text'] = 'A bi raje služu samo za zraven ali namesto službe?'
        elif motivacija == 'y':
            slot_izpis['text'] = 'Je kr legenda tale Luka'
        elif motivacija == 'z':
            slot_izpis['text'] = 'Hej a daš cifro ;)'
        elif motivacija == '1':
            slot_izpis['text'] = 'Hej :) A te lahko zmotim za minutko?'
        elif motivacija == '2':
            slot_izpis['text'] = 'Use narobe izgovorim, pa pametn sm hotu izpast'
        elif motivacija == '3':
            slot_izpis['text'] = 'A tvoj fant je tut v tem?'
        elif motivacija == '4':
            slot_izpis['text'] = 'Sm mislu če bi šla kdaj vn, tko na kkšno pijačko'
        elif motivacija == '5':
            slot_izpis['text'] = 'Ful te je lepo slišat'
        elif motivacija == '6':
            slot_izpis['text'] = 'Iskreno teb bl zaupam, sej vem da sm te blokiru na fejsu, ampak useen'
        elif motivacija == '7':
            slot_izpis['text'] = 'So mel na b:hipu 5 dni davčno, pa niso nobenih nepravilnosti odkril'
        elif motivacija == '8':
            slot_izpis['text'] = 'Ja mi smo ful dobrodelni, a si že slišu kdaj za Forest Children?'
        elif motivacija == '9':
            slot_izpis['text'] = 'A si ti uredu?'
        elif motivacija == '0':
            slot_izpis['text'] = 'Kok je Burja lačn'


            

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
    
def osvezi_prikaz_free_spini():
    global free_spini
    stevilo_free_spini['text'] = str(free_spini)

def osvezi_prikaz_multiplier():
    global multi
    stevilo_multiplier['text'] = str(multi)

def osvezi_prikaz_twoway():
    global twoway
    stevilo_twoway['text'] = str(se_koliko_twoway)




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

    osvezi_prikaz_free_spini()
    osvezi_prikaz_multiplier()
    osvezi_prikaz_twoway()

    

okno = tk.Tk()
okno.geometry('500x650')
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

okno_bonusi = tk.Frame(okno)
okno_bonusi.pack()


naslov_free_spini = tk.Label(okno_bonusi, font = ("TkDefaultFont", 13), text ='Free spini:', fg = 'gold', bg = "gray1")
naslov_free_spini.pack(side=tk.LEFT)

stevilo_free_spini = tk.Label(okno_bonusi, font = ("TkDefaultFont", 16), fg = 'gold', bg = "gray1")
stevilo_free_spini.pack(side=tk.LEFT)
osvezi_prikaz_free_spini()

naslov_multi = tk.Label(okno_bonusi, font = ("TkDefaultFont", 13), text ='  Multiplier:', fg = 'gold', bg = "gray1")
naslov_multi.pack(side=tk.LEFT)

stevilo_multiplier = tk.Label(okno_bonusi, font = ("TkDefaultFont", 16), fg = 'gold', bg = "gray1")
stevilo_multiplier.pack(side=tk.LEFT)
osvezi_prikaz_multiplier()

naslov_twoway = tk.Label(okno_bonusi, font = ("TkDefaultFont", 13), text ='  Twoway:', fg = 'gold', bg = "gray1")
naslov_twoway.pack(side=tk.LEFT)

stevilo_twoway = tk.Label(okno_bonusi, font = ("TkDefaultFont", 16), fg = 'gold', bg = "gray1")
stevilo_twoway.pack(side=tk.LEFT)
osvezi_prikaz_twoway()


preglednost7 = tk.Label(okno, bg = 'cornflowerblue')
preglednost7.pack()

slot_izpis = tk.Label(okno, font = ("TkDefaultFont", 13), fg = 'white', bg = 'cornflowerblue')
slot_izpis.pack()
osvezi_prikaz_besede()


slot_izpis_posebej = tk.Frame(okno)
slot_izpis_posebej.pack()

prva_crka = tk.Label(slot_izpis_posebej, font = ("TkDefaultFont", 28), fg = 'gold', bg = "gray1")
prva_crka.pack(side=tk.LEFT)
osvezi_prikaz1()

druga_crka = tk.Label(slot_izpis_posebej, font = ("TkDefaultFont", 28), fg = 'gold', bg = "gray1")
druga_crka.pack(side=tk.LEFT)
osvezi_prikaz2()

tretja_crka = tk.Label(slot_izpis_posebej, font = ("TkDefaultFont", 28), fg = 'gold', bg = "gray1")
tretja_crka.pack(side=tk.LEFT)
osvezi_prikaz3()

cetrta_crka = tk.Label(slot_izpis_posebej, font = ("TkDefaultFont", 28), fg = 'gold', bg = "gray1")
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

zapis_naslova = tk.Label(naslov, font = ("TkDefaultFont", 35), text = "b:hip zlata jama", bg= 'cornflowerblue', fg = 'gold').pack()

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
