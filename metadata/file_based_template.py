import metadata.base_template as base_template

class file_based_template(base_template.BaseTemplate):
    JSON = 'JSON'
    SINGLE_VALUE = 'SINGLE_VALUE'
    CSV = 'CSV'
    def __init__(self):
        super().__init__()
        self.data_file = None
        self.format = self.JSON

    def _prep(self):
        super()._validate()
        self._validate()
        import metadata._file_source as file_source
        if self.format == self.JSON:
            data = file_source.json_file_source(self.data_file)
        elif self.format == self.CSV:
            data = file_source.csv_file_source(self.data_file)
        elif self.format == self.SINGLE_VALUE:
            data = file_source.single_value_file_source(self.data_file)
        else:
            raise ValueError('no format')
        return data

    def run_multi_file(self):
        data = self._prep()
        super()._run(data)

    def _group_data(self, data, group_by):
        import itertools
        sorted_data = sorted(data, key = group_by)
        grouped_data = itertools.groupby(sorted_data, key=group_by)
        return grouped_data

    def run_single_file(self, group_by = None):
        data = self._prep()
        if group_by is None:
            super()._run_single_file(data)
        else:
            grouped_data = self._group_data(data, group_by)
            for key, group in grouped_data:
                super()._run_single_file(list(group))

    def _validate(self):
        if self.output_directory is None:
            raise ValueError()
        if self.template_directory is None:
            raise ValueError()
        if self.template_name is None:
            raise ValueError()
        if self.output_file_name_fn is None:
            raise ValueError()
