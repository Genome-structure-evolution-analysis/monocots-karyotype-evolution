# -*- coding: utf-8 -*-
# @Author: wjq
# @Date:   2023-08-04 00:52:10
# @Last Modified by:   wjq
# @Last Modified time: 2023-08-10 15:22:57

# names = ['Sb_Os', 'Sb_Tel', 'Ac_Sb', 'Ac_Os', 'Sp_Ac', 'Sp_El', 'El_Ac', 'El_Os', 'Ata_Sp', 'Ata_El', 'Amtr_Ata', 'Amtr_Sp']
names = ['Sb_Sb', 'Tel_Tel', 'Ac_Ac', 'Os_Os', 'Sp_Sp', 'El_El', 'Ata_Ata', 'Amtr_Amtr', 'APK_APK', 'Bdi_Bdi']

for na in names:
    nas = na.split('_')
    rbdata=f"""[blast]
num_thread = auto
evalue = 1e-5
outfmt = 6
max_target_seqs = 10
querypep = ../{nas[0]}.pep
subjectpep = ../{nas[1]}.pep
outblast = {na}.blast
"""

    rcdata1=f"""[colinearscan]
num_process = auto
num_thread = auto
lens_file1 = {nas[0]}.lens
lens_file2 = {nas[1]}.lens
gff_file1 = {nas[0]}.new.gff
gff_file2 = {nas[1]}.new.gff
blast_file = {na}.blast
save_block_file = {na}.block.rr.txt
"""

    rkdata2=f"""[ks]
species_cds1 = {nas[0]}.cds
species_cds2 = {nas[1]}.cds
block_file = {na}.block.rr.txt
save_ks_file = {na}.ks.txt
"""

    sf = open(f'run_blast-{na}.conf', 'w')
    sf.write(rbdata)
    # sf1 = open(f'run_ColinearScan-{na}.conf', 'w')
    # sf1.write(rcdata1)
    # sf2 = open(f'run_ks-{na}.conf', 'w')
    # sf2.write(rkdata2)


import os
import glob
import itertools
import subprocess
from multiprocessing import Pool


class RunBioSoftware:
    def __init__(self, num_process):
        self.num_process = num_process
        self.main()

    def run_data(self, config):
        if 'run_blast' in config:
            subprocess.call(f'AKRUP -rb {config}', shell=True)

        elif 'run_ColinearScan' in config:
            subprocess.call(f'AKRUP -rc {config}', shell=True)

        elif 'run_ks' in config:
            subprocess.call(f'AKRUP -rk {config}', shell=True)


    def main(self):
        # access = list(set([x.strip() for x in open('run_sra4.txt')]))
        files1 = glob.glob('run_blast*')
        files2 = glob.glob('run_ColinearScan*')
        files3 = glob.glob('run_ks*')
        access = files1+files2+files3
        p = Pool(self.num_process)
        # for lsname in [files1, files2, files3]:
        for lsname in [files1]:
            for acc in lsname:
                print(acc)
                p.apply_async(self.run_data, args=(acc,))

        p.close()
        p.join()

if __name__ == '__main__':

    process = 10
    RunBioSoftware(process)