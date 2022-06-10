# cv-rasa-tts
Computer Vision (Face Recognition) & RASA & Text-To-Speech


Code cURL snippet
```
curl --location --request POST 'http://localhost:5005/webhooks/rest/webhook' \
--header 'Content-Type: application/json' \
--data-raw '{
    "sender": "joao_test",
    "message": "/get_name{\"name\":\"test\"}"
}'
```
