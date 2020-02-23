# Search app backend

# INSTRUCTIONS

# Backend Code Challenge

Design a REST API endpoint that provides auto-complete suggestions from a list of contacts.

## Overview

- The endpoint is exposed at /suggestions
- The partial (or complete) search term is passed as a query string parameter ‘q’
- The contact can optionally be filtered by query string parameters ‘min_rate’ and ‘verified_skills’
- The endpoint returns a JSON response with an array of scored suggested matches
  _ The suggestions are sorted by descending score
  _ Each suggestion has a score between 0 and 1 (inclusive) indicating confidence in the suggestion (1 is most confident)
  _ Each suggestion has an ID which can be used to disambiguate between similarly named contacts.
  _ Each suggestion has a contact email address

## Requirements

- Please use Python. Use any tools you'd like in addition to Python that you feel comfortable with.
- End result should be deployed on a public cloud (there are free tiers available).

## Sample Responses

`GET /suggestions?q=Bran&rate_minimum=75&verified_skills=facebook_advertising`

```json
[
  {
    "_id": "5e2f3a706185a65d93c1e4cd",
    "index": 0,
    "guid": "a421d5c8-9da1-4dfa-99be-683d351e0021",
    "min_rate": "$268.45",
    "age": 31,
    "first_name": "Brandon",
    "last_name": "Dunn",
    "contact_email": "brandondunn@gmail.com",
    "verified_skills": [
      "facebook_marketing",
      "lifecycle_marketing",
      "conversion_rate_optimization",
      "quantitative_research",
      "customer_acquisition_strategy",
      "analytics_infrastructure",
      "go_to_market_strategy"
    ],
    "score": 0.6729
  },
  {
    "_id": "5e2f3a7074e54b91e8a5d2dc",
    "index": 1,
    "guid": "818e21ed-309c-4260-a0d0-f1045a667d39",
    "min_rate": "$179.85",
    "age": 35,
    "eyeColor": "blue",
    "first_name": "Lenora",
    "last_name": "Delacruz",
    "contact_email": "lenoradelacruz@yahoo.com",
    "verified_skills": [
      "facebook_marketing",
      "lifecycle_marketing",
      "conversion_rate_optimization",
      "podcast_advertising",
      "linkedin_advertising",
      "user_referral_programs"
    ],
    "score": 0.6677
  },
  {
    "_id": "5e2f3a70861b24f261e97530",
    "index": 2,
    "guid": "60a601b6-ff75-4e62-9f2f-88fff91d31dc",
    "min_rate": "$288.50",
    "age": 22,
    "eyeColor": "green",
    "first_name": "Elsa",
    "last_name": "Ruiz",
    "contact_email": "elsaruiz@codax.com",
    "verified_skills": [
      "lifecycle_marketing",
      "conversion_rate_optimization",
      "podcast_advertising",
      "facebook_organic",
      "facebook_paid_advertising",
      "mailchimp"
    ],
    "score": 0.3374
  }
]
```

# IMPLEMENTATION

## Setup

**Environment**

´´´bash
$ virtualenv -p python3 env
$ source env/bin/activate
´´´

**Run**

_Development_

´´´bash
\$ aufziehen dev
´´´

_Production_

´´´bash
\$ aufziehen prod
´´´

## Endpoint

`GET http://localhost:8080/suggestions/?q=bran&rate_minimum=75&verified_skills=facebook_marketing`
