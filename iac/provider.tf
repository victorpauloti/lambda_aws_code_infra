terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.15"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  profile = "awsmei"
  region = var.region
}