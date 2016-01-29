# -*- coding: Latin-1 -*-
#
# This file created Sept 14 2010 by Jim Kornelsen
#
# 13-Nov-10 JDK  Updated French translations for 1.0 release.
# 01-Apr-11 JDK  Added Spanish.  Localize dynamic labels and status messages.
# 22-Apr-11 JDK  Strings need to be unicode to handle accents correctly.
# 28-Oct-11 JDK  Finished Spanish and French for 1.2 release.
# 27-Feb-13 JDK  Can't modify dict in loop in python 3.3
# 11-Mar-13 JDK  Remove "Default" (use underlying name "Standard" instead).

"""
Handle localization of messages into French and Spanish.
Also gets the system locale and list of locales.

To maintain the translations dictionary, here is one approach:
1. Using Vim, change each entry in the dictionary into "eng" | "fr"
   Save as type .csv
2. Open in OOo Calc with | as delimiter.
   Sort by English, and delete duplicates.
3. Use Vim to change back into dictionary entries.

This module exports:
    theLocale
"""
import logging

from lingt.utils import util

logger = logging.getLogger("lingt.utils.locale")

# The system locale (instantiated after class definition).
theLocale = None

class Locale:
    """Call loadUnoObjs() before using getText()."""

    def __init__(self):
        self.unoObjs = None
        self.code = None  # two-letter ISO language code

    def loadUnoObjs(self, genericUnoObjs):
        """Initialize and get current OpenOffice locale."""
        if self.unoObjs:
            # Already loaded.
            return theLocale
        self.unoObjs = genericUnoObjs

        ## Get locale setting

        configProvider = self.unoObjs.smgr.createInstanceWithContext(
            "com.sun.star.configuration.ConfigurationProvider",
            self.unoObjs.ctx)
        args = (
            # trailing comma is required to make a tuple
            util.createProp("nodepath", "/org.openoffice.Setup/L10N"),
        )
        settings = configProvider.createInstanceWithArguments(
            "com.sun.star.configuration.ConfigurationAccess", args)
        OOLang = settings.getByName("ooLocale")
        self.code = OOLang[:2]  # grab first two characters
        logger.debug("locale = %s", self.code)

        ## Make the English key values case insensitive

        translationsLower = dict()
        for en in self.translations.keys():
            translationsLower[en.lower()] = self.translations[en]
        self.translations.update(translationsLower)
        return theLocale

    def getText(self, message_en):
        """Return L10N value.  If no translation is found for the current
        locale, returns the English message.
        """
        if message_en is None:
            return ""
        if self.code == "en":
            return message_en
        key = message_en.lower()
        if key in self.translations:
            phrase_translations = self.translations.get(key)
            message_other = phrase_translations.get(self.code)
            if message_other is not None and message_other != "":
                return message_other
        return message_en

    # ISO language codes used in struct com.sun.star.lang.Locale
    LANG_CODES = {
        'aa' : "Afar",
        'ab' : "Abkhazian",
        'af' : "Afrikaans",
        'am' : "Amharic",
        'ar' : "Arabic",
        'as' : "Assamese",
        'ay' : "Aymara",
        'az' : "Azerbaijani",
        'ba' : "Bashkir",
        'be' : "Byelorussian",
        'bg' : "Bulgarian",
        'bh' : "Bihari",
        'bi' : "Bislama",
        'bn' : "Bengali",
        'bo' : "Tibetan",
        'br' : "Breton",
        'ca' : "Catalan",
        'co' : "Corsican",
        'cs' : "Czech",
        'cy' : "Welsh",
        'da' : "Danish",
        'de' : "German",
        'dz' : "Bhutani",
        'el' : "Greek",
        'en' : "English",
        'eo' : "Esperanto",
        'es' : "Spanish",
        'et' : "Estonian",
        'eu' : "Basque",
        'fa' : "Persian",
        'fi' : "Finnish",
        'fj' : "Fiji",
        'fo' : "Faroese",
        'fr' : "French",
        'fy' : "Frisian",
        'ga' : "Irish",
        'gd' : "Scots Gaelic",
        'gl' : "Galician",
        'gn' : "Guarani",
        'gu' : "Gujarati",
        'ha' : "Hausa",
        'he' : "Hebrew",
        'hi' : "Hindi",
        'hr' : "Croatian",
        'hu' : "Hungarian",
        'hy' : "Armenian",
        'ia' : "Interlingua",
        'id' : "Indonesian",
        'ie' : "Interlingue",
        'ik' : "Inupiak",
        'is' : "Icelandic",
        'it' : "Italian",
        'iu' : "Inuktitut",
        'ja' : "Japanese",
        'jw' : "Javanese",
        'ka' : "Georgian",
        'kk' : "Kazakh",
        'kl' : "Greenlandic",
        'km' : "Cambodian",
        'kn' : "Kannada",
        'ko' : "Korean",
        'ks' : "Kashmiri",
        'ku' : "Kurdish",
        'ky' : "Kirghiz",
        'la' : "Latin",
        'ln' : "Lingala",
        'lo' : "Laothian",
        'lt' : "Lithuanian",
        'lv' : "Latvian",
        'mg' : "Malagasy",
        'mi' : "Maori",
        'mk' : "Macedonian",
        'ml' : "Malayalam",
        'mn' : "Mongolian",
        'mo' : "Moldavian",
        'mr' : "Marathi",
        'ms' : "Malay",
        'mt' : "Maltese",
        'my' : "Burmese",
        'na' : "Nauru",
        'ne' : "Nepali",
        'nl' : "Dutch",
        'no' : "Norwegian",
        'oc' : "Occitan",
        'om' : "Oromo (Afan)",
        'or' : "Oriya",
        'pa' : "Punjabi",
        'pl' : "Polish",
        'ps' : "Pashto, Pushto",
        'pt' : "Portuguese",
        'qu' : "Quechua",
        'rm' : "Rhaeto-Romance",
        'rn' : "Kirundi",
        'ro' : "Romanian",
        'ru' : "Russian",
        'rw' : "Kinyarwanda",
        'sa' : "Sanskrit",
        'sd' : "Sindhi",
        'sg' : "Sangho",
        'sh' : "Serbo-Croatian",
        'si' : "Sinhalese",
        'sk' : "Slovak",
        'sl' : "Slovenian",
        'sm' : "Samoan",
        'sn' : "Shona",
        'so' : "Somali",
        'sq' : "Albanian",
        'sr' : "Serbian",
        'ss' : "Siswati",
        'st' : "Sesotho",
        'su' : "Sundanese",
        'sv' : "Swedish",
        'sw' : "Swahili",
        'ta' : "Tamil",
        'te' : "Telugu",
        'tg' : "Tajik",
        'th' : "Thai",
        'ti' : "Tigrinya",
        'tk' : "Turkmen",
        'tl' : "Tagalog",
        'tn' : "Setswana",
        'to' : "Tonga",
        'tr' : "Turkish",
        'ts' : "Tsonga",
        'tt' : "Tatar",
        'tw' : "Twi",
        'ug' : "Uighur",
        'uk' : "Ukrainian",
        'ur' : "Urdu",
        'uz' : "Uzbek",
        'vi' : "Vietnamese",
        'vo' : "Volapuk",
        'wo' : "Wolof",
        'xh' : "Xhosa",
        'yi' : "Yiddish",
        'yo' : "Yoruba",
        'za' : "Zhuang",
        'zh' : "Chinese",
        'zu' : "Zulu"}

    def getLocaleList(self):
        """Returns a list of tuples with locale description and locale obj.
        This only shows a few locales set by the user, not a big list.
        """
        oLingu = self.unoObjs.smgr.createInstanceWithContext(
            "com.sun.star.linguistic2.LinguServiceManager",
            self.unoObjs.ctx)

        # css.linguistic2.Thesaurus, SpellChecker and Proofreader are allowed
        localeObjs = oLingu.getAvailableLocales(
            "com.sun.star.linguistic2.Thesaurus")

        descList = []
        for localeObj in localeObjs:
            desc = "%s (%s)" % (
                Locale.LANG_CODES[localeObj.Language], localeObj.Country)
            descList.append((desc, localeObj))
        return descList

    translations = {

        ## Dynamic labels in dialogs

        u"Back to Settings" : {
            'es' :
            u"Volver a la configuraci�n",
            'fr' :
            u"Atteindre la configuration",
        },
        u"Column" : {
            'es' :
            u"Columna",
            'fr' :
            u"Colonne",
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
        u"Get words" : {
            'es' :
            u"Obtener palabras",
            'fr' :
            u"Obtenir mots",
        },
        u"Go to Practice" : {
            'es' :
            u"Ir a la pr�ctica",
            'fr' :
            u"Atteindre exercices",
        },
        u"Make Empty List" : {
            'es' :
            u"Hacer una lista vac�a",
            'fr' :
            u"Cr�er liste vide",
        },
        u"Make List" : {
            'es' :
            u"Hacer una lista",
            'fr' :
            u"Cr�er liste",
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
            u"Practica de script",
            'fr' :
            u"Exercices d'�criture",
        },
        u"Script Practice - Settings" : {
            'es' :
            u"Practica de script - Configuraci�n",
            'fr' :
            u"Exercices d'�criture - Configuration",
        },
        u"Spelling" : {
            'es' :
            u"Ortograf�a",
            'fr' :
            u"V�rification d'orthographe",
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
        u"Word List and Spelling" : {
            'es' :
            u"Lista de palabras y ortograf�a",
            'fr' :
            u"Liste de mots et orthographe",
        },

        ## Localized text values

        u"(none)" : {
            'es' :
            u"(ninguno)",
            'fr' :
            u"(aucun)",
        },
        u"(cannot make word)" : {
            'es' :
            u"(no puede hacer la palabra)",
            'fr' :
            u"(impossible de cr�er mot)",
        },
        u"(Fallback Font)" : {
            'es' :
            u"(Fuente de Reserva)",
            'fr' :
            u"(Police de Remplacement)",
        },
        u"(no words found)" : {
            'es' :
            u"(no hay palabras encontradas)",
            'fr' :
            u"(aucun mot trouv�)",
        },
        u"Whole Document" : {
            'es' :
            u"Documento completo",
            'fr' :
            u"Document entier",
        },

        ## Status messages for ProgressBar

        u"Converting..." : {
            'es' :
            u"Convirtiendo...",
            'fr' :
            u"Conversion en cours...",
        },
        u"Finding text..." : {
            'es' :
            u"Buscando texto...",
            'fr' :
            u"Recherche de texte...",
        },
        u"Generating List..." : {
            'es' :
            u"Generando lista...",
            'fr' :
            u"Cr�ation de liste...",
        },
        u"Getting data..." : {
            'es' :
            u"Obteniendo datos...",
            'fr' :
            u"L�obtention des donn�es...",
        },
        u"Reading..." : {
            'es' :
            u"Leyendo...",
            'fr' :
            u"",
        },
        u"Saving file..." : {
            'es' :
            u"Guardando archivo...",
            'fr' :
            u"Enregistrement de fichier...",
        },
        u"Searching for occurrences..." : {
            'es' :
            u"Buscando ocurrencias...",
            'fr' :
            u"Recherche des occurrences...",
        },
        u"Sorting..." : {
            'es' :
            u"Ordenando...",
            'fr' :
            u"Triage...",
        },
        u"Loading data..." : {
            'es' :
            u"Cargando datos...",
            'fr' :
            u"Chargement des donn�es...",
        },

        ## Error messages

        u"%s is already in the list." : {
            'es' :
            u"%s ya est� en la lista.",
            'fr' :
            u"%s est d�j� dans la liste.",
        },
        u"Add '%s' as a new abbreviation?" : {
            'es' :
            u"Agregar '%s' como una abreviatura de nuevo?",
            'fr' :
            u"Ajouter '%s' comme nouvelle abr�viation?",
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
            u"Num�ro de r�f�rence %s introuvable.\n\nSuggestions\n%s",
        },
        u"Did not find any data in file %s" : {
            'es' :
            u"No ha encontrado ning�n dato en el archivo %s",
            'fr' :
            u"Aucune donn�e n'a �t� trouv�e dans le fichier %s",
        },
        u"Did not find any similar words." : {
            'es' :
            u"No encontr� algunas palabras similares.",
            'fr' :
            u"On n'a trouv� aucun mot similaire.",
        },
        u"Did not find any words for the list." : {
            'es' :
            u"No encontr� algunas palabras para la lista.",
            'fr' :
            u"On n'a trouv� aucun mot pour la liste.",
        },
        u"Did not find anything in column %s." : {
            'es' :
            u"No encontr� nada en la columna %s.",
            'fr' :
            u"On n'a rien trouv� dans colonne %s.",
        },
        u"Did not find scope of change." : {
            'es' :
            u"No ha encontrado el �mbito del cambio.",
            'fr' :
            u"L'�tendue de changement n'a pas �t� trouv�e.",
        },
        u"EncConverters does not seem to be installed properly." : {
            'es' :
            u"EncConverters no parece que se haya instalado correctamente.",
            'fr' :
            u"EncConverters semble �tre mal install�",
        },
        u"Error parsing %s user variable.  Please go to Insert -> Fields and "
        u"fix the problem." : {
            'es' :
            u"Error al analizar %s variable de usuario.  Por favor, vaya a "
            u"Insertar -> Campos y solucionar el problema.",
            'fr' :
            u"Erreur en analysant la variable utilisateur %s.  Veuillez "
            u"atteindre Insertion -> Champs pour r�soudre le probl�me.",
        },
        u"Error reading file %s" : {
            'es' :
            u"Error al leer el archivo %s",
            'fr' :
            u"Erreur en lisant le fichier %s",
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
        u"Error reading spreadsheet." : {
            'es' :
            u"Error al leer la hoja de c�lculo",
            'fr' :
            u"Erreur de lecture de classeur",
        },
        u"Error reading the list." : {
            'es' :
            u"Error al leer la lista.",
            'fr' :
            u"Erreur de lecture de liste.",
        },
        u"Error reading the list.\n\n%s" : {
            'es' :
            u"Error al leer la lista.\n\n%s",
            'fr' :
            u"Erreur de lecture de liste.\n\n%s",
        },
        u"Error writing to spreadsheet." : {
            'es' :
            u"Error al escribir al hoja de c�lculo.",
            'fr' :
            u"Erreur d'�criture de classeur.",
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
        u"Error: EncConverters returned %d%s." : {
            'es' :
            u"Error: EncConverters devolvi� %d%s.",
            'fr' :
            u"Erreur: EncConverters a r�pondu %d%s.",
        },
        u"Failed to encode string properly." : {
            'es' :
            u"No pudo codificar correctamente la cadena.",
            'fr' :
            u"Impossible d'encoder correctement la cha�ne.",
        },
        u"File does not seem to be from Toolbox or FieldWorks: %s" : {
            'es' :
            u"El archivo no parece ser del Toolbox o Fieldworks: %s",
            'fr' :
            u"Il semble que ce fichier n'a pas �t� cr�� par Toolbox ou "
            u"FieldWorks: %s",
        },
        u"File is already in the list." : {
            'es' :
            u"El archivo ya est� en la lista.",
            'fr' :
            u"Le fichier est d�j� dans la liste.",
        },
        u"Found %d similar words." : {
            'es' :
            u"Encontrado %d palabras similares.",
            'fr' :
            u"%d mots similaires trouv�s.",
        },
        u"Found %d words." : {
            'es' :
            u"Encontrado %d palabras.",
            'fr' :
            u"%d mots trouv�s.",
        },
        u"Found %d paragraphs and made %d change%s." : {
            'es' :
            u"Ha encontrado %d p�rrafos y hizo %d cambio%s.",
            'fr' :
            u"%d paragraphes trouv�s et %d changement%s faits.",
        },
        u"Found a ref number, but it must be in an outer table in order to "
        u"be updated." : {
            'es' :
            u"Ha encontrado un n�mero de referencia, pero debe estar en una "
            u"tabla de exterior para ser actualizados.",
            'fr' :
            u"N� de r�f.  trouv�, mais pour l'actualier il doit �tre dans un "
            u"cadre exterieur",
        },
        u"Frame style '%s' is missing" : {
            'es' :
            u"No se encuentra el estilo del marco '%s'",
            'fr' :
            u"Style de cadre '%s' introuvable",
        },
        u"If you want to use LIFT data, then first specify a LIFT file "
        u"exported from FieldWorks." : {
            'es' :
            u"Si desea utilizar los datos LIFT, en primer lugar especificar "
            u"un archivo LIFT exportados de Fieldworks.",
            'fr' :
            u"Pour utiliser des donn�es LIFT il faut sp�cifier un fichier "
            u"LIFT export� de FieldWorks.",
        },
        u"Library error: %s." : {
            'es' :
            u"Error de rutinas: %s.",
            'fr' :
            u"Erreur de logiciel: %s.",
        },
        u"Made %d change%s." : {
            'es' :
            u"Hizo %d cambio%s.",
            'fr' :
            u"%d changement%s faits.",
        },
        u"Made %d correction%s." : {
            'es' :
            u"Hizo %d correccione%s.",
            'fr' :
            u"On a fait %d correction%s.",
        },
        u"Made list of %d words." : {
            'es' :
            u"Hizo una lista de %d palabras.",
            'fr' :
            u"On a cr�� une liste de %d mots.",
        },
        u"Make this change?" : {
            'es' :
            u"�Hacer este cambio?",
            'fr' :
            u"Modifier ceci?",
        },
        u"Make this change?  (%s -> %s)" : {
            'es' :
            u"�Hacer este cambio?  (%s -> %s)",
            'fr' :
            u"Modifier ceci?  (%s -> %s)",
        },
        u"Missed word '%s'.  Keep going?" : {
            'es' :
            u"Hubo un problema con la palabra '%s'.  �Seguir adelante?",
            'fr' :
            u"Un probl�me en le mot '%s'.  Continuer?",
        },
        u"No changes, but modified style of %d paragraph%s." : {
            'es' :
            u"No hubo cambios, pero el estilo de %d p�rrafo%s se ha "
            u"modificado.",
            'fr' :
            u"Pas de changements, mais le style de %d paragraphe%s a �t� "
            u"chang�.",
        },
        u"No changes." : {
            'es' :
            u"No hubo cambios.",
            'fr' :
            u"Pas de changements.",
        },
        u"No converter was specified." : {
            'es' :
            u"No convertidor se ha especificado.",
            'fr' :
            u"Aucun convertisseur sp�cifi�.",
        },
        u"No data found." : {
            'es' :
            u"No se encontraron datos",
            'fr' :
            u"Aucune donn�e trouv�e.",
        },
        u"No locale was specified." : {
            'es' :
            u"Un locale no se ha especificado",
            'fr' :
            u"Aucuns param�tres r�gionaux sp�cifi�s.",
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
        u"No SF markers were specified.  Continue anyway?" : {
            'es' :
            u"Ning�n marcadores SFM fueron especificados.  �Desea continuar?",
            'fr' :
            u"Aucune balise SFM sp�cifi�e.  Continuer quand m�me?",
        },
        u"No spreadsheet is open." : {
            'es' :
            u"No hay ninguna hoja de c�lculo abierto.",
            'fr' :
            u"Aucun classeur est ouvert.",
        },
        u"No writing systems found." : {
            'es' :
            u"No se encontraron sistemas de escritura.",
            'fr' :
            u"Aucune syst�mes d'�criture trouv�e.",
        },
        u"No Xpath expressions were specified.  Continue anyway?" : {
            'es' :
            u"Ning�n expresiones XPath fueron especificadas.  "
            u"�Desea continuar?",
            'fr' :
            u"Aucune expression Xpath sp�cifi�e.  Continuer quand m�me?",
        },
        u"No text is selected." : {
            'es' :
            u"No hay texto seleccionado.",
            'fr' :
            u"Aucun texte s�lectionn�.",
        },
        u"Paragraph style '%s' is missing" : {
            'es' :
            u"No se encuentra el estilo de p�rrafo '%s'",
            'fr' :
            u"Style de paragraphe '%s' introuvable",
        },
        u"Please add a file to get words." : {
            'es' :
            u"Por favor, a�ada un archivo para obtener las palabras.",
            'fr' :
            u"Veuillez ajouter un fichier duquel on peut obtenir des mots.",
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
        u"Please enter a ref number.\n\nSuggestions\n%s" : {
            'es' :
            u"Por favor, introduzca un n�mero de referencia."
            u"\n\nSugerencias\n%s",
            'fr' :
            u"Veuillez entrer un num�ro de r�f�rence.\n\nSuggestions\n%s",
        },
        u"Please enter a value for column width." : {
            'es' :
            u"Por favor, introduzca un valor para el ancho de la columna.",
            'fr' :
            u"Veuillez entrer la largeur de colonne.",
        },
        u"Please go to Grammar Settings and specify a file." : {
            'es' :
            u"Por favor, vaya a la Configuraci�n de gram�tica y especifique "
            u"un archivo.",
            'fr' :
            u"Veuillez choisir un fichier dans Configuration de grammaire.",
        },
        u"Please go to Phonology Settings and specify a file." : {
            'es' :
            u"Por favor, vaya a la Configuraci�n de fonolog�a y especifique "
            u"un archivo.",
            'fr' :
            u"Veuillez sp�cifier un fichier dans Configuration de phonologie.",
        },
        u"Please load a word list by clicking on the Files... button.  When "
        u"file settings are finished, click Get words." : {
            'es' :
            u"Por favor, cargue una lista de palabras haciendo clic en el "
            u"bot�n Archivos.  Cuando la configuraci�n de archivo se haya "
            u"terminado, haga clic en Obtener palabras.",
            'fr' :
            u"Veuillez charger une liste de mots en cliquant sur Fichiers...  "
            u"Apr�s avoir fait la configuration de fichier",
        },
        u"Please open one or more documents to search." : {
            'es' :
            u"Por favor, abrir uno o m�s documentos para la b�squeda.",
            'fr' :
            u"Veuillez ouvrir un ou plusieurs documents � rechercher.",
        },
        u"Please save the current document first." : {
            'es' :
            u"Por favor, primero guarde el documento actual.",
            'fr' :
            u"Veuillez enregistrer d'abord le document actuel.",
        },
        u"Please save the spreadsheet first." : {
            'es' :
            u"Por favor, primero guarde la hoja de c�lculo.",
            'fr' :
            u"Veuillez d'abord enregistrer le classeur",
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
        u"Please select a language name." : {
            'es' :
            u"Por favor, seleccione un nombre de idioma.",
            'fr' :
            u"Veuillez s�lectionner un nom de langue.",
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
        u"Please select a paragraph style." : {
            'es' :
            u"Por favor, seleccione un estilo de p�rrafo.",
            'fr' :
            u"Veuillez choisir un style de paragraphe.",
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
        u"Please select an abbreviation in the list." : {
            'es' :
            u"Por favor, seleccione una abreviatura de la lista.",
            'fr' :
            u"Veuillez choisir une abr�viation dans la liste.",
        },
        u"Please select an item in the list." : {
            'es' :
            u"Por favor, seleccione un elemento de la lista.",
            'fr' :
            u"Veuillez choisir un �l�ment dans la liste.",
        },
        u"Please select or enter something to find." : {
            'es' :
            u"Por favor seleccione o escriba algo para buscar.",
            'fr' :
            u"Veuillez s�lectionner ou saisir quelque chose � rechercher.",
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
        u"Please specify a file to export." : {
            'es' :
            u"Por favor, especifique un archivo para exportar.",
            'fr' :
            u"Veuillez sp�cifier un fichier � exporter.",
        },
        u"Please specify a row between 2 and %d." : {
            'es' :
            u"Por favor, especifica una fila entre 2 y %d.",
            'fr' :
            u"Veuillez sp�cifier une ligne entre 2 et %d.",
        },
        u"Please specify a scope." : {
            'es' :
            u"Por favor, especifique un �mbito.",
            'fr' :
            u"Veuillez sp�cifier l'�tendue.",
        },
        u"Please specify a target." : {
            'es' :
            u"Por favor, especifique un destino.",
            'fr' :
            u"Veuillez sp�cifier un cible.",
        },
        u"Please specify a word list file.  To make a new empty list, go to "
        u"Word List and Spelling and then save the spreadsheet file." : {
            'es' :
            u"Por favor, especifique un archivo de una lista de palabras.  "
            u"Para crear una nueva lista vac�a, vaya a Lista de palabras y "
            u"ortograf�a y guarde el archivo de hoja de c�lculo.",
            'fr' :
            u"Veuillez sp�cifier un fichier de liste de mots.  Pour cr�er une "
            u"nouvelle liste vide, atteindre Liste de mots et orthographe, "
            u"puis enregistrer le classeur.",
        },
        u"Replaced %d example%s." : {
            'es' :
            u"reemplazado %d ejemplo%s.",
            'fr' :
            u"%d exemple%s a �t� remplas�.",
        },
        u"Some words could not be converted." : {
            'es' :
            u"Algunas palabras no se pueden convertir.",
            'fr' :
            u"Impossible de convertir certains mots",
        },
        u"Spell check finished." : {
            'es' :
            u"Spell check finished.",
            'fr' :
            u"V�rification d'orthographe termin�e.",
        },
        u"Successfully finished conversion." : {
            'es' :
            u"Terminado con �xito la conversi�n.",
            'fr' :
            u"Conversion termin�e avec succ�s.",
        },
        u"System error: Unable to get UNO object." : {
            'es' :
            u"Error del sistema: No se puede obtener objeto UNO.",
            'fr' :
            u"Erreur de syst�me�: Impossible d'acc�der � l'objet UNO.",
        },
        u"The cursor cannot be in a header or footer." : {
            'es' :
            u"El cursor no puede estar en un encabezado o en un pie de "
            u"p�gina.",
            'fr' :
            u"Le curseur ne peut pas se trouver dans un en-t�te ou dans un "
            u"pied de page.",
        },
        u"The cursor cannot be inside a table or frame." : {
            'es' :
            u"El cursor no puede estar dentro de una tabla o un marco.",
            'fr' :
            u"Le curseur ne peut pas se trouver dans un tableau ou dans un "
            u"cadre.",
        },
        u"There do not seem to be any examples to insert." : {
            'es' :
            u"No parece haber ning�n ejemplo para insertar.",
            'fr' :
            u"Il semble qu'il n'existe pas d'exemples � ins�rer.",
        },
        u"There was a problem while writing the list.\n\n%s" : {
            'es' :
            u"Hubo un problema al escribir la lista.\n\n%s",
            'fr' :
            u"Un probl�me est survenu en �crivant la liste.\n\n%s",
        },
        u"This document stores %s settings.  "
        u"Please leave it open while using %s.  "
        u"If you want to keep the settings to use again later, "
        u"then save this document." : {
            'es' :
            u"Este documento guarda la configuraci�n de %s.  "
            u"Por favor, dejarlo abierto durante el uso de %s.  "
            u"Si desea mantener la configuraci�n para utilizarlo m�s "
            u"adelante, guarde este documento.",
            'fr' :
            u"Ce document contient la configuration de la fonction %s.  "
            u"Veuillez le laisser ouvert en utilisant %s.  "
            u"Pour garder la configuration afin de la r�utiliser plus tard, "
            u"enregistrer ce document.",
        },
        u"This expression is already in the list." : {
            'es' :
            u"Esta expresi�n est� ya en la lista.",
            'fr' :
            u"Cette expression est d�j� dans la liste.",
        },
        u"This will change the case of the entire list from '%s' to '%s.' "
        u"Continue?" : {
            'es' :
            u"Esto cambiar� el caso de la lista completa de '%s' a '%s'.  "
            u"�Desea continuar?",
            'fr' :
            u"Ceci changera la casse de toute la liste de '%s' � '%s'.  "
            u"Continuer?",
        },
        u"To update examples, 'Outer table' must be marked in Grammar "
        u"Settings." : {
            'es' :
            u"'Tabla de exterior' debe estar en la Configuraci�n de "
            u"gram�tica.",
            'fr' :
            u"'Cadre exterieur' doit �tre dans Configuration de grammaire.",
        },
        u"Unexpected file type %s" : {
            'es' :
            u"Tipo de archivo inesperado %s",
            'fr' :
            u"Type de fichier %s inattendu",
        },
        u"Unexpected font type %s." : {
            'es' :
            u"Tipo de fuente inesperada %s.",
            'fr' :
            u"Police de type %s inattendue.",
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
        u"Update all examples now?  It is recommended to save a copy of your "
        u"document first." : {
            'es' :
            u"�Actualizar todos los ejemplos ahora?  Se recomienda que "
            u"primero guarde una copia de su documento.",
            'fr' :
            u"Actualiser tous les exemples maintenant?  Il est conseill� "
            u"d'enregistrer le document d'abord.",
        },
        u"Updated '%s' %d times in a row.  Keep going?" : {
            'es' :
            u"Actualizado '%s' %d veces seguidas.  �Seguir adelante?",
            'fr' :
            u"'%s' a �t� actualis� %d fois de suite.  Continuer?",
        },
        u"Updated %d example%s." : {
            'es' :
            u"Actualizado %d ejemplo%s.",
            'fr' :
            u"%d exemple%s a �t� actualis�.",
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
        u"'Whole Document' must be the only thing to find." : {
            'es' :
            u"'Documento Completo' debe ser la �nica cosa para buscar.",
            'fr' :
            u"'Document entier' doit �tre la seule chose � rechercher",
        },
        u"You did not specify anything to find.  Continue anyway?" : {
            'es' :
            u"No ha especificado nada que encontrar.  �Desea continuar?",
            'fr' :
            u"Vous n'avez sp�cifier aucune chose � rechercher.  Continuer "
            u"quand m�me?",
        },
    }

theLocale = Locale()

