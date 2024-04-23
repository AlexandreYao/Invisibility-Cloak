import cv2
import numpy as np

# Fonction pour soustraire l'arrière-plan de l'objet avec effet de transparence
def invisibility_effect(frame, background):
    # Convertir l'image de l'objet et l'arrière-plan en images en niveaux de gris
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
    
    # Soustraire l'arrière-plan de l'image de l'objet
    diff = cv2.absdiff(gray_frame, gray_background)
    
    # Appliquer un seuil pour obtenir un masque binaire
    _, mask = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    
    # Appliquer un flou gaussien à l'image de l'objet
    blurred_frame = cv2.GaussianBlur(frame, (15, 15), 0)
    
    # Inverser le masque
    mask_inv = cv2.bitwise_not(mask)
    
    # Remplacer les pixels de l'objet par ceux de l'arrière-plan flouté
    result = cv2.bitwise_and(blurred_frame, blurred_frame, mask=mask_inv)
    
    return result

# Capture vidéo à partir de la webcam
cap = cv2.VideoCapture(0)

# Capture de l'image de fond lorsque l'utilisateur appuie sur la touche "c"
print("Appuyez sur 'c' pour capturer l'image de fond...")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow('Background Capture', frame)
    
    # Sortir de la boucle si la touche 'c' est enfoncée
    if cv2.waitKey(1) & 0xFF == ord('c'):
        _, background = cap.read()
        break

# Fermer la fenêtre de capture de fond
cv2.destroyAllWindows()

# Demande à l'utilisateur d'appuyer sur une touche pour commencer
input("Appuyez sur une touche pour commencer...")

while True:
    # Lire le frame actuel de la webcam
    ret, frame = cap.read()
    if not ret:
        break
    
    # Appliquer l'effet d'invisibilité avec effet de transparence
    invisible_frame = invisibility_effect(frame, background)
    
    # Afficher le frame résultant
    cv2.imshow('Invisibility Effect', invisible_frame)
    
    # Sortir de la boucle si la touche 'q' est enfoncée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources et fermer les fenêtres
cap.release()
cv2.destroyAllWindows()
