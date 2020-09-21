#!/bin/bash

curl "http://localhost:8000/menus/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
