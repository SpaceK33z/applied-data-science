## Activity 2

Validity is violated:
Data-type constraints; all types are possible, there are no restrictions at all.
Range constraints; you can't have 10000 trousers, so there should be a limit.
Mandatory constraints; Some of the important fields should be required; like the gender field.
Set-Membership constraints; the gender question should be limited to three values.
Regular expression constraints; the income question should be validated against a regular expression.
Cross field validation; if zero is filled in as answer for 'How many trousers do you have?', you shouldn't be able to fill in the next question about how many you spend.

Decleansing is violated; nothing is properly cleaned up.

## Activity 3

- C: Remove `Apple`. Check the inputs against a phone model list. Everything that doesn't have a match should be seen as invalid.
- D: If the first character is `M`, it should be replaced with `Male`. If the first character is `F`, replace it with `Female`. All other values should be set to unknown.
- E: `Dutch`, `The Netherlands` should be renamed to `Netherland`
- F: Delete the following characters: `by`, `with`, `a`. Rename `bike` to `bicycle`. `foot` to `walking`. Replace `/`, `&`, `;` to `,`.  Trim whitespace.
- I: All non-numeric characters should be removed; if nothing is left it should be seen as invalid.
- J: All non-numeric characters should be removed (except for the `,`); if nothing is left it should be seen as invalid.
- K: Delete all non-numeric characters in the income question. This would remove `€` and `euros`.

## Activity 4

MCAR; the questions do not have a relationship between them, so there is nothing systematic about the missing data.
