# Esquema base de los formularios

En este documento se explica cómo serán almacenadas las diferentes preguntas de un formulario en un documento JSON.

La estructura está dividida en 3 objetos principales: **//TODO: ¿Son los únicos objetos generales?**

* **General**: Incluye la información necesaria del formaluario
* **Pregunta**: El objeto con la información necesaria para cada pregunta, esto también puede replicarse en preguntas anidadas. Este objeto será genérico e indiferente del nivel en el que se encuentre y contiene toda la información sobre el tipo de respuesta, limitaciones y objetos necesarios para su despliegue.
* **Limitaciones**: Arreglo que contiene todas aquellas limitaciones a las que pueda ser sometido de validación alguna pregunta o funcionalidad específica.

### General:

| Valor | Descripción | Tipo | Posibilidades |
|:----:|:----:|:----:|:----:|
| idForm | Identificador del formulario | int |  |
| title | Título del formulario | String |  |
| version | Versión en la que se encuentra el formulario | String | "1", "1.1", "1.2", ... |  **//TODO: Definir el manejo de versiones**
| date | Fecha en la que se actualizó el formulario | String | "AAAA-MM--DD" |
| description | Breve descripción del uso del formulario y su contenido | String |  |
| questions | Arreglo con objetos de preguntas | Array | [{P1}, {P2}] |

### Preguntas:

| Valor | Descripción | Tipo | Posibilidades |
|:----:|:----:|:----:|:----:|
| id | Identificador de la pregunta | String | "1", "1.1", "1.2", "1.2.1" | **//TODO: Definir si combiene un entero o String para ver ID anidado**
| text | Texto que se desplegará dentro del formulario | String | "Nombre", "Edad" |
| description | Descripción sobre la pregunta, no será visible en el formulario | String |  |
| name | Nombre con el cuál se hará referencia para el envío de las variables al servidor | String |  |
| placeholder | Texto que será mostrado en algunos campos del formulario como *hint*. No está disponible en todos los tipos de -Input- de HTML | String | "a@b" |
| value | Valor inicial del campo. Si este valor es usado el atributo *placeholder* se desactiva | String |  |
| type | Tipo de pregunta | String | [text, textarea, email, tel, range, number, date, radiobutton, checkbutton, etc...] |
| doesRepeat | Indica si esta pregunta incluye funcionalidad para ser introducido en repetidas ocasiones cuyo número es, generalmente, desconocido | Boolean | True - False |
| repeatLimitations | Objeto con información sobre las limitaciones de las posibles repeticiones del campo | Object | {"maxRepeats": #} |
| limitations | Objeto que incluye las posibles limitaciones para la validación del campo | Object | {"min": #, "max": #} |
| elements | En los casos de los campos que requieran un número limitado de respuestas se debe listar los elementos del mismo. Ej: select, list, etc | Array | ["A", "B", "C"] |

### Limitaciones:

#### limitations:

Información sobre la validación de cada campo específico

##### Tipo de campos: **//TODO: cehcar compatibilidad de tipos de campos para diferentes dispositivos y navegadores**
| Campo | Descripción | Posibilidades |
|:----:|:----:|:----:|:----:|
| text |  |  |  |
| password |  |  |  |
| checkbox |  |  |  |
| radio |  |  |  |
| submit |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

#### repeatLimitations:

Información sobre las limitaciones de la funcionalidad de repetición

| Valor | Descripción | Tipo | Posibilidades |
|:----:|:----:|:----:|:----:|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

