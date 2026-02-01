---
name: brand-guidelines
description: Retro risograph–inspired brand system with cream backgrounds, red accents, restrained grain texture, and Acumin Pro typography. Designed for production-grade frontend execution with intentional imperfection and high legibility.
license: Complete terms in LICENSE.txt
---

# Retro Risograph Brand System

## Design Intent

This brand system emulates the **analog imperfections of risograph printing** while remaining suitable for modern, production-grade frontend interfaces.

The goal is **intentional imperfection**:
- tactile, print-inspired character
- bold graphic presence
- restrained palette
- high legibility and clarity

This is not nostalgia for its own sake.  
Every visual decision must support **hierarchy, communication, and recognition**.

**Keywords**  
retro, risograph, analog, grain, cream, red, poster-like, tactile, print-inspired

---

## Context Sensitivity (Enforced)

This brand system scales with interface context:

- **Marketing & portfolio surfaces** → full expression allowed  
- **Landing pages** → texture and asymmetry allowed only if they preserve clarity  
- **UI-heavy or data-dense screens** → reduce grain, parallax, and overlap  
- **Accessibility-critical contexts** → remove decorative effects entirely

Style must never compromise readability, performance, or comprehension.

---

## Color System

### Core Palette

- **Background / Paper (Cream)**  
  `#F3F0E6`  
  Warm, paper-like off-white. Default background surface.

- **Primary Text (Soft Black)**  
  `#202020`  
  High contrast without the harshness of pure black.

- **Primary Accent (Retro Red)**  
  `#D93025`  
  Used for:
  - primary CTAs
  - key headlines
  - graphic emphasis  
  Must remain dominant and intentional.

- **Secondary Accent (Gold / Yellow)**  
  `#E6B800`  
  Use sparingly for highlights or decorative emphasis only.

- **Disallowed Colors**
  - Platform blues (`#0057FF`)  
  - Cool neutrals  
  - Expanded palettes without explicit justification

The strength of this system comes from **limitation**, not variety.

---

## Typography Doctrine

### Primary Typeface
**Acumin Pro** (Sans-serif)

Chosen for:
- modern neutrality
- strong weight range
- compatibility with bold, poster-like composition

### Usage Rules

**Headings**
- Bold or Semibold
- Tight tracking (`-0.01em` to `-0.03em`)
- Uppercase permitted for short headlines only
- Avoid decorative type effects

**Body Text**
- Regular weight
- Line-height: `1.45–1.6`
- Never condensed
- Prioritize long-form legibility

**Fallbacks**
`Helvetica Neue`, `Arial`, `sans-serif`

Typography carries the brand more than texture.  
If type hierarchy fails, the design fails.

---

## Texture & Imperfection (Strictly Controlled)

### Grain / Noise
- Subtle noise overlay only
- Opacity: **2–4%**
- Applied to large color fields only
- Never applied to body text

### Halftones
- Allowed for:
  - imagery
  - decorative shadows
  - background illustrations
- Must not interfere with text contrast

### Prohibited
- Heavy grain
- Animated noise
- Texture stacked over UI controls
- Texture used as filler

Texture is **atmosphere**, not decoration.

---

## Spatial Composition

### Layout Philosophy
- Poster-first thinking
- Strong blocks of color
- Clear hierarchy
- Deliberate negative space

### Rules
- Asymmetry is encouraged, not mandatory
- Overlap must reinforce hierarchy
- No random offsets
- No broken grids without purpose

When in doubt, choose clarity over collage.

---

## Motion & Depth

### Motion
- Motion is optional
- Never required for comprehension
- Avoid parallax by default
- Respect `prefers-reduced-motion`

### Shadows
- Hard, print-like shadows only
- No blur
- Offset shadows encouraged

Example:
```css
box-shadow: 4px 4px 0 #202020;
