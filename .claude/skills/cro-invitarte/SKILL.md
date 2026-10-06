---
name: cro-invitarte
description: "CRO y UX para InvitArte (Tienda Nube invitarteonline, Instagram, WhatsApp, landings). Usar cuando Matilde pida mejorar conversiones, auditar la tienda, una ficha de producto, una categoría, la home, el checkout, un formulario de datos del evento, precios, o cuando diga 'no vende', 'entran pero no compran', 'mejorá esta página', 'revisá la tienda'. También para armar tests A/B y aplicar psicología de compra de forma ética."
metadata:
  version: 1.0.0
  source: "Adaptado de coreyhaines31/marketingskills (MIT, © 2025 Corey Haines): skills cro, cro/references/form.md, cro/references/experiments.md, marketing-psychology, pricing/references/pricing-page-teardown.md"
---

# CRO y UX para InvitArte

Objetivo: que más visitas se conviertan en **ventas rentables** (no solo en clics o mensajes), manteniendo la estética elegante y la atención cercana de la marca.

## Contexto fijo del negocio

- **Producto:** invitaciones digitales interactivas (página web), invitaciones editables, InvitaIA y papelería imprimible (números de mesa, menú, cartel de bienvenida, tarjetas QR y de agradecimiento).
- **Canal de venta:** Tienda Nube `invitarteonline.mitiendanube.com` + WhatsApp + Instagram/Meta Ads.
- **Público:** novias, madres de quinceañeras, personas que organizan cumples, bautismos, comuniones y primer año. Argentina primero, LATAM después.
- **Compra emocional y con fecha límite:** la clienta compra para un evento único. Sus miedos: "¿va a quedar lindo?", "¿llego con los tiempos?", "¿es difícil de usar para mis invitados?", "¿qué pasa si quiero cambiar algo?".
- **Producto digital personalizado:** después del pago hay que pedir datos del evento → el post-compra es parte del CRO.

Antes de recomendar, aclarar siempre:
1. **Tipo de página:** home, categoría, ficha de producto, carrito/checkout, landing de anuncio, link de bio, conversación de WhatsApp.
2. **Objetivo de conversión:** compra directa, consulta por WhatsApp, pedido de demo o muestra, compra de un extra.
3. **Origen del tráfico:** Meta Ads, Instagram orgánico, Google, recomendación, clienta que vuelve.
4. **Datos disponibles:** visitas, carritos abandonados, pedidos, conversaciones. Si faltan datos clave, **preguntar antes de concluir**.

---

## Marco de análisis (en orden de impacto)

### 1. Claridad de la propuesta (lo más importante)
- ¿En 5 segundos se entiende **qué es** (una invitación web que se manda por WhatsApp), **para qué evento** y **por qué conviene**?
- ¿Habla de beneficios ("tus invitados confirman asistencia con un clic") y no solo de funciones ("formulario RSVP")?
- ¿Usa el lenguaje de la clienta ("la invi", "confirmar asistencia", "mandarla por WhatsApp") y no jerga técnica?

### 2. Títulos
- Home y landings: orientados al resultado. Ej.: "Tu invitación lista para mandar por WhatsApp, con confirmación de asistencia incluida".
- Que coincidan con el anuncio que trajo a la persona (**message match**: si el anuncio dice "XV años", la landing abre con XV años, no con bodas).
- Nombres de producto: diseño + tipo de evento. Revisar ortografía (por ejemplo "Londrés" → "Londres") y que sean consistentes (hoy conviven "Invitación Página Web |" e "Invitación Web- Por el Mundo |").

### 3. CTA (llamado a la acción)
- **Un CTA principal claro** por página, visible sin scrollear en el celular.
- El texto del botón comunica valor: "Ver la demo en vivo", "Quiero esta invitación", "Consultar por WhatsApp", en vez de "Ver más" o "Enviar".
- Jerarquía: principal = comprar; secundario = ver la demo o consultar. Repetir el CTA en los puntos de decisión (después de la demo, después de las preguntas frecuentes).

### 4. Jerarquía visual y facilidad de lectura
- Lo más importante se destaca. Mucho aire y que no se vea sobrecargado (coherente con el estilo de la marca).
- En el celular (donde está la mayoría del público): fotos o mockups del diseño **dentro de un celular**, porque así lo van a ver los invitados.
- Las imágenes tienen que mostrar el producto funcionando, no solo decorar.

### 5. Confianza y prueba social
- Testimonios reales con nombre, evento y, si se puede, captura de WhatsApp o foto.
- Cantidad de eventos realizados, reseñas, capturas de invitaciones reales publicadas.
- Ubicarlos **cerca del botón de compra** y después de cada beneficio que se promete.

### 6. Responder objeciones
Objeciones típicas de InvitArte y cómo responderlas:
| Objeción | Respuesta en la página |
|---|---|
| "¿Cómo queda?" | Link a demo navegable + video corto |
| "¿Llego a tiempo?" | Plazo de entrega explícito ("lista en X días hábiles") |
| "¿Y si quiero cambiar algo?" | Cuántas revisiones incluye y cómo se piden |
| "¿Es difícil para mis invitados?" | "Solo abren un link, no descargan nada" |
| "¿Cuánto dura online?" | Hasta cuándo queda activa |
| "¿Es caro?" | Comparar con lo que cuesta imprimir o enviar en papel; cuotas |
| "¿Cómo pago?" | Medios de pago visibles en la ficha |

Formato: sección de preguntas frecuentes en la ficha de producto, garantías y transparencia del proceso ("Pagás → completás un formulario → te mandamos la primera versión → ajustamos → la compartís").

### 7. Fricción
- Demasiados pasos o campos, el próximo paso no está claro, menú confuso, datos obligatorios que no hacen falta, carga lenta, problemas en el celular.
- En Tienda Nube revisar: variantes confusas, envío físico que se pide en un producto digital (`requires_shipping` tiene que ser falso), precio "Consultar" sin explicación, demasiadas categorías.

---

## Formato de entrega de una auditoría

1. **Cambios rápidos (hacer ya):** fáciles y con impacto probable inmediato.
2. **Cambios de alto impacto (priorizar):** requieren más trabajo.
3. **Ideas para testear:** hipótesis para un A/B test, no certezas.
4. **Textos alternativos:** 2 o 3 opciones de título y CTA, explicando el porqué de cada una.

Cada punto sigue la estructura que pide Matilde: qué funciona → qué mejorar → por qué → alternativa concreta → texto listo para usar. Separar **datos** de **opinión subjetiva**.

---

## Marcos por tipo de página (adaptados a Tienda Nube)

### Home
- Posicionamiento claro para quien no te conoce + camino rápido por tipo de evento (Boda / XV / Cumple / Bautismo).
- Tiene que servir a dos personas: la que ya está lista para comprar (va directo a las categorías) y la que todavía está investigando (demo, cómo funciona, testimonios).

### Categoría
- Pocas opciones bien mostradas le ganan a muchas sin orden (paradoja de la elección): destacar 3 o 4 "más elegidos".
- Fotos uniformes entre productos (coherencia visual) y precio visible.

### Ficha de producto (la página más importante)
1. Mockup en celular + link a demo en vivo arriba de todo.
2. Qué incluye (en texto, no solo en imagen).
3. Plazo de entrega + revisiones incluidas.
4. Testimonio cerca del botón "Comprar".
5. Preguntas frecuentes.
6. Extras sugeridos (papelería que combina con el diseño = ticket promedio más alto).

### Landing de anuncio
- Coincidencia total con el anuncio (título, imagen, oferta).
- Un solo CTA, sin menú si se puede, todo el argumento en una sola página.

### Precios / planes
- Si hay niveles (básica / completa / premium): 3 opciones, la del medio marcada como "Más elegida".
- Mostrar qué incluye cada nivel **en palabras**, no solo con tildes.
- Precio real visible en texto (no dentro de una imagen): lo necesitan las personas, Google y los asistentes de IA para poder citarlo.

---

## Formularios (datos del evento, consultas, contacto)

Cada campo cuesta conversiones: 3 campos es la base; de 4 a 6 bajan entre 10 y 25 %; 7 o más, entre 25 y 50 %.

- **Antes de la compra:** pedir lo mínimo (nombre + WhatsApp + tipo de evento). El resto, después.
- **Después de la compra (datos del evento):** formulario en varios pasos con barra de progreso:
  1. Lo fácil: nombres, tipo de evento, fecha.
  2. Lugar y horarios.
  3. Textos, fotos y música.
  4. Extras: dress code, regalos o CBU, confirmación de asistencia.
- Etiquetas siempre visibles (el placeholder es un ejemplo, no la etiqueta).
- Mensajes de error concretos ("Falta la fecha del evento"), sin borrar lo que ya se cargó.
- El botón dice qué va a pasar: "Enviar mis datos para empezar el diseño" en lugar de "Enviar".
- Cerca del formulario: "Te respondemos en menos de X horas" y "Tus datos solo se usan para tu invitación".
- En el celular: una sola columna, botones grandes (44 px o más), teclado correcto (tel, email, fecha).
- Medir: cuánta gente empieza el formulario, cuánta lo termina y en qué campo abandona.

---

## Psicología de compra aplicada (siempre de forma ética)

| Principio | Cómo aplicarlo en InvitArte |
|---|---|
| **Prueba social** | "Más de X eventos con InvitArte", testimonios con capturas reales |
| **Anclaje** | Mostrar primero el pack completo y después la invitación sola; comparar con el costo de imprimir en papel |
| **Efecto señuelo / opción del medio** | Tres niveles, con el del medio como mejor relación precio-valor |
| **Paradoja de la elección / Ley de Hick** | Menos opciones por pantalla y un "Más elegido" destacado |
| **Aversión a la pérdida / urgencia** | "Reservá tu fecha: tomamos X pedidos por semana" (**solo si es verdad**) |
| **Aversión al arrepentimiento** | Revisiones incluidas y proceso claro; reduce el miedo a "que no quede como quiero" |
| **Efecto IKEA** | La clienta elige colores, música y textos, y valora más lo que ayudó a crear |
| **Regla del pico y el final** | Una entrega memorable (video o mockup de presentación) y un buen cierre (mensaje de agradecimiento + pedido de reseña) |
| **Gradiente de meta** | Barra de progreso en el formulario y "¡Ya casi está tu invitación!" |
| **Contabilidad mental** | "Menos que imprimir 20 tarjetas" o mostrar el precio en cuotas |
| **Precios redondos o terminados en 9** | Redondos para lo premium (transmiten calidad); terminados en 9 para extras y entrada (transmiten oportunidad) |
| **Regla del 100** | Productos baratos: descuento en % ("20 % off"). Productos caros: descuento en pesos ("$5.000 off") |
| **Segundo orden** | Promos constantes educan a la clienta a esperar descuentos y erosionan el posicionamiento elegante |
| **Teoría de restricciones** | Encontrar el cuello de botella (¿poco tráfico? ¿muchas visitas y pocas ventas? ¿muchas consultas y pocos cierres?) antes de optimizar otra cosa |

---

## Banco de tests A/B (priorizados para InvitArte)

**Ficha de producto**
- Demo en vivo arriba de todo vs. debajo de las fotos.
- Mockup en celular vs. captura plana.
- Precio total vs. precio en cuotas destacado.
- Con o sin testimonio al lado del botón.
- "Comprar" vs. "Quiero esta invitación".

**Home / categorías**
- Entrada por tipo de evento vs. grilla de productos.
- Sección de "Más elegidos" vs. todo el catálogo.
- Sección "Cómo funciona" en 3 pasos (con o sin ella).

**Landing de anuncios**
- Landing específica por evento (XV / Boda) vs. home genérica.
- Video corto de la invitación funcionando vs. imágenes.
- CTA a WhatsApp vs. CTA a comprar directo.

**Oferta**
- Pack (invitación + papelería) vs. productos sueltos.
- Urgencia real ("cupos de la semana") con o sin ella.

Regla: cambiar **una sola variable por vez**, medir con suficiente volumen y anotar la hipótesis antes de testear.

---

## Métricas: no mezclar

- **Alcance / visitas** → **interacción** → **consultas por WhatsApp (leads)** → **carritos** → **ventas** → **rentabilidad** (margen después de horas de producción y publicidad).
- Embudo en la tienda: visitas → vista de producto → agregado al carrito → checkout iniciado → pago → datos del evento completos.
- Puntos de fuga típicos: ficha sin demo, carrito abandonado, consulta sin respuesta rápida, formulario post-compra a medio completar.

## Preguntas para hacer antes de una auditoría

1. ¿Cuál es la tasa de conversión actual y cuál es el objetivo?
2. ¿De dónde viene el tráfico (anuncios, orgánico, WhatsApp)?
3. ¿Qué pasa después de la compra (flujo de datos del evento)?
4. ¿Hay datos de carritos abandonados, consultas o métricas de Meta?
5. ¿Qué ya se probó?

## Herramientas disponibles

- Conexión con Tienda Nube: leer y editar productos (nombres, descripciones, SEO, categorías, visibilidad), pedidos, clientes, cupones, promociones, medios de pago y de envío. **No** permite tocar el tema ni el diseño de la tienda: para eso, pedir capturas a Matilde.
- **Toda edición en la tienda se confirma con Matilde antes de aplicarla** (los cambios se ven en vivo).
