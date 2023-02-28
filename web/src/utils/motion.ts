import { Variants } from 'framer-motion';

export const motionVariants: Variants = {
  offscreen: {
    x: -300,
    y: 300,
    scale: 0.3,
    rotate: -100,
  },
  onscreen: {
    x: 0,
    y: 0,
    rotate: 0,
    scale: 1,
    transition: {
      type: 'spring',
      bounce: 0.3,
      duration: 1,
    },
  },
  onhover: {
    scale: 0.99,
  },
};
