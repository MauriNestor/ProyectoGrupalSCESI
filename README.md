# Equipo **GRUPO BOMB SQUAD**

## GitFlow utilizado en el proyecto

El gitFlow que se utilizará en este proyecto es : **Ship/Show/Ask**.

## Bitacora del proyecto

### Descripcion
El mini-proyecto a desarrollar por este equipo es el de **Buscaminas en Python con Flask**,  es una implementación del clásico juego de buscaminas utilizando el lenguaje de programación Python y el framework web Flask. El juego consiste en descubrir todas las casillas del tablero sin hacer clic en ninguna mina. Cada casilla puede contener una mina o un número que indica la cantidad de minas adyacentes.

## Conclusiones de uso GIT
### Revision de Mauricion a Aron:
**Buenas practicas**
- commits pequeños, con pequeñas mejoras
- No utlizo puntos finales ni suspensivos para el titulo de commits
- titulos de commits menores a 50 caracteres

**Malas practicas**
- titulo de commit no usa un verbo imperativo
- ningun prefijo usado para hacer commit mas semanticos
- nombre de ramas poco consistente
- No uso nombre de accion que se realizara en la rama, por ejemplo: bug, feature, etc. 
- nulo uso de pull request

### Revision de Giuliano a Mauricio:
**Buenas practicas**

**Malas practicas**

### Revision de Mita a Guilanno:

### Revision de Aron a Mita:


## Git Aliases
Para optimizar el flujo de trabajo y mejorar la eficiencia del equipo, debia averce usado la configuracion de los siguientes aliases de Git que simplifican comandos frecuentemente utilizados:

- **Configuracion alias 'lg'**: Este alias es una abreviatura para `git log --oneline --graph --decorate`, lo que nos permite visualizar el historial de commits de una manera compacta y gráfica, facilitando la comprensión de la evolución del proyecto.
  ```bash
  git config --global alias.lg "log --oneline --graph --decorate" # Configura el alias 'lg'
  git lg # Muestra el historial de commits utilizando el alias 'lg'.
    - co: Alias para git checkout.

- **Configurar alias 'co'**: Este alias simplifica el cambio entre ramas o la restauración de archivos, haciendo el comando `git checkout` más rápido y fácil de usar. Para establecer este alias, ejecuta el siguiente comando:
  ```bash
  git config --global alias.co checkout # Configura el alias 'co' para 'git checkout'.
  git co develop # Cambia a la rama 'develop' utilizando el alias 'co'.

## Equipo de trabajo
- [@MauricioNestor](https://github.com/MauriNestor)
- [@Aron6625](https://github.com/Aron6625)
- [@GiuliannoMorales](https://github.com/GiuliannoMorales)
- [@mita08mm](https://github.com/mita08mm)

### Obejtivos Principales
- Hacer uso de git para versionamiento y desarrollo paralelo
- Adoptar flujo de trabajo que mas conozcamos o nos llame la atencion
- Aplicar buenas prácticas de desarrollo de software, incluyendo el uso de control de versiones con Git y el flujo de trabajo Ship, Show, Ask.
- Mejorar las habilidades de trabajo en equipo y colaboración en un proyecto de software.


### Objetivos Secundarios
- Desarrollar una versión funcional del juego de buscaminas que pueda ser jugada en un navegador web.
- Utilizar tecnologías modernas como Python, Flask, HTML y CSS para la implementación del juego.

### Buenas Prácticas Aplicadas en General:
#### Control de Versiones con Git:
Utilización de ramas para el desarrollo de nuevas funcionalidades y la resolución de problemas.
Flujo de Trabajo Ship, Show, Ask: Publicación periódica de avances del proyecto, demostraciones y solicitudes de retroalimentación.
#### Revisión de Código: 
Revisión regular del código por parte de otros miembros del equipo para identificar posibles mejoras y errores.
#### Documentación Clara y Concisa: 
Uso de comentarios en el código y documentación adicional para facilitar la comprensión y mantenimiento del proyecto.

###  Malas Prácticas en General:
**nombramiento de ramas incorrecto** Creacion de ramas innecearias, con nombres inapropiados.
**Falta de Comunicación:** Baja participación entre los mienbros.
**Ignorar las pruebas locales:** Código desorganizado y mal estructurado.

#### nombres de commits extraños
En muchos casos se uso nombres que no son estadares para nombramiento de commits

### Conclusión

El proyecto "Buscaminas en Python con Flask" fue un ejemplo de cómo intentar aplicar buenas prácticas de desarrollo de software y colaboración en equipo para crear una aplicación web funcional y de calidad. La adopción de un flujo de trabajo estructurado fue un poco limitada debido a poco compromiso en general del equipo.