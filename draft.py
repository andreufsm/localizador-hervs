#!/usr/bin/env python
# -*- coding: utf-8 -*-

arquivo_hervs = "C:\\Users\\André\\Downloads\\hg19.ALLHERV.gtf"
arquivo_fasta = open("C:\\Users\\André\\Downloads\\chr1 (2).fa\\chr1.fa")

fasta_completo = arquivo_fasta.read()
fasta_unica_linha = fasta_completo.replace("\n", "")

with open(arquivo_hervs, "r") as hervs:
  for linha in hervs:
      cromossomo = linha.split()[0]
      senso_ou_antisenso = linha.split()[6]
      if (senso_ou_antisenso == '-'):
          senso_ou_antisenso = 'neg'
      else:
          senso_ou_antisenso = 'pos'
      transcript_id = linha.split()[11]
      transcript_id = transcript_id[1:-2]
      repStart = linha.split()[19]
      repStart = repStart[1:-2]
      start = linha.split()[3]
      finish = linha.split()[4]

      # nome completo
      print(">" + cromossomo + "_" + senso_ou_antisenso + "_" + transcript_id + "_" + repStart + "_" + start + "_" + finish)
      # 830923 = 830927 (+4) inicio / fim 831248 = 831253 (+5)
      nome_arquivo = cromossomo + "_" + senso_ou_antisenso + "_" + transcript_id + "_" + repStart + "_" + start + "_" + finish
      titulo = ">" + cromossomo + "_" + senso_ou_antisenso + "_" + transcript_id + "_" + repStart + "_" + start + "_" + finish


      start = linha.split()[3]
      finish = linha.split()[4]
      start = int(start) + 4
      finish = int(finish) + 5
      print(fasta_unica_linha[start:finish])

      corpo = fasta_unica_linha[start:finish]

      novo_arquivo = open("C:\\Users\\André\\Downloads\\arquivos_rafa\\" + nome_arquivo + ".txt" , "w")
      novo_arquivo.write(titulo + "\n" + corpo)
      novo_arquivo.close()

