# Client Side Form Validation Cheat Sheet
@Student Hi all, here is a quick guide is to help you avoid a common bug: when a user enters an invalid input while editing or creating, the create or update action fails without providing any feedback to the user.

To prevent this issue, ensure that *every* frontend input includes some form of validations, such as:
- Minimum and maximum length
- Correct input types
- No blank values

Note: this guide doesn't cover server side validations, but it should help make client side form validations more straightforward :dkthumbsup:
## Steps
First, in VS Code, type `ctrl + p` or `cmd + p` to open search
```shell
ctrl + p
```
Next, in the search bar, type `%input`.
```shell
%input
```
Finally, use the down arrow to scroll through all `input` fields in the code base, ensuring they have sensible built in [browser validations](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation#using_built-in_form_validation).
## Commonly Used Validations
- required
- min / max / minLength / maxLength
- [common types](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#input_types): number, text, password, email, etc.
## Example Usage
```js
<label> Enter a Number
<input type="number" min={0} required />
</label>
```
