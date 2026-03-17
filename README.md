# Predicción de Aprobación de Préstamos Mediante Aprendizaje Automático

## Contexto del Proyecto

Los préstamos representan uno de los servicios financieros más importantes en el mundo moderno. Para los bancos, constituyen una fuente significativa de ingresos; para los individuos, son una herramienta que facilita el acceso a educación, vivienda, vehículos y otros bienes esenciales.

Sin embargo, la concesión de préstamos conlleva un riesgo inherente: el impago. Determinar si un solicitante tiene el perfil adecuado para recibir un crédito implica analizar múltiples variables de manera simultánea, lo que puede ser una tarea compleja, lenta y propensa a errores humanos cuando se realiza de forma manual.

En este contexto, el aprendizaje automático emerge como una solución eficiente y escalable para automatizar y optimizar el proceso de evaluación de solicitudes de préstamo, reduciendo los tiempos de respuesta y mejorando la precisión en las decisiones crediticias.

### 1. Industria objetivo
El proyecto está dirigido al sector bancario y financiero, con aplicación directa en:
* Bancos comerciales y entidades financieras
* Cooperativas de crédito
* Plataformas de préstamos en línea (Fintech)
* Microfinancieras

### 2. Definición del Problema
El proceso tradicional de evaluación de préstamos depende de analistas humanos que revisan manualmente expedientes y toman decisiones basadas en criterios internos. Este enfoque presenta las siguientes limitaciones:
* Lentitud en el procesamiento de solicitudes, generando tiempos de espera prolongados para el cliente.
* Inconsistencia en los criterios de evaluación entre distintos analistas.
* Dificultad para procesar grandes volúmenes de solicitudes de forma simultánea.
* Mayor riesgo de sesgos subjetivos en la toma de decisiones.
* Costos operativos elevados asociados al personal de evaluación.
    1. #### Pregunta central de investigación
¿Es posible predecir con precisión si un solicitante de préstamo será aprobado o rechazado, utilizando algoritmos de aprendizaje automático y variables socioeconómicas disponibles en el momento de la solicitud?

    2. #### Variables del problema
| #|	Variable            |   Descripción                 |
| - |:-------------|:-------------|
| 1|    Loan_ID             | 	Identificador único del préstamo    |
| 2|    Gender              | 	Género del solicitante	Male / Female|
| 3|    Married             | 	Estado civil del solicitante	Yes / No|
| 4| 	Dependents          | 	Número de personas a cargo	0, 1, 2, 3+|
| 5| 	Education           | 	Nivel educativo del solicitante	Graduate / Not Graduate|
| 6| 	Self_Employed       | 	¿El solicitante es independiente?	Yes / No|
| 7| 	ApplicantIncome     | 	Ingreso mensual del solicitante	|
| 8| 	CoapplicantIncome   | 	Ingreso del co-solicitante	Valor en USD|
| 9| 	LoanAmount          | 	Monto del préstamo solicitado en miles|
| 10| 	Loan_Amount_Term    | 	Plazo del préstamo en meses|
| 11| 	Credit_History      | 	Historial de repago de deudas	1 = Cumple / 0 = No|
| 12| 	Property_Area       | 	Área de ubicación del inmueble	Rural / Urban / Semi-urban|
| 13| 	Loan_Status         | (Objetivo)	Estado de aprobación del préstamo	Y = Aprobado / N = Rechazado |



### 3. Solución Propuesta
La solución consiste en desarrollar un sistema de predicción binaria utilizando algoritmos de aprendizaje automático supervisado, capaz de clasificar automáticamente cada solicitud como "Aprobada" o "Rechazada" con base en las variables disponibles al momento de la solicitud.

#### 3.1 Metodología
El proyecto sigue la metodología estándar de ciencia de datos (CRISP-DM), estructurada en las siguientes etapas:

#### 3.2 Algoritmos evaluados
Se evaluarán y compararán los siguientes algoritmos de clasificación:
* Regresión Logística: modelo base lineal, alta interpretabilidad.
* Support Vector Machine (SVM): efectivo en espacios de alta dimensionalidad.
* Árbol de Decisión: estructura jerárquica, fácil de visualizar e interpretar.
* Random Forest: conjunto de árboles, robusto ante el sobreajuste.
* Gradient Boosting: alto rendimiento en datos tabulares.
* K-Nearest Neighbors (KNN): clasifica en base a la similitud con los k vecinos más cercanos en el espacio de características.


#### 3.3 Métricas de evaluación
La selección del modelo final se basará en las siguientes métricas:

Métrica	Descripción	Importancia
* Exactitud (Accuracy)	Proporción de predicciones correctas	Alta
* Precisión	Predicciones positivas que son correctas	Alta
* Recall (Sensibilidad)	Casos positivos correctamente identificados	Crítica
* F1-Score	Media armónica entre precisión y recall	Alta
* AUC-ROC	Capacidad discriminativa del modelo	Alta


Nota: El Recall tiene especial importancia en este contexto, ya que un falso negativo (rechazar a un cliente solvente) representa una pérdida de oportunidad de negocio y un potencial daño reputacional.

#### 3.4 Tecnologías y herramientas
Categoría	Herramienta / Librería
Lenguaje de programación	Python 3.10+
Manipulación de datos	Pandas, NumPy
Visualización	Matplotlib, Seaborn, Plotly
Aprendizaje automático	Scikit-learn, XGBoost
Entorno de desarrollo	Jupyter Notebook / VS Code
Control de versiones	Git / GitHub
Despliegue (opcional)	Flask / Streamlit

### 4. Resultados Esperados
Al finalizar el proyecto, se espera obtener los siguientes entregables:

* Un modelo de clasificación con una exactitud superior al 80% sobre el conjunto de prueba.
* Un análisis comparativo entre los diferentes algoritmos evaluados.
* Visualizaciones que expliquen las variables de mayor influencia en la aprobación del préstamo.
* Un pipeline reproducible de preprocesamiento y entrenamiento del modelo.
* Un informe técnico con conclusiones y recomendaciones para el sector financiero.

#### 4.1 Impacto esperado
La implementación de este sistema podría generar un impacto significativo en las operaciones bancarias:
Área de impacto	Beneficio esperado
Eficiencia operativa	Reducción del tiempo de evaluación de días a segundos
Reducción de riesgo	Menor tasa de incumplimiento mediante mejor selección
Experiencia del cliente	Respuestas más rápidas y consistentes
Costos	Reducción de costos asociados a evaluación manual
Escalabilidad	Capacidad de procesar miles de solicitudes simultáneamente

### 5. Conclusiones
La predicción de aprobación de préstamos mediante aprendizaje automático representa una aplicación directa y de alto valor de la ciencia de datos en el sector financiero. A través de la automatización del proceso de evaluación, es posible mejorar tanto la eficiencia operativa como la calidad de las decisiones crediticias.

Este proyecto demuestra cómo técnicas de Machine Learning supervisado pueden aprender patrones complejos a partir de datos históricos y aplicarlos para generar predicciones confiables en tiempo real. La combinación de variables socioeconómicas como el historial crediticio, los ingresos y el nivel educativo permite construir modelos robustos con alta capacidad de generalización.

El éxito de este tipo de proyectos no solo depende de la calidad del modelo, sino también de la calidad de los datos, una adecuada ingeniería de características y una evaluación rigurosa que considere el contexto de negocio en el que se aplica.


#### API
Usar el siguiente objeto en el post

{
  "Gender": 1,
  "Married": 2,
  "Dependents": 3,
  "Education": 0,
  "Self_Employed": 0,
  "ApplicantIncome": 1000,
  "CoapplicantIncome": 0,
  "LoanAmount": 150,
  "Loan_Amount_Term": 180,
  "Credit_History": 1,
  "Property_Area": 1
}