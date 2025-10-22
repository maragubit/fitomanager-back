

def scrapping_amazon_drasanvi(soup, *args, **kwargs):
    """
    Extrae información de productos Drasanvi desde una página de Amazon.
    Devuelve un diccionario con descripción, composición e instrucciones de uso.
    """
    acerca_de = soup.find("div", id="feature-bullets")
    items = acerca_de.select("ul li span.a-list-item")
    descripcion = ""
    posologia = ""
    ingredientes = ""
    descripcion= items[0].get_text(strip=True)
    for item in items:
        texto = item.get_text(strip=True)
        if "modo de uso" in texto.lower():
            posologia = texto
        
    important=soup.find("div", id="important-information")
    items=important.select("div.a-section.content")
    
    # Buscar ingredientes y posología entre los párrafos
    for item in items:
        
        if "ingredientes" in item.text.lower(): #coge el bloque de ingredientes con sus padres e hijos
            ingredientes = item.prettify()

        if not posologia and "modo de uso" in item.text.lower():
            p_list=item.find("p")
            for p in p_list:
                if "modo de uso" in p.text.lower():
                    posologia = p.get_text(strip=True)
    print("posologia scrapping Drasanvi:", posologia)
    return {
        "descripcion": descripcion,
        "composicion": ingredientes,
        "posologia": posologia,
    }
    
def scrapping_amazon_solgar(soup, *args, **kwargs):
    """
    Extrae información de productos Solgar desde una página de Amazon.
    Devuelve un diccionario con descripción, composición e instrucciones de uso.
    """
    descripcion = ""
    posologia = ""
    ingredientes = ""
    descriptions_content = soup.select_one("#productDescription")
    descriptions_content= descriptions_content.find_all(["h3","p"])
    for element in descriptions_content:
        if "descripción" in element.get_text(strip=True).lower():
            descripcion_p = element.find_next_sibling("p")
            if descripcion_p:
                descripcion = descripcion_p.get_text(strip=True)
        if "ingredientes" in element.get_text(strip=True).lower():
            ingredientes_p = element.find_next_sibling("p")
            if ingredientes_p:
                ingredientes = ingredientes_p.get_text(strip=True)
        if "dirección" in element.get_text(strip=True).lower():
            posologia = element.find_next_sibling("p")
            if posologia:
                posologia = posologia.get_text(strip=True)
    
    # Implementar la lógica específica para Soria aquí
    return {
        "descripcion": descripcion,
        "composicion": ingredientes,
        "posologia": posologia,
    }
    
def scrapping_amazon_soria(soup, *args, **kwargs):
    """
    Extrae información de productos Soria desde una página de Amazon.
    Devuelve un diccionario con descripción, composición e instrucciones de uso.
    """
    # Implementar la lógica específica para Soria aquí
    descripcion = ""
    posologia = ""
    ingredientes = ""
    acerca_de= soup.find("div", id="feature-bullets")
    items = acerca_de.select("ul li span.a-list-item")
    descripcion= items[0].get_text(strip=True)
    
    important_inf=soup.find("div", id="important-information")
    items=important_inf.select("div.a-section.content")
    for item in items:
        if "ingredientes" in item.get_text().lower(): #coge el bloque de ingredientes con sus padres e hijos
            ingredientes = item.prettify()
        if "instrucciones" in item.get_text().lower():
            posologia = item.find("p").get_text(strip=True)
            
            
    return {
        "descripcion": descripcion,
        "composicion": ingredientes,
        "posologia": posologia,
    }
    
def scrapping_amazon_biojoy(soup, *args, **kwargs):
        """
        Extrae información de productos Epel desde una página de Amazon.
        Devuelve un diccionario con descripción, composición e instrucciones de uso.
        """
        # Implementar la lógica específica para Epel aquí
        important_info=soup.find("div", id="important-information")
        items=important_info.select("div.a-section.content")
        descripcion = ""
        posologia = ""
        ingredientes = ""
        for item in items:
            if "descripción" in item.get_text().lower(): 
                descripcion = item.find("p").get_text(strip=True)
            if "ingredientes" in item.get_text().lower(): 
                ingredientes = item.prettify()
            if "instrucciones" in item.get_text().lower() and  "nota legal" not in item.get_text().lower():
                posologia = item.find("p").get_text(strip=True)
        return {
            "descripcion": descripcion,
            "composicion": ingredientes,
            "posologia": posologia,
        }   