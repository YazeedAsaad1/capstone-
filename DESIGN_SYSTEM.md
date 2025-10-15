# Dark Mode Design System Documentation

## Overview
This design system provides a minimalistic, professional, dark mode interface for the Django To-Do List application. It emphasizes usability, accessibility, and responsive design with modern CSS techniques.

## 🎨 Color Palette

### Primary Colors
- **Background Primary**: `#0f0f0f` - Main background
- **Background Secondary**: `#1a1a1a` - Cards, header, footer
- **Background Tertiary**: `#2a2a2a` - Form inputs, hover states

### Text Colors
- **Text Primary**: `#ffffff` - Main headings, important text
- **Text Secondary**: `#b3b3b3` - Body text, descriptions
- **Text Muted**: `#666666` - Meta information, timestamps

### Accent Colors
- **Accent Primary**: `#3b82f6` - Links, primary buttons
- **Accent Secondary**: `#1d4ed8` - Button variants
- **Accent Hover**: `#2563eb` - Hover states

### Status Colors
- **Success**: `#10b981` - Success messages, completed tasks
- **Warning**: `#f59e0b` - Warning messages, medium priority
- **Danger**: `#ef4444` - Error messages, high priority

## 📱 Responsive Breakpoints

```css
/* Mobile First Approach */
xs: 0-479px     /* Extra small devices */
sm: 480-767px   /* Small devices */
md: 768-1023px  /* Medium devices (tablets) */
lg: 1024-1199px /* Large devices (small desktops) */
xl: 1200px+     /* Extra large devices */
```

## 🔤 Typography

### Font Family
- **Primary**: Inter (Google Fonts)
- **Fallback**: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif

### Font Sizes
- **xs**: 0.75rem (12px)
- **sm**: 0.875rem (14px)
- **base**: 1rem (16px)
- **lg**: 1.125rem (18px)
- **xl**: 1.25rem (20px)
- **2xl**: 1.5rem (24px)
- **3xl**: 1.875rem (30px)

## 📏 Spacing System

```css
--spacing-xs: 0.25rem   /* 4px */
--spacing-sm: 0.5rem    /* 8px */
--spacing-md: 1rem      /* 16px */
--spacing-lg: 1.5rem    /* 24px */
--spacing-xl: 2rem      /* 32px */
--spacing-2xl: 3rem     /* 48px */
```

## 🎯 Component Classes

### Layout Components
- `.container` - Main content wrapper with max-width
- `.card` - Content cards with shadow and hover effects
- `.header-container` - Header layout wrapper

### Navigation
- `.header-logo-container` - Logo wrapper
- `nav ul` - Navigation list
- `nav a` - Navigation links with hover effects

### Task Components
- `.task-list` - Container for task items
- `.task-item` - Individual task card
- `.task-header` - Task title and actions row
- `.task-title` - Task title styling
- `.task-actions` - Action buttons container
- `.task-description` - Task description text
- `.task-meta` - Task metadata (date, priority)
- `.task-priority` - Priority badge

### Form Components
- `.form-group` - Form field wrapper
- `.btn` - Base button class
- `.btn-primary` - Primary action button
- `.btn-secondary` - Secondary action button
- `.btn-danger` - Destructive action button
- `.btn-success` - Success action button

### Utility Classes
- `.text-center`, `.text-left`, `.text-right` - Text alignment
- `.mb-0` to `.mb-4` - Margin bottom utilities
- `.mt-0` to `.mt-4` - Margin top utilities
- `.hidden` - Hide element
- `.sr-only` - Screen reader only content

### Animation Classes
- `.fade-in` - Fade in animation
- `.slide-in` - Slide in animation
- `.loading` - Loading spinner

## ♿ Accessibility Features

### Keyboard Navigation
- All interactive elements are keyboard accessible
- Focus indicators with high contrast
- Skip link for keyboard users
- Proper ARIA labels and roles

### Screen Reader Support
- Semantic HTML structure
- ARIA labels for complex interactions
- Screen reader only content where needed
- Proper heading hierarchy

### Visual Accessibility
- High contrast ratios (WCAG AA compliant)
- Scalable text (supports up to 200% zoom)
- Reduced motion support
- High contrast mode support

## 🎭 Interactive Features

### Hover Effects
- Subtle transform animations
- Color transitions
- Shadow enhancements
- Scale effects on buttons

### Focus States
- Visible focus indicators
- Consistent focus styling
- Keyboard navigation support

### Loading States
- Form submission feedback
- Loading spinners
- Disabled state styling

## 📱 Mobile Optimizations

### Touch Targets
- Minimum 44px touch targets
- Adequate spacing between interactive elements
- Thumb-friendly navigation

### Layout Adaptations
- Stacked navigation on mobile
- Full-width buttons on small screens
- Optimized spacing for touch devices

### Performance
- Optimized images
- Minimal JavaScript
- Efficient CSS animations

## 🔧 Implementation Notes

### CSS Architecture
- CSS Custom Properties (variables) for theming
- Mobile-first responsive design
- Flexbox for layout
- CSS Grid for complex layouts

### JavaScript Enhancements
- Progressive enhancement approach
- Intersection Observer for animations
- Form validation feedback
- Accessibility improvements

### Browser Support
- Modern browsers (Chrome 60+, Firefox 55+, Safari 12+)
- Graceful degradation for older browsers
- CSS feature detection

## 🚀 Usage Examples

### Basic Card
```html
<div class="card fade-in">
  <h2>Card Title</h2>
  <p>Card content goes here.</p>
  <button class="btn btn-primary">Action</button>
</div>
```

### Task Item
```html
<li class="task-item">
  <div class="task-header">
    <h3 class="task-title">Task Title</h3>
    <div class="task-actions">
      <button class="btn btn-secondary">Edit</button>
      <button class="btn btn-danger">Delete</button>
    </div>
  </div>
  <div class="task-description">Task description...</div>
  <div class="task-meta">
    <span class="task-date">Created: Jan 1, 2024</span>
    <span class="task-priority priority-high">High</span>
  </div>
</li>
```

### Form Group
```html
<div class="form-group">
  <label for="task-title">Task Title</label>
  <input type="text" id="task-title" name="title" required>
</div>
```

## 🎨 Customization

### Changing Colors
Modify the CSS custom properties in `:root` to change the color scheme:

```css
:root {
  --accent-primary: #your-color;
  --bg-primary: #your-background;
}
```

### Adding New Components
Follow the established naming conventions and use the existing color and spacing variables for consistency.

### Theme Variations
The system supports theme switching through data attributes. Add `data-theme="light"` to the HTML element for light mode (when implemented).

## 📋 Checklist for New Components

- [ ] Uses CSS custom properties for colors and spacing
- [ ] Responsive design implemented
- [ ] Accessibility features included
- [ ] Hover and focus states defined
- [ ] Loading states considered
- [ ] Mobile optimization applied
- [ ] Cross-browser compatibility tested
