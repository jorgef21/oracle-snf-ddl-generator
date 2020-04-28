
class BaseTemplate(object):
    def __init__(self):
        self.output_directory = None
        self.template_directory = None
        self.template_name = None
        self.output_file_name_fn = None


    def _run(self, data):
        self._validate()
        import metadata.use_template as use_template
        use_template.use_template(self.template_directory,
                                  self.template_name,
                                  self.output_directory,
                                  self.output_file_name_fn,
                                  data)

    def _run_single_file(self, data):
        self._validate()
        import metadata.use_template as use_template
        use_template.use_template_single_file(self.template_directory,
                                  self.template_name,
                                  self.output_directory,
                                  self.output_file_name_fn,
                                  data)

    def _validate(self):
        if self.output_directory is None:
            raise ValueError("no out directory")
        if self.template_directory is None:
            raise ValueError("not template directory")
        if self.template_name is None:
            raise ValueError("no template name")
        if self.output_file_name_fn is None:
            raise ValueError("no output file name")


