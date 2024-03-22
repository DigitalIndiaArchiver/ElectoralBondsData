# Electoral Bond Data Repository

[![CSV Fiddle](https://img.shields.io/badge/CSV_Fiddle-View_Fiddle-blue)](https://csvfiddle.io/#JTdCJTIyaXNUYWJsZU1ldGFkYXRhT3BlbiUyMiUzQWZhbHNlJTJDJTIyaXNOZXdUYWJsZUZvcm1PcGVuJTIyJTNBZmFsc2UlMkMlMjJpc0NvbmZpcm1EZWxldGVRdWVyeU9wZW4lMjIlM0FmYWxzZSUyQyUyMmlzQ29uZmlybURyb3BUYWJsZU9wZW4lMjIlM0FmYWxzZSUyQyUyMmlzU2hhcmVEaWFsb2dPcGVuJTIyJTNBZmFsc2UlMkMlMjJkYlJlYWR5JTIyJTNBZmFsc2UlMkMlMjJ0YWJsZXMlMjIlM0ElNUIlN0IlMjJuYW1lJTIyJTNBJTIyQnJhbmNoZXMlMjIlMkMlMjJ1cmwlMjIlM0ElMjJodHRwcyUzQSUyRiUyRnJhdy5naXRodWJ1c2VyY29udGVudC5jb20lMkZEaWdpdGFsSW5kaWFBcmNoaXZlciUyRkVsZWN0b3JhbEJvbmRzRGF0YSUyRm1haW4lMkZkYXRhJTJGYnJhbmNoX2RldGFpbHMuY3N2JTIyJTJDJTIyY29sdW1ucyUyMiUzQSU1QiU1RCU3RCUyQyU3QiUyMm5hbWUlMjIlM0ElMjJQYXJ0aWVzJTIyJTJDJTIydXJsJTIyJTNBJTIyaHR0cHMlM0ElMkYlMkZyYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tJTJGRGlnaXRhbEluZGlhQXJjaGl2ZXIlMkZFbGVjdG9yYWxCb25kc0RhdGElMkZtYWluJTJGZGF0YSUyRmVuY2FzaGVkLmNzdiUyMiUyQyUyMmNvbHVtbnMlMjIlM0ElNUIlNUQlN0QlMkMlN0IlMjJuYW1lJTIyJTNBJTIyUHVyY2hhc2VycyUyMiUyQyUyMnVybCUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSUyRkRpZ2l0YWxJbmRpYUFyY2hpdmVyJTJGRWxlY3RvcmFsQm9uZHNEYXRhJTJGbWFpbiUyRmRhdGElMkZwdXJjaGFzZWQuY3N2JTIyJTJDJTIyY29sdW1ucyUyMiUzQSU1QiU1RCU3RCU1RCUyQyUyMnF1ZXJpZXMlMjIlM0ElN0IlMjIxNzExMDgyODEwLjU0MzA0MTIlMjIlM0ElN0IlMjJpZCUyMiUzQTE3MTEwODI4MTAuNTQzMDQxMiUyQyUyMnRpdGxlJTIyJTNBJTIyTWF0Y2hlZCUyMEJvbmRzJTIyJTJDJTIyYm9keSUyMiUzQSUyMnNlbGVjdCUyMCU1QyUyMkRhdGUlMjBvZiUyMFB1cmNoYXNlJTVDJTIyJTJDJTIwJTVDJTIyTmFtZSUyMG9mJTIwdGhlJTIwUHVyY2hhc2VyJTVDJTIyJTJDJTIwJTVDJTIyRGF0ZSUyMG9mJTIwRW5jYXNobWVudCU1QyUyMiUyQyUyMCU1QyUyMk5hbWUlMjBvZiUyMHRoZSUyMFBvbGl0aWNhbCUyMFBhcnR5JTVDJTIyJTJDJTIwJTVDbiUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMFBhcnRpZXMuRGVub21pbmF0aW9ucyUyQyUyMCU1QyUyMklzc3VlJTIwQnJhbmNoJTIwQ29kZSU1QyUyMiUyQyUyMCU1QyUyMlBheSUyMEJyYW5jaCUyMENvZGUlNUMlMjIlNUNuZnJvbSUyMFB1cmNoYXNlcnMlMkMlMjBQYXJ0aWVzJTVDbndoZXJlJTIwUHVyY2hhc2Vycy4lNUMlMjJCb25kJTIwTnVtYmVyJTVDJTIyJTIwJTNEJTIwUGFydGllcy4lNUMlMjJCb25kJTIwTnVtYmVyJTVDJTIyJTVDbmFuZCUyMFB1cmNoYXNlcnMuUHJlZml4JTIwJTNEJTIwUGFydGllcy5QcmVmaXglNUNuLS1hbmQlMjBQdXJjaGFzZXJzLiU1QyUyMkRhdGUlMjBvZiUyMFB1cmNoYXNlJTVDJTIyJTIwJTNEJTIwUGFydGllcy4lNUMlMjJEYXRlJTIwb2YlMjBFbmNhc2htZW50JTVDJTIyJTVDbm9yZGVyJTIwYnklMjAlNUMlMjJOYW1lJTIwb2YlMjB0aGUlMjBQb2xpdGljYWwlMjBQYXJ0eSU1QyUyMiUyQyUyMCU1QyUyMkRhdGUlMjBvZiUyMEVuY2FzaG1lbnQlNUMlMjIlM0IlNUNuJTVDbiUyMiUyQyUyMnJlc3VsdCUyMiUzQSU1QiU1RCUyQyUyMmVycm9yJTIyJTNBbnVsbCU3RCUyQyUyMjE3MTEwODI5MDEuMTcwMzA1NSUyMiUzQSU3QiUyMmlkJTIyJTNBMTcxMTA4MjkwMS4xNzAzMDU1JTJDJTIydGl0bGUlMjIlM0ElMjJTYW1lJTIwZGF5JTIwU2FtZSUyMGJyYW5jaCUyMGVuY2FzaG1lbnQlMjIlMkMlMjJib2R5JTIyJTNBJTIyU0VMRUNUJTIwJTVDbiUyMCUyMCUyMCUyMFB1cmNoYXNlcnMuJTVDJTIyRGF0ZSUyMG9mJTIwUHVyY2hhc2UlNUMlMjIlMkMlNUNuJTIwJTIwJTIwJTIwUHVyY2hhc2Vycy4lNUMlMjJOYW1lJTIwb2YlMjB0aGUlMjBQdXJjaGFzZXIlNUMlMjIlMkMlNUNuJTIwJTIwJTIwJTIwUGFydGllcy4lNUMlMjJEYXRlJTIwb2YlMjBFbmNhc2htZW50JTVDJTIyJTJDJTVDbiUyMCUyMCUyMCUyMFBhcnRpZXMuJTVDJTIyTmFtZSUyMG9mJTIwdGhlJTIwUG9saXRpY2FsJTIwUGFydHklNUMlMjIlMkMlNUNuJTIwJTIwJTIwJTIwUGFydGllcy5EZW5vbWluYXRpb25zJTJDJTVDbiUyMCUyMCUyMCUyMFB1cmNoYXNlcnMuJTVDJTIySXNzdWUlMjBCcmFuY2glMjBDb2RlJTVDJTIyJTJDJTVDbiUyMCUyMCUyMCUyMFBhcnRpZXMuJTVDJTIyUGF5JTIwQnJhbmNoJTIwQ29kZSU1QyUyMiU1Q25GUk9NJTIwJTVDbiUyMCUyMCUyMCUyMFB1cmNoYXNlcnMlMkMlMjBQYXJ0aWVzJTVDbldIRVJFJTIwJTVDbiUyMCUyMCUyMCUyMFB1cmNoYXNlcnMuJTVDJTIyQm9uZCUyME51bWJlciU1QyUyMiUyMCUzRCUyMFBhcnRpZXMuJTVDJTIyQm9uZCUyME51bWJlciU1QyUyMiU1Q24lMjAlMjAlMjAlMjBBTkQlMjBQdXJjaGFzZXJzLlByZWZpeCUyMCUzRCUyMFBhcnRpZXMuUHJlZml4JTVDbiUyMCUyMCUyMCUyMEFORCUyMFB1cmNoYXNlcnMuJTVDJTIyRGF0ZSUyMG9mJTIwUHVyY2hhc2UlNUMlMjIlMjAlM0QlMjBQYXJ0aWVzLiU1QyUyMkRhdGUlMjBvZiUyMEVuY2FzaG1lbnQlNUMlMjIlNUNuT1JERVIlMjBCWSUyMCU1Q24lMjAlMjAlMjAlMjBQYXJ0aWVzLiU1QyUyMk5hbWUlMjBvZiUyMHRoZSUyMFBvbGl0aWNhbCUyMFBhcnR5JTVDJTIyJTJDJTIwJTVDbiUyMCUyMCUyMCUyMFBhcnRpZXMuJTVDJTIyRGF0ZSUyMG9mJTIwRW5jYXNobWVudCU1QyUyMiUzQiU1Q24lMjIlMkMlMjJyZXN1bHQlMjIlM0ElNUIlNUQlMkMlMjJlcnJvciUyMiUzQW51bGwlN0QlN0QlMkMlMjJhY3RpdmVRdWVyeUlkJTIyJTNBJTIyMTcxMTA4MjkwMS4xNzAzMDU1JTIyJTJDJTIyYWN0aXZlVGFibGVNZXRhZGF0YUNvbHVtbnMlMjIlM0ElNUIlNUQlMkMlMjJsb2NhbFRhYmxlc1RvV2FybiUyMiUzQSU1QiU1RCUyQyUyMmlzUXVlcnlJblByb2dyZXNzJTIyJTNBZmFsc2UlMkMlMjJkaWRBZGROZXdUYWJsZVN1Y2NlZWQlMjIlM0FudWxsJTJDJTIyYWRkTmV3VGFibGVFcnJvciUyMiUzQW51bGwlMkMlMjJkcm9wVGFibGVOYW1lJTIyJTNBJTIyUGFydGllcyUyMiUyQyUyMmRlbGV0ZVF1ZXJ5SWQlMjIlM0ExNzExMDgzMDc5LjM3NDMzMyU3RA==) [![FlatGithub](https://img.shields.io/badge/FlatGithub-View%20Data-green?style=flat-square&logo=github)](https://flatgithub.com/DigitalIndiaArchiver/ElectoralBondsData)



This repository contains data and queries related to electoral bonds, including purchaser details and transaction information.

## Data

The repository includes the following data files:

- **purchasers.csv**: CSV file containing details of electoral bond purchasers.
- **parties.csv**: CSV file containing details of political parties receiving electoral bonds.
- **branches.csv**: CSV file containing information about bank branches.

### Data Fields

#### purchasers.csv

1. `Sr No.`: Serial number
2. `Reference No (URN)`: Unique Reference Number
3. `Journal Date`: Date of journal
4. `Date of Purchase`: Date of bond purchase
5. `Date of Expiry`: Date of bond expiry
6. `Name of the Purchaser`: Name of the bond purchaser
7. `Prefix`: Prefix of the bond
8. `Bond Number`: Electoral bond number
9. `Denominations`: Denominations
10. `Issue Branch Code`: Branch code of issue
11. `Issue Teller`: Teller ID of issue
12. `Status`: Status of the bond

#### parties.csv

1. `Sr No.`: Serial number
2. `Date of Encashment`: Date of bond encashment
3. `Name of the Political Party`: Name of the political party receiving the bond
4. `Account no. of Political Party`: Account number of the political party
5. `Prefix`: Prefix of the bond
6. `Bond Number`: Electoral bond number
7. `Denominations`: Denominations
8. `Pay Branch Code`: Branch code of payment
9. `Pay Teller`: Teller ID of payment

#### branches.csv

1. `IFSC`: Indian Financial System Code
2. `MICR`: Magnetic Ink Character Recognition
3. `BRANCH`: Branch Name
4. `ADDRESS`: Branch Address
5. `STATE`: State
6. `CONTACT`: Contact Information
7. `UPI`: UPI Availability (True/False)
8. `RTGS`: RTGS Availability (True/False)
9. `CITY`: City
10. `CENTRE`: Centre
11. `DISTRICT`: District
12. `NEFT`: NEFT Availability (True/False)
13. `IMPS`: IMPS Availability (True/False)
14. `SWIFT`: SWIFT Code
15. `ISO3166`: ISO 3166 Code
16. `BANK`: Bank Name
17. `BANKCODE`: Bank Code

## Queries

The repository includes SQL queries for retrieving and processing electoral bond data stored in the `purchasers.csv` and `parties.csv` files.

### Query Files

- **retrieve_purchaser_party_details.sql**: SQL query to retrieve details of bond purchasers and the political parties receiving the bonds.

## CSV Fiddle

Here's a CSV fiddle containing multiple queries on the electoral bond data:

