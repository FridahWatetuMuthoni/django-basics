# Django Basics Notes

## Include Tailwind Css in Django

1. Install Tailwindcss

```bash
npm init -y
npm install tailwindcss postcss autoprefixer
```

2. Configure Tailwind

```bash
npx tailwindcss init
```

3. Set Up Your Tailwind Input File

```css
/*input.css*/
@import url("https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap");

@tailwind base;
@tailwind components;
@tailwind utilities;
```

4. Configure PostCSS

Create a postcss.config.js file in your project root and add the following configuration:

```js
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
```

7. Add Django Static Settings

```python

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

```

8. Compile Tailwind for Development
   Adding the following scripts to package.js

```javascript
"scripts": {
    "build:css": "npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --minify",
    "dev:css": "npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch",
  },
```

How to run them

```bash
npm run build:css
npm run dev:css
```

9. Collect Static Files (Django Production)

```bash
python manage.py collectstatic
```
