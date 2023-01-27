# Day 43 - Introduction to CSS

- CSS Stands for **C**ascading **S**tyle **S**heet
- CSS is used to style markup language such as HTML or XML.

## Inline CSS

- CSS can be entered into tags inline, though this isn't the best way to do CSS as it makes changes more difficult
- `<body style="background-color: blue;">` the `background-color: blue;` portion is the CSS code to change the background of the body.
- Colors in CSS can be entered by name or hex code. [Color Hunt](https://colorhunt.co/) is a good site for finding color schemes.

## Internal CSS
 
- CSS can be added internally to a page by adding it between a `<style>` tag in the `<head>` of a page
- To change the background color we would do this:
```html
<head>
    <style>
        body {
            background-color: #EAF6F6;
        }
    </style>
</head>
```
- Any CSS code you want to enter will be in the format of `htmlcodetomodify { css-code: value;}`
- Some CSS has [default](https://www.w3schools.com/cssref/css_default_values.php) values that are applied to elements automatically 
- Pretty much everything that exists on a webpage is contained in [boxes](https://chrome.google.com/webstore/detail/pesticide-for-chrome/bakpbgckdnepkmkeaiomhmfcnejndkbi) 
- When changing the CSS for an element, it will affect all elements of that type on that page.
- When changing things such as height and width, you can use percentages rather than px to make the page more responsive to resizes. For example:
```html
<style>
     hr {
        background-color: white;
        border-style: none;
        height: 2px;
        width: 30%;
     }
</style>
```
- This would make the horizontal rule elements with the background color of white, no border, a height of 2 pixels, and the width will be 30% of the page (no matter what size the page is at the time).

## External CSS

- CSS can also be applied across multiple pages on a site by using an external CSS file and linking each page to that CSS file. That way you can easily keep a consistent style across your pages and change them all at once.
- To do this, you create a css file and write all of your CSS code in that. Then in the head of each page you link it using `<link rel="stylesheet" href="css/styles.css">`. When the page gets to that link tag it will see the stylesheet link tag and apply that CSS code to the page.
- If CSS is applied inline on a tag directly, that takes precedence, if a style is applied in the `<style>` tag at the top of a page, that is the next applied, if it isn't applied anywhere else, then it's applied from the external CSS file.
- Best practice is to implement all of your styles on the external CSS file

## CSS Syntax

- CSS syntax is `selector{property: value;}`
- The selector is the who, as in what html tag do you want to change? `h1` `h3` `body` for example
- Property is the what, as in what do you want to change about that tag? The color, the size, the alignment, etc.
- The value is the how, as in how do you want to change that tag. Do you want the color to be blue, the size to be 10%?
- When writing CSS it's best practice to write the properties in alphabetical order just to make it easier to find what you're looking for when re-reading your code later.

## CSS Selectors

- If you want to apply CSS more selectively, you can assign classes to your html. For example
```html
<img class="car" src="https://www.website.com/car.jpg">
<img src="https://www.website.com/dog.jpg">
```

- Then you can apply your css to just the "car" class
```css
.car {
    background-color: green;
}
```
- This way, only the car image would have a green background color, and the dog picture would not.

## Classes vs IDs

- You can also use the ID property of an HTML tag to select specific individual tags in your CSS
```html
<img id="car" src="https://www.website.com/car.jpg">
<img src="https://www.website.com/dog.jpg">
```

- Instead of using a `.` in your css you would use `#`
```css
#car {
    background-color: green;
}
```

- This would function the same way as our previous example using the class property.
- The difference between classes and IDs is that you can only have one ID tag with a specific name, but with classes you can have multiple of the same class name.
- Classes are more for groups of elements that you want to have the same properties.
- Use classes when you want to apply the same style to a group of related items.
- Use IDs when you want to apply a specific style to a single element on a page
- A tag can also have more than one class applied to it, but can only have one ID applied
```html
<img class="car motor" src="https://www.website.com/car.jpg">
```
- In this example the img tag has the `car` and `motor` classes applied to it.
- You cannot have more than one ID applied to a single element.
- It's more recommended to use Classes to apply styling to elements
- There are also [pseudo classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes) that allow you to select a different state of an HTML element such as when you hover your mouse over a specific element.
```css
img:hover {
    background-color: gold;
}
```
- The previous example would cause any image to change it's background color to gold as soon as a user hovers their mouse cursor over it.