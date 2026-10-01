import streamlit as st
import random
#bienvenida
st.write(":green[Sé bienvenida a la edición 1.1 de...]")
st.markdown("""
## ¿Qué tanto conoces a tu novio? 
###### omaigad
""")
st.divider()
st.info("""Esta es la versión mejorada del mismo jueguito de responder preguntas y así saber... ¿Qué tanto me conoces?
Para esto deberás ir respondiendo las preguntas que el juego te dará y dejarte llevar por tu intuición.
Espero que te guste y logres descubrir todos los finales y secretos 😼
""")
mejoras = st.button("Presiona aquí para ver las mejoras de esta versión", type="primary")
if mejoras:
    st.write("Mejoras de la versión 1.1:")
    with st.container(border=True):
     st.write("""La mejora más notable (además de la apariencia del juego en general es que ahora ya puedes escribir en cada una de las respuestas! Ponte creativa probando respuestas diferentes para obtener secretitos...   
     """)
    with st.container(border=True):
     st.write("También hay preguntas nuevas y mejoradas, además de pistas para ayudarte a conseguir los secretos que no existían en la versión anterior... intenta conseguir el 100%!")
    with st.container(border=True):
        st.write("*recuerda que a veces las respuestas no están entre las opciones*")

st.divider()
#Cosas del juego en sí
nopregunta = 0
puntos = 0
reppreguntas = 0
pregresp = 0
pff = 0

resprandomeu = [
    "Y si, me encanta (+1pts)",
    "Demasiado sexy (+1pts)",
    "Me la comería a besos (+1pts)",
    "Como pensaste eso? obvio si (+1pts)",
    "Tu sabes que eres sexy (+1pts)"
]
def reinicio2():
    nopregunta = 0
    puntos = 0
    reppreguntas = 0
    pregresp = 0
    pff = 0
st.write("En caso de emergencia o repetir una pregunta por accidente")
reinicio1 = st.button("Presiona aquí para reiniciar el puntaje si algo salió mal")
if reinicio1:
    reinicio2()
    
lista = st.text_input("Estas lista para empezar a responder?")
#verificar respuesta de preguntas
def resppreguntas():
    global reppreguntas
    if reppreguntas == 1:
        st.success("jmmm tuviste suerte esta vez...")
        st.success("Nada mal (+1pts)")
    elif reppreguntas == 0.5:     
        st.warning("Jmmm pregunta algo capciosa... (+0.5pts)")
    else:
        st.error("INCORRECTA:  " + "ihhh te pasas me rompes el corazón 💔" + "(+0pts)")
    
def masnopregunta():
    global reppreguntas
    global puntos
    global nopregunta
    global pregresp
    global resprandomeu
    global pff
    #INCIO PREGUNTA
    nopregunta = nopregunta + 1
    st.title(f":blue[PREGUNTA NO. {nopregunta}]")
    st.subheader(f":blue[La pregunta No. {nopregunta} dice: ]")
    with st.container(border=True):
        st.write("¿Cuál es mi comida favorita?")
    col1, col2 = st.columns(2)
    with col1:
        st.info("Huevos fritos")
        st.info("Pollo asado")
        st.info("Pastel de gelatina")
        st.info("Atol")
        st.info("Frijoles colorados")
        st.caption("Escribe aquí tu respuesta:")
    p1 = st.text_input("respuesta 1",)
    if p1:
        pregresp = pregresp + 1
        if "huev" in p1.lower():
            reppreguntas = 1
            puntos = puntos + 1
            resppreguntas()
        elif "eunice" in p1.lower():
            reppreguntas = 1
            puntos = puntos + 1
            st.success("Siempre comer Eunice es una buena opción (+1pts)")
        else:
            reppreguntas = 0
            puntos = puntos
            resppreguntas()
    else:
        st.error("Tienes que responer la pregunta")
    st.divider()
    #FIN PREGUNTA
    nopregunta = nopregunta + 1
    st.title(f":blue[PREGUNTA NO. {nopregunta}]")
    st.subheader(f":blue[La pregunta No. {nopregunta} dice: ]")
    with st.container(border=True):
        st.write("¿Cuál es mi número favorito?")
    col1, col2 = st.columns(2)
    with col1:
        st.info("13")
        st.info("23 casi 24")
        st.info("100")
        st.info("5")
        st.info("121")
        st.info("3")
        st.caption("Escribe aquí tu respuesta:")
    p2 = st.text_input("respuesta 2")
    if p2:
        pregresp = pregresp + 1
        if "5" in p2.lower():
            reppreguntas = 1
            puntos = puntos + 1
            resppreguntas()
        elif "casi" in p2.lower():
            reppreguntas =0.5
            puntos = puntos + 0.5
            st.warning("y si me meto con el? (+0.5pts)")
        elif "67" in p2.lower():
            reppreguntas = 1
            puntos = puntos + 1.67
            st.success("sixseven sixseven sixseven (+1.67pts)")
        elif "13" in p2.lower():
            reppreguntas = 0
            puntos = puntos
            resppreguntas()
            st.warning("Caaasi, pero no")
        else:
            reppreguntas = 0
            puntos = puntos
            resppreguntas()
    else:
        st.error("Tienes que responer la pregunta")
    st.divider()

    nopregunta = nopregunta + 1
    st.title(f":blue[PREGUNTA NO. {nopregunta}]")
    st.subheader(f":blue[La pregunta No. {nopregunta} dice: ]")
    with st.container(border=True):
        st.write("¿Cuál es mi videojuego favorito?")
    col1, col2 = st.columns(2)
    with col1:
        st.info("Five nights at freddys")
        st.info("Cuphead")
        st.info("Rayman")
        st.info("Minecraft")
        st.info("The last of us")
        st.info("Mario bros")
        st.info("Need for Speed MW")
        st.caption("Escribe aquí tu respuesta:")
    p3 = st.text_input("respuesta 3")
    if p3:
        pregresp = pregresp + 1
        if "todos" in p3.lower():
            reppreguntas = 1
            puntos = puntos + 1
            st.success("Exacto, todos (+1pts)")
        elif "rayman" in p3.lower() or "minecraft" in p3.lower() or "mario" in p3.lower():
            reppreguntas =0.5
            puntos = puntos + 0.5
            resppreguntas()
        else:
            reppreguntas = 0
            puntos = puntos
            resppreguntas()
    else:
        st.error("Tienes que responer la pregunta")
    st.divider()

    nopregunta = nopregunta + 1
    st.title(f":blue[PREGUNTA NO. {nopregunta}]")
    st.subheader(f":blue[La pregunta No. {nopregunta} dice: ]")
    with st.container(border=True):
        st.write("¿Para mí cuál es el país más bello del mundo?")
    col1, col2 = st.columns(2)
    with col1:
        st.info("España")
        st.info("Inglaterra")
        st.info("Argentina")
        st.info("Guatemala")
        st.info("México")
        st.caption("Escribe aquí tu respuesta:")
    p4 = st.text_input("respuesta 4")
    if p4:
        pregresp = pregresp + 1
        if "guatemala" in p4.lower():
            reppreguntas = 1
            puntos = puntos + 1
            resppreguntas()
        else:
            reppreguntas = 0
            puntos = puntos
            resppreguntas()
    else:
        st.error("Tienes que responer la pregunta")
    st.divider()

    nopregunta = nopregunta + 1
    st.title(f":blue[PREGUNTA NO. {nopregunta}]")
    st.subheader(f":blue[La pregunta No. {nopregunta} dice: ]")
    with st.container(border=True):
        st.write("¿Quién es mi jugador favorito de fútbol?")
    col1, col2 = st.columns(2)
    with col1:
        st.info("Messi")
        st.info("Lamine Yamal")
        st.info("Eden Hazard")
        st.info("Neymar Jr.")
        st.info("Cristiano Ronaldo")
        st.caption("Escribe aquí tu respuesta:")
    p5 = st.text_input("respuesta 5")
    if p5:
        pregresp = pregresp + 1
        if "neymar" in p5.lower():
            reppreguntas = 1
            puntos = puntos + 1
            resppreguntas()
        elif "eden" in p5.lower() or "messi" in p5.lower():
            reppreguntas =0.5
            puntos = puntos + 0.5
            resppreguntas()
            st.warning("Si... se podría decir que también es mi jugador favorito")
        else:
            reppreguntas = 0
            puntos = puntos
            resppreguntas()
    else:
        st.error("Tienes que responer la pregunta")
    st.divider()

    nopregunta = nopregunta + 1
    st.title(f":blue[PREGUNTA NO. {nopregunta}]")
    st.subheader(f":blue[La pregunta No. {nopregunta} dice: ]")
    with st.container(border=True):
        st.write("¿Si tuviera 1 millón de $, en que los gastaría?")
    col1, col2 = st.columns(2)
    with col1:
        st.info("Una casa en las lomas")
        st.info("Chingos de comida")
        st.info("El carro de mis sueños")
        st.info("Una colección de videojuegos retro")
        st.info("Ir a ver un partido del Barcelona")
        st.info("Una tele gigante")
        st.info("Invertirlo en acciones")
        st.info("Comprar un negocio")
        st.caption("Escribe aquí tu respuesta:")
    p6 = st.text_input("respuesta 6")
    if p6:
        pregresp = pregresp + 1
        if "clon" in p6.lower():
            reppreguntas = 1
            puntos = puntos + 1.33
            st.success("Omg como adivinaste que clonaría Eunices (+1.33pts)")
        elif "comida" in p6.lower() or "juegos" in p6.lower():
            reppreguntas =1
            puntos = puntos + 1
            resppreguntas()
        else:
            reppreguntas = 0
            puntos = puntos
            st.error("Si me alcanzaría pero no, de todas maneras:")
            resppreguntas()
    else:
        st.error("Tienes que responer la pregunta")
    st.divider()

    nopregunta = nopregunta + 1
    st.title(f":blue[PREGUNTA NO. {nopregunta}]")
    st.subheader(f":blue[La pregunta No. {nopregunta} dice: ]")
    with st.container(border=True):
        st.write("¿Qué cosa es lo que más me gusta de tí?")
        st.caption("Escribe aquí tu respuesta:")
        
    p7 = st.text_input("respuesta 7")
    if p7:
        pregresp = pregresp + 1
        if "todo" in p7.lower():
            reppreguntas = 1
            puntos = puntos + 2
            st.success("EXACTO, TODOOO (+2pts)")
        elif "cachet" in p7.lower():
            reppreguntas =1
            puntos = puntos + 1
            st.success("Uhum... y morderloss (+1pts)")
        elif "piern" in p7.lower():
            reppreguntas =1
            puntos = puntos + 1
            st.success("Super sexys (+1pts)")
        elif "lunar" in p7.lower():
            reppreguntas = 1
            puntos = puntos + 1
            st.success("Los lunares de tu carita son super hermosos (+1pts)")
        else:
            reppreguntas = 1
            puntos = puntos + 1
            aleatorio = random.choice(resprandomeu)
            st.success(aleatorio)
            
    else:
        st.error("Tienes que responer la pregunta")
    st.divider()

    nopregunta = nopregunta + 1
    st.title(f":blue[PREGUNTA NO. {nopregunta}]")
    st.subheader(f":blue[La pregunta No. {nopregunta} dice: ]")
    with st.container(border=True):
        st.write("¿Cuando muera que canción me gustaría que sonara?")
    col1, col2 = st.columns(2)
    with col1:
        st.info("Rises the moon - Liana Flores")
        st.info("Piensa en mí - Natalia Lafourcade con Vicentico")
        st.info("Solifican12 - Milo J")
        st.info("Soledad y el Mar - Natalia Lafourcade")
        st.info("Let You Break My Heart Again - Laufey")
    p8 = st.text_input("respuesta 8")     
    if p8:
        pregresp = pregresp + 1
        if "moon" in p8.lower() or "piensa" in p8.lower():
            reppreguntas = 1
            puntos = puntos + 1
            resppreguntas()
        elif "soledad" in p8.lower():
            reppreguntas = 0.5
            puntos = puntos + 0.5
            resppreguntas()
        else:
            reppreguntas = 0
            puntos = puntos
            resppreguntas()
    else:
        st.error("Tienes que responer la pregunta")
    st.divider()

    respfinal = 0
         
    if pregresp > 7.9:
     st.title("HAS TERMINADO TODAS LAS PREGUNTAS")
     st.success("Muy bien! Ya respondiste todas las preguntas, pero antes tengo una ULTIMA PREGUNTA PARA TI")
     st.success("Si aciertas ganarás 1 punto, pero si fallas sumarás 2 puntos (no hay opción múltiple)")
     final = st.text_input("¿Quieres intentar la pregunta final?")
     if "si" in final.lower():
         if "si" in final:
             st.write("Ok, vamos entonces")
             st.title(f":blue[PREGUNTA FINAL]")
             st.subheader("La pregunta final dice:")
             with st.container(border=True):
                 st.write("Si pudiera elegir una manera de morir ¿Cuál sería?")
         pf = st.text_input("respuesta final")
         if pf:
             if "ahoga" in pf.lower():
                 st.success("MUY BIEN, tu respuesta es correcta (+1pts)")
                 reppreguntas = 1
                 puntos = puntos + 1
                 respfinal = 1
             elif "senton" in pf.lower():
                 st.warning("Y tú como sabes? 😉 (+0.5pts)")
                 reppreguntas = 0.5
                 puntos = puntos + 0.5
                 respfinal = 1
             elif "nalg" in pf.lower():
                 st.warning("Y tú como sabes? 😉 (+0.5pts)")
                 reppreguntas = 0.5
                 puntos = puntos + 0.5
                 respfinal = 1
             else:
                 st.error("INCORRECTO (-2 pts)")
                 reppreguntas = 0
                 puntos = puntos - 2
                 resppreguntas()
                 respfinal = 1
     else:
      if final:
       pff = 1
       st.write("Okay")

    if pregresp > 6.9:
         
        st.title("ahora si vamos a ver tu resultado final")
        with st.container(border=True):
             if puntos < 6:
              st.write("Tu puntuación final fué de:", puntos, "pts/6pts")
             else:
                 st.write("Tu puntuación final fué de:", puntos, "pts/10pts")
        if puntos < 3:
            st.error("No me conoces nada 😭")
        elif 3.5 <= puntos <= 5.5:
            st.warning("Me conoces maso")
        elif puntos == 6:
            st.info("Me conoces bien")
        elif 6.5 <= puntos <= 9.5:
            st.success("Me conoces super bien 😀")
        elif puntos == 10:
            st.success("ME CONOCES PERFECTAMENTE")
        elif 10.66 <= puntos <= 10.69:
            st.success("Me conoces super six seven omg")
            st.success("SIXSEVENSIXSEVENSIXSEVENSIXSEVENSIXSEVENSIXSEVEN")
        elif 10.70 <= puntos <= 12:
            st.success("ME CONOCES SUPER PERFECTAMENTE, ERES EL AMOR DE MI VIDA")
            st.write("Has conseguido el 100% del juego, ¡Felicidades!")
            st.write("Muchas gracias por jugar el juego y conseguir el 100%, tu recompensa es...")
            st.title("COMIDA GRATIIISS")
            st.subheader("(recuerda pedirmela)")
    
    with st.container(border=True):
        st.write("Muchas gracias por jugar jugar el jueguito, espero que te haya gustado, sub y like 👍")
        st.title(f":blue[Tu puntuación final fué de {puntos}] 🎉")
    
    reiniciotodo = st.button("Quieres volver a jugar desde el inicio?")
    if reiniciotodo:
        reinicio2()
        st.title("para volver a jugar, sube hasta el tope y vuelve a escribir que estás lista para responder las preguntas")
 
if lista:
 if "si" or "lista" or "uhum" in lista.lower():
  st.success("Muy bien, empecemos entonces")
  masnopregunta()
 else:
  st.error("No importa, igual tienes que responder muajajaja 😈")
  masnopregunta()