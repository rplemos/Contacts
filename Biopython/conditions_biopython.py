"""
Author: Rafael Lemos - rafaellemos42@gmail.com
Date: 12/08/2024

License: MIT License
"""

# RULES
# 1 - must be made by different residue atoms
# 2 - aromatic = aromatic + aromatic
# 3 - hydrogenb => aceptor + donor
# 4 - hydrophobic: hydrofobic + hydrofobic
# 5 - Repulsive: positive=>positive or negative=>negative
# 6 - Atractive: positive=>negative or negative=>positive
# 7 - salt_bridge: positive=>negative or negative=>positive

categories = {
    'salt_bridge': (0, 3.9), # minimum and maximum distances, in Angstroms
    'hydrophobic': (2, 4.5),
    'hydrogen_bond': (0, 3.9),
    'repulsive': (2, 6),
    'attractive': (3.9, 6),
    'disulfide_bond': (0, 2.8),
}


contact_conditions = {
    'salt_bridge': lambda name1, name2: (contact_types[name1][2] == 1 and contact_types[name2][3] == 1) or (contact_types[name1][3] == 1 and contact_types[name2][2] == 1),
    'disulfide_bond': lambda name1, name2: name1 == "CYS:SG" and name2 == "CYS:SG",
    'hydrogen_bond': lambda name1, name2: ((contact_types[name1][4] == 1 and contact_types[name2][5] == 1) or (contact_types[name1][5] == 1 and contact_types[name2][4] == 1)),  
    'hydrophobic': lambda name1, name2: contact_types[name1][0] == 1 and contact_types[name2][0] == 1,
    'repulsive': lambda name1, name2: (contact_types[name1][2] == 1 and contact_types[name2][2] == 1) or (contact_types[name1][3] == 1 and contact_types[name2][3] == 1),
    'attractive': lambda name1, name2: (contact_types[name1][2] == 1 and contact_types[name2][3] == 1) or (contact_types[name1][3] == 1 and contact_types[name2][2] == 1),
}


# 'RES:ATOM':	[	Hydrophobic,	Aromatic,	Positive,	Negative,	Donor,	Acceptor	]
# 'ALA:CA':		[	0|1,			0|1,		0|1,		0|1,		0|1,	0|1			]
contact_types = {
    'ALA:N':[0, 0, 0, 0, 1, 0],
    'ALA:CA':[0, 0, 0, 0, 0, 0],
    'ALA:C':[0, 0, 0, 0, 0, 0],
    'ALA:O':[0, 0, 0, 0, 0, 1],
    'ALA:CB':[1, 0, 0, 0, 0, 0],
    
    'ARG:N':[0, 0, 0, 0, 1, 0],
    'ARG:CA':[0, 0, 0, 0, 0, 0],
    'ARG:C':[0, 0, 0, 0, 0, 0],
    'ARG:O':[0, 0, 0, 0, 0, 1],
    'ARG:CB':[1, 0, 0, 0, 0, 0],
    'ARG:CG':[1, 0, 0, 0, 0, 0],
    'ARG:CD':[0, 0, 0, 0, 0, 0],
    'ARG:NE':[0, 0, 1, 0, 1, 0],
    'ARG:CZ':[0, 0, 1, 0, 0, 0],
    'ARG:NH1':[0, 0, 1, 0, 1, 0],
    'ARG:NH2':[0, 0, 1, 0, 1, 0],
    
    'ASN:N':[0, 0, 0, 0, 1, 0],
    'ASN:CA':[0, 0, 0, 0, 0, 0],
    'ASN:C':[0, 0, 0, 0, 0, 0],
    'ASN:O':[0, 0, 0, 0, 0, 1],
    'ASN:CB':[1, 0, 0, 0, 0, 0],
    'ASN:CG':[0, 0, 0, 0, 0, 0],
    'ASN:OD1':[0, 0, 0, 0, 0, 1],
    'ASN:ND2':[0, 0, 0, 0, 1, 0],
    
    'ASP:N':[0, 0, 0, 0, 1, 0],
    'ASP:CA':[0, 0, 0, 0, 0, 0],
    'ASP:C':[0, 0, 0, 0, 0, 0],
    'ASP:O':[0, 0, 0, 0, 0, 1],
    'ASP:CB':[1, 0, 0, 0, 0, 0],
    'ASP:CG':[0, 0, 0, 0, 0, 0],
    'ASP:OD1':[0, 0, 0, 1, 0, 1],
    'ASP:OD2':[0, 0, 0, 1, 0, 1],
    
    'CYS:N':[0, 0, 0, 0, 1, 0],
    'CYS:CA':[0, 0, 0, 0, 0, 0],
    'CYS:C':[0, 0, 0, 0, 0, 0],
    'CYS:O':[0, 0, 0, 0, 0, 1],
    'CYS:CB':[1, 0, 0, 0, 0, 0],
    'CYS:SG':[0, 0, 0, 0, 1, 1],
    
    'GLN:N':[0, 0, 0, 0, 1, 0],
    'GLN:CA':[0, 0, 0, 0, 0, 0],
    'GLN:C':[0, 0, 0, 0, 0, 0],
    'GLN:O':[0, 0, 0, 0, 0, 1],
    'GLN:CB':[1, 0, 0, 0, 0, 0],
    'GLN:CG':[1, 0, 0, 0, 0, 0],
    'GLN:CD':[0, 0, 0, 0, 0, 0],
    'GLN:OE1':[0, 0, 0, 0, 0, 1],
    'GLN:NE2':[0, 0, 0, 0, 1, 0],
    
    'GLU:N':[0, 0, 0, 0, 1, 0],
    'GLU:CA':[0, 0, 0, 0, 0, 0],
    'GLU:C':[0, 0, 0, 0, 0, 0],
    'GLU:O':[0, 0, 0, 0, 0, 1],
    'GLU:CB':[1, 0, 0, 0, 0, 0],
    'GLU:CG':[1, 0, 0, 0, 0, 0],
    'GLU:CD':[0, 0, 0, 0, 0, 0],
    'GLU:OE1':[0, 0, 0, 1, 0, 1],
    'GLU:OE2':[0, 0, 0, 1, 0, 1],
    
    'GLY:N':[0, 0, 0, 0, 1, 0],
    'GLY:CA':[0, 0, 0, 0, 0, 0],
    'GLY:C':[0, 0, 0, 0, 0, 0],
    'GLY:O':[0, 0, 0, 0, 0, 1],
    
    'HIS:N':[0, 0, 0, 0, 1, 0],
    'HIS:CA':[0, 0, 0, 0, 0, 0],
    'HIS:C':[0, 0, 0, 0, 0, 0],
    'HIS:O':[0, 0, 0, 0, 0, 1],
    'HIS:CB':[1, 0, 0, 0, 0, 0],
    'HIS:CG':[0, 1, 0, 0, 0, 0],
    'HIS:ND1':[0, 1, 1, 0, 1, 1],
    'HIS:CD2':[0, 1, 0, 0, 0, 0],
    'HIS:CE1':[0, 1, 0, 0, 0, 0],
    'HIS:NE2':[0, 1, 1, 0, 1, 1],
    
    'ILE:N':[0, 0, 0, 0, 1, 0],
    'ILE:CA':[0, 0, 0, 0, 0, 0],
    'ILE:C':[0, 0, 0, 0, 0, 0],
    'ILE:O':[0, 0, 0, 0, 0, 1],
    'ILE:CB':[1, 0, 0, 0, 0, 0],
    'ILE:CG1':[1, 0, 0, 0, 0, 0],
    'ILE:CG2':[1, 0, 0, 0, 0, 0],
    'ILE:CD1':[1, 0, 0, 0, 0, 0],
    
    'LEU:N':[0, 0, 0, 0, 1, 0],
    'LEU:CA':[0, 0, 0, 0, 0, 0],
    'LEU:C':[0, 0, 0, 0, 0, 0],
    'LEU:O':[0, 0, 0, 0, 0, 1],
    'LEU:CB':[1, 0, 0, 0, 0, 0],
    'LEU:CG':[1, 0, 0, 0, 0, 0],
    'LEU:CD1':[1, 0, 0, 0, 0, 0],
    'LEU:CD2':[1, 0, 0, 0, 0, 0],
    
    'LYS:N':[0, 0, 0, 0, 1, 0],
    'LYS:CA':[0, 0, 0, 0, 0, 0],
    'LYS:C':[0, 0, 0, 0, 0, 0],
    'LYS:O':[0, 0, 0, 0, 0, 1],
    'LYS:CB':[1, 0, 0, 0, 0, 0],
    'LYS:CG':[1, 0, 0, 0, 0, 0],
    'LYS:CD':[1, 0, 0, 0, 0, 0],
    'LYS:CE':[0, 0, 0, 0, 0, 0],
    'LYS:NZ':[0, 0, 1, 0, 1, 0],
    
    'MET:N':[0, 0, 0, 0, 1, 0],
    'MET:CA':[0, 0, 0, 0, 0, 0],
    'MET:C':[0, 0, 0, 0, 0, 0],
    'MET:O':[0, 0, 0, 0, 0, 1],
    'MET:CB':[1, 0, 0, 0, 0, 0],
    'MET:CG':[1, 0, 0, 0, 0, 0],
    'MET:SD':[0, 0, 0, 0, 0, 1],
    'MET:CE':[1, 0, 0, 0, 0, 0],
    
    'PHE:N':[0, 0, 0, 0, 1, 0],
    'PHE:CA':[0, 0, 0, 0, 0, 0],
    'PHE:C':[0, 0, 0, 0, 0, 0],
    'PHE:O':[0, 0, 0, 0, 0, 1],
    'PHE:CB':[1, 0, 0, 0, 0, 0],
    'PHE:CG':[1, 1, 0, 0, 0, 0],
    'PHE:CD1':[1, 1, 0, 0, 0, 0],
    'PHE:CD2':[1, 1, 0, 0, 0, 0],
    'PHE:CE1':[1, 1, 0, 0, 0, 0],
    'PHE:CE2':[1, 1, 0, 0, 0, 0],
    'PHE:CZ':[1, 1, 0, 0, 0, 0],
    
    'PRO:N':[0, 0, 0, 0, 0, 0],
    'PRO:CA':[0, 0, 0, 0, 0, 0],
    'PRO:C':[0, 0, 0, 0, 0, 0],
    'PRO:O':[0, 0, 0, 0, 0, 1],
    'PRO:CB':[1, 0, 0, 0, 0, 0],
    'PRO:CG':[1, 0, 0, 0, 0, 0],
    'PRO:CD':[0, 0, 0, 0, 0, 0],
    
    'SER:N':[0, 0, 0, 0, 1, 0],
    'SER:CA':[0, 0, 0, 0, 0, 0],
    'SER:C':[0, 0, 0, 0, 0, 0],
    'SER:O':[0, 0, 0, 0, 0, 1],
    'SER:CB':[0, 0, 0, 0, 0, 0],
    'SER:OG':[0, 0, 0, 0, 1, 1],
    
    'THR:N':[0, 0, 0, 0, 1, 0],
    'THR:CA':[0, 0, 0, 0, 0, 0],
    'THR:C':[0, 0, 0, 0, 0, 0],
    'THR:O':[0, 0, 0, 0, 0, 1],
    'THR:CB':[0, 0, 0, 0, 0, 0],
    'THR:OG1':[0, 0, 0, 0, 1, 1],
    'THR:CG2':[1, 0, 0, 0, 0, 0],
    
    'TRP:N':[0, 0, 0, 0, 1, 0],
    'TRP:CA':[0, 0, 0, 0, 0, 0],
    'TRP:C':[0, 0, 0, 0, 0, 0],
    'TRP:O':[0, 0, 0, 0, 0, 1],
    'TRP:CB':[1, 0, 0, 0, 0, 0],
    'TRP:CG':[1, 1, 0, 0, 0, 0],
    'TRP:CD1':[0, 1, 0, 0, 0, 0],
    'TRP:CD2':[1, 1, 0, 0, 0, 0],
    'TRP:NE1':[0, 1, 0, 0, 1, 0],
    'TRP:CE2':[0, 1, 0, 0, 0, 0],
    'TRP:CE3':[1, 1, 0, 0, 0, 0],
    'TRP:CZ2':[1, 1, 0, 0, 0, 0],
    'TRP:CZ3':[1, 1, 0, 0, 0, 0],
    'TRP:CH2':[1, 1, 0, 0, 0, 0],
    
    'TYR:N':[0, 0, 0, 0, 1, 0],
    'TYR:CA':[0, 0, 0, 0, 0, 0],
    'TYR:C':[0, 0, 0, 0, 0, 0],
    'TYR:O':[0, 0, 0, 0, 0, 1],
    'TYR:CB':[1, 0, 0, 0, 0, 0],
    'TYR:CG':[1, 1, 0, 0, 0, 0],
    'TYR:CD1':[1, 1, 0, 0, 0, 0],
    'TYR:CD2':[1, 1, 0, 0, 0, 0],
    'TYR:CE1':[1, 1, 0, 0, 0, 0],
    'TYR:CE2':[1, 1, 0, 0, 0, 0],
    'TYR:CZ':[0, 1, 0, 0, 0, 0],
    'TYR:OH':[0, 0, 0, 0, 1, 1],
    
    'VAL:N':[0, 0, 0, 0, 1, 0],
    'VAL:CA':[0, 0, 0, 0, 0, 0],
    'VAL:C':[0, 0, 0, 0, 0, 0],
    'VAL:O':[0, 0, 0, 0, 0, 1],
    'VAL:CB':[1, 0, 0, 0, 0, 0],
    'VAL:CG1':[1, 0, 0, 0, 0, 0],
    'VAL:CG2':[1, 0, 0, 0, 0, 0],
}