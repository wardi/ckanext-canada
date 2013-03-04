from ckan.controllers.package import PackageController

class DataGCCAController(PackageController):
    def resource_edit2(self, id, resource_id, data=None, errors=None,
            error_summary=None):
        data = data or {}
        data['schema_description'] = 'sassafraz'
        return super(DataGCCAController, self).resource_edit(id,
            resource_id, data, errors, error_summary)
