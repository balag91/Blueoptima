provider "aws" {
    region = "us-east-1"
}

resource "aws_instance" "webserver" {
    ami = "ami-045393c081cabeb1f"
    instance_type = "t2.micro"
    tags = {
      "Hostname" = "webserver02"
      "Department" = "Frontend"
    }
    key_name = "demo12"    
}
output "instance_id" {
    value = aws_instance.webserver.id
}
