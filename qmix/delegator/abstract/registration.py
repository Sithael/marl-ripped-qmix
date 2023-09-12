import yaml


class ConstructRegistry:
    registered_constructs = {}

    @classmethod
    def register_construct(cls, construct_type, construct_class):
        cls.registered_constructs[construct_type] = construct_class

    @classmethod
    def create(cls, target_construct_class, path_to_construct_file, num_agents):
        construct_class = cls.registered_constructs.get(target_construct_class)
        if construct_class is None:
            raise ValueError(f"Invalid construct type: {construct_class}")

        if not hasattr(construct_class, "from_construct_registry_directive"):
            raise TypeError(
                f"{construct_class.__name__} does not implement 'from_construct_registry_directive' class method"
            )

        construct_registry_directive = {
            "path_to_construct_file": path_to_construct_file,
            "num_agents": num_agents,
        }

        return construct_class.from_construct_registry_directive(
            construct_registry_directive
        )

    @classmethod
    def get_registered_constructs(cls):
        return cls.registered_constructs

    @classmethod
    def get_construct(cls, construct_type):
        return cls.registered_constructs.get(construct_type)
