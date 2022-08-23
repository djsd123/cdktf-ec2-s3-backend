# cdktf-ec2-s3-backend

[cdktf]: https://www.hashicorp.com/blog/cdk-for-terraform-now-generally-available?mkt_tok=ODQ1LVpMRi0xOTEAAAGGSsfRqczjOAaZIIcpZwxRqy691dwDdS4wmJrr3nZ1rhP_ouGiRYj8liS9SA2MU8KXW4LQO9jfmBxPfIAIT9I-vnxLX-lS-e39JtyGoXSTLudRCw
[python]: https://www.python.org/downloads/
[pipenv]: https://pipenv.pypa.io/en/latest/install/#installing-pipenv/
[node]: https://nodejs.org/en/download/package-manager/
[cdk]: https://www.npmjs.com/package/cdktf-cli

An ec2 instance in python and Terraform [CDK] with an S3 backend based on this [example](https://learn.hashicorp.com/tutorials/terraform/cdktf-build)

## Requirements

| Name   | Version              |
|--------|----------------------|
| [node] | \>= 16.x, < 17.x     |
| [cdk]  | \>= 0.12, < 1        |
| [python] | \>= 3.7.x, < 4.x   |
| [pipenv] | \>= v2021, < v2023 |


## Usage

Install cdktf cli

```shell
npm install --global cdktf-cli@latest
```

Install the cdktf aws provider

```shell
pipenv install cdktf-cdktf-provider-aws
```

Deploy the EC2 instance

```shell
cdktf deploy
```

Cleanup

```shell
cdktf destroy
```
