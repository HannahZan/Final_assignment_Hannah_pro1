"""
Author: Hannah Zantinge
Date: 28-01-2023
Description: This module contains the references to the used images in
Final_assignment_programming_1_Hannah.ipynb.
"""

def bird_references(bird):
    cc_asa = "(Creative Commons Attribution-Share Alike license)"
    cc_a = "(Creative Commons Attribution license)"
    gfdl = "(GNU Free Documentation License)"
    fal = "(Free art license)"
    bird_references_dict = {"Greater Canada Goose" : f"taken by Fiver der Hellseher{cc_asa}",
                            "Barnacle goose": f"taken by Andreas Trepte{cc_asa}",
                            "Greylag Goose" : f"taken by Tom Koerner{cc_a}",
                            "Mute Swan" : f"Taken by Yerpo{cc_asa}",
                            "Egyptian Goose" : f"taken by Andreas Trepte{cc_asa}",
                            "Common Shelduck" : f"Taken by Dick Daniels{cc_asa}",
                            "Garganey" : f"Taken by Dick Daniels{cc_asa}",
                            "Northern Shoveler" : f"taken by Steve Sinclair{cc_a}",
                            "Gadwall" : f"taken by Andreas Trepte{cc_asa}",
                            "Mallard" : f"taken by  Richard Bartz{cc_asa}",
                            "Feral Mallard" : f"taken by Atamari{cc_asa}",
                            "Eurasian Teal" : f"taken by Shantanu Kuveskar{cc_asa}",
                            "Red-crested Pochard" : f"taken by David Iliff{cc_asa}",
                            "Common Pochard" : f"Taken by Imran Shah{cc_a}",
                            "Tufted duck" : f"taken by Andreas Trepte{cc_asa}",
                            "Common Eider" : f"taken by Rhododendrites{cc_asa}",
                            "Red-breasted Merganser" : f"taken by Peter Massas{cc_asa}",
                            "Black Grouse" : f"taken by Aconcagua{gfdl}",
                            "Grey Partridge" : f"taken by Marek Szczepanek{gfdl}",
                            "Common Quail" : f"taken by Christoph Moning{cc_a}",
                            "Common Pheasant" : f"taken by Charles J. Sharp{cc_asa}",
                            "Little Grebe" : f"taken by Andreas Trepte{cc_asa}",
                            "Great Crested Grebe" : f"taken by JJ Harrison{cc_asa}",
                            "Black-necked Grebe" : f"taken by Andreas Trepte{cc_asa}",
                            "White Stork" : f"taken by Charles J. Sharp{cc_asa}",
                            "Eurasian Spoonbill" : f"taken by Andreas Trepte{cc_asa}",
                            "Eurasian Bittern" : f"taken by Francesco Veronesi{cc_asa}",
                            "Grey Heron" : f"taken by Andreas Trepte{cc_asa}",
                            "Purple Heron" : f"taken by A. Savin{fal}"
                            }
    return bird_references_dict[bird]
