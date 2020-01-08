present = {"e":1, "es":2, "e":3, "ons":4, "ez":5, "ent":6}
imparfait = {"ais":1, "ais":2, "ait":3, "ions":4, "iez":5, "aient":6}

def analyse(verbe_conjugue):
    for terminaison in present.keys():
        if terminaison == verbe_conjugue[-(len(terminaison)):]:
            print("(" + verbe_conjugue[:-(len(terminaison))] + "er" + "," , present[terminaison] , ", présent)")
analyse("mange")
analyse("balayez")
analyse("travaillions")

def analyse(verbe_conjugue):
    verbe_traite = False
    for terminaison in imparfait.keys():
        if terminaison in verbe_conjugue[-(len(terminaison)):]:
            print("(" + verbe_conjugue[:-(len(terminaison))] + "er" + "," , imparfait[terminaison] , ", imparfait)")
            verbe_traite = True
    if verbe_traite == False:
        for terminaison in present.keys():
            if terminaison in verbe_conjugue[-(len(terminaison)):]:
                print("(" + verbe_conjugue[:-(len(terminaison))] + "er" + "," , present[terminaison] , ", présent)")        
    
analyse("mange")
analyse("balayez")
analyse("travaillions")