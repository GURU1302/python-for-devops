##CONDITIONAL HANDLING
import sys

instance_type = sys.argv[1]

if instance_type == "e2-medium":
    print("created")
elif instance_type == "ec2-micro":
    print("supra")
else:
    print("not created")