st = input()
sym = ''
chastota = 0
for el in st:
    if el != sym:
        if st.count(el) >= chastota:
            chastota = st.count(el)
            sym = el
    else:
        continue
print(sym)



