class DatabasePermission:
    access_list = []

    def user_has_access(self, obj):
        return obj.name in self.access_list

    def add_user_access(self, obj):
        self.access_list.append(obj.name)




