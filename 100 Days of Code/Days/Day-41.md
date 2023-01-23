# Day 41 - Introduction to HTML

- The internet works by servers that are on 24/7 which clients (other computers) access through internet service providers which send the request to a DNS server (which looks up the IP address of the website) and sends the IP address back to the client. The client then sends a direct request to that IP address through their ISP through the internet backbone. The browser then sends a message to that server and the server sends back the files the client needs to view that website.
- The data that is received from the server usually consists of three types of files:
  + HTML - Responsible for the structure of a website (such as images or text boxes etc). The "walls" of a website.
  + CSS - Responsible for styling a website. Things such as text color, font color, sizing, button styles etc. The "paint" of a website.
  + JavaScript - Code that allows a website to actually do things. The "electricity/plumbing" of a website.

- HTML is the foundation of all websites
- You *could* create a website in all HTML, but it wouldn't look very good/modern.
- HTML stands for Hypertext Markup Language. Based off the "markups" that editors used to put in manuscripts to specify changes for publishers.
- the `<h1>` [tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) creates a large heading and must be closed with `</h1>`. Similarly `<h2>` creates a slightly smaller heading. The heading tag gets smaller the larger the number and goes until `<h6>`. 
- When working with HTML it's important to close your tags or it applies that tag to anything after the tag.
```html
<h1>The Adventures of Sherlock Holmes</h1>
<h3>by</h3>
<h2>Arthur Conan Doyle</h2>
```
- [Devdocs.io](https://devdocs.io/), [W3 Schools](https://www.w3schools.com/html/), and [MDN](https://developer.mozilla.org/en-US/) are all good sources for HTML documentation (as well as other languages.
- To add space between elements in HTML you use the line break `<br>`
```html
<h1>The Adventures of Sherlock Holmes</h1>
<br>
<h3>by</h3>
<br>
<h2>Arthur Conan Doyle</h2>
```

### Structure of a HTML tag
- An HTML tag has a start tag and an end tag with the content in the middle `<start tag>content</end tag>`
- Some tags (such as `<br>`) do not have an end tag. These are called **self-closing tags**.
- The `<hr>` (horizontal rule) creates a horizontal line across the entire page.
- HTML tags can also have **attributes** inside of them that modify that element. For example `<hr size="3">` would create a slightly thicker horizontal rule.
- Looking at the documentation for tags is important so you know what you can do with those tags.
- HTML comments are in the form of `<--Comment goes here-->`

### HTML Boilerplate

- Every HTML document you create will have this code
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

</body>
</html>
```