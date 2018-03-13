from falcon.routing.compiled import CompiledRouter


class FormatRouter(CompiledRouter):

    def add_route(self, uri_template, method_map, resource):
        """
        Add .{content_type} route in addition to given format-less route
        """
        super().add_route(uri_template, method_map, resource)

        format_uri_template = f'{uri_template}.{{content_type}}'

        super().add_route(format_uri_template, method_map, resource)
