def ordenarFeed(publicacion: list) -> list:
    if len(publicacion) <=1:
        return publicacion

    if publicacion[0]==publicacion[1]:
        return ordenarFeed(publicacion[1:])
    else:
        return [publicacion[0]]+ordenarFeed(publicacion[1:])


print(ordenarFeed(publicacion=["Post A", "Post A", "Post V"]))