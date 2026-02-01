# GSAP Animation Patterns (Award-Winning Reference)

This document catalogs **award-winning animation patterns** commonly seen on Awwwards, CSSDA, and studio-grade websites built with GSAP + Next.js.
The focus is on narrative motion, physicality, and perceived performance.

---

## 1. ScrollTrigger Basics
```js
useGSAP(() => {
  gsap.from(".hero-text", {
    scrollTrigger: {
      trigger: ".hero-section",
      start: "top center",
      end: "bottom center",
      scrub: 1,
    },
    opacity: 0,
    y: 100,
    duration: 1,
  });
});
```

## 2. Text Splitting (Premium Typography Motion)
```js
const words = text.split(" ");
return words.map((word, i) => (
  <span key={i} className="word-wrapper overflow-hidden inline-block">
    <span className="word inline-block">{word}&nbsp;</span>
  </span>
));
```

```js
useGSAP(() => {
  gsap.from(".word", {
    y: "100%",
    stagger: 0.05,
    duration: 0.8,
    ease: "power4.out",
  });
});
```

## 3. Parallax Depth Layers
```js
useGSAP(() => {
  gsap.to(".background", {
    yPercent: -20,
    ease: "none",
    scrollTrigger: {
      trigger: ".parallax-container",
      scrub: true,
    },
  });
});
```

## 4. Horizontal Scroll Sections
```js
useGSAP(() => {
  const sections = gsap.utils.toArray(".panel");
  gsap.to(sections, {
    xPercent: -100 * (sections.length - 1),
    ease: "none",
    scrollTrigger: {
      trigger: ".container",
      pin: true,
      scrub: 1,
      snap: 1 / (sections.length - 1),
      end: "+=3000",
    },
  });
});
```

## 5. Direction-Aware Section Reveals
```js
useGSAP(() => {
  gsap.utils.toArray(".reveal").forEach((el) => {
    gsap.from(el, {
      y: el.dataset.direction === "up" ? -80 : 80,
      opacity: 0,
      duration: 0.9,
      ease: "power3.out",
      scrollTrigger: {
        trigger: el,
        start: "top 85%",
      },
    });
  });
});
```

## 6. Image Mask Reveals
```html
<div class="image-mask overflow-hidden">
  <img src="/image.jpg" />
</div>
```

```js
useGSAP(() => {
  gsap.from(".image-mask img", {
    scale: 1.2,
    yPercent: 20,
    duration: 1.2,
    ease: "power4.out",
    scrollTrigger: {
      trigger: ".image-mask",
      start: "top 80%",
    },
  });
});
```

## 7. Scroll-Driven Timelines
```js
useGSAP(() => {
  const tl = gsap.timeline({
    scrollTrigger: {
      trigger: ".story",
      start: "top top",
      end: "+=200%",
      scrub: true,
      pin: true,
    },
  });

  tl.from(".story-title", { y: 80, opacity: 0 })
    .from(".story-image", { scale: 1.1 }, "<")
    .from(".story-text", { y: 60, opacity: 0 });
});
```

## 8. Velocity-Based Motion
```js
useGSAP(() => {
  ScrollTrigger.create({
    onUpdate: (self) => {
      gsap.to(".velocity-item", {
        skewY: self.getVelocity() / 600,
        duration: 0.2,
        ease: "power3.out",
      });
    },
  });
});
```

## 9. Magnetic Cursor Interaction
```js
useGSAP(() => {
  const el = document.querySelector(".magnetic");

  el.addEventListener("mousemove", (e) => {
    const rect = el.getBoundingClientRect();
    const x = e.clientX - rect.left - rect.width / 2;
    const y = e.clientY - rect.top - rect.height / 2;

    gsap.to(el, {
      x: x * 0.3,
      y: y * 0.3,
      duration: 0.4,
      ease: "power3.out",
    });
  });

  el.addEventListener("mouseleave", () => {
    gsap.to(el, { x: 0, y: 0, duration: 0.6 });
  });
});
```

## 10. Page Transition Animations
```js
useGSAP(() => {
  gsap.fromTo(
    ".page",
    { y: 40, opacity: 0 },
    { y: 0, opacity: 1, duration: 0.8, ease: "power3.out" }
  );
});
```

## 11. Ambient Infinite Motion
```js
useGSAP(() => {
  gsap.to(".float", {
    y: -20,
    repeat: -1,
    yoyo: true,
    duration: 3,
    ease: "sine.inOut",
  });
});
```

## 12. Staggered Grid Reveals
```js
useGSAP(() => {
  gsap.from(".grid-item", {
    scale: 0.95,
    opacity: 0,
    stagger: { each: 0.08, from: "start" },
    duration: 0.6,
    ease: "power2.out",
    scrollTrigger: {
      trigger: ".grid",
      start: "top 80%",
    },
  });
});
```

---

## Award-Winning Principles
- Narrative over novelty
- Motion over opacity
- Timelines over isolated effects
- Consistent easing & timing
- Restraint and performance
