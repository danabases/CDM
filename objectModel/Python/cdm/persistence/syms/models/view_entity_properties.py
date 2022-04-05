# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .md_entity_properties import MDEntityProperties


class ViewEntityProperties(MDEntityProperties):
    """Database properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param origin_object_id: Entity object id maintained by the caller.
    :type origin_object_id: str
    :ivar object_id: Entity object id maintained by SyMS.
    :vartype object_id: str
    :ivar object_version: Entity object version maintained by SyMS.
    :vartype object_version: long
    :param publish_status: Possible values include: 'PUBLISHED'
    :type publish_status: str or :class:`PublishStatus
     <Microsoft.ADF.SyMSAPIClient.models.PublishStatus>`
    :param properties: Property bag
    :type properties: dict
    :param namespace:
    :type namespace: :class:`TableNamespace
     <Microsoft.ADF.SyMSAPIClient.models.TableNamespace>`
    :param partitioning:
    :type partitioning: :class:`TablePartitioning
     <Microsoft.ADF.SyMSAPIClient.models.TablePartitioning>`
    :param storage_descriptor:
    :type storage_descriptor: :class:`StorageDescriptor
     <Microsoft.ADF.SyMSAPIClient.models.StorageDescriptor>`
    :param view_original_text: View original text.
    :type view_original_text: str
    :param view_expanded_text: View expanded text.
    :type view_expanded_text: str
    :param temporary: Temporary.
    :type temporary: bool
    :param is_rewrite_enabled: Is rewrite enabled.
    :type is_rewrite_enabled: bool
    """ 

    _validation = {
        'object_id': {'readonly': True},
        'object_version': {'readonly': True},
        'namespace': {'required': True},
        'storage_descriptor': {'required': True},
    }

    _attribute_map = {
        'origin_object_id': {'key': 'OriginObjectId', 'type': 'str'},
        'object_id': {'key': 'ObjectId', 'type': 'str'},
        'object_version': {'key': 'ObjectVersion', 'type': 'long'},
        'publish_status': {'key': 'PublishStatus', 'type': 'PublishStatus'},
        'properties': {'key': 'Properties', 'type': '{object}'},
        'namespace': {'key': 'Namespace', 'type': 'TableNamespace'},
        'partitioning': {'key': 'Partitioning', 'type': 'TablePartitioning'},
        'storage_descriptor': {'key': 'StorageDescriptor', 'type': 'StorageDescriptor'},
        'view_original_text': {'key': 'ViewOriginalText', 'type': 'str'},
        'view_expanded_text': {'key': 'ViewExpandedText', 'type': 'str'},
        'temporary': {'key': 'Temporary', 'type': 'bool'},
        'is_rewrite_enabled': {'key': 'IsRewriteEnabled', 'type': 'bool'},
    }

    def __init__(self, namespace, storage_descriptor, origin_object_id=None, publish_status=None, properties=None, partitioning=None, view_original_text=None, view_expanded_text=None, temporary=None, is_rewrite_enabled=None):
        super(ViewEntityProperties, self).__init__(origin_object_id=origin_object_id, publish_status=publish_status, properties=properties)
        self.namespace = namespace
        self.partitioning = partitioning
        self.storage_descriptor = storage_descriptor
        self.view_original_text = view_original_text
        self.view_expanded_text = view_expanded_text
        self.temporary = temporary
        self.is_rewrite_enabled = is_rewrite_enabled