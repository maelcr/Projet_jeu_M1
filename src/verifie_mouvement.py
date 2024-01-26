from src.person import Player
from src.CaseVide import CaseVide
from src.Mur import Mur
from src.PorteFerme import PorteFerme
from src.PorteOuverte import PorteOuverte
from src.BarriereGauche import BarriereGauche
from src.BarriereDroite import BarriereDroite
from src.BarriereBas import BarriereBas
from src.BarriereHaut import BarriereHaut


def verifie_mouvement(map, joueur, direction):

    x_position_joueur=joueur.x
    y_position_joueur=joueur.y

    tuille = map[x_position_joueur][y_position_joueur]
    if (tuille==direction+4):
        
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
                                        map_a_print+=(chr(24))
        elif(tuille=="8"):    
                                        map_a_print+=(chr(36))
        elif(tuille=="9"):    
                                        map_a_print+=(chr(77))
        elif(tuille=="10"):    
                                        map_a_print+=(chr(20))
        elif(tuille=="11"):    
                                        map_a_print+=(chr(33))
        elif(tuille=="12"):    
                                        map_a_print+=(chr(63))
        elif(tuille=="13"):    
                                        map_a_print+=(chr(14))
        elif(tuille=="14"):    
                                        map_a_print+=(chr(15))
        elif(tuille=="15"):    
                                        map_a_print+=(chr(19))
        elif(tuille=="16"):    
                                           map_a_print+=(chr(23))



    return map