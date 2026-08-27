# Vaqtni birliklarga ajratish
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

T = int(input())
kun = T // 86400
qoldiq = T % 86400
soat = qoldiq // 3600
qoldiq = qoldiq % 3600
daqiqa = qoldiq // 60
sekunt = qoldiq % 60
print(kun)
print(soat)
print(daqiqa)
print(sekunt)