# Fichier de configuration pour le générateur de documentation Sphinx.  
# 
# Ce fichier ne contient qu'une sélection des options les plus courantes.  Pour un plein 
# list voir la documentation:  
# https://www.sphinx-doc.org/en/master/usage/configuration.html 

# - Configuration du chemin --------------------------------------------- -----------------  

# Si les extensions (ou modules à documenter avec autodoc) sont dans un autre répertoire,  
# ajoutez ces répertoires à sys.path ici.  Si le répertoire est relatif au  
# racine de la documentation, utilisez os.path.abspath pour le rendre absolu, comme illustré ici.  
# 
# import os 
# import sys  
# sys.path.insert (0, os.path.abspath ('.'))  


# -- Renseignements sur le projet --------------------------------------------- --------  

project   =   'Doc-logiciel'  
copyright   =   '2021, Aurelien BURET'  
author   =   'Aurélien BURET'  

# La version complète, y compris les balises alpha / beta / rc 
release   =   '1.0.0'  


# - Configuration générale --------------------------------------------- ------ 

# Ajoutez les noms de modules d'extension Sphinx ici, sous forme de chaînes.  Ils peuvent être 
# extensions fournies avec Sphinx (nommées 'sphinx.ext. *') ou votre 
# nous.  
extensions   =   [  
	'sphinx.ext.githubpages' , 
	'recommonmark',
	"sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode"
]  

source_suffix    =    ".rst"  
master_doc       =    "index"  



# Ajoutez ici tous les chemins contenant des modèles, relatifs à ce répertoire.  
templates_path   = [ '_templates' ] 

# Le langage du contenu généré automatiquement par Sphinx.  Se référer à la documentation  
# pour une liste des langues prises en charge. 
# 
# Ceci est également utilisé si vous effectuez une traduction de contenu via des catalogues gettext.  
# Habituellement, vous définissez "language" à partir de la ligne de commande pour ces cas.  
language   =   'fr'  

# Liste des modèles, relatifs au répertoire source, qui correspondent aux fichiers et  
# répertoires à ignorer lors de la recherche de fichiers source.  
# Ce modèle affecte également html_static_path et html_extra_path.  
exclude_patterns   = [ '_build' , 'Thumbs.db' , '.DS_Store' ] 


# - Options pour la sortie HTML ------------------------------------------- ------  

# Le thème à utiliser pour les pages d'aide HTML et HTML.  Voir la documentation pour  
# une liste de thèmes intégrés.  
# 
html_theme = "furo"

# Ajoutez ici tous les chemins contenant des fichiers statiques personnalisés (tels que des feuilles de style),  
# relatif à ce répertoire.  Ils sont copiés après les fichiers statiques intégrés,  
# donc un fichier nommé "default.css" écrasera le "default.css" intégré.  
html_static_path   = [ '_static' ]