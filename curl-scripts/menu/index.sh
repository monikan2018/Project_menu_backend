#!/bin/bash

curl "http://localhost:8000/menus/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
