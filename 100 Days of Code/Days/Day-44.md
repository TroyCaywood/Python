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

![image](https://user-images.githubusercontent.com/52113778/215216585-b16077ed-80a3-4826-9c3f-bf1a3c701670.png)

## CSS Display Property

- The display property in CSS has four different values:
  + Block - Elements take up the whole width of the screen "blocking" out any other elements from sitting next to it on the left or the right. Width can be changed.
    + Common block elements (default to block):
      + Paragraphs `<p>`
      + Headers `<h1>` through `<h6>`
      + Divisions `<div>`
      + Lists and list items `<ol>` `<ul>` and `<li>`
      + Forms `<form>`
  + Inline - Only takes up as much space as it needs to display that element. Width cannot be changed.
    + Common inline elements (default to inline):
      + Spans `<span>` (a lot like div, doesn't really do anything until you set some properties in CSS)
      + Images `<img>`
      + Anchors `<a>`
  + Inline-Block - Elements can be on the same line and width is adjustable
  + None - Setting a display property to none removes that element from the page. This will reposition the other elements on the page as if that element isn't there anymore.  Using `visibility: hidden;` instead simply hides the element, but all the other elements will still behave as if that element is still there, but invisible.

- By default some elements are block display such as `<h1>` elements

## CSS Static and Relative Positioning

- Rules for positioning:
  1. Content is everything: The size of your content determines the width and height of an element depending on the display property. For example, a block element takes up the full width of the page, but the height of the element is determined by the height of the content in that block.
  2. Order comes from code: The order that your code is written in determines the order in which the content is displayed on your page.
  3. Children sit on top of parents: Elements that are nested within other elements are layered on top of the parent element. In the following example, the `<p>` element would be sitting on top of the `<div>` element.
```html
    <div>
        <p>I like cats.</p>
    </div>
```
  
- Elements also have a position property 
  + Static: All HTML elements are static in their position by default. This just means they go along with the default rules.
  + Relative: Setting an element position property to relative allows you to adjust it's position relative to where it would have been if the position was static. For example, the following CSS would move an img element 20px to the right by adding 20px of space to the left of the element. You can also to the same with top, right, and bottom. When moving an element position, it does not affect the position of anything else on the screen, only that element. If an element moves to the space where another element is, it will display on top or below of that element. Really means you're adding a margin to the side that you move. Elements will flow around that margin area.
```html
img {
    position: relative;
    left: 20px;
}
```

## Absolute Positioning

- Rather than using relative positioning on elements you can also set `position` to absolute. When using absolute positioning on an element you are adding a margin relative to it's parent element rather than relative to where the element would have been like with relative positioning.
- Absolute positioning will affect other elements on the page unlike relative positioning.

## Fixed Positioning

- Using `position: fixed;` causes that element to stay fixed in it's position no matter whether the page is scrolling or not. This is useful for things like a nav bar that you want to keep at the top of the screen.

## Centering

- `text-align: center;` will center everything inside of that element that doesn't have a width set
- If an element does have a width set, you'll have to center it using `margin: 0 auto;` or `margin: auto 0;` (depending on if you want to center horizontally or vertically)

## Font Styling

- The font family can be set using `font-family: Verdana, sans-serif` (verdana and sans-serif are just examples). [Web safe fonts](https://www.w3schools.com/cssref/css_websafe_fonts.php)
- You can also have fallback fonts by [listing](https://www.cssfontstack.com) multiple fonts in `font-family`

## Font Sizing

- Font sizing can be adjusted using `font-size: 90px;` (or dynamically using percentages. 100% = 16px in font size, or em. 1 em = 16px)
- When using em or percentages, the size is added to its parent. For example, if you had an `<h1>` nested in the `<body>` and the body was set to `font-size: 100%` and the `<h1>` was set to `font-size: 50%` the total size for `<h1>` would be `150%`
- Rather than using `em`, you can use `rem`, which ignores the parent containers sizing. This is the most reliable and less error-prone way to do sizing.

## Float and Clear

- Using the `float` property on your elements causes the other elements to wrap around that element. You could use `float: right;` on an image for example if you wanted your text in that block to wrap around it to the right.
- You can use `clear: left;` (or right etc) on an element to clear the float so that part of the code block will not follow your previous float setting.
- It's recommended to only use `float` for wrapping text around images and not for positioning.

## Day 44 [Code Challenge](https://github.com/TroyCaywood/Python/tree/main/100%20Days%20of%20Code/CodeChallenges/Day-44) - Personal Website final CSS
