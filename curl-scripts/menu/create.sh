#!/bin/bash

curl "http://localhost:8000/menus/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "menus": {
      "date": "'"${DATE}"'"
      "breakfast": "'"${BREAKFAST}"'",
      "lunch": "'"${LUNCH}"'",
      "snack": "'"${SNACK}"'",
      "dinner": "'"${DINNER}"'"

    }
  }'

echo
