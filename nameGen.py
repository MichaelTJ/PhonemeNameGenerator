from random import randint, random

class phenome:
    def __init__(self, id, IPASymbol, graphemes, Examples, Voiced, Sharpness, roughness,
                 Sound_Location):
        self.id = id
        self.IPASymbol = IPASymbol
        self.graphemes = graphemes
        self.examples = Examples.split(", ")
        self.voiced = Voiced
        self.sharpness = Sharpness
        # self.Common = Common
        self.roughness = roughness
        # self.Cleanliness = Cleanliness
        self.sound_location = Sound_Location

class Grapheme:
    def __init__(self, id, spelling, example, rule, frequency):
        self.id = id
        self.spelling = spelling
        self.example = example
        self.rule = rule
        self.frequency = frequency

allPhenomes = []
allGraphemes = []

def initGraphemes():
    allGraphemes.append(Grapheme(25, "a", "At", "Closed syllable", 4192))
    allGraphemes.append(Grapheme(25, "a-e", "dAncE", "", 147))
    allGraphemes.append(Grapheme(26, "a", "Agent", "Open syllable", 1002))
    allGraphemes.append(Grapheme(26, "a-e", "AtE", "Final E", 790))
    allGraphemes.append(Grapheme(26, "ai", "rAIn", "AI digraph", 208))
    allGraphemes.append(Grapheme(26, "ay", "dAY", "AY digraph", 131))
    allGraphemes.append(Grapheme(26, "eigh", "EIGHt", "", 18))
    allGraphemes.append(Grapheme(26, "e", "cafE", "", 16))
    allGraphemes.append(Grapheme(26, "ea", "brEAk", "", 14))
    allGraphemes.append(Grapheme(26, "ei", "vEIl", "", 14))
    allGraphemes.append(Grapheme(26, "ey", "thEY", "", 14))
    allGraphemes.append(Grapheme(40, "a(r)", "Arm", "AR digraph", 474))
    allGraphemes.append(Grapheme(40, "a", "fAther", "", 44))
    allGraphemes.append(Grapheme(40, "ar-e", "lARgE", "", 31))
    allGraphemes.append(Grapheme(40, "ea(r)", "hEArt", "", 18))
    allGraphemes.append(Grapheme(39, "ar", "vARy", "", 64))
    allGraphemes.append(Grapheme(39, "are", "cARE", "", 50))
    allGraphemes.append(Grapheme(39, "air", "fAIR", "", 46))
    allGraphemes.append(Grapheme(39, "ere", "thERE", "", 31))
    allGraphemes.append(Grapheme(39, "ear", "bEAR", "", 13))
    allGraphemes.append(Grapheme(27, "e", "End", "Closed syllable", 3316))
    allGraphemes.append(Grapheme(27, "ea", "hEAd", "", 139))
    allGraphemes.append(Grapheme(27, "e-e", "fEncE", "", 79))
    allGraphemes.append(Grapheme(28, "e", "mE", "Open syllable", 1765))
    allGraphemes.append(Grapheme(28, "y", "verY", "Final Y", 1801))
    allGraphemes.append(Grapheme(28, "ee", "kEEp", "EE digraph", 249))
    allGraphemes.append(Grapheme(28, "ea", "EAt", "EA digraph", 245))
    allGraphemes.append(Grapheme(28, "e-e", "thEsE", "Final E", 62))
    allGraphemes.append(Grapheme(28, "ie", "fIEld", "", 62))
    allGraphemes.append(Grapheme(28, "i-e", "polIcE", "", 44))
    allGraphemes.append(Grapheme(28, "ey", "monEY", "", 40))
    allGraphemes.append(Grapheme(28, "i", "unIque", "", 38))
    allGraphemes.append(Grapheme(28, "ea-e", "pEAcE", "", 30))
    allGraphemes.append(Grapheme(28, "ie-e", "pIEcE", "", 23))
    allGraphemes.append(Grapheme(28, "ei", "cEIling", "", 16))
    allGraphemes.append(Grapheme(29, "i", "In", "Closed syllable", 5346))
    allGraphemes.append(Grapheme(29, "i-e", "gIvE", "", 339))
    allGraphemes.append(Grapheme(29, "a-e", "villAgE", "", 187))
    allGraphemes.append(Grapheme(29, "y", "sYstem", "", 100))
    allGraphemes.append(Grapheme(29, "ui", "bUIld", "", 16))
    allGraphemes.append(Grapheme(29, "ai", "captAIn", "", 15))
    allGraphemes.append(Grapheme(29, "ei", "forEIgn", "", 11))
    allGraphemes.append(Grapheme(30, "i-e", "IcE", "Final E", 555))
    allGraphemes.append(Grapheme(30, "i", "Item", "Open syllable", 554))
    allGraphemes.append(Grapheme(30, "y", "mY", "Final Y", 211))
    allGraphemes.append(Grapheme(30, "igh", "fIGHt", "", 88))
    allGraphemes.append(Grapheme(30, "ie", "pIE", "", 26))
    allGraphemes.append(Grapheme(30, "y-e", "tYpE", "", 23))
    allGraphemes.append(Grapheme(31, "o", "nOt", "Closed syllable", 1558))
    allGraphemes.append(Grapheme(31, "a", "whAt", "", 80))
    allGraphemes.append(Grapheme(31, "o-e", "lOdgE", "", 20))
    allGraphemes.append(Grapheme(32, "o", "Open", "Open syllable", 1876))
    allGraphemes.append(Grapheme(32, "o-e", "hOmE", "Final E", 370))
    allGraphemes.append(Grapheme(32, "oa", "OAt", "OA digraph", 126))
    allGraphemes.append(Grapheme(32, "ow", "OWn", "OW digraph", 124))
    allGraphemes.append(Grapheme(32, "ou", "mOUld", "", 29))
    allGraphemes.append(Grapheme(32, "oe", "tOE", "", 13))
    allGraphemes.append(Grapheme(32, "ou-e", "cOUrsE", "", 10))
    allGraphemes.append(Grapheme(42, "o(r)", "fOr", "R modified", 312))
    allGraphemes.append(Grapheme(42, "a", "All, war", "A before L&R", 165))
    allGraphemes.append(Grapheme(42, "au", "AUto", "AU digraph", 146))
    allGraphemes.append(Grapheme(42, "o", "dOg", "", 123))
    allGraphemes.append(Grapheme(42, "aw", "AWful", "AW digraph", 75))
    allGraphemes.append(Grapheme(42, "o-e", "hOrsE", "", 17))
    allGraphemes.append(Grapheme(42, "ough", "bOUGHt", "", 15))
    allGraphemes.append(Grapheme(42, "augh", "cAUGHt", "", 12))
    allGraphemes.append(Grapheme(33, "u", "pUll", "", 200))
    allGraphemes.append(Grapheme(33, "oo", "lOOk", "OO digraph - short", 114))
    allGraphemes.append(Grapheme(33, "o", "wOman", "", 17))
    allGraphemes.append(Grapheme(33, "u-e", "sUrE", "", 11))
    allGraphemes.append(Grapheme(36, "oi", "OIl", "OI digraph", 92))
    allGraphemes.append(Grapheme(36, "oy", "tOY", "OY digraph", 48))
    allGraphemes.append(Grapheme(37, "ou", "OUt", "OU digraph", 227))
    allGraphemes.append(Grapheme(37, "ow", "OWl", "OW digraph", 119))
    allGraphemes.append(Grapheme(38, "o", "Other", "important schwa", 1723))
    allGraphemes.append(Grapheme(38, "u", "Up", "closed syllable", 1509))
    allGraphemes.append(Grapheme(38, "a", "Ago", "important schwa", 1438))
    allGraphemes.append(Grapheme(38, "i", "anImal", "important schwa", 1347))
    allGraphemes.append(Grapheme(38, "e", "Effect", "important schwa", 763))
    allGraphemes.append(Grapheme(38, "ou", "dOUble", "", 366))
    allGraphemes.append(Grapheme(38, "o", "sOn", "", 112))
    allGraphemes.append(Grapheme(38, "e-e", "violEncE", "", 101))
    allGraphemes.append(Grapheme(38, "o-e", "sOmE", "", 47))
    allGraphemes.append(Grapheme(38, "u-e", "hUgE", "", 46))
    allGraphemes.append(Grapheme(38, "o", "dO", "", 37))
    allGraphemes.append(Grapheme(38, "y", "oxYgen", "", 23))
    allGraphemes.append(Grapheme(38, "ie", "patIEnt", "", 22))
    allGraphemes.append(Grapheme(38, "eo", "pidgEOn", "", 10))
    allGraphemes.append(Grapheme(38, "oo-e", "lOOsE", "", 12))
    allGraphemes.append(Grapheme(35, "u", "Unit", "Open syllable", 907))
    allGraphemes.append(Grapheme(35, "u-e", "tUnE", "Final E", 290))
    allGraphemes.append(Grapheme(35, "oo", "mOOn", "OO digraph - long", 173))
    allGraphemes.append(Grapheme(35, "ew", "nEW", "EW digraph", 60))
    allGraphemes.append(Grapheme(35, "ou", "yOU", "", 29))
    allGraphemes.append(Grapheme(35, "eu", "nEUtral", "", 28))
    allGraphemes.append(Grapheme(35, "ue", "blUE", "UE digraph", 27))
    allGraphemes.append(Grapheme(35, "oo-e", "gOOsE", "", 12))
    allGraphemes.append(Grapheme(35, "o-e", "mOvE", "", 12))
    allGraphemes.append(Grapheme(41, "er", "hER", "regular ER", 1979))
    allGraphemes.append(Grapheme(41, "or", "labOR", "regular OR", 321))
    allGraphemes.append(Grapheme(41, "ur", "tURn", "regular UR", 234))
    allGraphemes.append(Grapheme(41, "ar", "dollAR", "regular AR", 168))
    allGraphemes.append(Grapheme(41, "ir", "gIRl", "regular IR", 104))
    allGraphemes.append(Grapheme(41, "er-e", "nERvE", "", 41))
    allGraphemes.append(Grapheme(41, "ear", "EARth", "", 29))
    allGraphemes.append(Grapheme(41, "our", "jOURney", "", 21))
    #These added manually - not fequentenough in normal words
    allGraphemes.append(Grapheme(34, "u", "lUg", "", 5))
    allGraphemes.append(Grapheme(34, "oo", "blOOD", "", 5))
    allGraphemes.append(Grapheme(43, "ear", "EAR", "", 5))
    allGraphemes.append(Grapheme(43, "eer", "stEER", "", 5))
    allGraphemes.append(Grapheme(43, "ere", "hERE", "", 5))
    allGraphemes.append(Grapheme(44, "ure", "cURE", "", 5))

   #Consonants
    allGraphemes.append(Grapheme(1, "b", "Boy", "", 2242))
    allGraphemes.append(Grapheme(1, "bb", "raBBit", "", 63))
    allGraphemes.append(Grapheme(19, "ch", "CHild", "", 313))
    allGraphemes.append(Grapheme(19, "t", "picTure", "", 175))
    allGraphemes.append(Grapheme(19, "tch", "caTCH", "", 61))
    allGraphemes.append(Grapheme(19, "ti", "quesTIon", "", 13))
    allGraphemes.append(Grapheme(2, "d", "Dog", "", 3611))
    allGraphemes.append(Grapheme(2, "dd", "aDD", "", 74))
    allGraphemes.append(Grapheme(3, "f", "Fox", "", 1580))
    allGraphemes.append(Grapheme(3, "ph", "PHone", "", 242))
    allGraphemes.append(Grapheme(3, "ff", "cliFF", "", 177))
    allGraphemes.append(Grapheme(4, "g", "Girl", "", 1178))
    allGraphemes.append(Grapheme(4, "gg", "eGG", "", 67))
    allGraphemes.append(Grapheme(4, "gue", "leaGUE", "", 21))
    allGraphemes.append(Grapheme(4, "gu", "Guard", "", 19))
    allGraphemes.append(Grapheme(4, "gh", "GHost", "", 10))
    allGraphemes.append(Grapheme(5, "h", "Hot", "", 762))
    allGraphemes.append(Grapheme(6, "g", "Gem", "", 647))
    allGraphemes.append(Grapheme(6, "j", "Jump", "", 218))
    allGraphemes.append(Grapheme(6, "dge", "loDGE", "", 51))
    allGraphemes.append(Grapheme(6, "d", "eDucate", "", 32))
    allGraphemes.append(Grapheme(6, "gi", "leGIon", "", 14))
    allGraphemes.append(Grapheme(7, "c", "Cat", "", 3452))
    allGraphemes.append(Grapheme(7, "k", "Kind", "", 601))
    allGraphemes.append(Grapheme(7, "ck", "baCK", "", 290))
    allGraphemes.append(Grapheme(7, "ch", "CHord", "", 142))
    allGraphemes.append(Grapheme(7, "cc", "aCCount", "", 76))
    allGraphemes.append(Grapheme(7, "que", "uniQUE", "", 19))
    allGraphemes.append(Grapheme(7, "x", "foX", "", 245))
    allGraphemes.append(Grapheme(7, "cs", "physiCS", "", 26))
    allGraphemes.append(Grapheme(7, "x", "eXam", "", 43))
    allGraphemes.append(Grapheme(7, "qu", "QUick", "", 191))
    allGraphemes.append(Grapheme(8, "l", "Like", "", 4894))
    allGraphemes.append(Grapheme(8, "le", "abLE", "", 620))
    allGraphemes.append(Grapheme(8, "ll", "beLL", "", 489))
    allGraphemes.append(Grapheme(8, "el", "novEL", "", 19))
    allGraphemes.append(Grapheme(9, "m", "Man", "", 3302))
    allGraphemes.append(Grapheme(9, "mm", "coMMute", "", 140))
    allGraphemes.append(Grapheme(9, "mb", "laMB", "", 27))
    allGraphemes.append(Grapheme(9, "lm", "caLM", "", 17))
    allGraphemes.append(Grapheme(10, "n", "Nose", "", 7452))
    allGraphemes.append(Grapheme(10, "en", "dozEN", "", 128))
    allGraphemes.append(Grapheme(10, "nn", "fuNNy", "", 127))
    allGraphemes.append(Grapheme(10, "kn", "KNife", "", 41))
    allGraphemes.append(Grapheme(10, "on", "lessON", "", 41))
    allGraphemes.append(Grapheme(10, "gn", "siGN", "", 32))
    allGraphemes.append(Grapheme(23, "ng", "siNG", "", 362))
    allGraphemes.append(Grapheme(23, "n", "thiNk", "", 251))
    allGraphemes.append(Grapheme(11, "p", "Pig", "", 3296))
    allGraphemes.append(Grapheme(11, "pp", "haPPy", "", 153))
    allGraphemes.append(Grapheme(12, "r", "Rail", "", 9134))
    allGraphemes.append(Grapheme(12, "rr", "caRRy", "", 207))
    allGraphemes.append(Grapheme(12, "wr", "WRite", "", 48))
    allGraphemes.append(Grapheme(12, "rh", "RHythm", "", 16))
    allGraphemes.append(Grapheme(13, "s", "Sat", "", 4599))
    allGraphemes.append(Grapheme(13, "c", "City", "", 1067))
    allGraphemes.append(Grapheme(13, "ss", "paSS", "", 442))
    allGraphemes.append(Grapheme(13, "ps", "PSychology", "", 19))
    allGraphemes.append(Grapheme(20, "sh", "SHoe", "", 398))
    allGraphemes.append(Grapheme(20, "tion", "acTION", "", 820))
    allGraphemes.append(Grapheme(20, "ci", "speCIal", "", 119))
    allGraphemes.append(Grapheme(20, "ssi", "miSSIon", "", 51))
    allGraphemes.append(Grapheme(20, "si", "tenSIon", "", 38))
    allGraphemes.append(Grapheme(20, "ch", "CHef", "", 34))
    allGraphemes.append(Grapheme(20, "ti", "paTIent", "", 30))
    allGraphemes.append(Grapheme(20, "s", "Sugar", "", 20))
    allGraphemes.append(Grapheme(14, "t", "Toy", "", 7528))
    allGraphemes.append(Grapheme(14, "tt", "coTTon", "", 216))
    allGraphemes.append(Grapheme(14, "ed", "hookED", "", 28))
    allGraphemes.append(Grapheme(14, "bt", "douBT", "", 11))
    allGraphemes.append(Grapheme(21, "th", "THank", "", 411))
    allGraphemes.append(Grapheme(22, "th", "leaTHer", "", 10))
    allGraphemes.append(Grapheme(21, "th", "THey", "", 149))
    allGraphemes.append(Grapheme(15, "v", "Very", "", 1485))
    allGraphemes.append(Grapheme(16, "w", "With", "", 578))
    allGraphemes.append(Grapheme(16, "u", "sUite", "", 47))
    allGraphemes.append(Grapheme(16, "wh", "WHen", "", 89))
    allGraphemes.append(Grapheme(24, "y", "Yard", "", 53))
    allGraphemes.append(Grapheme(24, "i", "onIon", "", 66))
    allGraphemes.append(Grapheme(17, "z", "Zero", "", 229))
    allGraphemes.append(Grapheme(17, "s", "hiS", "", 640))
    allGraphemes.append(Grapheme(17, "es", "wivES", "", 44))
    allGraphemes.append(Grapheme(17, "zz", "jaZZ", "", 23))
    allGraphemes.append(Grapheme(17, "ss", "deSSert", "", 13))
    allGraphemes.append(Grapheme(18, "si", "eroSIon", "", 55))
    allGraphemes.append(Grapheme(18, "s", "meaSure", "", 34))
    allGraphemes.append(Grapheme(18, "g", "massaGe", "", 15))

def getGraphemes(num):
    output = []
    for x in allGraphemes:
        if x.id == num:
            output.append(x)
    return output


def initPhenomes():
    # id	IPASymbol	Graphemes	Examples	Voiced?	Sharpness	Common	roughness	Cleanliness	Sound Location
    allPhenomes.append(phenome(1, "b", getGraphemes(1),
                               "bug, bubble", "Yes",
                               7, 3, 1))
    allPhenomes.append(phenome(2, "d", getGraphemes(2),
                               "dad, add, milled", "Yes",
                               6, 3, 3))
    allPhenomes.append(phenome(3, "f", getGraphemes(3),
                               "fat, cliff, phone, enough, half, often", "No",
                               1, 1, 1))
    allPhenomes.append(phenome(4, "g", getGraphemes(4),
                               "gun, egg, ghost, guest, prologue", "Yes",
                               7, 6, 9))
    allPhenomes.append(phenome(5, "h", getGraphemes(5),
                               "hop, who", "No",
                               3, 2, 5))
    allPhenomes.append(phenome(6, "dʒ", getGraphemes(6),
                               "jam, wage, giraffe, edge, soldier, exaggerate", "Yes",
                               6, 6, 2))
    allPhenomes.append(phenome(7, "k", getGraphemes(7),
                               "kit, cat, chris, accent, folk, bouquet, queen, rack, box",
                               "No", 9, 8, 4))
    allPhenomes.append(phenome(8, "l", getGraphemes(8),
                               "live, well", "Yes",
                               3, 1, 3))
    allPhenomes.append(phenome(9, "m", getGraphemes(9),
                               "man, summer, comb, column, palm", "Yes",
                               2, 1, 1))
    allPhenomes.append(phenome(10, "n", getGraphemes(10),
                               "net, funny, know, gnat, pneumonic", "Yes",
                               2, 1, 3))
    allPhenomes.append(phenome(11, "p", getGraphemes(11),
                               "pin, dippy", "No",
                               6, 4, 1))
    allPhenomes.append(phenome(12, "r", getGraphemes(12),
                               "run, carrot, wrench, rhyme", "Yes",
                               5, 6, 4))
    allPhenomes.append(phenome(13, "s", getGraphemes(13),
                               "sit, less, circle, scene, psycho, listen, pace, course", "No",
                               3, 6, 3))
    allPhenomes.append(phenome(14, "t", getGraphemes(14),
                               "tip, matter, thomas, ripped", "No",
                               10, 6, 3))
    allPhenomes.append(phenome(15, "v", getGraphemes(15),
                               "vine, of, stephen, five", "Yes",
                               5, 6, 1))
    allPhenomes.append(phenome(16, "w", getGraphemes(16),
                               "wit, why, quick, choir", "Yes",
                               3, 3, 1))
    allPhenomes.append(phenome(17, "z", getGraphemes(17),
                               "zed, buzz, his, scissors, xylophone, craze", "Yes",
                               4, 8, 3))
    allPhenomes.append(phenome(18, "ʒ", getGraphemes(18),
                               "treasure, division, azure", "Yes",
                               4, 7, 3))
    allPhenomes.append(phenome(19, "tʃ", getGraphemes(19),
                               "chip, watch, future, action, righteous", "No",
                               8, 9, 4))
    allPhenomes.append(phenome(20, "ʃ", getGraphemes(20),
                               "sham, ocean, sure, special, pension, machine, conscience, station", "No",
                               5, 7, 4))
    allPhenomes.append(phenome(21, "θ", getGraphemes(21),
                               "thongs", "No",
                               6, 5, 3))
    allPhenomes.append(phenome(22, "ð", getGraphemes(22),
                               "leather", "Yes",
                               4, 4, 4))
    allPhenomes.append(phenome(23, "ŋ", getGraphemes(23),
                               "ring, pink, tongue", "Yes",
                               5, 4, 6))
    allPhenomes.append(phenome(24, "j", getGraphemes(24),
                               "you, onion, hallelujah", "Yes",
                               3, 2, 5))
    allPhenomes.append(phenome(25, "æ", getGraphemes(25),
                               "cat, plaid, laugh", "Yes",
                               5, 6, 6))
    allPhenomes.append(phenome(26, "eɪ", getGraphemes(26),
                               "bay, maid, weigh, straight, pay, foyer, filet, eight, gauge, mate, break, they", "Yes",
                               5, 5, 7))
    allPhenomes.append(phenome(27, "e", getGraphemes(27),
                               "end, bread, bury, friend, said, many, leopard, heifer, aesthetic", "Yes",
                               5, 3, 5))
    allPhenomes.append(phenome(28, "i:", getGraphemes(28),
                               "be, bee, meat, lady, key, phoenix, grief, ski, deceive, people, quay", "Yes",
                               5, 6, 6))
    allPhenomes.append(phenome(29, "ɪ", getGraphemes(29),
                               "it, england, women, busy, guild, gym, sieve", "Yes",
                               5, 6, 5))
    allPhenomes.append(phenome(30, "aɪ", getGraphemes(30),
                               "spider, sky, night, pie, guy, stye, aisle, island, height, kite", "Yes",
                               5, 5, 6))
    allPhenomes.append(phenome(31, "ɒ", getGraphemes(31),
                               "swan, honest, maul, slaw, fought", "Yes",
                               5, 3, 7))
    allPhenomes.append(phenome(32, "oʊ", getGraphemes(32),
                               "open, moat, bone, toe, sow, dough, beau, brooch, sew", "Yes",
                               5, 4, 8))
    allPhenomes.append(phenome(33, "ʊ", getGraphemes(33),
                               "wolf, look, bush, would", "Yes",
                               5, 2, 9))
    allPhenomes.append(phenome(34, "ʌ", getGraphemes(34),
                               "lug, monkey, blood, double", "Yes",
                               5, 2, 10))
    allPhenomes.append(phenome(35, "u:", getGraphemes(35),
                               "who, loon, dew, blue, flute, shoe, through, fruit, manoeuvre, group", "Yes",
                               5, 1, 9))
    allPhenomes.append(phenome(36, "ɔɪ", getGraphemes(36),
                               "join, boy, buoy", "Yes",
                               5, 3, 10))
    allPhenomes.append(phenome(37, "aʊ", getGraphemes(37),
                               "now, shout, bough", "Yes",
                               5, 8, 6))
    allPhenomes.append(phenome(38, "ə", getGraphemes(38),
                               "about, ladder, pencil, dollar, honour, augur", "Yes",
                               5, 4, 5))
    allPhenomes.append(phenome(39, "eəʳ", getGraphemes(39),
                               "chair, dare, pear, where, their, prayer", "Yes",
                               5, 3, 7))
    allPhenomes.append(phenome(40, "ɑ:", getGraphemes(40),
                               "arm", "Yes",
                               5, 7, 8))
    allPhenomes.append(phenome(41, "ɜ:ʳ", getGraphemes(41),
                               "bird, term, burn, pearl, word, journey, myrtle", "Yes",
                               5, 4, 6))
    allPhenomes.append(phenome(42, "ɔ:", getGraphemes(42),
                               "paw, ball, fork, poor, fore, board, four, taught, war, bought, sauce", "Yes",
                               5, 3, 2))
    allPhenomes.append(phenome(43, "ɪəʳ", getGraphemes(43),
                               "ear, steer, here, tier", "Yes",
                               5, 7, 6))
    allPhenomes.append(phenome(44, "ʊəʳ", getGraphemes(44),
                               "cure, tourist", "Yes",
                               5, 5, 9))
    for i in allPhenomes:
        i.frequency = 0
        for j in i.graphemes:
            i.frequency += j.frequency




def randNameBuilder():
    # put 3 sounds together
    finalName = ""
    examples = ""
    # print(allPhenomes[0].IPASymbol)
    for i in range(3):
        randPhenome = allPhenomes[randint(0, len(allPhenomes) - 1)]
        randGraphemeNum = randint(0, len(randPhenome.graphemes) - 1)
        finalName += randPhenome.graphemes[randGraphemeNum].spelling
        examples += randPhenome.graphemes[randGraphemeNum].example + " "

    print(finalName, ":", examples)

def freqNameBuilder():
    # put 3 sounds together
    finalName = ""
    examples = ""
    totalPhenomeFreq = 0
    for i in allPhenomes:
        totalPhenomeFreq += i.frequency

    for i in range(4):

        weightedPhenomeNum = randint(0, totalPhenomeFreq)
        weightedPhenome = getFrequencyWeighted(weightedPhenomeNum, allPhenomes)
        weightedGraphemeNum = randint(0, weightedPhenome.frequency)
        weightedGrapheme = getFrequencyWeighted(weightedGraphemeNum, weightedPhenome.graphemes)
        finalName += weightedGrapheme.spelling
        examples += weightedGrapheme.example + " "

    print(finalName, ":", examples)


def freqSharpNameBuilder():
    # put 3 sounds together
    finalName = ""
    examples = ""
    totalPhenomeWeighting = 0
    for i in allPhenomes:
        totalPhenomeWeighting += i.frequency*i.sharpness

    for i in range(4):
        weightedPhenomeNum = randint(0, totalPhenomeWeighting)
        weightedPhenome = getFrequencySharpnessWeighted(weightedPhenomeNum, allPhenomes)
        weightedGraphemeNum = randint(0, weightedPhenome.frequency)
        weightedGrapheme = getFrequencyWeighted(weightedGraphemeNum, weightedPhenome.graphemes)
        finalName += weightedGrapheme.spelling
        examples += weightedGrapheme.example + " "

    print(finalName, ":", examples)

def getFrequencyWeighted(num, items):
    for i in items:
        num -= i.frequency
        if num <= 0:
            return i
    return i

def getFrequencySharpnessWeighted(num, items):
    for i in items:
        num -= i.frequency*i.sharpness
        if num <= 0:
            return i
    return i

def getAllQualsWeighted(num, items):
    for i in items:
        num -= i.curMultiplier
        if num <= 0:
            return i
    return i

def getGraphemeFreqWeighted(num, graphemes):
    for i in graphemes:
        num -= i.adjFreq
        if num <= 0:
            return i
    return i

def allQualsNameGenerator(**kwargs):
    # put 3 sounds together

    totalPhenomeWeighting = 0

    curMax = 0
    for i in allPhenomes:
        if curMax < i.frequency:
            curMax = i.frequency


    for i in allPhenomes:
        curMultiplier = 1.0
        #heuristic: the difference between wanted and real
        curMultiplier *= 11 - abs(kwargs['sharpness']-i.sharpness)
        curMultiplier *= 11 - abs(kwargs['roughness']-i.roughness)
        curMultiplier *= 11 - abs(kwargs['sound_location']-i.sound_location)
        adjustedFrequency = i.frequency/curMax*10
        curMultiplier *= 11 - abs(kwargs['frequency'] - adjustedFrequency)
        i.curMultiplier = curMultiplier
        totalPhenomeWeighting += curMultiplier

    outGraphemes = []
    for i in range(4):
        #get the weighted phenome
        weightedPhenomeNum = random()*totalPhenomeWeighting
        weightedPhenome = getAllQualsWeighted(weightedPhenomeNum, allPhenomes)

        #set up the weightedGrapheme
        curMax = 0
        for j in weightedPhenome.graphemes:
            if curMax < j.frequency:
                curMax = j.frequency
        totalGraphsFreqWeight = 0
        for j in weightedPhenome.graphemes:
            adjustedFrequency = j.frequency / curMax * 10
            j.adjFreq = 11 - abs(kwargs['frequency'] - adjustedFrequency)
            totalGraphsFreqWeight += j.adjFreq

        #get the weighted grapheme
        #should probably swith to randnum 0-1 * totaGraphsFreqWeight
        weightedGraphemeNum = random()*totalGraphsFreqWeight
        weightedGrapheme = getGraphemeFreqWeighted(weightedGraphemeNum, weightedPhenome.graphemes)
        outGraphemes.append(weightedGrapheme)

    finalName = ""
    examples = ""

    #postWord is the second half of a ae_e split phoneme
    #assuming you don't get 2 split phenomes in a row
    postWord = ""
    for k in outGraphemes:
        if '-' in k.spelling:
            #assuming only 2 parts
            splitWords = k.spelling.split('-')
            finalName += splitWords[0]
            postWord = splitWords[1]
        else:
            finalName += k.spelling
            if postWord != "":
                finalName += postWord
                postWord = ""
        examples += k.example + " "

    if postWord != "":
        finalName += postWord

    print(finalName.title(), ":", examples)


class wantedPhonemeQual():
    def __init__(self, noUseIds = [], sharpness=[5,1], roughness=[5,1], sound_location=[5,1], frequency=[10,1]):
        # all qualities are tuples
        #[0] is quantity (1-10)
        #[1] is importance (1-10)
        self.sharpness = sharpness
        self.roughness = roughness
        self.sound_location = sound_location
        self.frequency = frequency
        self.noUseIds = noUseIds


def NameGen(wantedPhonemes):

    outGraphemes = []
    for pheno in wantedPhonemes:
        usablePhenomes = []
        for i in allPhenomes:
            if i.id not in pheno.noUseIds:
                usablePhenomes.append(i)
        curPheFreqMax = 0
        for i in usablePhenomes:
            if curPheFreqMax < i.frequency:
                curPheFreqMax = i.frequency
        totalPhenomeWeighting = 0
        for i in usablePhenomes:
            curMultiplier = 1.0
            # heuristic: the difference between wanted and real
            curMultiplier *= pheno.sharpness[1] * (11 - abs(pheno.sharpness[0] - i.sharpness))
            curMultiplier *= pheno.roughness[1] * (11 - abs(pheno.roughness[0] - i.roughness))
            curMultiplier *= pheno.sound_location[1] * (11 - abs(pheno.sound_location[0] - i.sound_location))
            adjustedFrequency = i.frequency / curPheFreqMax * 10
            curMultiplier *= pheno.frequency[1] * (11 - abs(pheno.frequency[0] - adjustedFrequency))
            i.curMultiplier = curMultiplier
            totalPhenomeWeighting += curMultiplier

        # get the weighted phenome
        randomNo = random()
        weightedPhenomeNum = randomNo * totalPhenomeWeighting
        weightedPhenome = getAllQualsWeighted(weightedPhenomeNum, usablePhenomes)

        # set up the weightedGrapheme
        curGraphFreqMax = 0
        for j in weightedPhenome.graphemes:
            if curGraphFreqMax < j.frequency:
                curGraphFreqMax = j.frequency
        totalGraphsFreqWeight = 0
        for j in weightedPhenome.graphemes:
            adjustedFrequency = j.frequency / curGraphFreqMax * 10
            j.adjFreq = pheno.frequency[1] * (11 - abs(pheno.frequency[0] - adjustedFrequency))
            totalGraphsFreqWeight += j.adjFreq

        # get the weighted grapheme
        weightedGraphemeNum = random() * totalGraphsFreqWeight
        weightedGrapheme = getGraphemeFreqWeighted(weightedGraphemeNum, weightedPhenome.graphemes)
        outGraphemes.append(weightedGrapheme)
    wordFromGraphemes(outGraphemes)


def wordFromGraphemes(wordGraphemes):

    finalName = ""
    examples = ""

    # postWord is the second half of a ae_e split phoneme
    # assuming you don't get 2 split phenomes in a row
    postWord = ""
    for k in wordGraphemes:
        if '-' in k.spelling:
            # assuming only 2 parts
            splitWords = k.spelling.split('-')
            finalName += splitWords[0]
            postWord = splitWords[1]
        else:
            finalName += k.spelling
            if postWord != "":
                finalName += postWord
                postWord = ""
        examples += k.example + " "

    if postWord != "":
        finalName += postWord

    print(finalName.title(), ":", examples)

def r():
    return (randint(1,11), randint(1,11))

initGraphemes()
initPhenomes()

if __name__ == '__main__':

    for i in range(10):
        #freqSharpNameBuilder()
        
        wantedPhonemes = []
        wantedPhonemes.append(wantedPhonemeQual(noUseIds = [], sharpness=(1,10), roughness=(5,1), sound_location=(10,10), frequency=(10,10)))
        wantedPhonemes.append(wantedPhonemeQual(noUseIds = [], sharpness=(10,10), roughness=(5,1), sound_location=(10,1), frequency=(10,10)))
        wantedPhonemes.append(wantedPhonemeQual(noUseIds = [], sharpness=(1,10), roughness=(5,1), sound_location=(1,1), frequency=(10,10)))
        wantedPhonemes.append(wantedPhonemeQual(noUseIds = [], sharpness=(10,10), roughness=(5,1), sound_location=(10,10), frequency=(10,10)))

        #allQualsNameGenerator(sharpness=10, roughness=10, sound_location=5, frequency=2)
        NameGen(wantedPhonemes)
'''

for i in range(10):
    # freqSharpNameBuilder()

    wantedPhonemes = []
    wantedPhonemes.append(wantedPhonemeQual(noUseIds=[], sharpness=r(), roughness=r(), sound_location=r(),frequency=(10,10)))
    wantedPhonemes.append(wantedPhonemeQual(noUseIds=[], sharpness=r(), roughness=r(), sound_location=r(),frequency=(10,10)))
    wantedPhonemes.append(wantedPhonemeQual(noUseIds=[], sharpness=r(), roughness=r(), sound_location=r(),frequency=(10,10)))
    wantedPhonemes.append(wantedPhonemeQual(noUseIds=[], sharpness=r(), roughness=r(), sound_location=r(),frequency=(10,10)))

    # allQualsNameGenerator(sharpness=10, roughness=10, sound_location=5, frequency=2)
    NameGen(wantedPhonemes)'''
