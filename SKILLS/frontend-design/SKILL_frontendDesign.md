---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (e.g. websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Produces creative, polished implementations that avoid generic AI aesthetics.
license: Complete terms in LICENSE.txt
---

This skill governs the creation of **distinctive, production-grade frontend interfaces** that avoid generic or templated “AI” aesthetics.

All output must be **real, working code** with exceptional attention to:
- visual identity
- typographic quality
- spatial composition
- motion design
- production readiness

The user provides frontend requirements: a component, page, application, or interface to build, optionally including context such as purpose, audience, or technical constraints.

Unless explicitly stated otherwise, implementations default to a **modern React-based production stack**.

---

## Design Thinking (Required)

Before writing code, establish and commit to a **single, intentional aesthetic direction**, scaled appropriately to context.

### Purpose
- What problem does this interface solve?
- Who is the primary user?
- What action or behavior does it encourage?

### Tone
Choose one clear direction and commit fully. Examples:
- Brutally minimal  
- Editorial / magazine  
- Luxury / refined  
- Industrial / utilitarian  
- Organic / tactile  
- Brutalist / raw  
- Playful / surreal  
- Retro-futuristic  

Do **not** hedge between styles.

### Constraints
- Framework or platform requirements
- Performance budgets
- Accessibility expectations
- Device and network limitations

### Differentiation
Identify the *primary distinguishing quality* of the interface.

Differentiation may emerge from:
- typography
- hierarchy
- color logic
- motion restraint
- compositional rigor

It does **not** always require visual provocation.

---

## Context Sensitivity (Enforced)

Design ambition must scale with **audience, purpose, and risk tolerance**.

- Marketing sites may tolerate expressiveness
- Internal tools prioritize clarity and predictability
- Data-heavy interfaces prioritize cognition
- Accessibility-critical interfaces prioritize stability and legibility

Distinctiveness must never undermine usability, trust, or task completion.

---

## Frontend Aesthetics Guidelines

### Typography
- Typography is the primary design material
- Choose characterful, intentional fonts
- Avoid overused defaults (Arial, Inter, Roboto, system fonts, Space Grotesk)
- Pair expressive display faces with calm, readable body text
- Maintain hierarchy through size, weight, rhythm, and spacing
- Respect line length, vertical rhythm, and optical balance

### Color & Theme
- Commit to a cohesive palette
- Prefer dominant colors with sharp accents
- Use CSS variables for all tokens
- Avoid timid, evenly distributed color systems

### Motion
- Motion must be intentional and optional (Follow **`modern-frontend-animations`** for execution)
- Favor fewer, higher-impact moments
- Motion may be reduced or removed entirely without loss of meaning
- No information may be conveyed *only* through animation


### Spatial Composition
- Grids are tools, not rules
- Break grids only when it serves clarity or narrative
- Dense or analytical interfaces may retain strict grid logic

### Backgrounds & Visual Texture
Use texture selectively:
- gradient meshes
- subtle grain
- translucency and blur
- decorative rules

Texture must reinforce hierarchy and tone — never act as filler.

---

## Scope Proportionality (Enforced)

The expressive weight of the design must match the scope of the artifact.

- Small components require restraint and precision
- Large surfaces may support stronger narrative or visual identity
- Avoid conceptual overengineering for trivial UI elements

---

## Interface Category Overrides

### Data-Dense Interfaces (Dashboards, Admin Panels)
- Prioritize scanability and hierarchy
- Maintain alignment and predictable structure
- Motion must be minimal and non-distracting
- Differentiation emerges from typography, spacing, and color logic

### Conversion-Oriented Interfaces
- Clarity and CTA visibility take precedence
- Proven structural patterns may be reinterpreted stylistically
- Novelty must never obscure intent or flow

### Accessibility-Critical Interfaces
- Support `prefers-reduced-motion`
- Motion and effects must degrade gracefully to zero
- Avoid visual overload, excessive blur, or layered translucency

### Design Systems & Component Libraries
- Consistency outweighs individual expressiveness
- Memorability emerges from coherence and rigor
- Components must be reusable and predictable

---

## Non-Negotiables

- No generic “AI” aesthetics
- No unrefined typography
- No decorative motion without purpose
- No visual decisions without intent

---

# Primary Stack & Execution Rules  
*(Enforced by default unless explicitly overridden)*

---

## Core Framework

**Next.js (App Router)**

- Server Components by default
- Client Components only when required for:
  - animation
  - interactivity
  - browser APIs
- Use modern patterns:
  - layouts
  - loading states
  - metadata
  - streaming where appropriate

---

## Responsive & Adaptive Design (Enforced)

Responsive behavior is a **design requirement**, not a technical fallback.

Rules:
- Design mobile-first
- Treat breakpoints as redesign opportunities
- Layouts must adapt structurally, not merely scale

Expectations:
- Typography reflows intentionally
- Navigation patterns may change form
- Dense layouts may become editorial on small screens
- Motion may be reduced or removed on low-power devices

A design that only works on desktop is incomplete.

---

## Color Contrast & Legibility (WCAG AAA – Enforced)

- Normal text: **7:1**
- Large text: **4.5:1**
- Interactive elements must be distinguishable in all states

Re-check contrast after:
- opacity
- blur
- overlays
- blend modes

---

## Styling System

**Tailwind CSS**

- Utility-first
- Design tokens via `:root` variables
- Extract abstractions when patterns repeat
- Every utility must serve hierarchy or rhythm

---

## Component System

**shadcn/ui**

- Foundation only
- Default styles must be transformed
- Never ship untouched components

---

## Motion & Animation

**GSAP (GreenSock)** is the primary engine. For detailed technical implementation, patterns, and orchestration, defer to the **`modern-frontend-animations`** skill.

Required for:
- page transitions
- hero sequences
- scroll-driven narratives

Guidelines:
- Prefer timelines over isolated tweens
- Always reference `modern-frontend-animations` for best practices on `useGSAP`, `ScrollTrigger` integration, and `Lenis` smooth scroll.


---

## Performance Supremacy (Enforced)

When performance constraints are explicit or implied:
- speed and stability override visual ambition
- motion, texture, and effects are optional
- responsiveness is mandatory

---

## Production Standards

All output must be:
- fully functional
- idiomatic Next.js + Tailwind
- accessible by default
- performant
- ready to ship

This is not concept art.  
This is **production-grade frontend engineering with taste**.

---

## Final Mandate

This skill exists to create interfaces that:
- do not look AI-generated
- feel intentionally authored
- balance ambition with responsibility

Intentionality over excess.  
Clarity over novelty.  
Execution over ideology.
