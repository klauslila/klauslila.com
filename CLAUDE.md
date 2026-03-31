# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal landing page for Klaus Lila — Senior Software Engineer & Technical Lead. Cinematic, scroll-driven product page (not a traditional portfolio) designed to sell Klaus as a candidate to aviation/airline/logistics companies. Think iPhone product page, not developer portfolio.

## Architecture

- **Single file**: `index.html` — all HTML, CSS, and JS in one file, zero external dependencies except Google Fonts
- **Fonts**: Space Grotesk (headings), DM Sans (body), B612 Mono (labels/data — Airbus cockpit font)
- **Color system**: Deep navy-black base (`#030508`), aviation crimson accent (`#c1121f`), sky blue secondary (`#4a9fe5`). Colors blend via gradients, never sit flat. The page should feel like a cockpit at night.
- **Aviation visuals**: SVG flight paths with gradient strokes and animated dash-draw. Two plane silhouettes follow paths via `<animateMotion>` + `<mpath>`. Runway approach lights at hero bottom. Atmospheric gradient backgrounds.
- **Animations**: Scroll-triggered `.fade-in` reveals via IntersectionObserver. AI methodology bars animate fill on scroll. Hero content staggers via CSS `@keyframes fadeUp` with delays. `prefers-reduced-motion` respected.
- **Sections**: Hero (name massive) → Story (aviation passion) → Numbers → Capabilities → Track Record → AI Methodology → CTA/Contact

## Development

```
open index.html
```

No build step, no package manager, no server required.

## Design Principles

- **Night aesthetic**: Backgrounds should be near-black with blue undertone, not neutral gray. This is what makes it feel aerospace.
- **Depth via glass**: Cards use `backdrop-filter: blur()` with `rgba` backgrounds and `rgba(255,255,255,0.08)` borders — frosted glass cockpit feel.
- **Gradients over flat color**: Accent text uses crimson→sky gradient. Number units use gradient. Bullet dots use gradient. Section backgrounds use atmospheric gradients.
- **Restraint**: One accent (crimson) used sparingly. Sky blue for links/labels/secondary. No multi-color competing elements.
- **Section labels** use `// the story` format in B612 Mono — engineering code-comment aesthetic.
- **Horizon dividers** between sections: gradient line blending sky blue → crimson → transparent.

## Content Guidelines

- Impact bullets use **senior verbs** (Architected, Drove, Designed, Established, Championed)
- Bold only keywords/buzzwords, not full sentences
- Key ATS terms to maintain: distributed systems, event-driven architecture, platform migration, API orchestration, cross-functional, AI-augmented development, LLM, RAG
- GitHub/LinkedIn/Email URLs in CTA section are placeholders — need real values before deployment

## SVG Flight Paths

The hero contains an SVG (`viewBox="0 0 1000 1000"`, `preserveAspectRatio="xMidYMid slice"`) with:
- 3 route paths (gradient strokes, dashed, animated dash-draw)
- 2 plane silhouettes using `<animateMotion>` locked to routes via `<mpath>`
- Planes use `rotate(90)` inner transform (polygon points up, needs rotating to face travel direction) + `rotate="auto"` on animateMotion for curve-following
- Runway approach lights: 3 rows of dots with perspective narrowing, white + red threshold markers, staggered blink animation
