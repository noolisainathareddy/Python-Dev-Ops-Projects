Question 1. Merge Two JSON Config Files

Use case: Base config + env override

Input (base.json)
{
  "replicas": 2,
  "region": "us-east-1"
}

Input (override.json)
{
  "replicas": 5
}

Task

Merge override into base

Output:

{
  "replicas": 5,
  "region": "us-east-1"
}