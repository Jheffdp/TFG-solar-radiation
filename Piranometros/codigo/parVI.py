##################################################################
## Parámetros de Corriente y Tensión
##################################################################
# Idc, Vdc, Iac, Vac
viIDs = [9, 9, 2, 2, # T1_S1
         10, 10, 3, 3, # T1_S2
         11, 11, 4, 4, # T1_S3
         12, 12, 5, 5, # T1_S4
         13, 13, 6, 6, # T1_S5
         14, 14, 7, 7, # T1_S6
         15, 15, 8, 8, # T1_S7
         22, 22, 16, 16, # T2_S1
         22, 22, 17, 17, # T2_S2
         22, 22, 18, 18, # T2_S3
         22, 22, 19, 19, # T2_S4
         22, 22, 20, 20, # T2_S5
         22, 22, 21, 21, # T2_S6
         28, 28, 23, 23, # SOLAREDGE
         28, 28, 24, 24, # HUAWEI
         28, 28, 25, 25, # SMA
         28, 28, 26, 26, # SOLIS
         28, 28, 27, 27 # FRONIUS
         ]

viDIRs_T1 = [0x0, 0xA, 0x0, 0x24] * 7

viDIRs_T2 = [0x0, 0xA, 0x0, 0x24,
             0xC, 0x16, 0x0, 0x24,
             0x18, 0x22, 0x0, 0x24,
             0x24, 0x2E, 0x0, 0x24,
             0x30, 0x3A, 0x0, 0x24,
             0x3C, 0x46, 0x0, 0x24]

viDIRs_T3 = [0x0, 0xA, 0x0, 0x24,
             0xC, 0x16, 0x0, 0x24,
             0x18, 0x22, 0x0, 0x24,
             0x24, 0x2E, 0x0, 0x24,
             0x30, 0x3A, 0x0, 0x24]

viDIRs = viDIRs_T1 + viDIRs_T2 + viDIRs_T3

viNames = ["T1_S1_Idc", "T1_S1_Vdc", "T1_S1_Iac", "T1_S1_Vac",
           "T1_S2_Idc", "T1_S2_Vdc", "T1_S2_Iac", "T1_S2_Vac",
           "T1_S3_Idc", "T1_S3_Vdc", "T1_S3_Iac", "T1_S3_Vac",
           "T1_S4_Idc", "T1_S4_Vdc", "T1_S4_Iac", "T1_S4_Vac",
           "T1_S5_Idc", "T1_S5_Vdc", "T1_S5_Iac", "T1_S5_Vac",
           "T1_S6_Idc", "T1_S6_Vdc", "T1_S6_Iac", "T1_S6_Vac",
           "T1_S7_Idc", "T1_S7_Vdc", "T1_S7_Iac", "T1_S7_Vac",
           "T2_S1_Idc", "T2_S1_Vdc", "T2_S1_Iac", "T2_S1_Vac",
           "T2_S2_Idc", "T2_S2_Vdc", "T2_S2_Iac", "T2_S2_Vac",
           "T2_S3_Idc", "T2_S3_Vdc", "T2_S3_Iac", "T2_S3_Vac",
           "T2_S4_Idc", "T2_S4_Vdc", "T2_S4_Iac", "T2_S4_Vac",
           "T2_S5_Idc", "T2_S5_Vdc", "T2_S5_Iac", "T2_S5_Vac",
           "T2_S6_Idc", "T2_S6_Vdc", "T2_S6_Iac", "T2_S6_Vac",
           "SOLAREDGE_Idc", "SOLAREDGE_Vdc", "SOLAREDGE_Iac", "SOLAREDGE_Vac",
           "HUAWEI_Idc",    "HUAWEI_Vdc",    "HUAWEI_Iac",    "HUAWEI_Vac", 
           "SMA_Idc",       "SMA_Vdc",       "SMA_Iac",       "SMA_Vac",    
           "SOLIS_Idc",     "SOLIS_Vdc",     "SOLIS_Iac",     "SOLIS_Vac",  
           "FRONIUS_Idc",   "FRONIUS_Vdc",   "FRONIUS_Iac",   "FRONIUS_Vac"]

viNs = [2] * 4 * 18 ## uint32, 4 variables, 18 sistemas

viMults = [0.001, 0.1, 0.001, 0.1] * 18
