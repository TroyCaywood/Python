# Day 42 - Intermediate HTML


### Tables
- To create a table in HTML you use the `<table>` tag
- Inside the table tags you use `<tr>` to create a table row.
- Inside the table row tags you use `<td>` to create table data in that row
```html
<table>
    <tr>
        <td>This is table data in a row</td>
        <td>This is table data in the same row</td>
    </tr>
    <tr>
        <td>This is table data in a new row</td>
    </tr>
</table>
```

- Tables can also have headers, body, and footers
- The table header contains `<tr>` tags and then `<th>` table header tags inside of those. The `<th>` tags will show up bold.
```html
<table>
    <thead>
        <tr>
            <th>This is a table head row</th>
            <th>This is another table head row</th>
        </tr>
    </thead>
    <tr>
        <td>This is table data in a row</td>
        <td>This is table data in the same row</td>
    </tr>
    <tr>
        <td>This is table data in a new row</td>
    </tr>
</table>
```
- Tables can also be nested inside each other, though using CSS to change table layouts is better practice.

### Forms

- The structure for forms can be created using HTML, but full functionality requires javascript
- The fields in a form are in the self closing `<input>` tags. This tag has many [type attributes](https://www.w3schools.com/tags/tag_input.asp) for things such as buttons, text boxes, password fields etc.
- The `<label>` tag is used to add text labels for input elements.
```html
<form class="" action="index.html" method="post">
    <label>Your Name:</label>
    <input type="text" name="" id="">
    <input type="submit" value="Submit">
    <input type="color" name="" id="">
    <br>
    <label for="">Do you want to sign up for the email list?</label>
    <input type="checkbox" name="" id="">
    <input type="password" name="" id="">
</form>
```
- A `<textarea>` is a larger text field that allows for multiple lines of text to be inputted. When creating a text area you must specify how many rows and columns it is by default.
```html
<textarea name="" id="" cols="30" rows="10"></textarea>
```
- You can also change the function of the submit button by changing the `action` type attribute of the form tag. For example `mailto:someemail@email.com' would open the default mail program on the user's computer and add the contents of the form