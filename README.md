# Respuestas a Preguntas de CI/CD

### 1. Flujo de trabajo completo implementado con Terraform
El nuevo pipeline automatiza todo el ciclo de vida del código, desde el cambio hasta la nube:
*   **Commit & CI:** Al pushear código, se ejecutan linters y pruebas unitarias.
*   **Build/Push Imagen:** Se empaqueta la aplicación en imagen de Docker y se sube a un registro (Docker Hub/GHCR), este es el **artefacto** principal que fluye por los entornos.
*   **Deploy TF Staging:** Terraform lee sus archivos HCL (`main.tf`, etc.) y provisiona o valida la infraestructura base en AWS para un entorno de pruebas idéntico al real.
*   **Update Service Staging:** Se despliega el contenedor Docker (la nueva imagen) en los servidores o servicios de Staging.
*   **Test Staging:** Se ejecutan pruebas de aceptación rigurosas interactuando con la URL de Staging recién desplegada.
*   **Deploy TF Prod / Update Service Prod:** Al pasar Staging, Terraform replica la infraestructura en Producción y se despliega la misma imagen Docker allí de manera confiable.
*   **Smoke Test Prod:** Valida que el despliegue final esté vivo (e.g. un `200 OK`) sin hacer tests pesados o mutar datos.

### 2. Infraestructura como código (Terraform) vs Despliegue Manual
*   **Ventajas:** Es reproducible, está versionado, y elimina los errores humanos típicos de "hacer clics" en la consola de AWS. Permite destruir y levantar todo en minutos.
*   **Desventajas:** La curva de aprendizaje es alta, y el manejo del "estado" de Terraform (`terraform.tfstate`) puede desincronizarse si se hacen cambios manuales por error.
*   **Experiencia con HCL:** Resulta ser muy declarativo y legible; en lugar de programar el "cómo" conectar cosas, se define el "qué" se quiere, lo cual facilita entender la arquitectura leyendo código.

### 3. Entorno de Staging en AWS: Velocidad vs. Seguridad
*   **Ventajas / Desventajas:** Proporciona una red de seguridad vital para probar condiciones reales (bases de datos en la nube, latencia, red) antes de afectar clientes, pero a cambio requiere más máquinas (costo) y añade tiempo al pipeline de despliegue.
*   **Impacto:** Reduce ligeramente la *velocidad* de entrega total desde el commit a Producción debido a los pasos adicionales, pero incrementa exponencialmente la *seguridad*, ya que los bugs de infraestructura y de integración mueren en Staging.

### 4. Pruebas contra Staging vs. Producción (Smoke Test)
*   **Diferencia:** En Staging (`test-staging`) se suelen correr pruebas end-to-end completas: probar cálculos exhaustivos, revisar la UI e incluso forzar errores lógicos. En Producción (`smoke-test-production`) solo se hace una evaluación muy ligera: hacer un ping al health-check de la app o revisar que retorne un HTTP 200 al hacer un get en el índice.
*   **Por qué:** Hacer pruebas agresivas en Producción podría generar sobrecarga, afectar métricas o modificar datos reales de los usuarios (suciedad en la base de datos). El smoke test solo responde a la pregunta inmediata: "¿Se cayó la aplicación al desplegar?".

### 5. Prácticas faltantes en el ciclo DevOps
Actualmente al ciclo completo de DevOps, aunque robusto, todavía puede sumar:
1.  **Monitorización y Observabilidad (Prometheus, Grafana, ELK):** El pipeline despliega exitosamente, pero una vez en producción no tenemos visibilidad en tiempo real del uso de CPU, memoria o si empiezan a saltar errores silenciosos 500 en los logs. Implementarlo permite reaccionar a incidentes post-despliegue.
2.  **Gestión Dinámica de Secretos (HashiCorp Vault o AWS Secrets Manager):** Ahora dependemos de variables de GitHub quemadas y credenciales de larga duración en el repo. Rotar secretos automáticamente y pasárselos directamente a la infraestructura mediante Terraform añadiría una capa importante de seguridad ante brechas en GitHub.

### 6. Experiencia agregando funcionalidades con CI/CD
*   **Experiencia general:** Es inmensamente más tranquilo desarrollar. La red de seguridad permite iterar rápido.
*   **Útil:** Encontrar errores de regresión (saber de inmediato cuando rompiste algo anterior) y no perder tiempo recordando comandos de despliegue o conexión por SSH.
*   **No tan útil (o frustrante):** La demora de los pipelines. Esperar minutos para que Terraform haga su validación y los contenedores hagan el build tras haber corregido un error tipográfico sencillo puede volver lento el proceso de feedback final frente a pruebas puramente locales.

### Terraform Outputs
- ALB URL Staging: http://calculadora-staging-alb-1227608249.us-east-1.elb.amazonaws.com/
- ALB URL Production: http://calculadora-production-alb-294547370.us-east-1.elb.amazonaws.com/