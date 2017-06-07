from Bio.Seq import Seq

primerF = Seq(raw_input("Enter forward primer sequence: "))
primerR = Seq(raw_input("Enter reverse primer sequence: "))


no_A_F = primerF.count("A")
no_T_F = primerF.count("T")
no_G_F = primerF.count("G")
no_C_F = primerF.count("C")
print(no_A_F, no_T_F, no_G_F, no_C_F)

no_A_R = primerR.count("A")
no_T_R = primerR.count("T")
no_G_R = primerR.count("G")
no_C_R = primerR.count("C")
print(no_A_R, no_T_R, no_G_R, no_C_R)

if len(primerF) < 14:
    tmF = (no_A_F + no_T_F) * 2 + (no_C_F + no_G_F) * 4
    print(tmF)
elif len(primerF) > 13:
    tmF = 64.9 + 41*(no_C_F + no_G_F - 16.4) / (no_A_F + no_T_F + no_G_F + no_C_F)
    print(tmF)

if len(primerR) < 14:
    tmR = (no_A_R + no_T_R) * 2 + (no_C_R + no_G_R) * 4
    print(tmR)
elif len(primerR) > 13:
    tmR = 64.9 + 41*(no_C_R + no_G_R - 16.4) / (no_A_R + no_T_R + no_G_R + no_C_R)
    print(tmR)

