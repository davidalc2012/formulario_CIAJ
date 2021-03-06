# Esquema base de los formularios

En este documento se explica cómo serán almacenadas las diferentes preguntas de un formulario en un documento JSON.

La estructura está dividida en 3 objetos principales: **//TODO: ¿Son los únicos objetos generales?**

* **General**: Incluye la información necesaria del formaluario
* **Pregunta**: El objeto con la información necesaria para cada pregunta, esto también puede replicarse en preguntas anidadas. Este objeto será genérico e indiferente del nivel en el que se encuentre y contiene toda la información sobre el tipo de respuesta, limitaciones y objetos necesarios para su despliegue.
* **Limitaciones**: Arreglo que contiene todas aquellas limitaciones a las que pueda ser sometido de validación alguna pregunta o funcionalidad específica. En los casos de las limitaciones tipo boolean, si esta no es incluída se considerará False
* **Condiciones**: Objeto que contiene las diferentes condiciones para bloquear, desbloquear, ocultar o mostrar un campo específico. **//TODO: Revisar si es necesario agregar condiciones para el comportamiento de los campos**

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

**//TODO: Añadir manejo de campos repetidos en bloque**

### Limitaciones:

#### limitations:

Información sobre la validación de cada campo específico

##### Tipo de campos: **//TODO: cehcar compatibilidad de tipos de campos para diferentes dispositivos y navegadores**
[input introduction](http://html5doctor.com/html5-forms-introduction-and-new-attributes/)
[HTML5 Input Types](http://html5doctor.com/html5-forms-input-types/)
[HTML Input types](https://html.com/attributes/input-type/)

| Campo | Descripción |
|:----:|:----:|
| text | Campo de texto simple |
| password | Entrada de texto en formato de contraseña |
| checkbox |  |
| radiobutton |  |
| submit | Botón que ejecuta la acción para enviar el formulario |
| button | Botón simple. Debe ligarse una acción de JavaScript |
| file | Permite subir archivos al formulario |
| hidden | Oculta el campo del formulario |
| reset | Resetea el valor de todos los campos del formulario |
| textarea | Permita la entrada de texto multilínea |
| select | Lista desplegable |
| email |  |
| url |  |
| tel |  |
| number |  |
| range |  |
| date |  |
| month |  |
| week |  |
| time |  |
| datetime |  |
| datetime-local |  |
| color |  |
| output | Permite mostrar resultados del procesamiento de los demás campos mediante una función JS |  |

##### Tipos de limitaciones:

| Valor | Descripción | Tipo | Input válidos |
|:----:|:----:|:----:|:----:|
| step | Saltos que se dará en la elección del número | float | number, range |
| required | Define si el campo es obligatorio o no | Boolean |  |
| readonly | Impide al usuario editar el campo | Boolean |  |
| placeholder | Texto que muestra indicaciones sobre la información que debe ser introducida en el campo |  | text, textarea, email, url, tel |
| pattern | Expresión regular que indica un aptrón para el texto introducido | String | text, textarea, email, tel, url |
| multiple | Permite introduci varios elementos en un campo | Boolean | file, email, text |
| min | Valor mínimo | Float, int | number, date, range |
| max | Valor máximo | Float, int | number, date, range |
| list | Permite añadir una lista de sugerencia de respuestas sin ser estas obligatorias | <datalist> <option>... | text, ... | [Atributo list](https://html.com/attributes/input-list/)
| autofocus | Indica si este campo es seleccionado desde que carga | Boolean |  |
| accesskey | Shortcut para ejecutar una acción específica | String |  |
| autocomplete | Activar el autocompletamiento según entradas pasadas del usuario en campos similares | Boolean |  |
| checked | Indica si el campo está activado | Boolean | checkbox, radiobutton |
| disabled | Se usa para saber si el campo se encuentra desactivado | Boolean |  |
| maxlength | Longitud máxima en caracteres de la respuesta | int | text, textarea, tel, email, password,  |
| size | Permite modificar el tamaño de los caractéres del campo. Revisar compatibilidad | int |  |
| src | Dirección a la imagen a ser mostrada | String | image |

#### repeatLimitations:

Información sobre las limitaciones de la funcionalidad de repetición. Sólo se toman en cuenta cuando el atributo doesRepeat es True.

| Valor | Descripción | Tipo |
|:----:|:----:|:----:|
| minRepeats | Indica el número mínimo de repeticiones. Si no se incluye no hay número mínimo de repeticiones | int |
| maxRepeats | Indica el número máximo de repeticiones. Si no se incluye no hay número máximo de repeticiones | int |


### Condiciones

| Valor | Descripción |
|:----:|:----:|
| hideIfParent | Esconde si se cumple(n) la(s) condicion(es) para la pregunta padre |
| showIfParent | Muestra si se cumple(n) la(s) condicion(es) para la pregunta padre |
| blockIfParent | Bloquea si se cumple(n) la(s) condicion(es) para la pregunta padre |
| unblockIfParent | Desbloquea si se cumple(n) la(s) condicion(es) para la pregunta padre |
| hideIfChildren | Esconde si se cumple(n) la(s) condicion(es) para la(s) pregunta(s) hijo |
| showIfChildren | Muestra si se cumple(n) la(s) condicion(es) para la(s) pregunta(s) hijo |
| blockIfChildren | Bloquea si se cumple(n) la(s) condicion(es) para la(s) pregunta(s) hijo |
| unblockIfChildren | Desbloquea si se cumple(n) la(s) condicion(es) para la(s) pregunta(s) hijo |
| setIf | Asigna un valor específico |
| deleteIf | Borra este campo del formulario. Esta acción no puede deshacerse |
