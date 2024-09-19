# TemaIA1

## Implementare

Am facut un frontend minimalist cu functii de: login, register, upload, delete.
Ca baza de date am folosit mongodb (pentru useri)
Pozele sunt stocate in directoare pentru fiecare user.
Pe backend am facut rutele cerute cu middleware-ul corespunzator.
Rutele nu pot fi accesate daca user-ul nu este autentificat.

## Probleme

Pentru ca am folosit mongodb am avut mari probleme cu docker (nu a dorit sa se conecteze la baza de date). Fara docker proiectul merge perfect pe masina locala.

dockerul ruleaza doar cu flagul: **--network host** dar apar erori
