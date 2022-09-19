import discord

class Roles:
    def __init__(self, guild):
        self.smesh_guild = guild
        self.staff_role = self.smesh_guild.get_role(991219359731163187)
        self.helper_role = self.smesh_guild.get_role(989892564691873793)
        self.support_role = self.smesh_guild.get_role(1009021230080348190)
        self.moder_role = self.smesh_guild.get_role(989891381575159870)
        self.curator_role = self.smesh_guild.get_role(989891621434851328)
        self.shield_role = self.smesh_guild.get_role(990166527934361621)
        self.admin_role = self.smesh_guild.get_role(989919570087256074)
        self.greenheart_role = self.smesh_guild.get_role(997025539170762802)
        self.clip_role = self.smesh_guild.get_role(922121104057851965)
        self.transparent_role = self.smesh_guild.get_role(1005493510054629406)
        self.ufo_role = self.smesh_guild.get_role(1005450014979522592)
        
    def get_all_staff_roles(self):
        staff_roles_list = [
            self.staff_role, 
            self.helper_role, 
            self.support_role, 
            self.moder_role, 
            self.curator_role, 
            self.shield_role, 
            self.admin_role, 
            self.greenheart_role, 
            self.clip_role, 
            self.transparent_role, 
            self.ufo_role
        ]
        return staff_roles_list
    
    def roles_check(self, *, member, roles_list):
        return [x for x in member.roles if x in roles_list]   
