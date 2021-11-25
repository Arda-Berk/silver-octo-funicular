sequence = input("Enter the sequence:\n")

result = ""

amino_acids = {
  'UUU':'Phe',
  'UUC':'Phe',
  'UUA':'Leu',
  'UUG':'Leu',
  'UCU':'Ser',
  'UCC':'Ser',
  'UCA':'Ser',
  'UCG':'Ser',
  'UAU':'Tyr',
  'UAC':'Tyr',
  'UAA':'stop',
  'UAG':'stop',
  'UGU':'Cys',
  'UGC':'Cys',
  'UGA':'stop',
  'UGG':'Trp',
  'CUU':'Leu',
  'CUC':'Leu',
  'CUA':'Leu',
  'CUG':'Leu',
  'CCU':'Pro',
  'CCC':'Pro',
  'CCA':'Pro',
  'CCG':'Pro',
  'CAU':'His',
  'CAC':'His',
  'CAA':'Gln',
  'CAG':'Gln',
  'CGU':'Arg',
  'CGC':'Arg',
  'CGA':'Arg',
  'CGG':'Arg',
  'AUU':'Ile',
  'AUC':'Ile',
  'AUA':'Ile',
  'AUG':'Met',
  'ACU':'Thr',
  'ACC':'Thr',
  'ACA':'Thr',
  'ACG':'Thr',
  'AAU':'Asn',
  'AAC':'Asn',
  'AAA':'Lys',
  'AAG':'Lys',
  'AGU':'Ser',
  'AGC':'Ser',
  'AGA':'Arg',
  'AGG':'Arg',
  'GUU':'Val',
  'GUC':'Val',
  'GUA':'Val',
  'GUG':'Val',
  'GCU':'Ala',
  'GCC':'Ala',
  'GCA':'Ala',
  'GCG':'Ala',
  'GAU':'Asp',
  'GAC':'Asp',
  'GAA':'Glu',
  'GAG':'Glu',
  'GGU':'Gly',
  'GGC':'Gly',
  'GGA':'Gly',
  'GGG':'Gly'
  }

if "AUG" in sequence:
  new_sequence = sequence[sequence.index("AUG"):]
  for i in range(0, len(new_sequence)//3):
    aa = new_sequence[0 + i*3] + new_sequence[1 + i*3] + new_sequence[2 + i*3]
    if amino_acids[aa] != "stop":
      result += amino_acids[aa] + "-"
    else:
      print(result.rstrip("-"))
else:
  print("Invalid!")
