def use_template(template_dir, template_name, output_dir, output_file_name_fn, data):
    """
    One data item per file
    :param template_dir:
    :param template_name:
    :param output_dir:
    :param output_file_name_fn:
    :param data:
    :return:
    """
    import jinja2
    template_environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_dir),
        undefined=jinja2.StrictUndefined,
    )
    template = template_environment.get_template(template_name)
    for data_structure in data:
        rendered_output = template.render(data_structure)
        output_file_name = output_file_name_fn(data_structure)
        import os
        output_full_path = os.path.join(output_dir, output_file_name)
        with open(output_full_path, 'w') as output_file:
            output_file.write(rendered_output)


def use_template_single_file(template_dir, template_name, output_dir, output_file_name_fn, data):
    """
    One file for all data
    :param template_dir:
    :param template_name:
    :param output_dir:
    :param output_file_name_fn:
    :param data:
    :return:
    """
    import jinja2
    template_environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_dir),
        undefined=jinja2.StrictUndefined,
    )
    template = template_environment.get_template(template_name)
    rendered_output = template.render(data = data)
    output_file_name = output_file_name_fn(data)
    import os
    output_full_path = os.path.join(output_dir, output_file_name)
    with open(output_full_path, 'w') as output_file:
        output_file.write(rendered_output)


