# 2026-03-22 — Spec-Driven Development Starter Kit (borrador)

## Objetivos
- Permitir que un equipo en Windows 11 sin permisos admin ejecute SDD.
- Centralizar las specs como "single source of truth".
- Dejar listo un flujo multi-agente (Spec → Implement → Verifier → Orchestrator).

## Componentes
1. **Plantillas de spec** (`specs/`)
   - Feature.md, API.md, Acceptance.md
   - Campos obligatorios + checklist
2. **CLI portátil**
   - Node.js 22 portable + `npx specify`
   - Scripts npm (`spec:plan`, `spec:implement`, `spec:verify`)
3. **Agentes soportados**
   - GitHub Spec Kit (Copilot)
   - Claude Code (via CLI)
   - Cursor (WSL opcional)
4. **Sin Docker (fase 1)**
   - Todo se ejecuta en VS Code portable
   - Logs en `runs/` y handoffs en `handoffs/`
5. **Con Docker (fase 2)**
   - Contenedores OpenShell/NemoClaw
   - OpenGoat para orquestación

## Próximos pasos
- [ ] Generar plantilla YAML para Features
- [ ] Escribir guía "Sin admin" (instalar Node+VSCode portables)
- [ ] Script `npm run spec:plan` (invoca `npx specify plan`)
- [ ] Integrar con OpenGoat (definir org + roles)
