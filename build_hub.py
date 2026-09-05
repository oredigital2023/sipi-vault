import json

# Load tools data
with open('sipi-vault/tools_data.json', 'r', encoding='utf-8') as f:
    tools = json.load(f)

# Load existing index.html
with open('sipi-vault/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build Tools HTML
tools_cards_list = []
for t in tools:
    loc_cloud = t['location_cloud']
    loc_local = t['location_local']
    name = t['name']
    desc = t['description']
    tech = t['tech']
    how = t['how_to_use']
    inter = t['interrelation']
    icon = t['icon']
    badge_class = t['badge_class']
    cat_name = t['category_name']
    cat = t['category']
    status = t['status']
    cloud_label = t['cloud_label']

    card = f'''
      <!-- TOOL: {t['id']} -->
      <article class="tool-card {cat} rounded-2xl bg-sipi-card border border-sipi-cardBorder hover:border-sipi-neon/40 transition-all p-6 flex flex-col justify-between group shadow-lg">
        <div>
          <!-- Top Badges -->
          <div class="flex items-center justify-between gap-2 mb-3.5">
            <div class="flex items-center gap-2 flex-wrap">
              <span class="text-lg">{icon}</span>
              <span class="text-[11px] font-semibold px-2.5 py-1 rounded-md {badge_class}">{cat_name}</span>
            </div>
            <span class="text-[10px] font-bold uppercase tracking-wider text-sipi-neon bg-sipi-neon/10 px-2 py-0.5 rounded border border-sipi-neon/30">{status}</span>
          </div>

          <!-- Title & Description -->
          <h3 class="text-xl font-bold font-serif text-white group-hover:text-sipi-neon transition-colors mb-1.5">
            {name}
          </h3>
          <p class="text-xs text-sipi-text/90 mb-4 leading-relaxed">
            {desc}
          </p>

          <!-- Tech & Specs -->
          <div class="rounded-xl bg-sipi-bg/70 border border-sipi-cardBorder/70 p-3 mb-3 text-[11px] text-sipi-textMuted">
            <strong class="text-white font-medium">Tecnología / Stack:</strong> {tech}
          </div>

          <!-- Details Info Box -->
          <div class="space-y-2.5 mb-5">
            <div class="rounded-xl bg-sipi-bg/50 border border-sipi-cardBorder/50 p-3 text-xs">
              <span class="font-semibold text-sipi-peach flex items-center gap-1.5 mb-1">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                Ubicación & Acceso
              </span>
              <p class="text-sipi-textMuted text-[11px]">
                <span class="text-white/80">Local:</span> <code class="text-xs text-sipi-neon bg-sipi-card px-1.5 py-0.5 rounded">{loc_local}</code>
              </p>
            </div>

            <div class="rounded-xl bg-sipi-bg/50 border border-sipi-cardBorder/50 p-3 text-xs">
              <span class="font-semibold text-emerald-400 flex items-center gap-1.5 mb-1">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                ¿Cómo se usa?
              </span>
              <p class="text-sipi-text/80 text-[11px] leading-relaxed">
                {how}
              </p>
            </div>

            <div class="rounded-xl bg-sipi-bg/50 border border-sipi-cardBorder/50 p-3 text-xs">
              <span class="font-semibold text-sipi-neon flex items-center gap-1.5 mb-1">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"></path></svg>
                Interrelación en el Embudo
              </span>
              <p class="text-sipi-textMuted text-[11px] leading-relaxed">
                {inter}
              </p>
            </div>
          </div>
        </div>

        <!-- Action Button -->
        <div class="pt-3 border-t border-sipi-cardBorder flex items-center gap-2">
          <a href="{loc_cloud}" target="_blank" rel="noopener noreferrer" 
             class="w-full py-2.5 px-3 rounded-xl text-xs font-bold bg-sipi-bg border border-sipi-cardBorder hover:border-sipi-neon hover:text-sipi-neon text-white transition-all flex items-center justify-center gap-1.5 shadow-sm">
            <span>{cloud_label}</span>
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
          </a>
          <button onclick="copyToClipboardText('{loc_cloud}', 'Enlace copiado al portapapeles')" title="Copiar Enlace" 
                  class="p-2.5 rounded-xl bg-sipi-bg border border-sipi-cardBorder text-sipi-textMuted hover:text-sipi-neon hover:border-sipi-neon/50 transition-all">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3"></path></svg>
          </button>
        </div>
      </article>'''
    tools_cards_list.append(card)

tools_cards_html = '\n'.join(tools_cards_list)

# Now construct the complete new index.html with view switcher
full_html = f'''<!DOCTYPE html>
<html lang="es" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SIPI Vault · Bóveda & Bitácora del Ecosistema @fuel_w_roxy</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            sipi: {{
              bg: '#0a0f08',
              card: '#131c11',
              cardBorder: '#233320',
              cardHover: '#182416',
              neon: '#7efe6d',
              neonDim: '#5ec250',
              peach: '#ffb595',
              peachDim: '#d48866',
              text: '#f2f5f0',
              textMuted: '#94a58f',
              accent: '#344b30'
            }}
          }},
          fontFamily: {{
            serif: ['Playfair Display', 'serif'],
            sans: ['DM Sans', 'sans-serif']
          }}
        }}
      }}
    }}
  </script>
  <style>
    body {{
      background-color: #0a0f08;
      color: #f2f5f0;
      font-family: 'DM Sans', sans-serif;
    }}
    .custom-scrollbar::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    .custom-scrollbar::-webkit-scrollbar-track {{
      background: #0e150c;
    }}
    .custom-scrollbar::-webkit-scrollbar-thumb {{
      background: #2a3b26;
      border-radius: 4px;
    }}
    .custom-scrollbar::-webkit-scrollbar-thumb:hover {{
      background: #7efe6d;
    }}
  </style>
</head>
<body class="min-h-screen flex flex-col bg-sipi-bg antialiased selection:bg-sipi-neon selection:text-black">

  <!-- Lock Screen Modal -->
  <div id="lockScreen" class="fixed inset-0 z-50 flex items-center justify-center bg-sipi-bg/95 backdrop-blur-xl p-4 transition-all duration-300">
    <div id="lockBox" class="max-w-sm w-full bg-sipi-card border border-sipi-cardBorder rounded-3xl p-8 shadow-2xl text-center flex flex-col items-center transform transition-transform duration-200">
      <!-- Shield Icon -->
      <div class="w-16 h-16 rounded-2xl bg-gradient-to-tr from-sipi-cardBorder to-sipi-neon/20 border border-sipi-neon/40 flex items-center justify-center text-sipi-neon shadow-xl shadow-sipi-neon/10 mb-5">
        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
      </div>

      <h2 class="text-2xl font-bold font-serif text-white mb-1">SIPI Vault</h2>
      <p class="text-xs text-sipi-textMuted mb-6">Acceso privado a las estrategias de <span class="text-white font-medium">@fuel_w_roxy</span></p>

      <!-- PIN Display Dots -->
      <div id="pinDots" class="flex items-center gap-3.5 mb-6">
        <span class="pin-dot w-4 h-4 rounded-full border-2 border-sipi-cardBorder transition-all duration-200"></span>
        <span class="pin-dot w-4 h-4 rounded-full border-2 border-sipi-cardBorder transition-all duration-200"></span>
        <span class="pin-dot w-4 h-4 rounded-full border-2 border-sipi-cardBorder transition-all duration-200"></span>
        <span class="pin-dot w-4 h-4 rounded-full border-2 border-sipi-cardBorder transition-all duration-200"></span>
      </div>

      <!-- Error message -->
      <p id="pinError" class="text-xs text-red-400 font-semibold mb-4 h-4 transition-opacity opacity-0">PIN incorrecto. Inténtalo de nuevo.</p>

      <!-- Keypad -->
      <div class="grid grid-cols-3 gap-2.5 w-full max-w-[260px]">
        <button onclick="pressPin('1')" class="pin-btn h-13 py-3 rounded-2xl bg-sipi-bg border border-sipi-cardBorder hover:border-sipi-neon/50 text-lg font-bold text-white active:scale-95 transition-all">1</button>
        <button onclick="pressPin('2')" class="pin-btn h-13 py-3 rounded-2xl bg-sipi-bg border border-sipi-cardBorder hover:border-sipi-neon/50 text-lg font-bold text-white active:scale-95 transition-all">2</button>
        <button onclick="pressPin('3')" class="pin-btn h-13 py-3 rounded-2xl bg-sipi-bg border border-sipi-cardBorder hover:border-sipi-neon/50 text-lg font-bold text-white active:scale-95 transition-all">3</button>
        <button onclick="pressPin('4')" class="pin-btn h-13 py-3 rounded-2xl bg-sipi-bg border border-sipi-cardBorder hover:border-sipi-neon/50 text-lg font-bold text-white active:scale-95 transition-all">4</button>
        <button onclick="pressPin('5')" class="pin-btn h-13 py-3 rounded-2xl bg-sipi-bg border border-sipi-cardBorder hover:border-sipi-neon/50 text-lg font-bold text-white active:scale-95 transition-all">5</button>
        <button onclick="pressPin('6')" class="pin-btn h-13 py-3 rounded-2xl bg-sipi-bg border border-sipi-cardBorder hover:border-sipi-neon/50 text-lg font-bold text-white active:scale-95 transition-all">6</button>
        <button onclick="pressPin('7')" class="pin-btn h-13 py-3 rounded-2xl bg-sipi-bg border border-sipi-cardBorder hover:border-sipi-neon/50 text-lg font-bold text-white active:scale-95 transition-all">7</button>
        <button onclick="pressPin('8')" class="pin-btn h-13 py-3 rounded-2xl bg-sipi-bg border border-sipi-cardBorder hover:border-sipi-neon/50 text-lg font-bold text-white active:scale-95 transition-all">8</button>
        <button onclick="pressPin('9')" class="pin-btn h-13 py-3 rounded-2xl bg-sipi-bg border border-sipi-cardBorder hover:border-sipi-neon/50 text-lg font-bold text-white active:scale-95 transition-all">9</button>
        <button onclick="clearPin()" class="pin-btn h-13 py-3 rounded-2xl bg-sipi-bg/40 border border-sipi-cardBorder text-xs font-semibold text-sipi-textMuted active:scale-95 transition-all">Limpiar</button>
        <button onclick="pressPin('0')" class="pin-btn h-13 py-3 rounded-2xl bg-sipi-bg border border-sipi-cardBorder hover:border-sipi-neon/50 text-lg font-bold text-white active:scale-95 transition-all">0</button>
        <button onclick="backspacePin()" class="pin-btn h-13 py-3 rounded-2xl bg-sipi-bg/40 border border-sipi-cardBorder text-sipi-textMuted hover:text-white active:scale-95 transition-all flex items-center justify-center">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2M3 12l6.414-6.414A2 2 0 0110.828 5H20a2 2 0 012 2v10a2 2 0 01-2 2h-9.172a2 2 0 01-1.414-.586L3 12z"></path></svg>
        </button>
      </div>

      <p class="text-[11px] text-sipi-textMuted/60 mt-6">PIN por defecto: <code class="text-sipi-neon bg-sipi-bg px-1.5 py-0.5 rounded">2026</code></p>
    </div>
  </div>

  <!-- App Wrapper (Protected) -->
  <div id="appContainer" class="hidden min-h-screen flex flex-col">

    <!-- Toast Notification -->
    <div id="toast" class="fixed bottom-6 right-6 z-50 transform translate-y-24 opacity-0 transition-all duration-300 pointer-events-none bg-sipi-neon text-black font-semibold px-5 py-3 rounded-xl shadow-2xl flex items-center gap-3">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
      <span id="toast-text">¡Texto copiado al portapapeles!</span>
    </div>

    <!-- Header & Brand Bar -->
    <header class="border-b border-sipi-cardBorder bg-sipi-card/80 backdrop-blur-md sticky top-0 z-40">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex flex-col md:flex-row items-center justify-between gap-4">
        
        <!-- Left: Logo & View Switcher -->
        <div class="flex items-center gap-4 w-full md:w-auto justify-between md:justify-start">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-sipi-cardBorder to-sipi-neon/20 border border-sipi-neon/40 flex items-center justify-center text-sipi-neon shadow-lg shadow-sipi-neon/10">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
            </div>
            <div>
              <div class="flex items-center gap-2">
                <h1 class="text-xl font-bold font-serif tracking-wide text-white">SIPI Vault</h1>
                <span class="text-[10px] uppercase font-bold tracking-widest px-2 py-0.5 rounded-full bg-sipi-neon/10 text-sipi-neon border border-sipi-neon/30">Hub de Ejecución</span>
              </div>
              <p class="text-xs text-sipi-textMuted">Ecosistema & Contenidos · <span class="text-white font-medium">@fuel_w_roxy</span></p>
            </div>
          </div>

          <!-- View Switcher Tabs -->
          <div class="flex items-center gap-1 p-1 rounded-xl bg-sipi-bg border border-sipi-cardBorder">
            <button id="viewBtnIdeas" onclick="switchMainView('ideas')" class="px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-sipi-neon text-black shadow-sm flex items-center gap-1.5">
              <span>💡</span>
              <span class="hidden sm:inline">Bóveda de Ideas</span>
              <span class="sm:hidden">Ideas</span>
            </button>
            <button id="viewBtnTools" onclick="switchMainView('tools')" class="px-3 py-1.5 rounded-lg text-xs font-semibold transition-all text-sipi-textMuted hover:text-white flex items-center gap-1.5">
              <span>🗺️</span>
              <span class="hidden sm:inline">Bitácora Ecosistema</span>
              <span class="sm:hidden">Bitácora</span>
            </button>
          </div>
        </div>

        <!-- Right: Search & Lock Button -->
        <div class="flex items-center gap-3 w-full md:w-auto">
          <div class="relative w-full sm:w-72">
            <input type="text" id="searchInput" placeholder="Buscar por palabra clave..." 
                   class="w-full bg-sipi-bg/90 border border-sipi-cardBorder rounded-xl pl-9 pr-4 py-2 text-sm text-sipi-text placeholder-sipi-textMuted/60 focus:outline-none focus:border-sipi-neon focus:ring-1 focus:ring-sipi-neon transition-all">
            <svg class="w-4 h-4 absolute left-3 top-3 text-sipi-textMuted" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
          </div>
          <button onclick="lockVault()" title="Bloquear Bóveda" class="p-2.5 rounded-xl bg-sipi-bg border border-sipi-cardBorder text-sipi-textMuted hover:text-red-400 hover:border-red-400/40 transition-all flex items-center gap-1.5 text-xs font-semibold shrink-0">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
            <span class="hidden sm:inline">Bloquear</span>
          </button>
        </div>
      </div>

      <!-- Sub-Filter Bar: Ideas -->
      <div id="ideasFilterBar" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2.5 flex items-center gap-2 overflow-x-auto custom-scrollbar border-t border-sipi-cardBorder/40">
        <button onclick="filterPhase('all')" class="phase-btn active px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all bg-sipi-neon text-black font-semibold shadow-sm">
          Todas las Ideas (3)
        </button>
        <button onclick="filterPhase('fase-1')" class="phase-btn px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all bg-sipi-card border border-sipi-cardBorder text-sipi-textMuted hover:text-white hover:border-sipi-neon/40">
          🟢 Fase 1: Siembra & Cimientos (1)
        </button>
        <button onclick="filterPhase('fase-2')" class="phase-btn px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all bg-sipi-card border border-sipi-cardBorder text-sipi-textMuted hover:text-white hover:border-yellow-400/40">
          🟡 Fase 2: Tracción & Octubre (2)
        </button>
        <button onclick="filterPhase('fase-3')" class="phase-btn px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all bg-sipi-card border border-sipi-cardBorder text-sipi-textMuted hover:text-white hover:border-purple-400/40">
          🟣 Fase 3: Autoridad & Escala (0)
        </button>
      </div>

      <!-- Sub-Filter Bar: Tools -->
      <div id="toolsFilterBar" class="hidden max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2.5 flex items-center gap-2 overflow-x-auto custom-scrollbar border-t border-sipi-cardBorder/40">
        <button onclick="filterToolCat('all')" class="tool-cat-btn active px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all bg-sipi-neon text-black font-semibold shadow-sm">
          Todas las Herramientas (14)
        </button>
        <button onclick="filterToolCat('operaciones')" class="tool-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all bg-sipi-card border border-sipi-cardBorder text-sipi-textMuted hover:text-white hover:border-blue-400/40">
          📊 Operaciones & Ventas (3)
        </button>
        <button onclick="filterToolCat('redes')" class="tool-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all bg-sipi-card border border-sipi-cardBorder text-sipi-textMuted hover:text-white hover:border-pink-400/40">
          📲 Redes & Automatización (3)
        </button>
        <button onclick="filterToolCat('productos')" class="tool-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all bg-sipi-card border border-sipi-cardBorder text-sipi-textMuted hover:text-white hover:border-amber-400/40">
          📖 Productos & Revista (4)
        </button>
        <button onclick="filterToolCat('inteligencia')" class="tool-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all bg-sipi-card border border-sipi-cardBorder text-sipi-textMuted hover:text-white hover:border-emerald-400/40">
          🧠 Inteligencia & Minería (2)
        </button>
        <button onclick="filterToolCat('agentes')" class="tool-cat-btn px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all bg-sipi-card border border-sipi-cardBorder text-sipi-textMuted hover:text-white hover:border-purple-400/40">
          🤖 Equipo Agentes IA (2)
        </button>
      </div>

    </header>

    <!-- Main Container -->
    <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">

      <!-- ========================================== -->
      <!-- VIEW 1: BÓVEDA DE IDEAS                    -->
      <!-- ========================================== -->
      <section id="ideasView">
        <!-- Hero / Stage Context Banner -->
        <div class="mb-8 p-5 rounded-2xl bg-gradient-to-r from-sipi-card to-sipi-card/30 border border-sipi-cardBorder flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div>
            <div class="flex items-center gap-2 mb-1">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
              <span class="text-xs uppercase tracking-wider font-bold text-emerald-400">Estado de Operación Actual</span>
            </div>
            <h2 class="text-lg font-bold font-serif text-white">Canal en Fase 1 · Incubando Convocatorias para Octubre</h2>
            <p class="text-xs text-sipi-textMuted mt-1 max-w-2xl">
              Priorizamos publicaciones cotidianas de la UVa y rendimiento diario para cimentar seguidores. Las estrategias de alto volumen de comentarios (Networking Baits) están protegidas en la Fase 2 listas para desplegarse cuando alcancemos la masa crítica.
            </p>
          </div>
          <div class="flex items-center gap-2 self-end md:self-center">
            <a href="BOVEDA_ESTRATEGIAS_ROXY.md" target="_blank" class="px-3.5 py-2 rounded-xl text-xs font-semibold bg-sipi-bg border border-sipi-cardBorder hover:border-sipi-neon/50 text-sipi-text flex items-center gap-2 transition-all">
              <svg class="w-4 h-4 text-sipi-neon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
              Ver Markdown Maestro
            </a>
          </div>
        </div>

        <!-- Ideas Grid -->
        <div id="ideasGrid" class="grid grid-cols-1 lg:grid-cols-2 gap-6">

          <!-- CARD 1: VAULT-003 (Fase 1) -->
          <article class="idea-card fase-1 rounded-2xl bg-sipi-card border border-sipi-cardBorder hover:border-sipi-neon/40 transition-all p-6 flex flex-col justify-between group shadow-lg">
            <div>
              <div class="flex items-center justify-between gap-2 mb-4">
                <div class="flex items-center gap-2 flex-wrap">
                  <span class="font-mono text-xs font-bold px-2.5 py-1 rounded-md bg-sipi-bg border border-sipi-cardBorder text-sipi-neon">VAULT-003</span>
                  <span class="text-[11px] font-semibold px-2.5 py-1 rounded-md bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Fase 1: Siembra</span>
                  <span class="text-[11px] font-medium px-2 py-0.5 rounded-md bg-sipi-bg/70 text-sipi-textMuted border border-sipi-cardBorder">Reel / Foto UVa</span>
                </div>
                <span class="text-[10px] font-bold uppercase tracking-wider text-emerald-400 bg-emerald-950/40 px-2 py-0.5 rounded border border-emerald-500/30">Lista para Publicar</span>
              </div>

              <h3 class="text-xl font-bold font-serif text-white group-hover:text-sipi-neon transition-colors mb-2">
                La Realidad de un Plan B en la UVa
              </h3>
              <p class="text-xs text-sipi-textMuted mb-4">
                <strong>Objetivo:</strong> Identificación generacional con estudiantes de Valladolid y jóvenes con ambición de ingresos extra sin dejar su carrera.
              </p>

              <div class="space-y-3 mb-6">
                <div class="rounded-xl bg-sipi-bg/80 border border-sipi-cardBorder/70 p-3.5">
                  <div class="flex items-center justify-between mb-1.5">
                    <span class="text-xs font-semibold text-sipi-peach flex items-center gap-1.5">
                      <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                      Concepto Visual & Foto
                    </span>
                    <button onclick="copyToClipboard('prompt-003', 'Prompt copiado')" class="text-[11px] text-sipi-textMuted hover:text-sipi-neon transition-colors flex items-center gap-1">
                      Copiar Prompt
                    </button>
                  </div>
                  <p class="text-xs text-sipi-text/90 line-clamp-2">
                    Foto cotidiana realista de Roxy sentada en su mesa de estudio en Valladolid con su portátil, apuntes de carrera y una taza de té verde herbal humeante. Luz suave natural.
                  </p>
                  <input type="hidden" id="prompt-003" value="A realistic candid photograph of a 20-year-old Spanish female student sitting at a study desk in her student apartment in Valladolid. She has brown wavy hair, wearing a comfortable knit sweater. On the desk: an open laptop, university notebooks with handwriting, colorful highlighters, and a glass mug of hot herbal green tea. Soft warm lighting, authentic mood, 35mm film photography aesthetic, realistic depth of field --ar 4:5 --v 6.0">
                </div>

                <div class="rounded-xl bg-sipi-bg/80 border border-sipi-cardBorder/70 p-3.5">
                  <span class="text-xs font-semibold text-sipi-neon flex items-center gap-1.5 mb-1.5">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z"></path></svg>
                    Gancho & Copy (Voz de Roxy)
                  </span>
                  <p class="text-xs text-sipi-text/80 line-clamp-3 italic">
                    «Todos te dicen que estudies una carrera para "asegurarte el futuro". Lo que casi nadie te dice es que hoy en día un título no te asegura nada si no aprendes a construir tus propias oportunidades...»
                  </p>
                  <textarea id="caption-003" class="hidden">Todos te dicen que estudies una carrera para «asegurarte el futuro».
Lo que casi nadie te dice es que hoy en día un título no te asegura nada si no aprendes a construir tus propias oportunidades.

Tengo 20 años, estoy en segundo de carrera en la UVa y el año pasado me di cuenta de una verdad incómoda: la mayoría de egresados terminan en empleos de prácticas precarias o trabajando de algo que ni les llena ni les paga el coste de vida.

No dejé la carrera. Decidí hacer algo más inteligente: dedicar 1 hora y media al día a construir mi propio Plan B digital. Sin jefes, aprendiendo habilidades de negocio reales y ganando energía en lugar de perderla con café de máquina.

Si tú también sientes que el camino tradicional se queda corto, no estás loco. Solo necesitas un plan.

¿Estudias, trabajas o las dos cosas? Cuéntame abajo cómo te organizas 👇📚

#UniversitariosValladolid #UVa #EstudiantesEspaña #PlanB #EducacionFinancieraJoven #EmprenderJoven</textarea>
                </div>

                <div class="rounded-xl bg-sipi-bg/80 border border-sipi-cardBorder/70 p-3.5">
                  <span class="text-xs font-semibold text-white flex items-center gap-1.5 mb-1.5">
                    <svg class="w-3.5 h-3.5 text-sipi-peach" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
                    Prospección por DM (0 Enlaces)
                  </span>
                  <p class="text-xs text-sipi-textMuted line-clamp-2">
                    Elogio empático a quien comente sobre compaginar estudios o curro, ofreciendo guía de rutinas de energía para estudiantes si reconocen cansancio.
                  </p>
                  <textarea id="dm-003" class="hidden">¡Hola [Nombre]! Vi tu comentario en la publicación sobre compaginar la carrera. Qué mérito tiene lo que haces con [sus estudios o trabajo]. La verdad es que a veces da la sensación de que el día no tiene suficientes horas... ¿Qué estás estudiando o a qué te dedicas?</textarea>
                </div>
              </div>
            </div>

            <div class="grid grid-cols-2 gap-2.5 pt-4 border-t border-sipi-cardBorder">
              <button onclick="copyToClipboard('caption-003', '¡Caption de Instagram copiado!')" class="w-full py-2.5 px-3 rounded-xl text-xs font-bold bg-sipi-neon text-black hover:bg-sipi-neonDim transition-all flex items-center justify-center gap-1.5 shadow-sm">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3"></path></svg>
                Copiar Caption
              </button>
              <button onclick="copyToClipboard('dm-003', '¡Guión de DM copiado!')" class="w-full py-2.5 px-3 rounded-xl text-xs font-semibold bg-sipi-bg border border-sipi-cardBorder hover:border-sipi-peach text-sipi-text hover:text-sipi-peach transition-all flex items-center justify-center gap-1.5">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path></svg>
                Copiar DM
              </button>
            </div>
          </article>

          <!-- CARD 2: VAULT-001 (Fase 2 - Octubre) -->
          <article class="idea-card fase-2 rounded-2xl bg-sipi-card border border-sipi-cardBorder hover:border-yellow-400/40 transition-all p-6 flex flex-col justify-between group shadow-lg">
            <div>
              <div class="flex items-center justify-between gap-2 mb-4">
                <div class="flex items-center gap-2 flex-wrap">
                  <span class="font-mono text-xs font-bold px-2.5 py-1 rounded-md bg-sipi-bg border border-sipi-cardBorder text-sipi-neon">VAULT-001</span>
                  <span class="text-[11px] font-semibold px-2.5 py-1 rounded-md bg-yellow-500/10 text-yellow-400 border border-yellow-500/20">Fase 2: Octubre</span>
                  <span class="text-[11px] font-medium px-2 py-0.5 rounded-md bg-sipi-bg/70 text-sipi-textMuted border border-sipi-cardBorder">Networking Bait</span>
                </div>
                <span class="text-[10px] font-bold uppercase tracking-wider text-yellow-400 bg-yellow-950/40 px-2 py-0.5 rounded border border-yellow-500/30">Guardada para Octubre</span>
              </div>

              <h3 class="text-xl font-bold font-serif text-white group-hover:text-yellow-400 transition-colors mb-2">
                Directorio Abierto de Emprendedores
              </h3>
              <p class="text-xs text-sipi-textMuted mb-4">
                <strong>Objetivo:</strong> Disparar los comentarios largos, activar el algoritmo de Meta y perfilar emprendedores locales para prospección por mensaje privado.
              </p>

              <div class="space-y-3 mb-6">
                <div class="rounded-xl bg-sipi-bg/80 border border-sipi-cardBorder/70 p-3.5">
                  <div class="flex items-center justify-between mb-1.5">
                    <span class="text-xs font-semibold text-sipi-peach flex items-center gap-1.5">
                      <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                      Diseño Gráfico 4:5 & Banner
                    </span>
                    <button onclick="copyToClipboard('prompt-001', 'Prompt copiado')" class="text-[11px] text-sipi-textMuted hover:text-yellow-400 transition-colors flex items-center gap-1">
                      Copiar Prompt
                    </button>
                  </div>
                  <p class="text-xs text-sipi-text/90 line-clamp-2">
                    Banner superior verde bosque (#0E150C) con texto en Playfair Display: "DIRECTORIO DE EMPRENDEDORES". Foto de Roxy con portátil y té en cafetería de Valladolid.
                  </p>
                  <input type="hidden" id="prompt-001" value="A high-end editorial lifestyle photograph for an Instagram post in 4:5 aspect ratio. The scene shows a genuine 20-year-old Spanish female university student with brunette wavy hair, sitting at a wooden cafe table in Valladolid, Spain. Laptop, dotted notebook with blueprints, glass mug with healthy herbal green tea. Clean graphic design typography banner at the top in forest green (#0E150C) reading 'DIRECTORIO DE EMPRENDEDORES' in Playfair Display serif, and subtitle 'Deja tu proyecto en comentarios y conectemos'. Soft natural morning light, cozy professional student entrepreneur aesthetic --ar 4:5 --v 6.0 --style raw">
                </div>

                <div class="rounded-xl bg-sipi-bg/80 border border-sipi-cardBorder/70 p-3.5">
                  <span class="text-xs font-semibold text-yellow-400 flex items-center gap-1.5 mb-1.5">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z"></path></svg>
                    Copy Completo de Convocatoria
                  </span>
                  <p class="text-xs text-sipi-text/80 line-clamp-3 italic">
                    «Este post no es para mí, es para ti. Si tienes una marca, un proyecto o estás empezando un emprendimiento: hoy nos promocionamos gratis aquí abajo 👇...»
                  </p>
                  <textarea id="caption-001" class="hidden">Este post no es para mí, es para ti. Si tienes una marca, un proyecto o estás empezando un emprendimiento: hoy nos promocionamos gratis aquí abajo 👇

La verdad por delante: no soy ninguna gurú de las finanzas ni te voy a decir que te harás millonario en 30 días. Tengo 20 años, estoy en segundo de carrera en la UVa y, en paralelo a las clases y los exámenes, decidí montar mi propio Plan B porque tenía claro que depender de un solo camino no era para mí.

Y si algo he aprendido estos meses es lo difícil que se hace arrancar cuando:
1️⃣ Tu presupuesto para publicidad es exactamente 0€.
2️⃣ La gente de tu entorno no siempre entiende tus ganas de crear algo propio.
3️⃣ Te faltan horas y energía en el día para llegar a todo.

Por eso abro este post como un DIRECTORIO ABIERTO y pizarra de networking para toda la comunidad.

¿Cómo funciona la dinámica?
1. Deja en un comentario el @ de tu proyecto o marca personal.
2. Cuéntanos en 2 o 3 líneas qué haces, a quién ayudas y cuál es tu mayor ilusión con él.
3. Si eres de Valladolid o de Castilla y León, ¡indícalo! Me encantaría que nos conociéramos en persona o nos tomáramos un café de ideas ☕️
4. REGLA DE ORO DE LA COMUNIDAD: Entra en el perfil de al menos 2 personas que hayan comentado, déjales unas palabras de apoyo o un follow. Estamos todos en el mismo barco.

Me voy a pasar uno a uno por todos vuestros proyectos para leeros, compartir algunos por Stories y dejaros un mensaje.

¡Los comentarios son todos vuestros! ¿Qué estás construyendo? Te leo abajo 👇⚡️

#EmprendedoresValladolid #JovenesEmprendedores #ComunidadEmprendedora #EstuFuel #PlanB #NetworkingEspana #UniversidadDeValladolid #UVa</textarea>
                </div>

                <div class="rounded-xl bg-sipi-bg/80 border border-sipi-cardBorder/70 p-3.5">
                  <span class="text-xs font-semibold text-white flex items-center gap-1.5 mb-1.5">
                    <svg class="w-3.5 h-3.5 text-yellow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
                    Protocolo Anti-Baneo por DM (Paso 1 a 4)
                  </span>
                  <p class="text-xs text-sipi-textMuted line-clamp-2">
                    1. Respuesta pública validando marca. 2. DM con elogio sincero sin links. 3. Sondeo de tiempo/energía. 4. Entrega de SIPI Magazine en PDF.
                  </p>
                  <textarea id="dm-001" class="hidden">[PASO 1 - FEED]: ¡Qué proyectazo, [Nombre]! Me encanta lo que hacéis con [su producto]. Te he dejado un mensajito por privado para charlar un ratito sobre ello ✨

[PASO 2 - DM 1]: ¡Hola [Nombre]! 👋 Acabo de ver el comentario que dejaste en el post y entré a ver tu cuenta. Me parece una pasada lo que estás montando con [detalle real]. Me alegra un montón ver a gente joven con tantas ganas de crear cosas propias. ¿Cuánto tiempo llevas con el proyecto?

[PASO 3 - DM 2]: ¡Qué mérito tiene! Yo estoy en segundo de carrera en la UVa y compagino las clases con mi propio proyecto digital, y sé de sobra lo que desgasta intentar llegar a todo. En tu caso, ¿es tu dedicación principal o también te toca compaginarlo? ¿Cómo vas de tiempo y energía?

[PASO 4 - DM 3]: Te entiendo al 100%... Justo con el equipo preparamos una edición especial en PDF de nuestra revista digital enfocada en productividad para emprendedores y rutinas de energía para rendir sin quemarse. Si te apetece leerla, te la paso encantada por aquí o por WhatsApp para que la tengas guardada ✨</textarea>
                </div>
              </div>
            </div>

            <div class="grid grid-cols-2 gap-2.5 pt-4 border-t border-sipi-cardBorder">
              <button onclick="copyToClipboard('caption-001', '¡Caption de Instagram copiado!')" class="w-full py-2.5 px-3 rounded-xl text-xs font-bold bg-yellow-400 text-black hover:bg-yellow-300 transition-all flex items-center justify-center gap-1.5 shadow-sm">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3"></path></svg>
                Copiar Caption
              </button>
              <button onclick="copyToClipboard('dm-001', '¡Protocolo de DM copiado!')" class="w-full py-2.5 px-3 rounded-xl text-xs font-semibold bg-sipi-bg border border-sipi-cardBorder hover:border-yellow-400 text-sipi-text hover:text-yellow-400 transition-all flex items-center justify-center gap-1.5">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path></svg>
                Copiar DM
              </button>
            </div>
          </article>

          <!-- CARD 3: VAULT-002 (Fase 2 - Octubre) -->
          <article class="idea-card fase-2 rounded-2xl bg-sipi-card border border-sipi-cardBorder hover:border-yellow-400/40 transition-all p-6 flex flex-col justify-between group shadow-lg">
            <div>
              <div class="flex items-center justify-between gap-2 mb-4">
                <div class="flex items-center gap-2 flex-wrap">
                  <span class="font-mono text-xs font-bold px-2.5 py-1 rounded-md bg-sipi-bg border border-sipi-cardBorder text-sipi-neon">VAULT-002</span>
                  <span class="text-[11px] font-semibold px-2.5 py-1 rounded-md bg-yellow-500/10 text-yellow-400 border border-yellow-500/20">Fase 2: Octubre</span>
                  <span class="text-[11px] font-medium px-2 py-0.5 rounded-md bg-sipi-bg/70 text-sipi-textMuted border border-sipi-cardBorder">Carrusel Editorial</span>
                </div>
                <span class="text-[10px] font-bold uppercase tracking-wider text-yellow-400 bg-yellow-950/40 px-2 py-0.5 rounded border border-yellow-500/30">Guardada para Octubre</span>
              </div>

              <h3 class="text-xl font-bold font-serif text-white group-hover:text-yellow-400 transition-colors mb-2">
                Convocatoria: Talento Emergente SIPI Magazine
              </h3>
              <p class="text-xs text-sipi-textMuted mb-4">
                <strong>Objetivo:</strong> Elevar el estatus institucional de Roxy a Directora Editorial y cualificar con alta precisión a candidatos para el modelo de negocio.
              </p>

              <div class="space-y-3 mb-6">
                <div class="rounded-xl bg-sipi-bg/80 border border-sipi-cardBorder/70 p-3.5">
                  <div class="flex items-center justify-between mb-1.5">
                    <span class="text-xs font-semibold text-sipi-peach flex items-center gap-1.5">
                      <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                      Carrusel Editorial 4 Slides
                    </span>
                    <button onclick="copyToClipboard('prompt-002', 'Estructura copiada')" class="text-[11px] text-sipi-textMuted hover:text-yellow-400 transition-colors flex items-center gap-1">
                      Ver Slides
                    </button>
                  </div>
                  <p class="text-xs text-sipi-text/90 line-clamp-2">
                    Carrusel estilo revista de moda/negocios. Portada elegante con título: "Convocatoria Nuevos Emprendedores". Slides explicando la difusión y el sello digital.
                  </p>
                  <input type="hidden" id="prompt-002" value="Slide 1: Convocatoria de Nuevos Emprendedores para SIPI Magazine #2 | Slide 2: Beneficios de difusión y sello de historia destacada | Slide 3: Cómo participar en comentarios | Slide 4: Fecha límite Octubre 2026">
                </div>

                <div class="rounded-xl bg-sipi-bg/80 border border-sipi-cardBorder/70 p-3.5">
                  <span class="text-xs font-semibold text-yellow-400 flex items-center gap-1.5 mb-1.5">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z"></path></svg>
                    Copy de Prestigio & Convocatoria
                  </span>
                  <p class="text-xs text-sipi-text/80 line-clamp-3 italic">
                    «No todos los proyectos nacen con millones de euros en inversión. Los más valiosos casi siempre nacen con una ilusión enorme, horas de insomnio y un corazón gigante...»
                  </p>
                  <textarea id="caption-002" class="hidden">No todos los proyectos nacen con millones de euros en inversión. Los más valiosos casi siempre nacen con una ilusión enorme, horas de insomnio y un corazón gigante.

En el equipo de SIPI Magazine creemos que el talento emergente merece ser visto. Por eso, en la próxima edición de nuestra revista digital vamos a dedicar una sección especial a destacar historias reales de personas que están construyendo sus propios negocios desde cero.

Si tienes una marca, un servicio o un proyecto propio y quieres que te conozcan en nuestra comunidad:
1. Déjanos en comentarios tu @ y a qué te dedicas.
2. Te escribiremos por privado con un mini-cuestionario para conocer tu historia.

Tu proyecto merece una portada. Cuéntanoslo abajo 👇✨

#SIPIMagazine #TalentoEmergente #MujeresEmprendedoras #EmprenderConProposito #RevistaDigital #ComunidadSIPI</textarea>
                </div>

                <div class="rounded-xl bg-sipi-bg/80 border border-sipi-cardBorder/70 p-3.5">
                  <span class="text-xs font-semibold text-white flex items-center gap-1.5 mb-1.5">
                    <svg class="w-3.5 h-3.5 text-yellow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
                    Cuestionario de Cualificación Editorial
                  </span>
                  <p class="text-xs text-sipi-textMuted line-clamp-2">
                    4 preguntas que evalúan su "Por Qué", su reto principal (tiempo/energía/ventas) y su apertura a una vía complementaria de ingresos del 1 al 10.
                  </p>
                  <textarea id="dm-002" class="hidden">¡Hola [Nombre]! Nos encantó tu iniciativa y queremos considerarte para la sección 'Talento Emergente' en la próxima edición de SIPI Magazine. Para redactar tu reseña y conocer al humano detrás de la marca, cuéntanos en un par de líneas:

1. ¿Cuál fue tu mayor motivación para empezar tu proyecto?
2. Siendo realistas, hoy en día ¿qué te cuesta más: la falta de tiempo, el bajón de energía a media tarde o conseguir clientes?
3. ¿Cuántas horas le dedicas a la semana y qué haces para mantener a raya el estrés?
4. Si surgiera un proyecto paralelo que complementara tus ingresos sin robarte 10 horas al día, del 1 al 10, ¿qué tan abierto estarías a escuchar?</textarea>
                </div>
              </div>
            </div>

            <div class="grid grid-cols-2 gap-2.5 pt-4 border-t border-sipi-cardBorder">
              <button onclick="copyToClipboard('caption-002', '¡Caption de Revista copiado!')" class="w-full py-2.5 px-3 rounded-xl text-xs font-bold bg-yellow-400 text-black hover:bg-yellow-300 transition-all flex items-center justify-center gap-1.5 shadow-sm">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3"></path></svg>
                Copiar Caption
              </button>
              <button onclick="copyToClipboard('dm-002', '¡Cuestionario de DM copiado!')" class="w-full py-2.5 px-3 rounded-xl text-xs font-semibold bg-sipi-bg border border-sipi-cardBorder hover:border-yellow-400 text-sipi-text hover:text-yellow-400 transition-all flex items-center justify-center gap-1.5">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path></svg>
                Copiar Preguntas
              </button>
            </div>
          </article>

        </div>
      </section>

      <!-- ========================================== -->
      <!-- VIEW 2: BITÁCORA DEL ECOSISTEMA            -->
      <!-- ========================================== -->
      <section id="toolsView" class="hidden">
        <!-- Architecture Pipeline Banner -->
        <div class="mb-8 p-6 rounded-2xl bg-gradient-to-r from-sipi-card to-sipi-card/30 border border-sipi-cardBorder">
          <div class="flex items-center gap-2 mb-2">
            <span class="w-2.5 h-2.5 rounded-full bg-sipi-neon animate-pulse"></span>
            <span class="text-xs uppercase tracking-wider font-bold text-sipi-neon">Mapa de Arquitectura & Embudo de Negocio</span>
          </div>
          <h2 class="text-xl font-bold font-serif text-white mb-2">Directorio Maestro de Herramientas del Ecosistema SIPI</h2>
          <p class="text-xs text-sipi-textMuted max-w-3xl leading-relaxed mb-6">
            Inventario completo de los 5 pilares operativos construidos para <strong>@fuel_w_roxy</strong>, <strong>EstuFuel</strong> y <strong>Sistema SIPI</strong>. Cada pieza cumple un rol preciso en el flujo que transforma un espectador en seguidor, suscriptor, cliente y socio distribuidor de red.
          </p>

          <!-- Pipeline Visual Flow -->
          <div class="grid grid-cols-2 md:grid-cols-5 gap-3 text-center">
            <div class="p-3 rounded-xl bg-sipi-bg/80 border border-sipi-cardBorder">
              <span class="text-xs font-bold text-emerald-400 block mb-1">1. Inteligencia</span>
              <p class="text-[11px] text-sipi-text font-medium">ViralLens & Vault</p>
              <p class="text-[10px] text-sipi-textMuted mt-0.5">Minería & Ganchos</p>
            </div>
            <div class="p-3 rounded-xl bg-sipi-bg/80 border border-sipi-cardBorder">
              <span class="text-xs font-bold text-pink-400 block mb-1">2. Atracción</span>
              <p class="text-[11px] text-sipi-text font-medium">Instagram @roxy</p>
              <p class="text-[10px] text-sipi-textMuted mt-0.5">Contenido UVa</p>
            </div>
            <div class="p-3 rounded-xl bg-sipi-bg/80 border border-sipi-cardBorder">
              <span class="text-xs font-bold text-pink-400 block mb-1">3. Automatización</span>
              <p class="text-[11px] text-sipi-text font-medium">SIPI Bot Roxy</p>
              <p class="text-[10px] text-sipi-textMuted mt-0.5">DMs & Keywords</p>
            </div>
            <div class="p-3 rounded-xl bg-sipi-bg/80 border border-sipi-cardBorder">
              <span class="text-xs font-bold text-amber-400 block mb-1">4. Conversión</span>
              <p class="text-[11px] text-sipi-text font-medium">SIPI Magazine</p>
              <p class="text-[10px] text-sipi-textMuted mt-0.5">Lead Magnet & Citas</p>
            </div>
            <div class="p-3 rounded-xl bg-sipi-bg/80 border border-sipi-cardBorder col-span-2 md:col-span-1">
              <span class="text-xs font-bold text-blue-400 block mb-1">5. Operaciones</span>
              <p class="text-[11px] text-sipi-text font-medium">EstuFuel Suite</p>
              <p class="text-[10px] text-sipi-textMuted mt-0.5">CRM, Ventas & Red</p>
            </div>
          </div>
        </div>

        <!-- Tools Grid (14 tools) -->
        <div id="toolsGrid" class="grid grid-cols-1 lg:grid-cols-2 gap-6">
{tools_cards_html}
        </div>
      </section>

      <!-- Empty Search State -->
      <div id="noResults" class="hidden text-center py-16">
        <div class="w-16 h-16 rounded-full bg-sipi-card border border-sipi-cardBorder mx-auto flex items-center justify-center text-sipi-textMuted mb-3">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
        </div>
        <h4 class="text-base font-bold text-white mb-1">No se encontraron resultados</h4>
        <p class="text-xs text-sipi-textMuted">Prueba ajustando el término de búsqueda o cambiando de pestaña o categoría.</p>
      </div>

    </main>

    <!-- Footer -->
    <footer class="border-t border-sipi-cardBorder/60 py-6 bg-sipi-bg/90 mt-12 text-center">
      <p class="text-xs text-sipi-textMuted">
        <strong>SIPI Vault</strong> · Bóveda de Contenidos & Bitácora del Ecosistema · Conectado con agentes IA
      </p>
    </footer>

  </div> <!-- End of #appContainer -->

  <!-- Scripts -->
  <script>
    // PIN Authentication System
    const VAULT_PIN = "2026";
    let enteredPin = "";

    function checkSavedAuth() {{
      if (localStorage.getItem('sipi_vault_auth') === 'granted') {{
        showApp();
      }} else {{
        showLock();
      }}
    }}

    function pressPin(digit) {{
      if (enteredPin.length < 4) {{
        enteredPin += digit;
        updatePinDots();
        if (enteredPin.length === 4) {{
          setTimeout(verifyPin, 150);
        }}
      }}
    }}

    function clearPin() {{
      enteredPin = "";
      updatePinDots();
      hideError();
    }}

    function backspacePin() {{
      if (enteredPin.length > 0) {{
        enteredPin = enteredPin.slice(0, -1);
        updatePinDots();
        hideError();
      }}
    }}

    function updatePinDots() {{
      const dots = document.querySelectorAll('.pin-dot');
      dots.forEach((dot, index) => {{
        if (index < enteredPin.length) {{
          dot.classList.remove('border-sipi-cardBorder', 'bg-transparent');
          dot.classList.add('border-sipi-neon', 'bg-sipi-neon', 'shadow-md', 'shadow-sipi-neon/50');
        }} else {{
          dot.classList.remove('border-sipi-neon', 'bg-sipi-neon', 'shadow-md', 'shadow-sipi-neon/50');
          dot.classList.add('border-sipi-cardBorder', 'bg-transparent');
        }}
      }});
    }}

    function verifyPin() {{
      if (enteredPin === VAULT_PIN) {{
        localStorage.setItem('sipi_vault_auth', 'granted');
        showApp();
      }} else {{
        showError();
        shakeLockBox();
        setTimeout(clearPin, 600);
      }}
    }}

    function showError() {{
      const err = document.getElementById('pinError');
      err.classList.remove('opacity-0');
      err.classList.add('opacity-100');
    }}

    function hideError() {{
      const err = document.getElementById('pinError');
      err.classList.remove('opacity-100');
      err.classList.add('opacity-0');
    }}

    function shakeLockBox() {{
      const box = document.getElementById('lockBox');
      box.classList.add('animate-bounce');
      setTimeout(() => box.classList.remove('animate-bounce'), 400);
    }}

    function showApp() {{
      document.getElementById('lockScreen').classList.add('hidden');
      document.getElementById('appContainer').classList.remove('hidden');
    }}

    function showLock() {{
      document.getElementById('lockScreen').classList.remove('hidden');
      document.getElementById('appContainer').classList.add('hidden');
      clearPin();
    }}

    function lockVault() {{
      localStorage.removeItem('sipi_vault_auth');
      showLock();
      showToast('Bóveda bloqueada');
    }}

    // Physical keyboard listener for PIN
    window.addEventListener('keydown', (e) => {{
      if (document.getElementById('lockScreen').classList.contains('hidden')) return;
      if (e.key >= '0' && e.key <= '9') {{
        pressPin(e.key);
      }} else if (e.key === 'Backspace') {{
        backspacePin();
      }} else if (e.key === 'Escape' || e.key === 'Delete') {{
        clearPin();
      }}
    }});

    // Run auth check on load
    checkSavedAuth();

    // ==========================================
    // VIEW SWITCHER LOGIC
    // ==========================================
    let currentMainView = 'ideas'; // 'ideas' or 'tools'
    let currentPhase = 'all';
    let currentToolCat = 'all';

    function switchMainView(view) {{
      currentMainView = view;
      const btnIdeas = document.getElementById('viewBtnIdeas');
      const btnTools = document.getElementById('viewBtnTools');
      const viewIdeas = document.getElementById('ideasView');
      const viewTools = document.getElementById('toolsView');
      const barIdeas = document.getElementById('ideasFilterBar');
      const barTools = document.getElementById('toolsFilterBar');
      const searchInput = document.getElementById('searchInput');

      if (view === 'ideas') {{
        btnIdeas.className = "px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-sipi-neon text-black shadow-sm flex items-center gap-1.5";
        btnTools.className = "px-3 py-1.5 rounded-lg text-xs font-semibold transition-all text-sipi-textMuted hover:text-white flex items-center gap-1.5";
        viewIdeas.classList.remove('hidden');
        viewTools.classList.add('hidden');
        barIdeas.classList.remove('hidden');
        barTools.classList.add('hidden');
        searchInput.placeholder = "Buscar por copy, gancho o avatar...";
      }} else {{
        btnTools.className = "px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-sipi-neon text-black shadow-sm flex items-center gap-1.5";
        btnIdeas.className = "px-3 py-1.5 rounded-lg text-xs font-semibold transition-all text-sipi-textMuted hover:text-white flex items-center gap-1.5";
        viewTools.classList.remove('hidden');
        viewIdeas.classList.add('hidden');
        barTools.classList.remove('hidden');
        barIdeas.classList.add('hidden');
        searchInput.placeholder = "Buscar por herramienta, tecnología o función...";
      }}

      applyFilters();
    }}

    // Filters for Ideas
    function filterPhase(phase) {{
      currentPhase = phase;
      document.querySelectorAll('.phase-btn').forEach(btn => {{
        btn.classList.remove('bg-sipi-neon', 'text-black', 'font-semibold', 'bg-yellow-400');
        btn.classList.add('bg-sipi-card', 'text-sipi-textMuted');
      }});

      const activeBtn = event.currentTarget;
      if (phase === 'all' || phase === 'fase-1') {{
        activeBtn.classList.remove('bg-sipi-card', 'text-sipi-textMuted');
        activeBtn.classList.add('bg-sipi-neon', 'text-black', 'font-semibold');
      }} else if (phase === 'fase-2') {{
        activeBtn.classList.remove('bg-sipi-card', 'text-sipi-textMuted');
        activeBtn.classList.add('bg-yellow-400', 'text-black', 'font-semibold');
      }} else if (phase === 'fase-3') {{
        activeBtn.classList.remove('bg-sipi-card', 'text-sipi-textMuted');
        activeBtn.classList.add('bg-purple-400', 'text-black', 'font-semibold');
      }}

      applyFilters();
    }}

    // Filters for Tools
    function filterToolCat(cat) {{
      currentToolCat = cat;
      document.querySelectorAll('.tool-cat-btn').forEach(btn => {{
        btn.classList.remove('bg-sipi-neon', 'text-black', 'font-semibold');
        btn.classList.add('bg-sipi-card', 'text-sipi-textMuted');
      }});

      const activeBtn = event.currentTarget;
      activeBtn.classList.remove('bg-sipi-card', 'text-sipi-textMuted');
      activeBtn.classList.add('bg-sipi-neon', 'text-black', 'font-semibold');

      applyFilters();
    }}

    document.getElementById('searchInput').addEventListener('input', applyFilters);

    function applyFilters() {{
      const query = document.getElementById('searchInput').value.toLowerCase().trim();
      let visibleCount = 0;

      if (currentMainView === 'ideas') {{
        const cards = document.querySelectorAll('.idea-card');
        cards.forEach(card => {{
          const matchesPhase = (currentPhase === 'all') || card.classList.contains(currentPhase);
          const cardText = card.innerText.toLowerCase();
          const matchesQuery = !query || cardText.includes(query);

          if (matchesPhase && matchesQuery) {{
            card.style.display = 'flex';
            visibleCount++;
          }} else {{
            card.style.display = 'none';
          }}
        }});
      }} else {{
        const toolCards = document.querySelectorAll('.tool-card');
        toolCards.forEach(card => {{
          const matchesCat = (currentToolCat === 'all') || card.classList.contains(currentToolCat);
          const cardText = card.innerText.toLowerCase();
          const matchesQuery = !query || cardText.includes(query);

          if (matchesCat && matchesQuery) {{
            card.style.display = 'flex';
            visibleCount++;
          }} else {{
            card.style.display = 'none';
          }}
        }});
      }}

      const noResults = document.getElementById('noResults');
      if (visibleCount === 0) {{
        noResults.classList.remove('hidden');
      }} else {{
        noResults.classList.add('hidden');
      }}
    }}

    function copyToClipboard(elementId, successMessage = '¡Copiado con éxito!') {{
      const el = document.getElementById(elementId);
      if (!el) return;

      const text = el.value || el.innerText;
      copyToClipboardText(text, successMessage);
    }}

    function copyToClipboardText(text, successMessage = '¡Copiado al portapapeles!') {{
      navigator.clipboard.writeText(text).then(() => {{
        showToast(successMessage);
      }}).catch(err => {{
        console.error('Error al copiar:', err);
        showToast('Error al copiar al portapapeles');
      }});
    }}

    function showToast(message) {{
      const toast = document.getElementById('toast');
      const toastText = document.getElementById('toast-text');
      toastText.innerText = message;

      toast.classList.remove('translate-y-24', 'opacity-0');
      toast.classList.add('translate-y-0', 'opacity-100');

      setTimeout(() => {{
        toast.classList.remove('translate-y-0', 'opacity-100');
        toast.classList.add('translate-y-24', 'opacity-0');
      }}, 2500);
    }}
  </script>
</body>
</html>
'''

with open('sipi-vault/index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print('sipi-vault/index.html generated successfully. Total length:', len(full_html))
