# CODEBASE MAP

Проект — **статический сайт** (HTML, CSS, TypeScript → JS). Без React и без Next.js.

## Страницы (корень репозитория)

- главная → `index.html`
- уроки (заглушка) → `lessons.html`
- упражнения (заглушка) → `exercises.html`

## Стили

- основные стили → `css/main.css`
- базовая цветовая палитра интерфейса задаётся в `:root` внутри `css/main.css` (`--bg`, `--text`, `--muted`, `--primary`, `--primary-strong`, `--line`)
- текущая тема: тёмно-зелёная (`--bg: #0d1f17`, `--surface: #173a2d`, `--primary: #2fbf71`)

## Скрипты

- исходник TypeScript → `src/main.ts`
- собранный для браузера → `js/main.js` (генерируется командой `npm run build`)

## Материалы и документы

- методические материалы диплома → `docs/notes/methodology-summary.md`
- заметки → `docs/notes/`
- учебник PDF → `docs/textbook/` (`progress.pdf`, `progress_theory.pdf`)

## Правила и промпты

- роутер задач → `.cursor/router.md`
- правила проекта → `.cursor/project-rules.md`
- урок → `.cursor/prompts/build-lesson.md`
- упражнение → `.cursor/prompts/generate-exercise.md`
- упрощение текста A1 → `.cursor/prompts/simplify-a1-text.md`
- speech feedback → `.cursor/prompts/speech-feedback.md`

## Принципы

- не смешивать большие куски контента прямо в HTML без необходимости (позже можно вынести в JSON и подставлять через JS);
- логику проверки упражнений держать в отдельных TS-модулях в `src/` по мере роста проекта;
- интерфейс оставлять простым: без персонализации и без лишних блоков на главной.
