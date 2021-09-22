# Search-UI-Testing

> How to test a search bar?

This project aims to open up ideas to test search bars with adequate coverage, and using Google as an example

### Used Test Scenarios

A) Numbers
- Positive decimals (one-digit, multi-digit)
- Negative decimals (one-digit, multi-digit)
- Floats
- Zero

B) Letters
- Single Characters
- Words (small cases, Capital case, UPPER CASE)
- Words with typos (missing letter, extra letter)
- Word of a different language
- Sentence (< 32 search limit)
- Paragraph (= 32 search limit)
- Paragraph (> 32 search limit)
- Gibberish
- Special characters in URL query (ex: q, ?, etc.)
- Special word operator in advanced search
- Special character operator in advanced search
- URL
- Null


## Built With

- Python

### Prerequisites

- Python 3.8.3
- Selenium 3.141.0

## 🤝  Resources

- Stackoverflow (for small code tips and sharing a few testcases)
- Browserstack (how to use Selenium with Python)
- PEP8 and RealPython (Python style conventions)
- Github (which I used to find awesome readme templates like this one :fire:)
- Wikipedia (Google advanced search using operators)
- Google guide (helped with knowing more about the search limit and other useful tips)

## Show your support

Give a ⭐️ if you like this project!

## 📝 License

This project is [MIT](./MIT.md) licensed.
