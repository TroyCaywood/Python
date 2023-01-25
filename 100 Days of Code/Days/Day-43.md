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