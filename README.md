# Distributed Problem Solver System

## Descripción General
Este proyecto consiste en un sistema de software distribuido compuesto por tres módulos principales: **Client**, **ProblemSolver** y **DataServer**.

El sistema está diseñado para generar datos y resolver problemas computacionales a partir de solicitudes del usuario, siguiendo una arquitectura modular y comunicación entre servicios.

---

## Descripción del Sistema
El sistema funciona mediante la interacción de tres componentes independientes:

- **Client**: Gestiona la interacción con el usuario a través de una interfaz de línea de comandos (CLI).
- **ProblemSolver**: Procesa el problema solicitado utilizando datos obtenidos desde el DataServer.
- **DataServer**: Genera datos numéricos aleatorios basados en diferentes distribuciones de probabilidad.

Estos módulos trabajan conjuntamente para ejecutar el flujo completo de resolución de problemas.

---

## Arquitectura
El sistema sigue una arquitectura modular distribuida:

- La comunicación entre **Client → ProblemSolver** se realiza mediante **sockets** usando formato JSON.
- La comunicación entre **ProblemSolver → DataServer** se realiza mediante **HTTP** usando formato JSON.
- Se garantiza la confidencialidad de los datos durante la transmisión entre servicios.

---

## Módulos

### Client (Golang)
**Responsabilidades:**
- Proporciona una interfaz CLI para:
  - Seleccionar el problema a resolver
  - Definir la cantidad de valores a procesar
- Muestra o guarda los resultados en disco
- Permite apagar el sistema mediante un mecanismo de autenticación

**Tecnologías:**
- Golang
- Comunicación por sockets (JSON)

---

### ProblemSolver (Python)
**Responsabilidades:**
- Consume datos del DataServer
- Resuelve el problema solicitado
- Mantiene un registro (log) de operaciones

**Características clave:**
- Uso de **patrones de diseño creacionales** para instanciar problemas
- Garantiza la **confidencialidad de datos** en la comunicación

**Tecnologías:**
- Python

---

### DataServer (Flask - Python)
**Responsabilidades:**
- Genera números enteros positivos de forma aleatoria usando:
  - Distribución uniforme
  - Distribución normal
- Expone los datos mediante endpoints HTTP en formato JSON
- Mantiene un registro (log) de operaciones

**Características clave:**
- Aplicación del principio de **inversión de dependencias**
- Soporte para múltiples distribuciones de probabilidad

**Tecnologías:**
- Python (Flask)

---

## Problemas Soportados
El sistema permite resolver los siguientes problemas:

- **FizzBuzz**
- **Fibonacci Verifier**
- **Prime Classifier**:
  - Número primo
  - Semiprimo
  - Semiprimo-cuadrático
  - Ninguno de los anteriores

---

## Estrategia de Pruebas

El proyecto sigue un enfoque basado en la **pirámide de pruebas**:

### Pruebas Unitarias
- Implementadas en:
  - ProblemSolver (usando pytest)
  - DataServer (usando Postman)
- Validan:
  - Lógica de resolución de problemas
  - Encriptación y desencriptación
  - Respuestas HTTP y códigos de estado

### Pruebas End-to-End
- Validación completa del sistema
- Implementadas mediante **comparación de archivos**
- Verifican que la salida del sistema coincida con el resultado esperado

---

## Enfoque de Desarrollo (TDD)
El sistema fue desarrollado siguiendo el ciclo de **Test-Driven Development (TDD)**:

- **RED**: Pruebas fallidas iniciales por errores de lógica, sintaxis o concepto  
- **GREEN**: Corrección del código hasta que todas las pruebas pasan  

Este enfoque permitió identificar:
- Errores lógicos
- Problemas conceptuales (como la clasificación de semiprimos)
- Inconsistencias entre resultados esperados y obtenidos

---

## Consideraciones de Seguridad
- Se garantiza la confidencialidad de los datos en la comunicación entre módulos
- Se implementan mecanismos de encriptación y desencriptación validados mediante pruebas

---

## Flujo de Ejecución
1. El usuario interactúa con el **Client**
2. El Client envía la solicitud a **ProblemSolver**
3. ProblemSolver solicita datos a **DataServer**
4. DataServer genera y retorna los datos
5. ProblemSolver procesa la información
6. Los resultados son enviados de vuelta al Client

---

## Estructura del Proyecto
client/

DataServer/

problemSolver/

---

## Conclusión
Este proyecto demuestra la implementación de un sistema distribuido que integra múltiples tecnologías y principios de diseño, como arquitectura modular, comunicación entre servicios y desarrollo guiado por pruebas.

También evidencia los retos asociados al trabajo con múltiples lenguajes y la correcta integración entre componentes.

---

## Referencias
- StackOverflow
- Documentación técnica de Golang y Python
- Herramientas de inteligencia artificial como apoyo al desarrollo
