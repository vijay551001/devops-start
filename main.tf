# 1. Tell Terraform we want to use the Docker provider tool
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

# 2. Command Terraform to ensure our cloud image exists locally
resource "docker_image" "my_app_image" {
  name         = "vijay551001/my-first-devops-app:latest"
  keep_locally = true
}

# 3. Command Terraform to spin up and manage the running container process
resource "docker_container" "my_app_container" {
  image = docker_image.my_app_image.image_id
  name  = "terraform-managed-app"
  
  ports {
    internal = 8000
    external = 8081
  }
}
