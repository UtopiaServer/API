class ItemStack:

    def __init__(self, registry_name, count, nbt_data):
        self.registry_name = registry_name
        self.count = count
        self.nbt_data = nbt_data