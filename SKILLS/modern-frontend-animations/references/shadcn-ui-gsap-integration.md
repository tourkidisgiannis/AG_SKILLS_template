# shadcn/ui + GSAP Integration (Award‑Grade Patterns)

Combining **shadcn/ui** composable primitives with **GSAP** to achieve *award‑level motion* in React 18 / Next.js applications.

This guide extends basic integration with **production‑proven patterns** used in high‑end SaaS, portfolios, and editorial sites.

---

## Purpose

**shadcn/ui**
- Accessibility‑first
- Radix‑powered state machines
- Minimal styling assumptions

**GSAP**
- Deterministic timelines
- Scroll‑aware motion
- Velocity & sequencing control

**Core Principle**

Radix controls **state & accessibility**  
GSAP controls **motion**  
React stays **out of the animation loop**

---

## 1. Animating Dialogs & Sheets (Portal‑Safe)

Radix Dialog content is **portalled and conditionally mounted**.  
Animation must occur **after mount**, not during render.

### Recommended Pattern

```tsx
'use client';

import { Dialog, DialogContent, DialogTrigger } from "@/components/ui/dialog";
import { useRef } from "react";
import gsap from "gsap";

export function AnimatedDialog() {
  const contentRef = useRef<HTMLDivElement | null>(null);

  const handleOpenChange = (open: boolean) => {
    if (!open) return;

    requestAnimationFrame(() => {
      if (!contentRef.current) return;

      gsap.fromTo(
        contentRef.current,
        { y: 24, opacity: 0, scale: 0.96 },
        {
          y: 0,
          opacity: 1,
          scale: 1,
          duration: 0.4,
          ease: "back.out(1.6)",
          clearProps: "transform"
        }
      );
    });
  };

  return (
    <Dialog onOpenChange={handleOpenChange}>
      <DialogTrigger>Open</DialogTrigger>
      <DialogContent ref={contentRef}>
        <h2 className="text-lg font-semibold">Animated Content</h2>
      </DialogContent>
    </Dialog>
  );
}
```

### Why This Wins

- Portal‑safe
- No race conditions
- No React re‑renders
- Clear ownership boundaries

---

## 2. Coordinated Entry / Exit (Delayed Unmount)

Radix does **not delay unmounts** by default.  
If you need exit animations, you must control visibility manually.

**Rule:** GSAP finishes → then unmount.

(Production apps often wrap DialogContent in a presence controller.)

---

## 3. Hover Animations for Cards (GSAP > CSS)

Use GSAP when hover motion requires *easing, depth, or shared timelines*.

```tsx
'use client';

import gsap from "gsap";
import { useGSAP } from "@gsap/react";
import { useRef } from "react";

export function AnimatedCards() {
  const containerRef = useRef<HTMLDivElement | null>(null);

  useGSAP(() => {
    const cards = gsap.utils.toArray<HTMLElement>(".card");

    cards.forEach(card => {
      const tl = gsap.timeline({ paused: true });

      tl.to(card, {
        y: -10,
        boxShadow: "0 20px 25px -5px rgb(0 0 0 / 0.1)",
        duration: 0.25,
        ease: "power2.out"
      });

      card.addEventListener("mouseenter", () => tl.play());
      card.addEventListener("mouseleave", () => tl.reverse());
    });
  }, { scope: containerRef });

  return (
    <div ref={containerRef} className="grid grid-cols-3 gap-6">
      <div className="card rounded-xl border p-6">Card A</div>
      <div className="card rounded-xl border p-6">Card B</div>
      <div className="card rounded-xl border p-6">Card C</div>
    </div>
  );
}
```

### Why This Wins

- Precise easing
- Reversible timelines
- No CSS transition conflicts

---

## 4. Staggered Component Reveals (Lists, Menus)

Common for menus, dropdowns, command palettes.

```tsx
useGSAP(() => {
  gsap.from(".menu-item", {
    y: 16,
    opacity: 0,
    stagger: 0.05,
    duration: 0.4,
    ease: "power3.out"
  });
});
```

**Rule:** stagger children, not parents.

---

## 5. Scroll‑Aware shadcn Sections

Combine shadcn layout primitives with GSAP ScrollTrigger.

```tsx
useGSAP(() => {
  gsap.from(".feature", {
    y: 60,
    opacity: 0,
    duration: 0.8,
    ease: "power3.out",
    stagger: 0.15,
    scrollTrigger: {
      trigger: ".features",
      start: "top 80%",
    }
  });
});
```

**Used for:** feature grids, pricing tiers, testimonials

---

## 6. Velocity‑Based Motion (Premium Detail)

Add physicality without visual noise.

```ts
ScrollTrigger.create({
  onUpdate: (self) => {
    gsap.to(".velocity-text", {
      skewY: self.getVelocity() / 800,
      duration: 0.2,
      ease: "power3.out"
    });
  }
});
```

---

## 7. GSAP vs CSS (Decision Matrix)

### Use GSAP When
- Motion is sequenced
- Timing matters
- Scroll or velocity is involved
- Multiple elements coordinate

### Prefer CSS When
- Focus / hover states
- Simple opacity or scale
- No orchestration required

---

## 8. Best Practices (Non‑Negotiable)

- Always use `'use client'`
- Use refs over selectors when possible
- Scope selectors with `useGSAP`
- Avoid layout‑thrashing properties
- Never bind animation to React state
- Let Radix handle focus & ARIA
- Clear transforms when mixing with Tailwind

---

## Mental Model

If animation breaks accessibility, **it is wrong**.  
If animation requires React state, **it is wrong**.  
If animation feels decorative, **remove it**.

**Great motion is invisible until it’s missing.**
