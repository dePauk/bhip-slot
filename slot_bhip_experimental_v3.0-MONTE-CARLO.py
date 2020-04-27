global krediti, win_bhip
import tkinter as tk
import random
import time

krediti = 0
spin_value = 1
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
        se_koliko_twoway += 12
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

def multi(n):
    #rtp = 0
    #krediti = 0
    for i in range(n):
        igraj()
    #rtp = 100*((n*spin_value)+krediti)/n
    #return (rtp)


    



#mainloop()

#multiplay(10)
