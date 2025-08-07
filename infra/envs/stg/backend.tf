terraform {
  backend "gcs" {
    bucket = "salon-tf-state-single"
    prefix = "terraform/stg"
  }
}
