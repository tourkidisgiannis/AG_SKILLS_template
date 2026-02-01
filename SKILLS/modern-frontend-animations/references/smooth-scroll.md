# Smooth Scroll (Lenis + GSAP Integration)

For award-winning websites, standard browser scrolling often feels "jagged." **Lenis** is the industry standard for smooth, inertia-based scrolling that works perfectly with GSAP ScrollTrigger.

## 1. Installation

```bash
npm install @studio-freight/lenis
```

## 2. Basic Setup (Next.js App Router)

Create a provider to wrap your application.

```tsx
'use client';

import { ReactLenis, useLenis } from '@studio-freight/react-lenis';
import { useEffect, useRef } from 'react';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

export function SmoothScrollProvider({ children }: { children: React.ReactNode }) {
  const lenisRef = useRef<any>();

  useEffect(() => {
    function update(time: number) {
      lenisRef.current?.lenis?.raf(time * 1000);
    }

    gsap.ticker.add(update);

    return () => {
      gsap.ticker.remove(update);
    };
  }, []);

  return (
    <ReactLenis root ref={lenisRef} options={{ lerp: 0.1, duration: 1.5, smoothWheel: true }}>
      {children}
    </ReactLenis>
  );
}
```

## 3. GSAP ScrollTrigger Integration

Lenis needs to notify ScrollTrigger when the scroll position changes. The `ReactLenis` component handles this automatically if `root` is set, but for custom setups:

```javascript
lenis.on('scroll', ScrollTrigger.update);

gsap.ticker.add((time) => {
  lenis.raf(time * 1000);
});

gsap.ticker.lagSmoothing(0);
```

## 4. Usage in Components

You can access the lenis instance via a hook to control scrolling programmatically (e.g., for anchor links).

```tsx
const lenis = useLenis(({ scroll }) => {
  // called on every scroll
});

const scrollToContact = () => {
  lenis?.scrollTo('#contact', { lerp: 0.1 });
};
```

## 5. Performance Tips

- **Disable on Mobile?**: Some studios prefer native scroll on mobile. Lenis can be toggled via options.
- **Lag Smoothing**: Use `gsap.ticker.lagSmoothing(0)` to prevent GSAP from "jumping" during heavy renders while smooth scrolling.
- **Lerp vs Duration**: `lerp` (Linear Interpolation) is usually preferred for a "liquid" feel (0.05 to 0.1).
