from aws_cdk import CfnOutput, Duration, Stack, aws_s3
from constructs import Construct


class CdkStarterStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        myL2Bucket = aws_s3.Bucket(self, "MyL2Bucket",
            lifecycle_rules=[
                aws_s3.LifecycleRule(
                    expiration=Duration.days(365))
            ]
        )
        
        output = CfnOutput(self, "MyL2BucketOutput",
            value=myL2Bucket.bucket_name,
            description="My L2 Bucket"
        )