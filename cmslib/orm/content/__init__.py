"""Content mappings.

This package provides modules to map
content on so-called "clients".
"""
from cmslib.orm.content.deployment import MODELS as DEPLOYMENT_MODELS
from cmslib.orm.content.deployment import DeploymentBaseChart
from cmslib.orm.content.deployment import DeploymentConfiguration
from cmslib.orm.content.deployment import DeploymentMenu
from cmslib.orm.content.group import MODELS as GROUP_MODELS
from cmslib.orm.content.group import GroupBaseChart
from cmslib.orm.content.group import GroupConfiguration
from cmslib.orm.content.group import GroupMenu


__all__ = [
    "MODELS",
    "DeploymentBaseChart",
    "DeploymentConfiguration",
    "DeploymentMenu",
    "GroupBaseChart",
    "GroupConfiguration",
    "GroupMenu",
]


MODELS = (*DEPLOYMENT_MODELS, *GROUP_MODELS)
