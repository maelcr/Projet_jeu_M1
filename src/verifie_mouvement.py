from src.person import Player
from src.CaseVide import CaseVide
from src.Mur import Mur
from src.PorteFerme import PorteFerme
from src.PorteOuverte import PorteOuverte
from src.BarriereGauche import BarriereGauche
from src.BarriereDroite import BarriereDroite
from src.BarriereBas import BarriereBas
from src.BarriereHaut import BarriereHaut
from src.Tresor import Tresor
from src.Marchand import Marchand
from src.Aubergiste import Aubergiste
from src.Personne import Personne
from src.Panneau import Panneau
from src.Sphinx import Sphinx
from src.Piege import Piege
from src.PiegeMortel import PiegeMortel
from src.EntreeGrotte import EntreeGrotte

def verifie_mouvement(map, joueur, direction):

    x_position_joueur=joueur.x
    y_position_joueur=joueur.y

    
    if not (map[x_position_joueur][y_position_joueur]==direction+4):
        if(direction==0):
            tuille = map[x_position_joueur-1][y_position_joueur]
        if(direction==1):
            tuille = map[x_position_joueur+1][y_position_joueur]
        if(direction==2):
            tuille = map[x_position_joueur][y_position_joueur-1]
        if(direction==3):
            tuille = map[x_position_joueur][y_position_joueur+1]

        if(tuille=="0"):    
            case=CaseVide()
        elif(tuille=="1"):    
            case=Mur()
        elif(tuille=="2"):    
            case=PorteFerme()
        elif(tuille=="3"):    
            case=PorteOuverte()
        elif(tuille=="4"):    
            case=BarriereGauche()
        elif(tuille=="5"):    
            case=BarriereDroite()
        elif(tuille=="6"):    
            case=BarriereBas()
        elif(tuille=="7"):    
            case=BarriereHaut()
        elif(tuille=="8"):    
            case=Tresor()
        elif(tuille=="9"):    
            case=Marchand()
        elif(tuille=="10"):    
            case=Aubergiste()
        elif(tuille=="11"):    
            case=Personne()
        elif(tuille=="12"):    
            case=Panneau()
        elif(tuille=="13"):    
            case=Sphinx()
        elif(tuille=="14"):    
            case=Piege()
        elif(tuille=="15"):    
            case=PiegeMortel()
        elif(tuille=="16"):    
            case=EntreeGrotte
        
        traversable=0
        if(case.traversable(joueur)==1):
            traversable=1



    return map, traversable