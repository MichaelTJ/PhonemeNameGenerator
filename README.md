# phonemeNameGenerator
A name generator based off the pronunciation of words (phonetics). 

The 44 phonemes have been categorised completely subjectively by sharpness (t=10, m=1), roughness/ugliness (g=9,f=1), and soundlocation(1=front of mouth, 10=back of throat). 
Other attributes like voiced and frequency are calculated more objectively.

Optional remove phonemes from the options list.

You get to choose how many phonemes, their attributes and the weighting of their attributes.


Usage:
    
    initGraphemes()
    initPhenomes() 
    
    #Create a list of wanted phonemes. These 4 will make up a word
    wantedPhonemes = []
    
    #sharpness(1,10) means the phoneme should be 1/10 sharp with an importance of 10/10
    wantedPhonemes.append(wantedPhonemeQual(noUseIds = [], sharpness=(1,10), roughness=(5,1), sound_location=(10,10), frequency=(10,10)))
    wantedPhonemes.append(wantedPhonemeQual(noUseIds = [], sharpness=(10,1), roughness=(5,1), sound_location=(10,1), frequency=(10,10)))
    wantedPhonemes.append(wantedPhonemeQual(noUseIds = [], sharpness=(1,10), roughness=(5,1), sound_location=(1,1), frequency=(10,10)))
    wantedPhonemes.append(wantedPhonemeQual(noUseIds = [], sharpness=(10,1), roughness=(5,1), sound_location=(10,10), frequency=(10,10)))

    #allQualsNameGenerator(sharpness=10, roughness=10, sound_location=5, frequency=2)
    NameGen(wantedPhonemes)
    
Output:

    Urboe : Up Rail Boy lOdgE
