# modules a importer
import pytesseract
import tweepy 
from PIL import Image
from textparser import Error

# modules deja diaponibles
import os


#connection a l'api de twiter
consumer_key = "BGK0F5EWsbpypm6w59hFBHzOw"
consumer_secret ="0Z38Oy747x4A83EZirdX5h6SGlDIUfAJ7wRxjLsi0B5REkkrta"
access_token = "1375070617448423428-IrNB2BAP2KLUXBFv4yyE95eH4mZYvm"
access_token_secret ="p2uSfFvL8Ch7XUIcVnW8UiNUUhV0awQ1UCcyIptIv0ZLc"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

#extraction du texte contenu dans l description

"""for status in tweepy.Cursor(api.home_timeline, screen_name = "@MinisteredelaS1").items(1186628409524404226):
    try:
        #ecriture dans le fichier data.txt
        fichier = open("data.txt", "a")
        fichier.write(status.text)
    except Exception:
        pass
    finally:
        fichier.close()"""

#parcours et recuperation des donnees      

mon_fichier=open("data.txt","r")
ligne = mon_fichier.readline()
test=0
nvCas=0
contacts=0
commun=0
gueris=0
while ligne:        
    if "Tests" in ligne:
        for s in ligne.split():
            if s.isdigit():
                test=s
                print(test,"tests")

    if "Nouveaux cas" in ligne:
        for s in ligne.split():
            if s.isdigit():
                nvCas=s
                print(nvCas,"nouveaux cas")

    if "Cas contacts" in ligne:
        for s in ligne.split():
            if s.isdigit():
                contacts=s
                print(contacts,"Cas contacts")

    if "Cas communautaires" in ligne:
        for s in ligne.split():
            if s.isdigit():
                commun=s
                print(commun,"Cas communautaires ")

    if "Guéris" in ligne:
        for s in ligne.split():
            if s.isdigit():
                gueris=s
                print(s,"Guéris")            
    ligne = mon_fichier.readline()
mon_fichier.close() 


# lister les elements du dossier
contenu = os.listdir('images/')

os.chdir('images')

# parcours de chaque element du dossier
for elemement in contenu:
    nom = str(elemement)
    # extraction des ecritures
    text = pytesseract.image_to_string(Image.open(nom))
    tab = text.split()
    a = "tests"
    b = "positifs"
    nbpositif=0
    nbtest=0
    for mot in tab:
        # extraction du nombre de tests
        if mot == a:
            indice = tab.index(mot)
            mot = tab[indice-1]
            mot = mot.replace(".", "")
            try:
                nbtest=int(mot)
            except ValueError:
                pass
            print("nb test ",nbtest)  


 

