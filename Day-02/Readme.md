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

Question 2: Read JSON Log File and Filter Errors

Use case: Log analysis

Input (logs.json)
[
  {"level": "INFO", "msg": "Started"},
  {"level": "ERROR", "msg": "DB connection failed"},
  {"level": "ERROR", "msg": "Timeout"}
]

Task

Print only error messages:

DB connection failed
Timeout