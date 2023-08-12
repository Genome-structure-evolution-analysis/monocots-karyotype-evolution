# -*- coding: utf-8 -*-
# @Author: wjq
# @Date:   2023-07-27 04:50:05
# @Last Modified by:   wjq
# @Last Modified time: 2023-08-11 16:26:01

import os
import glob

name_change = {'APK':'APK',"Os":"Oryza sativa","Sp":"Spirodela polyrhiza","El":"Elaeis guineensis","Ac":"Ananas comosus","Ab":"Ananas bracteatus",
                "Ata":"Acorus tatarinowii","Vvi":"Vitis vinifera","Amtr":"Amborella trichopoda","Koli":"Kobresia littledalei",
                "Asse":"Asparagus setaceus","Asof":"Asparagus officinalis","Muac":"Musa acuminata","Ziof":"Zingiber officinale",
                "Vapl":"Vanilla planifolia","Sobi":"Sorghum bicolor","Aga":"Acorus gramineus","Sb":"Sorghum bicolor",
                "Tel":"Thinopyrum elongatum","Bdi":"Brachypodium distachyon","AcaA":"Acorus calamus A","AcaB":"Acorus calamus B"}

files = glob.glob('*.blast')
print(len(files))
for file in files:
    name = os.path.basename(file)
    names = name.split('.')[0].split('_')
    spec1 = name_change[names[0]]
    spec2 = name_change[names[1]]
    sf = open('blast_dotplot-auto.conf', 'w')
    text = f"""[dotplot]
genome1_name = {spec1}
genome2_name = {spec2}
lens_file1 = {names[0]}.lens
lens_file2 = {names[1]}.lens
gff_file1 = {names[0]}.new.gff
gff_file2 = {names[1]}.new.gff
blast_file = {names[0]}_{names[1]}.blast
savefile = {names[0]}_{names[1]}.blast.dotplot.png
multiple = 2
score = 100
evalue = 1e-5
repnum = 20
hitnum = 5
dpi=300
"""
    print(text)
    sf.write(text)
    sf.close()
    os.system('AKRUP -d blast_dotplot-auto.conf')


