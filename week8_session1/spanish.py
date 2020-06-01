import spacy

es_parser = spacy.load("es_core_news_md")


oracion = "Python es un lenguaje de programación multiparadigma. Esto significa que más que forzar a los programadores a adoptar un estilo particular de programación, permite varios estilos: programación orientada a objetos, programación imperativa y programación funcional. Otros paradigmas están soportados mediante el uso de extensiones."

parsed = es_parser(oracion)


for token in parsed:
    print(token, token.pos_, token.lemma_)
