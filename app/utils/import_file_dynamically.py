import importlib.util

def import_module_dynamically(module_path, class_name='Main'):
    """
    Import a Python module dynamically.

    Args:
        module_path (str): The absolute path to the module.

    Returns:
        The imported module.
    """
    spec = importlib.util.spec_from_file_location("module.name", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    return getattr(module, class_name)
