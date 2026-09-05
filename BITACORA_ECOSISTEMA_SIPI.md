# 🗺️ Bitácora Oficial del Ecosistema SIPI & Directorio Maestro de Herramientas

> **Guía Maestra de Arquitectura, Operación, Ubicación e Interrelación de Herramientas Digitales.**  
> *Ecosistema @fuel_w_roxy · Sistema SIPI · EstuFuel · Centro AURA Valladolid*

---

## 📌 Mapa Conceptual del Ecosistema

El ecosistema está concebido como un **embudo integral de atracción, conversión, fidelización y duplicación**, donde cada herramienta cumple una función estratégica definida:

```mermaid
flowchart TD
    subgraph P1["1. INTELIGENCIA & TENDENCIAS"]
        VL["ViralLens Dual-Engine<br/>(Gemini 3.8 Flash + Apify)"]
        SV["SIPI Vault<br/>(Bóveda por Fases + PIN 2026)"]
    end

    subgraph P2["2. ATRACCIÓN & AUTOMATIZACIÓN"]
        IG["Instagram @fuel_w_roxy<br/>(Marca Personal Estudiante UVa)"]
        BOT["SIPI Bot Roxy<br/>(Meta Webhook en Cloudflare Worker)"]
        WEB["Portal SIPI Ecosistema<br/>(Astro + Netlify + Cal.com)"]
    end

    subgraph P3["3. PRODUCTOS & PRESTIGIO"]
        MAG["SIPI Magazine<br/>(Revista Digital Ed. 01 & 02)"]
        MAN["Manual SIPI<br/>(Guía Maestra 7 Módulos)"]
        LM["Guía 7 Desayunos Energéticos<br/>(Lead Magnet + Meta Ads)"]
        AURA["Centro AURA Parquesol<br/>(Tarjetas de Convicción Web)"]
    end

    subgraph P4["4. OPERACIONES & VENTAS"]
        EPS["EstuFuel Pro Suite<br/>(PWA + Supabase + CRM + POS)"]
        B2B["Prospección B2B Valladolid<br/>(Polígonos Argales & San Cristóbal)"]
    end

    subgraph P5["5. EQUIPO DE AGENTES IA"]
        AG["7 Agentes Especializados<br/>(Director, Creativo, Editor, etc.)"]
        SK["Habilidades de Cumplimiento<br/>(Estrategia Roxy, Meta Ads)"]
    end

    VL -->|Inspiración y ganchos validados| SV
    SV -->|Copys y guiones por fases| IG
    IG -->|Comentarios y mensajes directos| BOT
    BOT -->|Entrega de enlaces y citas| WEB
    WEB -->|Lectura y descarga de recursos| MAG & LM
    MAG & LM -->|Prospectos cualificados de salud/red| EPS
    B2B -->|Alianzas con comercios locales| AURA & EPS
    AG & SK -->|Dirección, redacción y auditoría continua| P1 & P2 & P3 & P4
```

---

## 🧭 Índice de Herramientas Registradas

1. [Pilar 1: Inteligencia de Mercado & Minería Viral](#pilar-1-inteligencia-de-mercado--minería-viral)
   - 1.1. ViralLens Dual-Engine
   - 1.2. SIPI Vault
2. [Pilar 2: Atracción, Redes Sociales & Automatización](#pilar-2-atracción-redes-sociales--automatización)
   - 2.1. Canal de Instagram @fuel_w_roxy
   - 2.2. Fan Page de Facebook (Crece con Roxy)
   - 2.3. SIPI Bot Roxy (Meta Webhook Serverless)
   - 2.4. Portal Web SIPI Ecosistema
3. [Pilar 3: Publicaciones Editoriales, Lead Magnets & Bienestar](#pilar-3-publicaciones-editoriales-lead-magnets--bienestar)
   - 3.1. SIPI Magazine (Revista Digital)
   - 3.2. Manual SIPI (Producto Digital Terminado)
   - 3.3. Guía 7 Desayunos Energéticos (Lead Magnet)
   - 3.4. Centro AURA Parquesol & Generador de Tarjetas de Convicción
4. [Pilar 4: Operaciones Comerciales, CRM & Gestión de Ventas](#pilar-4-operaciones-comerciales-crm--gestión-de-ventas)
   - 4.1. EstuFuel Pro Suite (Plataforma Core)
   - 4.2. Herbalife Sales Manager (Precursor Financiero)
   - 4.3. EstuFuel Prospect Manager (Precursor CRM)
   - 4.4. Sistema de Prospección B2B Valladolid
5. [Pilar 5: Motor de Agentes de IA & Habilidades Especializadas](#pilar-5-motor-de-agentes-de-ia--habilidades-especializadas)
   - 5.1. Equipo de 7 Subagentes Orquestados
   - 5.2. Habilidades de Marca y Compliance

---

## Pilar 1: Inteligencia de Mercado & Minería Viral

### 1.1. ViralLens Dual-Engine
* **¿Qué es?:** Plataforma de software analítico para detectar publicaciones y reels atípicos (*outliers*) en TikTok e Instagram, despiezando su narrativa, hooks visuales y transcripciones segundo a segundo mediante inteligencia artificial multimodal.
* **Motor de IA:** Google Gemini 3.8 Flash (`gemini-3.8-flash`) + Scraper Apify Free Tier.
* **¿Para qué sirve?:** Para no inventar contenido desde cero, sino identificar con precisión matemática qué está funcionando en el mercado de bienestar, hábitos y emprendimiento, adaptándolo al canal de Roxy.
* **Ubicación Local:** `ViralLens Dual-Engine/`
* **Acceso en la Nube:** [https://virallens-roxy.streamlit.app](https://virallens-roxy.streamlit.app)
* **Repositorio GitHub:** [oredigital2023/virallens-dual-engine](https://github.com/oredigital2023/virallens-dual-engine)
* **Cómo se usa:**
  1. Entra a la web e introduce una palabra clave (ej. `#emprenderjoven`, `#habitosaludables`) o el `@usuario` de un creador.
  2. Revisa el *Radar de Detección* con los posts ordenados por puntuación de anomalía (*Outlier Score*).
  3. Pulsa en *"Analizar con Gemini"* para obtener el guión técnico, ganchos visuales y psicología de retención.
  4. Guarda el análisis en el *Swipe File* y descarga la ficha en Markdown.
* **Interrelación:** Alimenta a **SIPI Vault** con ideas probadas. Cuando una idea de ViralLens se adapta para Roxy, se cataloga en la Bóveda por su fase de madurez.

---

### 1.2. SIPI Vault (Bóveda Estratégica de Contenidos)
* **¿Qué es?:** Repositorio centralizado de ideas, copys listos para publicar, prompts de imagen y guiones de prospección por DM, clasificados por Fases de Madurez (Fase 1: Siembra, Fase 2: Tracción - Octubre, Fase 3: Escala) y protegidos con PIN.
* **¿Para qué sirve?:** Evita que las mejores ideas estratégicas y guiones se pierdan en conversaciones de chat. Permite que Roxy copie textos y guiones al portapapeles en 1 solo clic desde su teléfono.
* **Ubicación Local:** `sipi-vault/` (y puntero maestro en raíz: `BOVEDA_ESTRATEGIAS_ROXY.md`).
* **Acceso en la Nube:** [https://oredigital2023.github.io/sipi-vault/](https://oredigital2023.github.io/sipi-vault/)
* **Repositorio GitHub:** [oredigital2023/sipi-vault](https://github.com/oredigital2023/sipi-vault)
* **Seguridad:** Bloqueo con PIN de 4 dígitos (PIN por defecto: `2026`).
* **Cómo se usa:**
  1. Roxy abre el enlace en su móvil y teclea `2026`.
  2. Filtra por fase (ej. *Fase 1* para publicar hoy o *Fase 2* para preparar Octubre).
  3. Pulsa *"Copiar Caption"* para pegarlo directamente en Instagram, o *"Copiar DM"* para responder a prospectos.
* **Interrelación:** Es el puente entre el análisis de mercado de **ViralLens**, la creatividad de los **Agentes IA** y la publicación real en **Instagram (@fuel_w_roxy)**.

---

## Pilar 2: Atracción, Redes Sociales & Automatización

### 2.1. Canal de Instagram Oficial: `@fuel_w_roxy`
* **¿Qué es?:** El escaparate principal de atracción orgánica y marca personal de Roxy.
* **Identidad:** Estudiante de 20 años de 2º curso en la Universidad de Valladolid (UVa), construyendo su Plan B independiente sin humos de gurú ni promesas de dinero fácil.
* **Filosofía de Contenido:** Principios de Robert Kiyosaki (Construir activos vs trabajar por dinero, libertad de tiempo, energía física para rendir en exámenes y negocio).
* **Ubicación / URL:** [https://www.instagram.com/fuel_w_roxy](https://www.instagram.com/fuel_w_roxy)
* **Interrelación:** Genera el tráfico inicial de personas interesadas en bienestar o negocio que activan el **SIPI Bot Roxy** mediante palabras clave en comentarios y mensajes directos.

---

### 2.2. Fan Page de Facebook: `Crece con Roxy - Emprendimiento y Bienestar Joven`
* **¿Qué es?:** Página comercial de Facebook vinculada obligatoriamente a la cuenta profesional de Instagram para habilitar los permisos de Graph API y Webhooks de Meta.
* **Identificador de Página (Page ID):** `1310307268827979`
* **Uso:** Soporte de autenticación OAuth, suscripción a webhooks de eventos de mensajería y comentarios de Instagram.

---

### 2.3. SIPI Bot Roxy (Meta Webhook Serverless)
* **¿Qué es?:** Bot inteligente alojado en Cloudflare Workers conectado a la Graph API de Meta Developers para automatizar la atención en Instagram en tiempo real.
* **Meta App IDs:** `2192490035037803` / `1388501373257200`
* **Ubicación Técnica:** Worker en `https://sipi.fuelwroxy.workers.dev/api/instagram/webhook`
* **Documentación Técnica:** [`ESTADO_INTEGRACION_INSTAGRAM_BOT_ROXY.md`](file:///c:/Users/orelv/Downloads/Habilidades%20de%20Herbalife/ESTADO_INTEGRACION_INSTAGRAM_BOT_ROXY.md)
* **Funcionalidades Clave:**
  - **Palabras Clave Automatizadas:**
    - `REVISTA` o `SIPI`: Entrega la Edición 01 de SIPI Magazine.
    - `ENERGIA` o `TEST`: Enlace al test de autoevaluación corporal.
    - `AURA`: Información y ubicación del centro de bienestar en Parquesol (Valladolid).
    - `PROYECTO`: Enlace a agendamiento para conocer el modelo de negocio.
    - `CITA`: Agendamiento directo de asesoría.
  - **Detección Automática de Contactos:** Reconoce teléfonos españoles (`6XXXXXXXX`, `+34...`) y emails en el chat y responde confirmando su registro para seguimiento.
  - **Flujo Dual Comentario-DM:** Deja un comentario público cálido en el post y envía los detalles por privado al usuario.
  - **Modo Transición Anti-Baneos:** Protegido contra bloqueos de Meta (`#368`) alternando entre textos sin enlaces y URLs oficiales seguras.

---

### 2.4. Portal Web SIPI Ecosistema
* **¿Qué es?:** Sitio web oficial del ecosistema que centraliza la captura de leads, agendamiento y recursos de Roxy.
* **Stack Tecnológico:** Astro + Netlify + Cloudflare Workers + MailerLite (Email marketing) + Cal.com (Agendamiento) + ManyChat.
* **Repositorio GitHub:** [oredigital2023/sipi-ecosistema](https://github.com/oredigital2023/sipi-ecosistema)
* **Página de Enlaces (Link in Bio):** `https://sipi.fuelwroxy.workers.dev/links`
* **Interrelación:** Recibe el tráfico enviado por el bot de Instagram, captura los datos de los prospectos y los sincroniza con la base de datos de **EstuFuel Pro Suite**.

---

## Pilar 3: Publicaciones Editoriales, Lead Magnets & Bienestar

### 3.1. SIPI Magazine (Revista Digital)
* **¿Qué es?:** Revista digital de estilo de vida, nutrición consciente, mentalidad emprendedora y rendimiento. Es la carta de presentación institucional de la comunidad.
* **Edición Actual:** Edición 01 (Publicada). Edición 02 en preparación con la sección *"Talento Emergente: Las Mentes Detrás de los Negocios con Propósito"*.
* **Ubicación de Diseños:** `assets/designs/sipi_magazine.html` y maquetas en `assets/designs/`
* **Interrelación:** Actúa como **Lead Magnet de alto estatus**. Se entrega a través del bot con la palabra clave `REVISTA` y sirve de plataforma para entrevistar y cualificar a nuevos prospectos.

---

### 3.2. Manual SIPI (Producto Digital Terminado)
* **¿Qué es?:** Guía maestra y formativa en 7 módulos diseñada para la duplicación y capacitación de distribuidores independientes de la red SIPI.
* **Contenido Modular:** Filosofía SIPI, Ser Producto del Producto, Método de Atracción Digital, Sistema de Conversación y Cierres Éticos, Fidelización en 21 y 90 días, Construcción de Equipo y Compliance Legal.
* **Ubicación:** `productos/manual-sipi/`
  - Documento completo: [`manual-sipi-completo.md`](file:///c:/Users/orelv/Downloads/Habilidades%20de%20Herbalife/productos/manual-sipi/manual-sipi-completo.md)
  - Versión maquetada para imprenta/PDF: [`manual-sipi-print-ready.html`](file:///c:/Users/orelv/Downloads/Habilidades%20de%20Herbalife/productos/manual-sipi/manual-sipi-print-ready.html)
* **Interrelación:** Herramienta de bienvenida y formación entregada a cada nuevo distribuidor que se incorpora a la red de Roxy.

---

### 3.3. Guía «7 Desayunos Energéticos» (Lead Magnet)
* **¿Qué es?:** Recetario descargable de alto valor para personas que sufren de cansancio matutino o falta de tiempo, combinando productos funcionales de Herbalife con ingredientes cotidianos.
* **Ubicación:** `productos/guia-7-desayunos-energeticos/`
  - Guía completa: [`guia-7-desayunos-energeticos.md`](file:///c:/Users/orelv/Downloads/Habilidades%20de%20Herbalife/productos/guia-7-desayunos-energeticos/guia-7-desayunos-energeticos.md)
  - Copys para anuncios publicitarios: [`anuncios-meta-ads-y-redes.md`](file:///c:/Users/orelv/Downloads/Habilidades%20de%20Herbalife/productos/guia-7-desayunos-energeticos/anuncios-meta-ads-y-redes.md)
* **Interrelación:** Imán de prospectos para campañas de Meta Ads y DMs fríos orientados al avatar de bienestar y pérdida de peso sin hablar de "dietas milagro".

---

### 3.4. Centro AURA Parquesol & Generador de Tarjetas de Convicción
* **¿Qué es?:** Herramienta web interactiva para el equipo del Centro de Bienestar AURA en Parquesol (Valladolid), diseñada para generar pósters, tarjetas de convicción, manejo de objeciones y argumentos de nutrición y negocio con exportación gráfica (`html2canvas`).
* **Ubicación Local:** [`tarjetas_conviccion_aura_sipi/index.html`](file:///c:/Users/orelv/Downloads/Habilidades%20de%20Herbalife/tarjetas_conviccion_aura_sipi/index.html)
* **Cómo se usa:** Se abre en el navegador local para seleccionar tarjetas por categoría (*Nutrición*, *Negocio*, *Objeciones*), personalizar textos y descargar imágenes para imprimir o enviar por WhatsApp.
* **Interrelación:** Apoyo de mostrador y ventas presenciales para el equipo físico en Valladolid.

---

## Pilar 4: Operaciones Comerciales, CRM & Gestión de Ventas

### 4.1. EstuFuel Pro Suite (Plataforma Core de Negocio)
* **¿Qué es?:** El sistema operativo central del negocio de distribución. Una Progressive Web App (PWA) bento-grid conectada a Supabase (PostgreSQL) que gestiona todas las operaciones comerciales y de equipo.
* **Módulos Integrados:**
  1. *Dashboard Financiero:* Beneficio neto real, coste de producto, volumen personal (VP) y saldo de caja.
  2. *Calculadora de Ventas:* PVP personalizado, consumos personales, deducción de citas y cálculo automático de márgenes.
  3. *Directorio 360° de Clientes:* Segmentación por nichos (Nutrición, Belleza, Híbridos), LTV, historial de compras y diferenciación de distribuidores convertidos.
  4. *Pipeline de Prospectos:* Embudo interactivo (Nuevo $\rightarrow$ Contactado $\rightarrow$ Cita Agendada $\rightarrow$ En Seguimiento $\rightarrow$ Convertido).
  5. *Red Multinivel:* Árbol de downlines, cálculo de diferenciales de mayoreo (25%, 35%, 42%, 50%) y liquidación de comisiones.
  6. *Shake Bar POS:* Punto de venta rápido para club de nutrición con control de stock y fidelización por puntos.
  7. *Agenda & Citas:* Calendario mensual con conversión automática del importe de la cita en descuento de producto.
  8. *Motor de IA Gemini 2.5:* Scoring predictivo de prospectos y clientes con mayor potencial para la red.
* **Ubicación Local:** `estufuel-pro-suite/`
* **Repositorio GitHub:** [oredigital2023/estufuel-pro-suite](https://github.com/oredigital2023/estufuel-pro-suite)
* **Base de Datos:** Supabase PostgreSQL con Row Level Security (RLS).
* **Cómo se arranca localmente:** Ejecutar `python server.py` dentro de la carpeta y acceder a `http://localhost:8000`.

---

### 4.2. Módulos Precursores Históricos
* **Herbalife Sales Manager (`herbalife-sales-manager/`):** Primer software financiero desarrollado para el control de inventario y caja de Herbalife ([repo](https://github.com/oredigital2023/herbalife-sales-manager)). Sus lógicas contables se integraron en *EstuFuel Pro Suite*.
* **EstuFuel Prospect Manager (`estufuel-prospect-manager/`):** Precursor del CRM para la captura y seguimiento de contactos y referidos por WhatsApp ([repo](https://github.com/oredigital2023/estufuel-prospect-manager)).

---

### 4.3. Estrategia y Guiones de Prospección B2B Valladolid
* **¿Qué es?:** Sistema estructurado de alianzas estratégicas locales para Valladolid, diseñado para abordar comercios y empresas de polígonos industriales (San Cristóbal y Argales).
* **Archivos Clave:**
  - [`prospectos_estrategicos_b2b.md`](file:///c:/Users/orelv/Downloads/Habilidades%20de%20Herbalife/prospectos_estrategicos_b2b.md): Mapeo de clínicas de fisioterapia, centros de pilates, peluquerías, academias de baile y clubes deportivos en Valladolid.
  - [`guiones_abordaje_b2b.md`](file:///c:/Users/orelv/Downloads/Habilidades%20de%20Herbalife/guiones_abordaje_b2b.md): Guiones de abordaje presencial y telefónico para ofrecer córners de hidratación, talleres de nutrición laboral o eventos cruzados con Centro AURA.

---

## Pilar 5: Motor de Agentes de IA & Habilidades Especializadas

### 5.1. El Equipo de 7 Subagentes Orquestados (`.agents/agents/`)

| Subagente | Archivo | Rol y Responsabilidad Principal |
| :--- | :--- | :--- |
| 👑 **Director de Proyecto** | [`director.md`](file:///c:/Users/orelv/Downloads/Habilidades%20de%20Herbalife/.agents/agents/director.md) | Orquestador maestro. Recibe los requerimientos del usuario, descompone tareas, delega en especialistas y vela por que toda idea se catalogue en **SIPI Vault**. |
| ✍️ **Creativo & Ads** | [`creativo-ads.md`](file:///c:/Users/orelv/Downloads/Habilidades%20de%20Herbalife/.agents/agents/creativo-ads.md) | Especialista en copywriting publicitario, hooks de 3 segundos, prompts para Midjourney/DALL-E, copys para Instagram y guiones de prospección 1 a 1 por DM sin enlaces en frío. |
| 📖 **Editor Editorial SIPI** | [`editor-editorial-sipi.md`](file:///c:/Users/orelv/Downloads/Habilidades%20de%20Herbalife/.agents/agents/editor-editorial-sipi.md) | Redactor jefe de *SIPI Magazine* y *Manual SIPI*. Diseña convocatorias de prestigio, cuestionarios de cualificación de candidatos y maquetación de secciones. |
| 🔍 **Investigador de Mercado** | [`investigador.md`](file:///c:/Users/orelv/Downloads/Habilidades%20de%20Herbalife/.agents/agents/investigador.md) | Analista de tendencias, estudio de los dolores del avatar (mamás, universitarios, oficinistas) y benchmarking de cuentas competidoras. |
| 🎁 **Creador de Recursos** | [`recursos-lead-magnets.md`](file:///c:/Users/orelv/Downloads/Habilidades%20de%20Herbalife/.agents/agents/recursos-lead-magnets.md) | Diseña guías de hábitos, recetarios, retos de 21 días y planes descargables de captación. |
| 💻 **Web Digital Builder** | [`web-digital-builder.md`](file:///c:/Users/orelv/Downloads/Habilidades%20de%20Herbalife/.agents/agents/web-digital-builder.md) | Programador frontend de landing pages, páginas de opt-in, tableros interactivos y visualizadores web con Tailwind CSS. |
| 🛡️ **Auditor & Compliance** | [`auditor-compliance.md`](file:///c:/Users/orelv/Downloads/Habilidades%20de%20Herbalife/.agents/agents/auditor-compliance.md) | Filtro de calidad que verifica ortografía, coherencia de marca y cumplimiento estricto de las políticas de Meta Ads y Herbalife (cero promesas de ingresos rápidos, cero afirmaciones médicas). |

---

### 5.2. Habilidades de Marca y Compliance (`.agents/skills/`)
* **`estrategia-herbalife-roxy`:** ADN de identidad de Roxy (estudiante UVa, 20 años, tono humilde, filosofía Kiyosaki, producto como accesorio de energía y contexto local en Valladolid).
* **`meta-ads-herbalife`:** Reglas publicitarias estrictas para campañas de pago (evitar baneos por multinivel, sin antes/después, sin ingresos garantizados).
* **`creador-de-agentes`:** Guía técnica para conceptualizar, configurar y orquestar nuevos subagentes personalizados en Antigravity.

---

## 🔄 Resumen de Enlaces Rápidos y Accesos en la Nube

| Herramienta / Portal | Acceso en la Nube | Repositorio GitHub |
| :--- | :--- | :--- |
| **SIPI Vault (Bóveda + Bitácora)** | [https://oredigital2023.github.io/sipi-vault/](https://oredigital2023.github.io/sipi-vault/) *(PIN: 2026)* | `oredigital2023/sipi-vault` |
| **ViralLens Dual-Engine** | [https://virallens-roxy.streamlit.app](https://virallens-roxy.streamlit.app) | `oredigital2023/virallens-dual-engine` |
| **Portal SIPI Ecosistema** | `https://sipi.fuelwroxy.workers.dev/links` | `oredigital2023/sipi-ecosistema` |
| **EstuFuel Pro Suite** | Netlify / Local (`localhost:8000`) | `oredigital2023/estufuel-pro-suite` |
| **Instagram @fuel_w_roxy** | [https://www.instagram.com/fuel_w_roxy](https://www.instagram.com/fuel_w_roxy) | - |
