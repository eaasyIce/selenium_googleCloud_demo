gcloud builds submit --tag gcr.io/studied-beanbag-362003/demo-web-crawler

gcloud run deploy --image gcr.io/studied-beanbag-362003/demo-web-crawler:latest --platform managed   --allow-unauthenticated


--project=studied-beanbag-362003