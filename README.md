gcloud builds submit --tag gcr.io/my-first-dash-app/peer_review_dash  --project=my-first-dash-app

gcloud run deploy peerreviewdash --image gcr.io/my-first-dash-app/peer_review_dash:latest --platform managed  --project=my-first-dash-app --allow-unauthenticated
