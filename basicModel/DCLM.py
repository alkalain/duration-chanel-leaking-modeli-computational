#paramètres 
#temps estimé
tpsEstimee=0
#temps distracteur
distTps=0
#d | dist : la durée du stimulu distracteur

#poids 
#@param 0<=k<=1
#w : le poid du distracteur dans l’obtention de t^.
def weight(k,dist,tps):
    return k**abs(tps-dist)
#temps estimé
#t | tps : la durée du stimulu cible
#t^ | tpsEstime: la durée perçue du stimulu cible
def tpsEstime(tps,dist,w):
    return ((tps + dist * w)/(1+w))

#DCLM fct

def DCLM(k,d,t):
    w=weight(k,d,t)
    print(w)
    return tpsEstime(t,d,w)

print(DCLM(0.5,2,1))
