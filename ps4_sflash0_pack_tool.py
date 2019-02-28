# PS4 Sflash0 pack tool
# SocraticBliss (R)
# Thanks to zecoxao <3

'''
    0x0 <- Header (0x1000)
    0x1000 <- Unk (0x1000)
    0x2000 <- MBR1 (0x1000) (for sflash0s1.cryptx3b)
    0x3000 <- MBR2 (0x1000) (for sflash0s1.cryptx3)
    0x4000 <- sflash0s0x32b (emc_ipl) (0x60000)
    0x64000 <- sflash0s0x32 (emc_ipl) (0x60000)
    0xC4000 <- sflash0s0x33 (eap_kbl) (0x80000)
    0x144000 <- sflash0s0x34 (wifi fw) (0x80000)
    0x1C4000 <- sflash0s0x38 (nvs) (0xC000)
    0x1D0000 <- sflash0s0x0 (blank1) (0x30000)
    0x200000 <- Header2 (0x1000)
    0x201000 <- Unk2 (0x1000)
    0x202000 <- MBR3 (0x1000) (for sflash0s1.cryptx2b)
    0x203000 <- MBR4 (0x1000) (for sflash0s1.cryptx2)
    0x204000 <- sflash0s1.cryptx2b (sam_ipl/secure loader) (0x3E000)
    0x242000 <- sflash0s1.cryptx2 (sam_ipl/secure loader) (0x3E000)
    0x280000 <- sflash0s1.cryptx1 (idata) (0x80000)
    0x300000 <- sflash0s1.cryptx39 (bd_hrl?) (0x80000)
    0x380000 <- sflash0s1.cryptx6 (Virtual TRM) (0x40000)
    0x3C0000 <- sflash0s1.cryptx3b (secure kernel, secure modules) (0xCC0000)
    0x1080000 <- sflash0s1.cryptx3 (secure kernel, secure modules) (0xCC0000)
    0x1D40000 <- sflash0s1.cryptx40 (blank2) (0x2C0000)
'''

import os
import sys

SFLASH0 = [
('header.bin',   0x0,       0x1000),
('unknown.bin',  0x1000,    0x1000),
('mbr1.bin',     0x2000,    0x1000),
('mbr2.bin',     0x3000,    0x1000),
('emc_iplb.bin', 0x4000,    0x60000),
('emc_ipl.bin',  0x64000,   0x60000),
('emc_kbl.bin',  0xC4000,   0x80000),
('wifi_fw.bin',  0x144000,  0x80000),
('nvs.bin',      0x1C4000,  0xC000),
('blank.bin',    0x1D0000,  0x30000),
('header2.bin',  0x200000,  0x1000),
('unknown2.bin', 0x201000,  0x1000),
('mbr3.bin',     0x202000,  0x1000),
('mbr4.bin',     0x203000,  0x1000), 
('sam_iplb.bin', 0x204000,  0x3E000),
('sam_ipl.bin',  0x242000,  0x3E000),
('idata.bin',    0x280000,  0x80000),
('bd_hrl.bin',   0x300000,  0x80000),
('vtrm.bin',     0x380000,  0x40000),
('secureb.bin',  0x3C0000,  0xCC0000),
('secure.bin',   0x1080000, 0xCC0000),
('blank2.bin',   0x1D40000, 0x2C0000),
]

def unpack(file, dir):

    with open(file, 'rb') as input:
        sflash0 = input.read()
        
        for num, entry in enumerate(SFLASH0):
            with open('%s/%s' % (dir, SFLASH0[num][0]), 'wb') as output:
                begin = SFLASH0[num][1]
                end = begin + SFLASH0[num][2]
                
                output.write(sflash0[begin:end])
                print('Unpacked %s' % SFLASH0[num][0])

def pack(dir, name):

    with open(name, 'wb') as output:
        for num, entry in enumerate(SFLASH0):
            with open('%s/%s' % (dir, SFLASH0[num][0]), 'rb') as input:
                output.write(input.read())

def main(argc, argv):
    
    if argc not in [2, 3]:
        raise SystemExit('\nUsage: python %s <input> [output]' % argv[0])
    
    if os.path.isfile(argv[1]):
        if argc == 3:
            try:
                os.makedirs(argv[2])
            except:
                pass

        unpack(argv[1], argv[2] if argc == 3 else '.')
    
    else:
        pack(argv[1], argv[2] if argc == 3 else 'sflash0.bin')
    
    print('\nDone!')

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)