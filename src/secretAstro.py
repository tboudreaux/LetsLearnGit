import numpy as np

def HowManyStarsAreTherePerGalaxy(lum,dlum,norm,alpha):
    
    dn=lum**(-alpha)/dlum

    print('you gotta integrate this baby')
    return dn

def HowManyGalaxiesAreThere():
    return 125000000000
    # thank you google

if __name__ == "__main__":
    print(f"There are {HowManyStarsAreTherePerGalaxy()*HowManyGalaxiesAreThere()} Stars In the Universe")
