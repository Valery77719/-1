# TODO Найдите количество книг, которое можно разместить на дискете
v=1.44
pages=100
str_=50
sim_=25
save=4 #б

V=int(v*1024*1024)

book=save*sim_*str_*pages

total=V//book
print("Количество книг, помещающихся на дискету:", total)
