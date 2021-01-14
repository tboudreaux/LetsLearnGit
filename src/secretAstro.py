import numpy as np

def HowManyStarsAreTherePerGalaxy(lum,dlum,norm,alpha):
    
    dn=lum**(-alpha)/dlum

    return dn

def HowManyGalaxiesAreThere():
    # Abby Edit Here

if __name__ == "__main__":
    print(f"There are {HowManyStarsAreTherePerGalaxy()*HowManyGalaxiesAreThere()} Stars In the Universe")
