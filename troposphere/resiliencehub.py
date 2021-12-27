# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 51.0.0


from . import AWSObject, AWSProperty, Tags
from .validators import integer
from .validators.resiliencehub import (
    validate_resiliencypolicy_policy,
    validate_resiliencypolicy_tier,
)


class PhysicalResourceId(AWSProperty):
    """
    `PhysicalResourceId <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-physicalresourceid.html>`__
    """

    props = {
        "AwsAccountId": (str, False),
        "AwsRegion": (str, False),
        "Identifier": (str, True),
        "Type": (str, True),
    }


class ResourceMapping(AWSProperty):
    """
    `ResourceMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-app-resourcemapping.html>`__
    """

    props = {
        "LogicalStackName": (str, False),
        "MappingType": (str, True),
        "PhysicalResourceId": (PhysicalResourceId, True),
        "ResourceName": (str, False),
    }


class App(AWSObject):
    """
    `App <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-app.html>`__
    """

    resource_type = "AWS::ResilienceHub::App"

    props = {
        "AppTemplateBody": (str, True),
        "Description": (str, False),
        "Name": (str, True),
        "ResiliencyPolicyArn": (str, False),
        "ResourceMappings": ([ResourceMapping], True),
        "Tags": (Tags, False),
    }


class FailurePolicy(AWSProperty):
    """
    `FailurePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resiliencehub-resiliencypolicy-failurepolicy.html>`__
    """

    props = {
        "RpoInSecs": (integer, True),
        "RtoInSecs": (integer, True),
    }


class ResiliencyPolicy(AWSObject):
    """
    `ResiliencyPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resiliencehub-resiliencypolicy.html>`__
    """

    resource_type = "AWS::ResilienceHub::ResiliencyPolicy"

    props = {
        "DataLocationConstraint": (str, False),
        "Policy": (validate_resiliencypolicy_policy, True),
        "PolicyDescription": (str, False),
        "PolicyName": (str, True),
        "Tags": (Tags, False),
        "Tier": (validate_resiliencypolicy_tier, True),
    }
