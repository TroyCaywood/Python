# Day 42 - Intermediate HTML

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
- Tables can also be nested inside of each other, though using CSS to change table layouts is better practice