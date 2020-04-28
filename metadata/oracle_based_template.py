
class oracle_based_template(object):
    def __init__(self):
        self.output_directory = None
        self.template_directory = None
        self.template_name = None
        self.output_file_name_fn = None
        self.host = None
        self.port = None
        self.sid = None
        self.service_name = None
        self.username = None
        self.password = None
        self.sql = None


    def run(self):
        self._validate()
        import connect_oracle.query_oracle as query_oracle
        if self.sid is not None:
            data = query_oracle.select_query_SID(self.host,
                                                 self.port,
                                                 self.sid,
                                                 self.username,
                                                 self.password,
                                                 self.sql)
        else:
            data = query_oracle.select_query_service_name(self.host,
                                                 self.port,
                                                 self.service_name,
                                                 self.username,
                                                 self.password,
                                                 self.sql)

        import metadata.use_template as use_template
        use_template.use_template(self.template_directory,
                                  self.template_name,
                                  self.output_directory,
                                  self.output_file_name_fn,
                                  data)

    def _validate(self):
        if self.output_directory is None:
            raise ValueError()
        if self.template_directory is None:
            raise ValueError()
        if self.template_name is None:
            raise ValueError()
        if self.output_file_name_fn is None:
            raise ValueError()
        if self.host is None:
            raise ValueError()
        if self.port is None:
            raise ValueError()
        if self.sid is None and self.service_name is None:
            raise ValueError()
        if self.username is None:
            raise ValueError()
        if self.password is None:
            raise ValueError()
        if self.sql is None:
            raise ValueError()


