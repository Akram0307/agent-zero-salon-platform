terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.30"
    }
  }
}

provider "google" {
  project = "salon-autonomous-ai-467811"
  region  = "asia-south1"
}

# Example: create Secret Manager secrets namespace for stg
resource "google_secret_manager_secret" "jwt_stg" {
  secret_id = "stg-jwt-signing-key"
  replication { auto {} }
}
