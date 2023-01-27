# Day 44 - Intermediate CSS


## Favicon
- A favicon is the icon that shows up on the tab in chrome or whatever browser you are using next to the name of the website
- The favicon is saved somewhere on your site and set using a `<link>` tag
```html
<link rel="icon" href="favicon.ico">
```

## HTML Divs

- The `<div>` tag is used to structure and divide up a webpage using CSS

```html
<body>
    <div class="">
        <h1>I'm Bob</h1>
        <p>An aspiring programmer</p>
    </div>
```

```css
div {
    background-color: #E4F9F5;
}
```

- In the previous example, only the div section would have it's background changed.

## Box Model

- An element in CSS has a width and a height
- Elements can also have a border that can be expanded, which adds that many pixels to the width and height of the element. For example `{ border-width: 50px; }` would add a 50 px border to whatever element you assigned it to. Meaning that element would be 50px taller and 50px wider in total.
- The border can also be adjusted per side (top, bottom, left, right).
- Elements can also have padding which adds space between the element and the border `{ padding: 20px; }` would add 20 pixels of space between the element and margin. Meaning the element would be 20 pixels larger on all sides.
- Padding can also be adjusted per side (top, bottom, left, right).
- Finally, elements can have a margin outside the border to add more space between it and other elements `{ margin: 10px; }` would add a 10 px margin on all sides.
- Margin can be adjusted per side (top, bottom, left, right).