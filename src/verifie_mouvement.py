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
from src.quiz import Quiz
from src.dial import Dialogue

def verifie_mouvement(map, joueur, direction):

    x_position_joueur=joueur.x
    y_position_joueur=joueur.y

    peux_bouger=1
    traversable=0
    texte=""
    fin_du_jeu=0
    if(map[y_position_joueur][x_position_joueur]=="4" or map[y_position_joueur][x_position_joueur]=="5" or map[y_position_joueur][x_position_joueur]=="6" or map[y_position_joueur][x_position_joueur]=="7" ):
        if(map[y_position_joueur][x_position_joueur]=="4" and direction!=0):
            peux_bouger=0
        if(map[y_position_joueur][x_position_joueur]=="5" and direction!=1):
            peux_bouger=0
        if(map[y_position_joueur][x_position_joueur]=="6" and direction!=2):
            peux_bouger=0
        if(map[y_position_joueur][x_position_joueur]=="7" and direction!=3):
            peux_bouger=0

    
    if (peux_bouger==1):
        if(direction==0):
            tuille = map[y_position_joueur][x_position_joueur-1]
        if(direction==1):
            tuille = map[y_position_joueur][x_position_joueur+1]
        if(direction==3):
            tuille = map[y_position_joueur-1][x_position_joueur]
        if(direction==2):
            tuille = map[y_position_joueur+1][x_position_joueur]

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
            case=EntreeGrotte()
        
        
        if(case.traversable(joueur)==1):
            traversable=1

        if(case.boiteDialogue(joueur)==1):
            #APPEZL FONCTION DIALOGUE
            texte="***\nPLACEHOLDER PLACEHOLDER PLACEHOLDER PLACEHOLDER PLACEHOLDER\n***\n"

        if(case.enigme()==1):
            question=Quiz("src/questions.xml")
            ouverture_porte=question.jouer()
            if(ouverture_porte==1):
                if(direction==0):
                    map[y_position_joueur][x_position_joueur-1]="3"
                if(direction==1):
                    map[y_position_joueur][x_position_joueur+1]="3"
                if(direction==3):
                    map[y_position_joueur-1][x_position_joueur]="3"
                if(direction==2):
                    map[y_position_joueur+1][x_position_joueur]="3"

        if(case.trouveTresors(joueur)==1):
            joueur.update_resources(1)
            texte="***\nVous avez trouver un trésor, augmentant votre richesse\n***\n"
            if(direction==0):
                map[y_position_joueur][x_position_joueur-1]="0"
            if(direction==1):
                map[y_position_joueur][x_position_joueur+1]="0"
            if(direction==3):
                map[y_position_joueur-1][x_position_joueur]="0"
            if(direction==2):
                map[y_position_joueur+1][x_position_joueur]="0"
        
        if(case.gagneVie(joueur)==1):
            texte="***\nVous vous reposez à l'auberge, et regagnez 1 point de vie\n***\n"

        if(case.piege(joueur)==1):
            texte="***\nVous êtes tomber dans un piege !\n***\n"
            if(direction==0):
                map[y_position_joueur][x_position_joueur-1]="0"
            if(direction==1):
                map[y_position_joueur][x_position_joueur+1]="0"
            if(direction==3):
                map[y_position_joueur-1][x_position_joueur]="0"
            if(direction==2):
                map[y_position_joueur+1][x_position_joueur]="0"

        if(case.boiteDialogue(joueur)==1):
            dialogue=Dialogue("src/dialogue.xml", joueur, direction)
            dialogue.jouer()
            

        if(case.ending(joueur)==1):
            fin_du_jeu=1

            


    return map, traversable, texte, fin_du_jeu