#paramètres 
#temps estimé
tpsEstimee=0
#temps distracteur
distTps=0
#poids 

#@param 0<k<1
def weight(k,dist,tps):
    return k**abs(tps-dist)
#temps estimé
def tpsEstime(tps,dist,w):
    return ((tps + dist * w)/(1+w))
