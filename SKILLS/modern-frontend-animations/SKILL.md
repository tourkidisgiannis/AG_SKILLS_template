---
name: modern-frontend-animations
description: Professional animations using GSAP, Next.js, and shadcn/ui. Use when the user wants to build high-end, "award-winning" landing pages, complex scroll-based animations, or smooth interactive UI components. Trigger this when a project requires Next.js, Tailwind CSS, and sophisticated motion design.
---

# Modern Frontend Animations

This skill enables the creation of premium, interactive web experiences using the modern frontend stack: Next.js, Tailwind CSS, shadcn/ui, and GSAP. 

All animations implemented with this skill must follow the **BOLD aesthetic direction** and **Motion Philosophy** established in the **`frontend-design`** skill.


## Core Setup

To use this skill effectively, the project should be initialized with:
1. **Next.js** (App Router preferred)
2. **Tailwind CSS**
3. **shadcn/ui**
4. **GSAP** (`npm install gsap @gsap/react`)

## Workflow Decision Tree

1. **Static UI?** → Use shadcn/ui + Tailwind for layout.
2. **Simple Micro-interactions?** → Use Tailwind transitions or shadcn/ui built-in animations.
3. **Complex Motion/Scroll Effects?** → Use **GSAP**.
   - **Scroll-based?** → Use `ScrollTrigger`.
   - **Text Effects?** → Use `SplitText` patterns.
   - **Page Transitions?** → Use GSAP with Next.js router events.

## GSAP in React/Next.js

Always use the `@gsap/react` package's `useGSAP()` hook for safe animation management.

```javascript
'use client';
import { useRef } from 'react';
import gsap from 'gsap';
import { useGSAP } from '@gsap/react';

export default function AnimatedComponent() {
  const container = useRef();

  useGSAP(() => {
    // gsap animations here...
    gsap.to(".box", { rotation: 360, duration: 2 });
  }, { scope: container }); // scope for selector text

  return (
    <div ref={container}>
      <div className="box">Animate me</div>
    </div>
  );
}
```

## Award-Winning Patterns

### 1. Liquid Scroll
Use `ScrollTrigger` with `scrub: true` to tie animations directly to the scroll position.

### 2. Typography Reveal
Animate characters or words using staggering effects for a premium feel.

### 3. Smooth Orchestration
Combine multiple timelines to create complex, multi-stage animations that feel cohesive.

## Resources

- **Animation Patterns**: [gsap-animation-patterns.md](references/gsap-animation-patterns.md)
- **shadcn/ui Integration**: [shadcn-ui-gsap-integration.md](references/shadcn-ui-gsap-integration.md)
- **Smooth Scroll**: [smooth-scroll.md](references/smooth-scroll.md)
