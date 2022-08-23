#!/usr/bin/env python
from constructs import Construct
from cdktf import App, DataTerraformRemoteStateS3, S3Backend, TerraformOutput, TerraformStack
from cdktf_cdktf_provider_aws import AwsProvider, s3, ec2


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        region = "eu-west-1"
        bucket = "kel-pulumi-inf-state"
        key = "cdktf/cdk-ec2"

        AwsProvider(self, "AWS", region=region)

        # S3 Backend - https://www.terraform.io/docs/backends/types/s3.html
        # Bucket must already exist
        S3Backend(self,
                  bucket=bucket,
                  key=key,
                  region=region
                  )

        # Reference Remote State for it's outputs
        # remote_state = DataTerraformRemoteStateS3(self, "other",
        #                                          bucket=bucket,
        #                                          key=key
        #                                          )

        # Reference Remote State object
        # s3.DataAwsS3BucketObject(self, 'object',
        #                          bucket=bucket,
        #                          key=key,
        #                          )

        amazon_linux_2 = ec2.DataAwsAmi(self, "amazon-linux-2",
                                        most_recent=True,
                                        owners=["amazon"],
                                        filter=[
                                                ec2.DataAwsAmiFilter(
                                                                     name="name",
                                                                     values=["amzn2-ami-hvm-*-x86_64-ebs"]
                                                                     )
                                                 ]
                                        )


        ec2_instance = ec2.Instance(self, "compute",
                                    ami=amazon_linux_2.image_id,
                                    instance_type="t2.micro",
                                    )

        TerraformOutput(self, "public_ip",
                        value=ec2_instance.public_ip
                        )


app = App()
MyStack(app, "cdktf-ec2")

app.synth()
