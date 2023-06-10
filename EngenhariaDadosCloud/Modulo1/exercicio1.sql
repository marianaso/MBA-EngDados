## EXERCICIO PRATICO MODULO 1

#select AVG(nu_nota_mt) from consumer_zone where tp_sexo = 'F';
#select AVG(nu_nota_ch) from consumer_zone where tp_sexo = 'M' and sg_uf_esc = 'SP';
#select AVG(nu_nota_ch) from consumer_zone where no_municipio_esc = 'Natal';
#select no_municipio_esc, AVG(nu_nota_mt) from consumer_zone group by no_municipio_esc order by AVG(nu_nota_mt) desc limit 10;
#select count(nu_inscricao) from consumer_zone where no_municipio_esc = 'Recife' and no_municipio_prova = 'Recife';
#select AVG(nu_nota_ch) from consumer_zone where sg_uf_esc = 'SC' and not q008 = 'A';
#select AVG(nu_nota_mt) from consumer_zone where tp_sexo = 'F' and no_municipio_esc = 'Belo Horizonte'and (q002 = 'F' or q002 = 'G');
