## Para escuchar el audio con el microfono de la computadora
import speech_recognition as sr
import subprocess as sub 
import pyautogui as auto
import pyttsx3 as voz
from time import sleep


def interpretar (comando_de_audio):
    comando_de_audio=comando_de_audio.split(' ')
    ver_codigo=('código' or 'github')in comando_de_audio
    inteligencia=('inteligencia' and 'artificial') in comando_de_audio
    prueba_Turing=('turing') in comando_de_audio
    ia_Debil=('débil') in comando_de_audio
    ia_Fuerte=('fuerte') in comando_de_audio
    salir=('salir' or 'finalizar') in comando_de_audio
    percepcion=('percepción') in comando_de_audio
    agente_Simple=('simple')in comando_de_audio
    agente_Objetivos=('agente' and 'basado' and 'en' and 'objetivos') in comando_de_audio
    agente_Utilidad=('agente' and 'basado' and 'en' and 'utilidad') in comando_de_audio
    agente=('agente') in comando_de_audio

    a_res1=('resolvente' or 'problema'or 'problemas') in comando_de_audio
    objetivo=('objetivo') in comando_de_audio
    estado=('estado') in comando_de_audio
    solucion=('solución') in comando_de_audio
    abstraccion=('abstracción') in comando_de_audio
    bus_h=('busqueda' and 'heurística') in comando_de_audio
    bus_n_i=('búsqueda' and 'no' and 'informada') in comando_de_audio
    busqueda=('búsqueda') in comando_de_audio
    restriccion=('restricción' or 'restricciones') in comando_de_audio
    sbc=('sbc' or 'sistemas') in comando_de_audio
    conocimiento=('conocimiento') in comando_de_audio
    regla=('regla' or 'reglas') in comando_de_audio
    al_inf=('inferencia') in comando_de_audio
    red_sem=('semánticas') in comando_de_audio
    raz=('razonamiento') in comando_de_audio
    raz_pro=('progresivo') in comando_de_audio
    raz_reg=('regresivo') in comando_de_audio
    log_p=('proposicional') in comando_de_audio
    raz_inc=('incertidumbre') in comando_de_audio
    mod_proba=('probabilísticos') in comando_de_audio
    red_baye=('redes' and 'bayesianas') in comando_de_audio
    mod_mar=('modelos' and 'markov') in comando_de_audio
    met_reg=('metodos' and 'reglas') in comando_de_audio
    arb_reg=('arboles' and 'regresión') in comando_de_audio
    mod_bio=('modelos' and 'bioinspirados') in comando_de_audio
    red_neu=('redes' and 'neuronales') in comando_de_audio
    com_evo=('computacion' and 'evolutiva') in comando_de_audio
    apli_uso=('aplicaciones' or 'aplica') in comando_de_audio
    agente_Modelos=('agente' and 'basado' and 'en' and 'modelos') in comando_de_audio
   
    if ver_codigo is True:
        abrir_codigo()
    elif inteligencia is True:
        abrir_Inteligencia()
    elif salir is True:
        cerrar()
    elif prueba_Turing is True:
        abrir_Turing()
    elif ia_Debil is True:
        abrir_Debil()
    elif ia_Fuerte is True:
        abrir_Fuerte()
    elif agente_Simple is True:
        abrir_Agente_Simple()
    elif agente_Objetivos is True:
        abrir_Agente_Objetivos()
    elif agente_Utilidad is True:
        abrir_Agente_Utilidad()
    elif a_res1 is True:
        a_res()    
    elif percepcion is True:
        abrir_Percepcion()
    elif objetivo is True:
        abrir_objetivo()
    elif estado is True:
        abrir_estado()
    elif solucion is True:
        abrir_solucion()
    elif abstraccion is True:
        abrir_abstraccion()
    elif bus_h is True:
        abrir_bus_h()   
    elif bus_n_i is True:
        abrir_bus_n_i()
    elif busqueda is True:
        abrir_busqueda()        
    elif restriccion is True:
        abrir_restriccion()
    elif sbc is True:
        abrir_sbc()
    elif conocimiento is True:
        abrir_conocimiento()
    elif regla is True:
        abrir_regla()
    elif al_inf is True:
        abrir_al_inf()
    elif red_sem is True:
        abrir_red_sem()
    elif raz_pro is True:
        abrir_raz_pro()
    elif raz_reg is True:
        abrir_raz_reg()
    elif log_p is True:
        abrir_log_p()
    elif raz_inc is True:
        abrir_raz_inc()
    elif raz is True:
        abrir_raz()
    
    elif mod_proba is True:
        modelos_proba()

    elif red_baye is True:
        redes_baye()

    elif mod_mar is True:
        redes_mar()

    elif met_reg is True:
        metodos_reglas()

    elif arb_reg is True:
        arboles_regresion()

    elif mod_bio is True:
        modelos_bio()

    elif red_neu is True:
        redes_neuro()

    elif com_evo is True:
        compu_evolutiva()

    elif apli_uso is True:
        aplicaciones()

    elif agente_Modelos is True:
        abrir_Agente_Modelos()

    elif agente is True:
        abrir_Agente()
        
def abrir_Inteligencia():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Inteligencia Artificial: Existen cuatro principales enfoques para definir la Inteligencia Artificial: \n\tSistemas que piensan como humanos: Involucra la automatización de actividades que tienen que ver con el proceso de pensamiento humano. \n\tSistemas que actúan como humanos: Involucra el desarrollo de máquinas con capacidad de realizar funciones como los humanos. \n\tSistemas que piensan racionalmente: Involucra el estudio de las facultades mentales mediante el uso de modelos computacionales. \n\tSistemas que actúan racionalmente: Involucra el estudio del diseño de agentes inteligentes.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Inteligencia Artificial: Existen cuatro principales enfoques para definir la Inteligencia Artificial: Sistemas que piensan como humanos: Involucra la automatización de actividades que tienen que ver con el proceso de pensamiento humano. Sistemas que actúan como humanos: Involucra el desarrollo de máquinas con capacidad de realizar funciones como los humanos. Sistemas que piensan racionalmente: Involucra el estudio de las facultades mentales mediante el uso de modelos computacionales. Sistemas que actúan racionalmente: Involucra el estudio del diseño de agentes inteligentes.')
    dani.runAndWait()
    
def abrir_codigo():
    sub.call([r'C:/Users/Lupita/Desktop/ProyectoIA/Proyecto/navegar.bat'])
    return None
def cerrar():
    sleep(1.5)
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Gracias por participar')
    dani.runAndWait()
    print('Que te vaya bonito')
    exit()
def abrir_Turing():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Prueba de Turing: Prueba diseñada para proporcionar una definición operacional y satisfactoria de inteligencia.\nSirve para diferenciar entre entidades inteligentes y seres humanos.\nNo existe interacción física entre el evaluador y el computador. \nPara que la entidad inteligente pase la prueba, ésta debe estar dotada de Visión computacional y Robótica.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Prueba de Turing: Prueba diseñada para proporcionar una definición operacional y satisfactoria de inteligencia. Sirve para diferenciar entre entidades inteligentes y seres humanos. No existe interacción física entre el evaluador y el computador. Para que la entidad inteligente pase la prueba, ésta debe estar dotada de Visión computacional y Robótica.')
    dani.runAndWait()
def abrir_Debil():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('IA débil: Hipótesis que afirma que es posible que las máquinas actúen con inteligencia. Es la idea más extendida entre los desarrolladores.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('IA débil: Hipótesis que afirma que es posible que las máquinas actúen con inteligencia. Es la idea más extendida entre los desarrolladores.')
    dani.runAndWait()
def abrir_Fuerte():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('IA fuerte: Hipótesis que afirma que las máquinas son capaces de pensar.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('IA fuerte: Hipótesis que afirma que las máquinas son capaces de pensar.')
    dani.runAndWait()
def abrir_Agente():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Agente: Es algo que razona y está dotado de controles autónomos, son capaces de percibir su entorno, pueden persistir durante un \n período prolongado, se adaptan a los cambios y son capaces de alcanzar objetivos diferentes.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Agente: Es algo que razona y está dotado de controles autónomos, son capaces de percibir su entorno, pueden persistir durante un período prolongado, se adaptan a los cambios y son capaces de alcanzar objetivos diferentes')
    dani.runAndWait()
def abrir_Percepcion():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Percepción: Se refiere a la habilidad del agente para recibir entradas en cualquier instante.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Percepción: Se refiere a la habilidad del agente para recibir entradas en cualquier instante.')
    dani.runAndWait()
def abrir_Agente_Simple():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Agente reactivo simple: Es el agente más sencillo y seleccionan las acciones a partir de las percepciones actuales, ignorando todas las percepciones pasadas.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Agente reactivo simple: Es el agente más sencillo y seleccionan las acciones a partir de las percepciones actuales, ignorando todas las percepciones pasadas.')
    dani.runAndWait()
def abrir_Agente_Modelos():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Agente reactivo basado en modelos: Maneja un estado interno que depende de las percepciones pasadas y éstas deben irse actualizando.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Agente reactivo basado en modelos: Maneja un estado interno que depende de las percepciones pasadas y éstas deben irse actualizando.')
    dani.runAndWait()
def abrir_Agente_Objetivos():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Agente basado en objetivos: Además de la descripción del estado actual, el agente necesita información sobre su meta, es decir, las situaciones que son deseables y posibles.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Agente basado en objetivos: Además de la descripción del estado actual, el agente necesita información sobre su meta, es decir, las situaciones que son deseables y posibles.')
    dani.runAndWait()
def abrir_Agente_Utilidad():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Agente basado en utilidad: Además de la descripción del estado actual y una meta, es necesario distinguir los estados de mayor utilidad.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Agente basado en utilidad: Además de la descripción del estado actual y una meta, es necesario distinguir los estados de mayor utilidad.')
    dani.runAndWait()
    
def a_res():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Agentes resolventes-problemas: Agentes inteligentes cuyo propósito es encontrar una secuencia de acciones para cumplir un estado objetivo.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Agentes resolventes-problemas: Agentes inteligentes cuyo propósito es encontrar una secuencia de acciones para cumplir un estado objetivo.')
    dani.runAndWait()
    
def abrir_objetivo():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Objetivo: Conjunto de estados del mundo que satisfacen un problema.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Objetivo: Conjunto de estados del mundo que satisfacen un problema.')
    dani.runAndWait()
    
def abrir_estado():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Estado: Descripción actual del mundo o problema.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Estado: Descripción actual del mundo o problema.')
    dani.runAndWait()
    
def abrir_busqueda():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Búsqueda: Proceso para hallar una secuencia que cumple un objetivo.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Búsqueda: Proceso para hallar una secuencia que cumple un objetivo.')
    dani.runAndWait()
    
def abrir_solucion():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Solución: Camino de un estado inicial a un estado objetivo. La resolución de problemas se lleva a cabo por medio de búsquedas en el espacio otorgado.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Solución: Camino de un estado inicial a un estado objetivo. La resolución de problemas se lleva a cabo por medio de búsquedas en el espacio otorgado.')
    dani.runAndWait()
    
def abrir_abstraccion():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Abstracción: Proceso de eliminar detalles de una representación sin perder su significado.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Abstracción: Proceso de eliminar detalles de una representación sin perder su significado.')
    dani.runAndWait()
    
def abrir_bus_n_i():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Búsqueda no informada: Solo se proporciona la información del estado que define el problema, genera los estados conforme se avanza al objetivo. Algunos ejemplos son: búsqueda por amplitud, búsqueda primero en profundidad y búsqueda de costo uniforme.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Búsqueda no informada: Solo se proporciona la información del estado que define el problema, genera los estados conforme se avanza al objetivo. Algunos ejemplos son: búsqueda por amplitud, búsqueda primero en profundidad y búsqueda de costo uniforme.')
    dani.runAndWait()
    
def abrir_bus_h():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Búsqueda heurística: También conocida como búsqueda informada, utiliza información adicional específica para cada problema más allá de la definición. Las funciones heurísticas son fundamentales (cálculo del camino más corto del inicio al fin) para estas búsquedas. Algunos ejemplos son: búsqueda A*, búsqueda voraz y el algoritmo Dijkstra.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Búsqueda heurística: También conocida como búsqueda informada, utiliza información adicional específica para cada problema más allá de la definición. Las funciones heurísticas son fundamentales (cálculo del camino más corto del inicio al fin) para estas búsquedas. Algunos ejemplos son: búsqueda A*, búsqueda voraz y el algoritmo Dijkstra.')
    dani.runAndWait()
    
def abrir_restriccion():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Problemas de satisfacción de restricciones: Las variables correspondientes poseen un dominio, impidiendo que tomen ciertos valores. Se resuelven por medio de algoritmos como la búsqueda con vuelta atrás y el ascenso de colinas.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Problemas de satisfacción de restricciones: Las variables correspondientes poseen un dominio, impidiendo que tomen ciertos valores. Se resuelven por medio de algoritmos como la búsqueda con vuelta atrás y el ascenso de colinas.')
    dani.runAndWait()
    
def abrir_sbc():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('SBC: Sistemas basados en conocimientos, expresan el conocimiento de forma que humanos y ordenadores puedan entender.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('SBC: Sistemas basados en conocimientos, expresan el conocimiento de forma que humanos y ordenadores puedan entender.')
    dani.runAndWait()
    
def abrir_conocimiento():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Conocimiento: Un concepto que se puede considerar como un conjunto de hechos o verdades sobre un tema. Desde un punto de vista computacional, es el mapeo entre objetos y relaciones del dominio de un problema. \nAl representarlo, se deben cumplir cuatro condiciones: adecuación, eficiencia, extensibilidad y propiedad.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Conocimiento: Un concepto que se puede considerar como un conjunto de hechos o verdades sobre un tema. Desde un punto de vista computacional, es el mapeo entre objetos y relaciones del dominio de un problema. \nAl representarlo, se deben cumplir cuatro condiciones: adecuación, eficiencia, extensibilidad y propiedad.')
    dani.runAndWait()
    
def abrir_regla():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Reglas: Restricciones independientes que definen secciones del conocimiento y aseguran cumplir con un dominio para la resolución de conflictos.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Reglas: Restricciones independientes que definen secciones del conocimiento y aseguran cumplir con un dominio para la resolución de conflictos.')
    dani.runAndWait()
    
def abrir_al_inf():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Algoritmos de inferencia: Determinan cómo utilizar una base de conocimiento. Se dividen en tres grandes familias: encadenamiento hacia adelante, encadenamiento hacia atrás y sistemas de demostración de teoremas basados en la resolución.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Algoritmos de inferencia: Determinan cómo utilizar una base de conocimiento. Se dividen en tres grandes familias: encadenamiento hacia adelante, encadenamiento hacia atrás y sistemas de demostración de teoremas basados en la resolución.')
    dani.runAndWait()
    
def abrir_red_sem():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Redes semánticas: Algoritmos eficientes para inferir propiedades de un objeto en base a su pertenencia a cierta categoría. Funcionan como apoyo gráfico para visualizar bases de conocimiento.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Redes semánticas: Algoritmos eficientes para inferir propiedades de un objeto en base a su pertenencia a cierta categoría. Funcionan como apoyo gráfico para visualizar bases de conocimiento.')
    dani.runAndWait()
    
def abrir_raz():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Razonamiento: Proceso para obtener conclusiones, juicios o inferencias a partir de hechos o premisas. Existen varios tipos como el deductivo (movimiento de lo general a lo particular) y el inductivo (basado en observaciones previas).')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Razonamiento: Proceso para obtener conclusiones, juicios o inferencias a partir de hechos o premisas. Existen varios tipos como el deductivo (movimiento de lo general a lo particular) y el inductivo (basado en observaciones previas).')
    dani.runAndWait()
    
def abrir_raz_pro():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Razonamiento progresivo: Evoluciona a una conclusión a partir de las premisas.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Razonamiento progresivo: Evoluciona a una conclusión a partir de las premisas.')
    dani.runAndWait()
    
def abrir_raz_reg():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Razonamiento regresivo: Empieza con la conclusión y decide si las reglas establecidas pueden obtenerla.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Razonamiento regresivo: Empieza con la conclusión y decide si las reglas establecidas pueden obtenerla.')
    dani.runAndWait()
    
def abrir_log_p():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Lógica proposicional: Define las reglas para determinar el valor de verdad de una sentencia.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Lógica proposicional: Define las reglas para determinar el valor de verdad de una sentencia.')
    dani.runAndWait()
    
def abrir_raz_inc():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Razonamiento con incertidumbre: Problema sin modelos exactos ni garantía en su definición, esta incertidumbre se genera cuando hay un conflicto relacionado a los hechos o las reglas. Es posible representarlas con símbolos o números para obtener posibles soluciones.')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Razonamiento con incertidumbre: Problema sin modelos exactos ni garantía en su definición, esta incertidumbre se genera cuando hay un conflicto relacionado a los hechos o las reglas. Es posible representarlas con símbolos o números para obtener posibles soluciones.')
    dani.runAndWait()
    
def modelos_proba():
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Los modelos probabilísticos son una representacion de la realidad sobre la que podemos nosotros hacer inferencias, estos se dividen en 2:Redes Bayesianas y Modelos de Markov')
    dani.runAndWait()

def redes_baye():
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Las redes bayesianas son un tipo de modelo grafo probabilistico la cual se utiliza para representar un conjunto de variables aleatorias y sus dependientes condicionales, a que nos referimos con esto las probabilidades que un evento provoque otro.')
    dani.runAndWait()

def redes_mar():
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('los modelos de Markov son un metodo que se utiliza basicamente para hacer estudios de coste y efectividad.')
    dani.runAndWait()

def metodos_reglas():
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('los metodos con base en reglas son modelos de representacion del conocimiento se usan de una manera muy amplia. De aquí obtenemos los arboles de regresion. ')
    dani.runAndWait()

def arboles_regresion():
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Los árboles de regresión son representaciones graficas que se realizan para resolver problemas, estos se utilizan para crear modelos predictivos de aprendizaje.')
    dani.runAndWait()

def modelos_bio():
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('los modelos bioinspirados son sistemas construidos por medio de un hardware configurables y sistemas electrónicos simulan la forma de pensar, procesar y resolver problemas de sistemas biológicos. De estos surgen las redes neuronales y la computacion evolutiva')
    dani.runAndWait()

def redes_neuro():
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Las redes neuronales estan inspiradas en la biología osea que con este modelo se aprende con la experiencia osea modifica su comportamiento con la respuesta del entorno, este modelo abstrae la informacion del conjunto de entradas que tenga')
    dani.runAndWait()

def compu_evolutiva():
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('La computacion evolutiva trata de resolver problemas, con el fin de encontrar el mejor resultado al problema, podemos decir o referirnos en el entorno del mas fuerte o mas apto sobrevive, en este caso el mejor')
    dani.runAndWait()

def aplicaciones():
    sub.call(('start notepad.exe'), shell=True)
    sleep(1.5)
    auto.write('Los modelos predictivos en el sector público: La gestion de infraestructuras y servicios públicos es complejo y cada decisión debe tener en cuenta muchos parámetros, los elementos como la captación, el procesamiento y el analisis de los datos permite a la (IA) realizar proyecciones más precisas, indicando los diagramas de cada decisión su aporte y coste.\nTambien tenemos la investigación y desarrollo en el ámbito de la salud: La Inteligencia artificial es el núcleo de diferentes programas de investigación, ya que esta ofrece resultados mas prometedores, ya que el analisis predictivo y el reconocimiento de imágenes puede ayudar a salvar pacientes, incluso antes de que se manifieste la enfermedad.\nSeguridad informatica y protección de datos: este es uno de los puntos clave de la inteligencia artificial, ya que el acceso, intercambio y uso de informacion son esenciales para cualquier empresa, cualquier programa basado en ciberseguridad basado en inteligencia artificial ayuda a detectar diferentes fallos en una red.\nFinalmente la traduccion automática: esto es igual enfocado hacia las empresas pero esto es mas en cuestión de dar un buen servicio, para este caso, la inteligencia artificial puede enfocarse en las solicitudes de los clientes traduciendo asi las solicitudes para dar una respuesta adaptada a lo que el cliente necesite. ')
    dani = voz.init()
    velocidad=dani.getProperty('rate')
    dani.setProperty('rate',velocidad-25)
    dani.setProperty('voice','TTS_MS_ES-MX_SABINA_11.0')
    dani.say('Lo más destacado de las aplicaciones son: los modelos predictivos en el sector publico, tambien se tiene la investigacion y desarrollo en el ambito de la salud, seguridad informatica y proteccion de datos y por ultimo en la traduccion automática')
    dani.runAndWait()

##escuchar el audio con el microfono 
c=0
while c!=1:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("¿Qué concepto deseas aprender?")
        audio = r.listen(source)

    try:
        #En caso de entender el audio
        comando=r.recognize_google(audio,language='es-MX')
        print ("Creo que dijiste: " + comando)
        interpretar(comando)
        #En caso de no entender
    except sr.UnknownValueError:
        print("No te pude entender")
    except sr.RequestError as e:
        #En caso de no tener conexión a internet
        print("No pude obtener respuesta del servicio de Google Speech Recognition; {0}".format(e))
