# Validation during input

Values input in an input field of type text or combo can be subjected to a validation. Depending on the type of content, different **validators** or a combination of validators is used.

- **numberRangeValidator**: The permitted range of values for a number is defined by means of an upper limit and a lower limit.
- **contentValidator**: Input text is checked with the help of a regular expression.
- **keyValidator**: The input is restricted to a specific subset of characters with a regular expression.

If the validators are combined, the following sequence has to be followed:

1. keyValidator
2. contentValidator
3. numberRangeValidator