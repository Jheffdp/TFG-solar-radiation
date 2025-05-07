##################################################################
## Parámetros de potencia (Pdc, Pac, PF)
##################################################################
powerIDs = [9, 2, 2, # T1_S1
       10, 3, 3, # T1_S2
       11, 4, 4, # T1_S3
       12, 5, 5, # T1_S4
       13, 6, 6, # T1_S5
       14, 7, 7, # T1_S6
       15, 8, 8, # T1_S7
       22, 16, 16, # T2_S1
       22, 17, 17, # T2_S2
       22, 18, 18, # T2_S3
       22, 19, 19, # T2_S4
       22, 20, 20, # T2_S5
       22, 21, 21, # T2_S6
       28, 23, 23, # SOLAREDGE
       28, 24, 24, # HUAWEI
       28, 25, 25, # SMA
       28, 26, 26, # SOLIS
       28, 27, 27] # FRONIUS


powerDIRs_T1 = [0x2, 0x18, 0x26] * 7 # 0x2 Pdc, 0x18 Pac, 0x26 PF en T1

powerDIRs_T2 = [0x2, 0x18, 0x26, # T2_S1
                0xE, 0x18, 0x26, # T2_S2
                0x1A, 0x18, 0x26, # T2_S3
                0x26, 0x18, 0x26, # T2_S4
                0x32, 0x18, 0x26, # T2_S5
                0x3E, 0x18, 0x26] # T2_S6

powerDIRs_T3 = [0x2, 0x18, 0x26, # SOLAREDGE
                0xE, 0x18, 0x26, # HUAWEI
                0x1A, 0x18, 0x26, # SMA
                0x26, 0x18, 0x26, # SOLIS
                0x32, 0x18, 0x26] # FRONIUS

powerDIRs = powerDIRs_T1 + powerDIRs_T2 + powerDIRs_T3

powerNames = ["T1_S1_Pdc", "T1_S1_Pac", "T1_S1_PF",
              "T1_S2_Pdc", "T1_S2_Pac", "T1_S2_PF",
              "T1_S3_Pdc", "T1_S3_Pac", "T1_S3_PF",
              "T1_S4_Pdc", "T1_S4_Pac", "T1_S4_PF",
              "T1_S5_Pdc", "T1_S5_Pac", "T1_S5_PF",
              "T1_S6_Pdc", "T1_S6_Pac", "T1_S6_PF",
              "T1_S7_Pdc", "T1_S7_Pac", "T1_S7_PF",
              "T2_S1_Pdc", "T2_S1_Pac", "T2_S1_PF",
              "T2_S2_Pdc", "T2_S2_Pac", "T2_S2_PF",
              "T2_S3_Pdc", "T2_S3_Pac", "T2_S3_PF",
              "T2_S4_Pdc", "T2_S4_Pac", "T2_S4_PF",
              "T2_S5_Pdc", "T2_S5_Pac", "T2_S5_PF",
              "T2_S6_Pdc", "T2_S6_Pac", "T2_S6_PF",
              "SOLAREDGE_Pdc", "SOLAREDGE_Pac", "SOLAREDGE_PF",
              "HUAWEI_Pdc", "HUAWEI_Pac", "HUAWEI_PF",
              "SMA_Pdc", "SMA_Pac", "SMA_PF",
              "SOLIS_Pdc", "SOLIS_Pac", "SOLIS_PF",
              "FRONIUS_Pdc", "FRONIUS_Pac", "FRONIUS_PF"]

#4 uint64 (Pac and Pdc), 2 uint32 (PF), 18 sistemas
powerNs = [4, 4, 2]  * 18

# Potencia en vatios
powerMults = [0.1, 0.1, 0.001] * 18
