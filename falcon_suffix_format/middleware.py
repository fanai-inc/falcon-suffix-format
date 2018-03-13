class SetContentType:

    def process_resource(self, req, resp, resource, params):
        """
        After routing but before the request handler is called, process
        the content_type given in the url
        """

        content_type = params.pop('content_type', None)

        if content_type:
            req.content_type = f'application/{content_type}'
            resp.content_type = f'application/{content_type}'
