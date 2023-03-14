#map() = applies a functio to each item an iterable(list,tuple,etc)
#map(function,iterable)

store = [

        ("shirts",20.00),
        ("pants",25.00),
        ("Jackets",50.00),
        ("Socks",10.00)

]

to_euros = lambda data:(data[0],data[1]*0.82)
to_dollars = lambda data:(data[0],data[1]/0.82)

store_euros = list(map(to_euros ,store))

for i in store_euros:
    print(i)



store_dolars = list(map(to_dollars ,store))

for i in store_euros:
    print(i)