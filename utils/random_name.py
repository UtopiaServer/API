from random import randint, choice
 
class FantasyNameGenerator(object):
    """
        Random fantasy name generator
    """
 
    # on déclare les lettres, leurs positions voulues dans le nom
    # et un poids de fréquence d'apparition
 
    # voyelles
    VOWELS = (
        (('start', 'middle', 'end'), (
                (5, ("a", "e", "i", "o", "u")),
                (1, ("ae", "ai", "ao", "au", "aa", "ea", "eo", "eu", "ee", "ia",
                     "io", "iu", "ii", "oa", "oe", "oi", "ou", "oo", "eau", "y"))
        )),
        (('middle'), (
            (1, ("'",)),
        ))
    )
 
    # consonnes
    CONSONANTS = (
        (('start', 'middle', 'end'), (
                (3, ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p",
                     "r", "s", "t", "v", "w")),
                (1, ("x", "y", "z", "sc", "ch", "gh", "ph", "sh", "th", "sk", "wk", "st"))
        )),
        (('middle', 'end'), (
                (1, ("ck", "nk", "rk", "ss")),
        )),
        (('start', 'middle'), (
                (2, ("br", "dr", "fr", "gr", "kr", )),
                (1, ("cr", "pr", "sr", "tr", "qu", "wh", "cl", "fl", "gl", "kl",
                     "ll", "pl", "sl", "str"))
        )),
    )
 
    # on génère deux listes de type ((lettre, position), (lettre, position)...)
    # pour pouvoir piocher au hasard dedans
    SYLLABLES_POOL = [[], []]
 
    for i, group in enumerate((VOWELS, CONSONANTS)):
        pool = SYLLABLES_POOL[i]
        for place, pack in group:
            for frequency, letters in pack:
                for letter in letters:
                    pool.extend(((letter, set(place)),) * frequency)
 
 
    def __init__(self, min_syllable=2, max_syllable=None):
        self.min_syllable = min_syllable
        self.max_syllable = max_syllable or (min_syllable + 2)
 
    def __iter__(self):
        # juste pour le plaisir d'avoir le générateur itérable
        while True:
            yield self.get_new_name()
 
    # générer un nom avec les réglages de l'instance
    def get_new_name(self):
        return self.generate_name(self.min_syllable, self.max_syllable)
 
    @classmethod
    def generate_name(cls, min_syllable, max_syllable, base=""):
 
        # méthode pour générer un nom à indépendament de l'instance
 
        # on génère aléatoirement la taille du mot et le son de départ
        length, pool = randint(min_syllable, max_syllable), randint(0, 1)
 
        # pour chaque syllabe, on en choppe une au hasard et on change de pool
        # si la syllable n'est pas à la bonne place, on tire à nouveau
        for i in range(1, length + 1):
 
            while True:
 
                letter, place = choice(cls.SYLLABLES_POOL[pool])
 
                if i == 1:
                    if 'start' not in place:
                        continue
                elif i == length:
                    if 'end' not in place:
                        continue
                else:
                    if 'middle' not in place:
                        continue
 
                base += letter
                pool = abs(pool - 1)
                break
 
        return base.title()