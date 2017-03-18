from ckantoolkit import get_or_bust, side_effect_free, ObjectNotFound

from ckanext.scheming.helpers import (
    scheming_dataset_schemas, scheming_get_dataset_schema,
    scheming_group_schemas, scheming_get_group_schema,
    scheming_organization_schemas, scheming_get_organization_schema,
    )

from ckanext.scheming import helpers as h
from ckan.plugins import toolkit as tk
from ckan import logic as l


@side_effect_free
def scheming_dataset_schema_list(context, data_dict):
    '''
    Return a list of dataset types customized with the scheming extension
    '''
    return list(scheming_dataset_schemas())

@side_effect_free
def scheming_dataset_schema_show(context, data_dict):
    '''
    Return the scheming schema for a given dataset type

    :param type: the dataset type
    :param expanded: True to expand presets (default)
    '''
    t = get_or_bust(data_dict, 'type')
    expanded = data_dict.get('expanded', True)
    s = scheming_get_dataset_schema(t, expanded)
    if s is None:
        raise ObjectNotFound()
    return s

@side_effect_free
def scheming_group_schema_list(context, data_dict):
    '''
    Return a list of group types customized with the scheming extension
    '''
    return list(scheming_group_schemas())

@side_effect_free
def scheming_group_schema_show(context, data_dict):
    '''
    Return the scheming schema for a given group type

    :param type: the group type
    :param expanded: True to expand presets (default)
    '''
    t = get_or_bust(data_dict, 'type')
    expanded = data_dict.get('expanded', True)
    s = scheming_get_group_schema(t, expanded)
    if s is None:
        raise ObjectNotFound()
    return s


@side_effect_free
def scheming_organization_schema_list(context, data_dict):
    '''
    Return a list of organization types customized with the scheming extension
    '''
    return list(scheming_organization_schemas())

@side_effect_free
def scheming_organization_schema_show(context, data_dict):
    '''
    Return the scheming schema for a given organization type

    :param type: the organization type
    :param expanded: True to expand presets (default)
    '''
    t = get_or_bust(data_dict, 'type')
    expanded = data_dict.get('expanded', True)
    s = scheming_get_organization_schema(t, expanded)
    if s is None:
        raise ObjectNotFound()
    return s


def package_update(context, data_dict):
    excluded_extras = h.scheming_get_excluded_extras_from_form()
    package = tk.get_action('package_show')(context, {'id': data_dict['id']})
    extras = []
    for extra in package['extras']:
        if extra['key'] in excluded_extras:
            extras.append(extra)
    data_dict['extras'].extend(extras)
    package = l.action.update.package_update(context, data_dict)
    return package
