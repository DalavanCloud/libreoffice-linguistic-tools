#!/usr/bin/python
# -*- coding: Latin-1 -*-

# Locale.py
#              
# Change History:
#   Created Sept 14 2010 by Jim Kornelsen
#
#   13-Nov-10 JDK  Updated French translations for 1.0 release.
#   01-Apr-11 JDK  Added Spanish.  Localize dynamic labels and status messages.
#   22-Apr-11 JDK  Strings need to be unicode to handle accents correctly.
#   28-Oct-11 JDK  Finished Spanish and French for 1.2 release.

"""
Handle L10N: localization of messages into French, Spanish

To maintain the translations dictionary, here is one approach:
1. Using Vim, change each entry in the dictionary into "eng" | "fr"
   Save as type .csv
2. Open in OOo Calc with | as delimiter.
   Sort by English, and delete duplicates.
3. Use Vim to change back into dictionary entries.
"""

import logging
from lingt.Utils import Utils

class Locale:
    def __init__(self, unoObjs):
        """Initialize and get current OOo locale."""
        self.logger = logging.getLogger("lingt.Utils.Locale")

        ## Get locale setting

        configProvider = unoObjs.smgr.createInstanceWithContext(
            "com.sun.star.configuration.ConfigurationProvider", unoObjs.ctx)
        args = (
            # trailing comma is required to make a tuple
            Utils.createProp("nodepath", "/org.openoffice.Setup/L10N"),
        )
        settings = configProvider.createInstanceWithArguments(
                   "com.sun.star.configuration.ConfigurationAccess", args)
        OOLang = settings.getByName("ooLocale")
        self.locale = OOLang[:2]  # grab first two characters
        self.logger.debug("locale = " + Utils.safeStr(self.locale))

        ## Make the English key values case insensitive

        for en in self.translations.keys():
            self.translations[en.lower()] = self.translations[en]

    def getText(self, message_en):
        """Return L10N value.  If no translation is found for the current
        locale, returns the English message.
        """
        if message_en is None:
            return ""
        if self.locale == "en":
            return message_en
        key = message_en.lower()
        if self.translations.has_key(key):
            phrase_translations = self.translations.get(key)
            message_other = phrase_translations.get(self.locale)
            if message_other is not None and message_other != "":
                return message_other
        return message_en

    translations = {

        ## Dynamic labels in dialogs

        u"Back to Settings" : {
            'es' :
            u"Volver a la configuraci�n",
            'fr' :
            u"Atteindre la configuration",
        },
        u"Get Phonology Examples" : {
            'es' :
            u"Obtener ejemplos de fonolog�a",
            'fr' :
            u"Obtenir des exemples de phonologie",
        },
        u"Get Interlinear Grammar Examples" : {
            'es' :
            u"Obtener ejemplos de gram�tica",
            'fr' :
            u"Obtenir des exemples de grammaire",
        },
        u"Go to Practice" : {
            'es' :
            u"Ir a la pr�ctica",
            'fr' :
            u"Atteindre exercices",
        },
        u"Replace with Example" : {
            'es' :
            u"Reemplazar con ejemplo",
            'fr' :
            u"Remplacer par exemple",
        },
        u"Replace All" : {
            'es' :
            u"Reemplazar todo",
            'fr' :
            u"Remplacer tout",
        },
        u"Script Practice" : {
            'es' :
            "Practica de script",
            'fr' :
            "Exercices d'�criture",
        },
        u"Script Practice - Settings" : {
            'es' :
            "Practica de script - Configuraci�n",
            'fr' :
            "Exercices d'�criture - Configuration",
        },
        u"Update Example" : {
            'es' :
            u"Actualizar el ejemplo",
            'fr' :
            u"Mettre l'exemple � jour",
        },
        u"Update All" : {
            'es' :
            u"Actualizar todos",
            'fr' :
            u"Tout mettre � jour",
        },

        ## Localized text values

        u"(none)" : {
            'es' :
            u"(ninguno)",
            'fr' :
            u"(aucun)",
        },
        u"Default" : {      # the built-in default style name
            'es' :
            u"Predeterminado",
            'fr' :
            u"Standard",
        },
        u"(cannot make word)" : {
            'es' :
            u"(no puede hacer la palabra)",
            'fr' :
            u"(impossible de cr�er mot)",
        },
        u"(no words found)" : {
            'es' :
            u"(no hay palabras encontradas)",
            'fr' :
            u"(aucun mot trouv�)",
        },

        ## Status messages for ProgressBar

        u"Converting..." : {
            'es' :
            u"Convirtiendo...",
            'fr' :
            u"Conversion en cours...",
        },
        u"Searching for occurrences..." : {
            'es' :
            u"Buscando ocurrencias...",
            'fr' :
            u"Recherche des occurrences...",
        },
        u"Loading data..." : {
            'es' :
            u"Cargando datos...",
            'fr' :
            u"Chargement des donn�es...",
        },

        ## Error messages

        u"Add '%s' as a new abbreviation?" : {
            'es' :
            u"Agregar '%s' como una abreviatura de nuevo?",
            'fr' :
            u"Ajouter '%s' comme nouvelle abr�viation ?",
        },
        u"Cannot be in a header or footer." : {
            'es' :
            u"No puede ser en un encabezado o un pie de p�gina.",
            'fr' :
            u"Interdit dans un en-t�te ou pied de page.",
        },
        u"Cannot be inside a table or frame." : {
            'es' :
            u"No se puede estar dentro de una tabla o un marco.",
            'fr' :
            u"Interdit dans un tableau ou cadre",
        },
        u"Cannot find file %s" : {
            'es' :
            u"No se puede encontrar el archivo %s",
            'fr' :
            u"Impossible de trouver le fichier %s",
        },
        u"Cannot insert text here." : {
            'es' :
            u"No se puede insertar texto aqu�.",
            'fr' :
            u"Impossible d'ins�rer texte ici.",
        },
        u"Character style '%s' is missing" : {
            'es' :
            u"No se encuentra el estilo de car�cter '%s'",
            'fr' :
            u"Style de caract�re '%s' introuvable",
        },
        u"Column width is not a number." : {
            'es' :
            u"El ancho de columna no es un n�mero.",
            'fr' :
            u"La largeur de colonne n'est pas un nombre.",
        },
        u"Converting..." : {
            'es' :
            u"Conversi�n en proceso...",
            'fr' :
            u"Conversion en cours...",
        },
        u"Could not find ref number %s" : {
            'es' :
            u"No se encuentra el n�mero de referencia %s",
            'fr' :
            u"Num�ro de r�f�rence %s introuvable.",
        },
        u"Could not find ref number %s\n\nSuggestions\n%s" : {
            'es' :
            u"No se encuentra el n�mero de referencia %s\n\nSugerencias\n%s",
            'fr' :
            u"Num�ro de r�f�rence %s introuvable. Suggestion(s)�: %s",
        },
        u"Did not find any data in file %s" : {
            'es' :
            u"No ha encontrado ning�n dato en el archivo %s",
            'fr' :
            u"Aucune donn�e n'a �t� trouv�e dans le fichier %s",
        },
        u"Did not find scope of change." : {
            'es' :
            u"No ha encontrado el �mbito del cambio.",
            'fr' :
            u"L'�tendue de changement n'a pas �t� trouv�e.",
        },
        u"Error parsing %s user variable. Please go to Insert -> Fields and " +
        u"fix the problem." : {
            'es' :
            u"Error al analizar %s variable de usuario. Por favor, vaya a " +
            u"Insertar -> Campos y solucionar el problema.",
            'fr' :
            u"Erreur en analysant la variable utilisateur %s. Veuillez " +
            u"atteindre Insertion -> Champs pour r�soudre le probl�me.",
        },
        u"Error reading file %s\n\n%s" : {
            'es' :
            u"Error al leer el archivo %s\n\n%s",
            'fr' :
            u"Erreur en lisant le fichier %s\n\n%s",
        },
        u"Error with file: %s" : {
            'es' :
            u"Error con el archivo: %s",
            'fr' :
            u"Erreur de fichier : %s",
        },
        u"Error: Could not create dialog." : {
            'es' :
            u"Error: No se pudo crear el di�logo.",
            'fr' :
            u"Erreur : Impossible de cr�er dialogue.",
        },
        u"Error: Could not show dialog window." : {
            'es' :
            u"Error: No se pudo mostrar el cuadro de di�logo.",
            'fr' :
            u"Erreur : Impossible d'afficher dialogue.",
        },
        u"File does not seem to be from Toolbox or FieldWorks: %s" : {
            'es' :
            u"El archivo no parece ser del Toolbox o Fieldworks: %s",
            'fr' :
            u"Il semble que ce fichier n'a pas �t� cr�� par Toolbox ou " +
            u"FieldWorks: %s",
        },
        u"File is already in the list." : {
            'es' :
            u"El archivo ya est� en la lista.",
            'fr' :
            u"Le fichier est d�j� dans la liste.",
        },
        u"Found %d paragraphs and made %d change(s)." : {
            'es' :
            u"Ha encontrado %d p�rrafos y hizo %d cambio(s).",
            'fr' :
            u"%d paragraphes trouv�s et %d changements faits.",
        },
        u"Found a ref number, but it must be in an outer table in order to " +
        u"be updated." : {
            'es' :
            u"Ha encontrado un n�mero de referencia, pero debe estar en una " +
            u"tabla de exterior para ser actualizados.",
            'fr' :
            u"N� de r�f. trouv�, mais pour l'actualier il doit �tre dans un " +
            u"cadre exterieur",
        },
        u"Frame style '%s' is missing" : {
            'es' :
            u"No se encuentra el estilo del marco '%s'",
            'fr' :
            u"Style de cadre '%s' introuvable",
        },
        u"If you want to use LIFT data, then first specify a LIFT file " +
        u"exported from FieldWorks." : {
            'es' :
            u"Si desea utilizar los datos LIFT, en primer lugar especificar " +
            u"un archivo LIFT exportados de Fieldworks.",
            'fr' :
            u"Pour utiliser des donn�es LIFT il faut sp�cifier un fichier " +
            u"LIFT export� de FieldWorks.",
        },
        u"Made %d changes." : {
            'es' :
            u"%d cambios realizados",
            'fr' :
            u"%d changements faits.",
        },
        u"No changes, but modified style of %d paragraph(s)." : {
            'es' :
            u"No hubo cambios, pero el estilo de %d p�rrafo(s) se ha " +
            u"modificado.",
            'fr' :
            u"Pas de changements, mais le style de %d paragraphes a �t� " +
            u"chang�.",
        },
        u"No changes." : {
            'es' :
            u"No hubo cambios.",
            'fr' :
            u"Pas de changements.",
        },
        u"No more existing examples found." : {
            'es' :
            u"No se ha encontrado m�s ejemplos existentes",
            'fr' :
            u"Il n'y a plus d'exemples trouv�s.",
        },
        u"No more possible abbreviations found." : {
            'es' :
            u"No se ha encontrado m�s abreviaturas posibles",
            'fr' :
            u"On ne trouve plus des abr�viations possibles.",
        },
        u"No more reference numbers found." : {
            'es' :
            u"No se ha encontrado m�s n�meros de referencia",
            'fr' :
            u"On ne trouve plus des num�ros de r�f�rence.",
        },
        u"No text is selected." : {
            'es' :
            u"No hay texto seleccionado.",
            'fr' :
            u"Aucun texte s�lectionn�. ",
        },
        u"Paragraph style '%s' is missing" : {
            'es' :
            u"No se encuentra el estilo de p�rrafo '%s'",
            'fr' :
            u"Style de paragraphe '%s' introuvable",
        },
        u"Please do not select individual table cells." : {
            'es' :
            u"Por favor, no seleccione las celdas individuales de la tabla.",
            'fr' :
            u"Veuillez ne pas choisir des cellules individuelles.",
        },
        u"Please enter a number for max length." : {
            'es' :
            u"Por favor, introduzca un n�mero para la longitud m�xima.",
            'fr' :
            u"Veuillez entrer la longueur maximum.",
        },
        u"Please enter a ref number." : {
            'es' :
            u"Por favor, introduzca un n�mero de referencia.",
            'fr' :
            u"Veuillez entrer un num�ro de r�f�rence.",
        },
        u"Please enter a value for column width." : {
            'es' :
            u"Por favor, introduzca un valor para el ancho de la columna.",
            'fr' :
            u"Veuillez entrer la largeur de colonne.",
        },
        u"Please go to Grammar Settings and specify a file." : {
            'es' :
            u"Por favor, vaya a la Configuraci�n de gram�tica y especifique " +
            u"un archivo.",
            'fr' :
            u"Veuillez choisir un fichier dans Configuration de grammaire.",
        },
        u"Please go to Phonology Settings and specify a file." : {
            'es' :
            u"Por favor, vaya a la Configuraci�n de fonolog�a y especifique " +
            u"un archivo.",
            'fr' :
            u"Veuillez sp�cifier un fichier dans Configuration de phonologie.",
        },
        u"Please select a converter." : {
            'es' :
            u"Por favor, seleccione un convertidor.",
            'fr' :
            u"Veuillez choisir un convertisseur.",
        },
        u"Please select a file in the list." : {
            'es' :
            u"Por favor, seleccione un archivo en la lista.",
            'fr' :
            u"Veuillez choisir un fichier dans la liste.",
        },
        u"Please select a scope character style." : {
            'es' :
            u"Por favor, seleccione un estilo de car�cter �mbito.",
            'fr' :
            u"Veuillez choisir un style de caract�re pour l'�tendue.",
        },
        u"Please select a scope font." : {
            'es' :
            u"Por favor, seleccione una fuente �mbito.",
            'fr' :
            u"Veuillez choisir une police pour l'�tendue.",
        },
        u"Please select a scope paragraph style." : {
            'es' :
            u"Por favor, seleccione un estilo de p�rrafo �mbito.",
            'fr' :
            u"Veuillez choisir un style de paragraphe pour l'�tendue.",
        },
        u"Please select a script." : {
            'es' :
            u"Por favor, seleccione un script.",
            'fr' :
            u"Veuillez choisir un �criture.",
        },
        u"Please select a target font." : {
            'es' :
            u"Por favor, seleccione una fuente destino.",
            'fr' :
            u"Veuillez choisir une police cible.",
        },
        u"Please select a target style." : {
            'es' :
            u"Por favor, seleccione un estilo destino.",
            'fr' :
            u"Veuillez choisir un style cible.",
        },
        u"Please select an item in the list." : {
            'es' :
            u"Por favor, seleccione un elemento de la lista.",
            'fr' :
            u"Veuillez choisir un �l�ment dans la liste.",
        },
        u"Please select the converter again." : {
            'es' :
            u"Por favor, seleccione el convertidor de nuevo.",
            'fr' :
            u"Veuillez choisir encore le convertisseur.",
        },
        u"Please specify SFMs." : {
            'es' :
            u"Por favor, especifique los SFMs.",
            'fr' :
            u"Veuillez sp�cifier les balises (SFMs).",
        },
        u"Please specify a scope." : {
            'es' :
            u"Por favor, especifique un �mbito.",
            'fr' :
            u"Veuillez sp�cifier l'�tendue.",
        },
        u"Searching for occurrences..." : {
            'es' :
            u"Buscando ocurrencias...",
            'fr' :
            u"Recherche des occurrences...",
        },
        u"System error: Unable to get UNO object." : {
            'es' :
            u"Error del sistema: No se puede obtener objeto UNO.",
            'fr' :
            u"Erreur de syst�me�: Impossible d'acc�der � l'objet UNO.",
        },
        u"The cursor cannot be in a header or footer." : {
            'es' :
            u"El cursor no puede estar en un encabezado o en un pie de p�gina.",
            'fr' :
            u"Le curseur ne peut pas se trouver dans un en-t�te ou dans un " +
            u"pied de page.",
        },
        u"The cursor cannot be inside a table or frame." : {
            'es' :
            u"El cursor no puede estar dentro de una tabla o un marco.",
            'fr' :
            u"Le curseur ne peut pas se trouver dans un tableau ou dans un " +
            u"cadre.",
        },
        u"There do not seem to be any examples to insert." : {
            'es' :
            u"No parece haber ning�n ejemplo para insertar.",
            'fr' :
            u"Il semble qu'il n'existe pas d'exemples � ins�rer.",
        },
        u"This will change the case of the entire list from '%s' to '%s.' " +
        u"Continue?" : {
            'es' :
            u"Esto cambiar� el caso de la lista completa de '%s' a '%s'. " +
            u"�Desea continuar?",
            'fr' :
            u"Ceci changera la casse de toute la liste de '%s' � '%s'. " +
            u"Continuer ?",
        },
        u"Unexpected file type %s" : {
            'es' :
            u"Tipo de archivo inesperado %s",
            'fr' :
            u"Type de fichier %s inattendu",
        },
        u"Unexpected new value %s." : {
            'es' :
            u"Nuevo valor inesperado %s.",
            'fr' :
            u"Nouvelle valeur inattendue %s.",
        },
        u"Unexpected value %s" : {
            'es' :
            u"Valor inesperado %s.",
            'fr' :
            u"Valeur inattendue %s",
        },
        u"Unknown file type for %s" : {
            'es' :
            u"Tipo de archivo desconocido para %s",
            'fr' :
            u"Type de fichier inconnu pour %s",
        },
        u"Update all examples now?  It is recommended to save a copy of your " +
        u"document first." : {
            'es' :
            u"�Actualizar todos los ejemplos ahora?  Se recomienda que " +
            u"primero guarde una copia de su documento.",
            'fr' :
            u"Actualiser tous les exemples maintenant ? Il est conseill� " +
            u"d'enregistrer le document d'abord.",
        },
        u"Updated '%s' %d times in a row. Keep going?" : {
            'es' :
            u"Actualizado '%s' %d veces seguidas. �Seguir adelante?",
            'fr' :
            u"'%s' a �t� actualis� %d fois de suite. Continuer ?",
        },
        u"Value %d for column width is too high." : {
            'es' :
            u"El valor de %d para el ancho de columna es demasiado alta.",
            'fr' :
            u"%d est trop grande comme largeur de colonne.",
        },
        u"Value for column width must be more than zero." : {
            'es' :
            u"El valor para el ancho de columna debe ser mayor de cero.",
            'fr' :
            u"La largeur de colonne doit �tre sup�rieure � z�ro.",
        },
    }
