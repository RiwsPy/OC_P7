STOP_WORDS = {
    "a", "abord", "absolument", "afin", "ah", "ai", "aie", "ailleurs",
    "ainsi", "ait", "allaient", "allo", "allons", "allô", "alors", "anterieur",
    "anterieure", "anterieures", "apres", "après", "as",
    "assez", "attendu", "au",
    "aucun", "aucune", "aujourd", "aujourd'hui", "aupres", "auquel", "aura",
    "auraient", "aurait", "auront", "aussi", "autre", "autrefois", "autrement",
    "autres", "autrui", "aux", "auxquelles", "auxquels", "avaient", "avais",
    "avait", "avant", "avec", "avoir", "avons", "ayant",
    "b", "bah", "bas", "basee",
    "bat", "beau", "beaucoup", "bien", "bigre", "boum",
    "bravo", "brrr", "c", "car",
    "ce", "ceci", "cela", "celle", "celle-ci", "celle-là",
    "celles", "celles-ci",
    "celles-là", "celui", "celui-ci", "celui-là", "cent",
    "cependant", "certain",
    "certaine", "certaines", "certains", "certes", "ces",
    "cet", "cette", "ceux",
    "ceux-ci", "ceux-là", "chacun", "chacune", "chaque",
    "cher", "chers", "chez",
    "chiche", "chut", "chère", "chères", "ci", "cinq", "cinquantaine",
    "cinquante", "cinquantième", "cinquième", "clac",
    "clic", "combien", "comme",
    "comment", "comparable", "comparables", "compris", "concernant", "contre",
    "couic", "crac", "d", "da", "dans", "de", "debout",
    "dedans", "dehors", "deja",
    "delà", "depuis", "dernier", "derniere", "derriere", "derrière", "des",
    "desormais", "desquelles", "desquels", "dessous", "dessus", "deux",
    "deuxième", "deuxièmement", "devant", "devers", "devra", "different",
    "differentes", "differents", "différent", "différente", "différentes",
    "différents", "dire", "directe", "directement", "dit", "dite", "dits",
    "divers", "diverse", "diverses", "dix", "dix-huit", "dix-neuf", "dix-sept",
    "dixième", "doit", "doivent", "donc", "dont", "douze", "douzième", "dring",
    "du", "duquel", "durant", "dès", "désormais", "e", "effet", "egale",
    "egalement", "egales", "eh", "elle", "elle-même", "elles", "elles-mêmes",
    "en", "encore", "enfin", "entre", "envers", "environ", "es", "est", "et",
    "etant", "etc", "etre", "eu", "euh", "eux", "eux-mêmes", "exactement",
    "excepté", "extenso", "exterieur", "f", "fais", "faisaient", "faisant",
    "fait", "façon", "feront", "fi", "flac", "floc",
    "font", "g", "gens", "h", "ha",
    "hein", "hem", "hep", "hi", "ho", "holà", "hop",
    "hormis", "hors", "hou", "houp",
    "hue", "hui", "huit", "huitième", "hum", "hurrah",
    "hé", "hélas", "i", "il",
    "ils", "importe", "j", "je", "jusqu", "jusque", "juste", "k", "l", "la",
    "laisser", "laquelle", "las", "le", "lequel", "les",
    "lesquelles", "lesquels",
    "leur", "leurs", "longtemps", "lors", "lorsque", "lui",
    "lui-meme", "lui-même",
    "là", "lès", "m", "ma", "maint", "maintenant", "mais", "malgre", "malgré",
    "maximale", "me", "meme", "memes", "merci", "mes",
    "mien", "mienne", "miennes",
    "miens", "mille", "mince", "minimale", "moi", "moi-meme", "moi-même",
    "moindres", "moins", "mon", "moyennant", "multiple", "multiples", "même",
    "mêmes", "n", "na", "naturel", "naturelle", "naturelles"
    "ne", "neanmoins",
    "necessaire", "necessairement", "neuf", "neuvième", "ni", "nombreuses",
    "nombreux", "non", "nos", "notamment", "notre", "nous", "nous-mêmes",
    "nouveau", "nul", "néanmoins", "nôtre", "nôtres", "o", "oh", "ohé", "ollé",
    "olé", "on", "ont", "onze", "onzième", "ore", "ou", "ouf", "ouias", "oust",
    "ouste", "outre", "ouvert", "ouverte", "ouverts", "o|", "où", "p", "paf",
    "pan", "par", "parce", "parfois", "parle", "parlent", "parler", "parmi",
    "parseme", "partant", "particulier", "particulière", "particulièrement",
    "pas", "passé", "pendant", "pense", "permet", "personne", "peu", "peut",
    "peuvent", "peux", "pff", "pfft", "pfut", "pif", "pire", "plein", "plouf",
    "plus", "plusieurs", "plutôt", "possessif", "possessifs", "possible",
    "possibles", "pouah", "pour", "pourquoi", "pourrais", "pourrait",
    "pouvait", "prealable", "precisement", "premier", "première",
    "premièrement", "pres", "probable", "probante", "procedant", "proche",
    "près", "psitt", "pu", "puis", "puisque", "pur",
    "pure", "q", "qu", "quand",
    "quant", "quant-à-soi", "quanta", "quarante", "quatorze", "quatre",
    "quatre-vingt", "quatrième", "quatrièmement", "que", "quel", "quelconque",
    "quelle", "quelles", "quelqu'un", "quelque", "quelques", "quels", "qui",
    "quiconque", "quinze", "quoi", "quoique", "r", "rare", "rarement", "rares",
    "relative", "relativement", "remarquable", "rend", "rendre", "restant",
    "reste", "restent", "restrictif", "retour", "revoici", "revoilà", "rien",
    "s", "sa", "sacrebleu", "sait", "sans", "sapristi", "sauf", "se", "sein",
    "seize", "selon", "semblable", "semblaient", "semble", "semblent",
    "sent", "sept", "septième", "sera", "seraient", "serait", "seront", "ses",
    "seul", "seule", "seulement", "si", "sien",
    "sienne", "siennes", "siens",
    "sinon", "six", "sixième", "soi", "soi-même",
    "soit", "soixante", "son",
    "sont", "sous", "souvent", "specifique",
    "specifiques", "speculatif", "stop",
    "strictement", "subtiles", "suffisant",
    "suffisante", "suffit", "suis",
    "suit", "suivant", "suivante", "suivantes",
    "suivants", "suivre",
    "superpose", "sur", "surtout", "t", "ta", "tac",
    "tant", "tardive", "te",
    "tel", "telle", "tellement", "telles", "tels",
    "tenant", "tend", "tenir",
    "tente", "tes", "tic", "tien", "tienne",
    "tiennes", "tiens", "toc", "toi",
    "toi-même", "ton", "touchant", "toujours", "tous",
    "tout", "toute",
    "toutefois", "toutes", "treize", "trente", "tres",
    "trois", "troisième",
    "troisièmement", "trop", "très", "tsoin", "tsouin",
    "tu", "té", "u", "un",
    "une", "unes", "uniformement", "unique", "uniques",
    "uns", "v", "va", "vais",
    "vas", "vers", "via", "vif", "vifs", "vingt", "vivat",
    "vive", "vives", "vlan",
    "voici", "voilà", "vont", "vos", "votre", "vous",
    "vous-mêmes", "vu", "vé",
    "vôtre", "vôtres", "w", "x", "y", "z", "zut", "à",
    "â", "ça", "ès", "étaient",
    "étais", "était", "étant", "été", "être", "ô"
    }

SKIP_WORDS = {
    "salut", "hello", "grandpy", "connais", "bonjour", "bonsoir",
    "papy", "bot", "pybot",
    "dis", "adresse", "hey", "hi", "grandma", "indiquer",
    "trouver", "plait", "sais",
    }

NO_POSITION = \
    "Quoi ? Je n'ai pas compris, peux-tu répéter plus fort ?"
NO_GOOGLE = \
    "Oulala, il y a quelque chose que cloche par ici."
NO_WIKI = \
    "Je ne connais pas cet endroit, il faudrait que tu m'y emmènes !"
NO_WIKI_INFO = \
    "Oui, oui j'ai déjà entendu parlé de cet endroit \
mais ma mémoire n'est plus ce qu'elle était..."
I_HAVE_THE_RESPONSE = "Voici l'adresse : "

from random import choice


class Sentence:
    BEGIN = [
        "Ha oui... Cela me rappelle le jour où c'est",
        "Je crois pas que tu connaisses l'histoire de",
        "Hoo... Je pourrais aussi bien te conter l'épopée de",
        "Tu connais la dernière ? Il paraît que c'est",
        "Fichtre, tout cela me rappelle l'époque où je vadrouillais avec",
        "Sacrebleu, ça me fait penser à",
        "Saperlipopette, j'y suis déjà allé avec",
        "Cela fait une paye dis donc, t'ai-je raconté l'aventure avec",
        "Rappelle moi de te raconter l'histoire incroyable de",
    ]

    NICKNAME = [
        "Mursul",
        "Fil",
        "Maxou",
        "Mart",
        "Bébert",
        "Ulysse",
        "Sasha",
        "Eden",
        "Scratchy",
        "Missy",
        "Barbe-blanche",
        "Lyn",
        "Leone",
        "Piggy",
        "Murphy",
        "Rover",
        "Al",
        "Claude",
        "Dominique",
        "Lou",
        "Ange",
        "Charlie",
    ]

    JOB = [
        "- le boulanger pas la factrice -",
        "- la factrice pas le boulanger -",
        "- le voisin du 78 un peu étrange -",
        "- l'ancienne voisine un peu étrange -",
        "- dont je n'arrive plus à me souvenir du visage -",
        "- la 8ème personne la plus dingue que je n'ai jamais rencontré -",
        "- personne ne la revu depuis la grande Dépression -",
        "- un chat noir comme on n'en fait plus -",
        "- tu l'as rencontré une fois quand tu étais enfant -",
        "- le tigre domestique du 4ème -",
        "- une éléphante de compagnie -",
        "- un hamster tout mignon -",
        "- ha ! j'en ris rien que d'y penser -",
    ]

    VERB = [
        "qui a conquis",
        "qui a dressé",
        "qui a pelé",
        "qui a enfilé",
        "qui a perdu",
        "qui a grimpé",
        "qui a découvert",
        "qui a dévoré",
        "qui a allumé",
        "qui a lustré",
    ]

    COMPLEMENT = [
        "sa bague de fiançaille...",
        "son os à ronger...",
        "une chaîne de vélo...",
        "la noirceur du coeur des Hommes...",
        "au 7ème Ciel...",
        "une salopette devant le Président...",
        "un brasier ardent...",
        "un slip usagé...",
        "un extraterrestre...",
        "un véritable trésor de pirate...",
        "l'amour de toute une vie...",
        "ses chaussures en direct...",
    ]

    @classmethod
    def create_random_sentence(cls) -> str:
        """
            Generates a sentence by randomly selecting a word in each list
        """
        return ' '.join((
            choice(cls.BEGIN),
            choice(cls.NICKNAME),
            choice(cls.JOB),
            choice(cls.VERB),
            choice(cls.COMPLEMENT)))
