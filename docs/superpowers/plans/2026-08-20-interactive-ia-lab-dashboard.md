# Laboratorio Interactivo de Asistentes de IA - Plan de Implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a highly polished, interactive, single-page web dashboard (`index.html`) at the root of the repository that serves as a visual "IA Assistant Lab" for the course students.

**Architecture:** Self-contained Single Page Application (SPA) using HTML5, modern semantic JavaScript, and custom Vanilla CSS with custom properties, smooth transitions, glassmorphic cards, and responsive grids. 

**Tech Stack:** HTML5, Vanilla CSS3 (Gradients, Flexbox, CSS Grid, Custom scrollbars), Vanilla JavaScript (ES6+).

## Global Constraints
- **Styling:** Strict adherence to Vanilla CSS (no Tailwind CSS, no external JS framework dependencies to ensure instant local loading).
- **Theme:** "Futuristic Ultra Dark" using deep slates (#0b0f19), purple (#8b5cf6), and neon teal (#14b8a6) accents.
- **Portability:** The file must be fully self-contained and runnable locally by double-clicking `index.html` or hosting on GitHub Pages with zero servers.
- **Languages:** Complete support for Spanish copywriting as established in the course curriculum.

---

## Files to be Touched / Created
- Create: `index.html` (The complete self-contained application)
- Create: `docs/superpowers/plans/2026-08-20-interactive-ia-lab-dashboard.md` (This plan)

---

### Task 1: Scaffolding and Aesthetic Theme Setup

**Files:**
- Create: `index.html`

**Interfaces:**
- Produces: The basic HTML skeleton with custom Vanilla CSS variables, global styles, and responsive layout grid.

- [ ] **Step 1: Write the initial structure of index.html**
Write the base HTML shell with meta tags, responsive viewport, and a `<style>` block containing CSS custom variables:
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Laboratorio de Asistente IA - Academia AAA</title>
    <style>
        :root {
            --bg-main: #0b132b;
            --bg-card: #1c2541;
            --bg-card-hover: #222e50;
            --primary: #6c5ce7;
            --primary-glow: rgba(108, 92, 231, 0.4);
            --accent: #00b894;
            --accent-glow: rgba(0, 184, 148, 0.4);
            --text-main: #f5f6fa;
            --text-muted: #a4b0be;
            --border-color: rgba(255, 255, 255, 0.1);
        }
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        body {
            background-color: var(--bg-main);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
        }
    </style>
</head>
<body>
    <header style="padding: 20px; border-bottom: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center;">
        <h1 style="font-size: 24px; color: var(--text-main);">🤖 Laboratorio Asistente IA</h1>
        <span style="font-size: 14px; background: var(--primary); padding: 5px 12px; border-radius: 20px;">Academia AAA</span>
    </header>
    <main id="app-container" style="flex: 1; display: grid; grid-template-columns: 280px 1fr; gap: 20px; padding: 20px;">
        <aside id="sidebar"></aside>
        <section id="workspace"></section>
    </main>
</body>
</html>
```

- [ ] **Step 2: Add sidebar navigation tabs and dashboard grid**
Write CSS and HTML for the sidebar navigation links: "Enjambre de Agentes", "Temario del Curso", "Simulador de Embudo", and "Bóveda de Prompts". Add active tab states with glowing highlights.

- [ ] **Step 3: Test and verify local load**
Verify that the `index.html` loads correctly in any web browser with smooth gradients and a modern dark aesthetic.

- [ ] **Step 4: Commit scaffolding**
```bash
git add index.html
git commit -m "feat: setup basic HTML scaffolding and dark theme variables"
```

---

### Task 2: Implement "Bóveda de Prompts y Configuración" Tab

**Files:**
- Modify: `index.html`

**Interfaces:**
- Consumes: Prompt configurations from `agents/AGENTES_CONFIG_Y_PROMPTS.md`.
- Produces: A searchable list of the 8 agents with copy-to-clipboard functionality for their System Prompts.

- [ ] **Step 1: Write the prompt library layout in CSS**
Create modern grid styles with glassmorphic cards for each agent.
```css
.agent-card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 20px;
    transition: all 0.3s ease;
    cursor: pointer;
}
.agent-card:hover {
    background: var(--bg-card-hover);
    transform: translateY(-5px);
    box-shadow: 0 10px 20px var(--primary-glow);
}
```

- [ ] **Step 2: Add the data arrays and render logic in JS**
Add an array of objects containing data for all 8 agents (Orquestador, Scraper, Copywriter, etc.) with their respective system prompts. Write a JavaScript function `renderPromptVault()` that displays them visually and supports filter search by name.

- [ ] **Step 3: Add copy-to-clipboard functionality**
Implement a copy button inside each card that copy the exact System Prompt to the user's clipboard and flashes a "¡Copiado! 📋" animation.

- [ ] **Step 4: Verify prompt layout**
Ensure clicking copy behaves properly and matches contents of `agents/AGENTES_CONFIG_Y_PROMPTS.md`.

- [ ] **Step 5: Commit Prompt Vault**
```bash
git add index.html
git commit -m "feat: implement prompt vault tab with search and clipboard-copy"
```

---

### Task 3: Implement Interactive "Enjambre de Agentes (Chat Simulator)"

**Files:**
- Modify: `index.html`

**Interfaces:**
- Consumes: The agent definitions and capabilities.
- Produces: An interactive terminal interface simulating real-time agent "thinking" (Chain of Thought), tool calling, and resulting outputs.

- [ ] **Step 1: Create layout for Chat Console**
Create a two-column view:
- Left: Chat dialogue area with input field and model selector.
- Right: Terminal monitor ("Consola de Pensamientos") with green/blue monospaced font output.

- [ ] **Step 2: Write simulated responses engine**
Write JavaScript that triggers when the user hits "Send" or clicks one of the quick suggestions (e.g., "Generar copy de pauta", "Calificar lead WhatsApp"). The engine must:
1. Print the user message in the chat.
2. Animate step-by-step thoughts in the Terminal Monitor (e.g. `[PENSAMIENTO] Cargando módulo de Copywriting...`).
3. Animate simulated tool executions in the Terminal (e.g. `[TOOL] execute_scraper_tool({ url: "..." }) -> Output: OK`).
4. Append a final beautifully formatted response to the main chat window.

- [ ] **Step 3: Integrate real-world outputs from marketing_studio and funnels**
Ensure that when a user asks to "Generar Guion Viral" or "Generar Copy Ads", the simulated response outputs the exact high-converting copy assets from your `GUIONES_VIRALES_Y_ANUNCIOS.md` file!

- [ ] **Step 4: Verify chat loops**
Ensure terminal scroll stays at the bottom and outputs simulate realistic agent pipelines.

- [ ] **Step 5: Commit Chat Simulator**
```bash
git add index.html
git commit -m "feat: implement interactive agent swarm simulator with terminal thought logs"
```

---

### Task 4: Implement "Temario Interactivo" and "Embudo n8n" Tabs

**Files:**
- Modify: `index.html`

**Interfaces:**
- Consumes: Data from `curriculum/CURSO_MAESTRO_TEMARIO.md` and `funnels/EMBUDO_MANYCHAT_Y_SKOOL.md`.
- Produces: Accordion lesson expansion and interactive workflow step clicker.

- [ ] **Step 1: Build Course Syllabus Accordion**
Create custom CSS accordions where clicking on Modules 0, 1, 2, 3, or 4 reveals the lessons, learning targets, and download links for simulated JSON workflows.

- [ ] **Step 2: Build Interactive ManyChat & Skool Funnel Step-Clicker**
Create a visual progress flow representing:
`Post/Reel Comment -> ManyChat DM -> BANT Qualification -> Google Calendar -> Skool Classroom -> Paid Scale`
Clicking on any step displays a sidebar pop-up showing ManyChat template messages, conditional branches, and automations running under the hood.

- [ ] **Step 3: Double-check links and states**
Verify that all navigation between tabs (Chat, Syllabus, Funnel, Vault) is seamless and persistent.

- [ ] **Step 4: Commit and finalize index.html**
```bash
git add index.html
git commit -m "feat: add interactive syllabus accordion and visual funnel simulator"
```
