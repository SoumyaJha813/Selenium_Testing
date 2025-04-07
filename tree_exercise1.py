class TreeNode:
    def __init__(self, name, designation):
        self.children = []
        self.name = name
        self.designation = designation
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

    def print_tree(self, property_name):
        if property_name == 'both':
            value = self.name + " (" + self.designation + ")"
        elif property_name == "name":
            value = self.name
        else:
            value = self.designation

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ' '
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(property_name)

def build_management_tree():

    infra_head = TreeNode("Vishwa", "Infrastructure Head")ceo = TreeNode("Nilupul", 'CEO')
    app_head = TreeNode("Aamir", "Appication Head")

    cto = TreeNode("Chinmay", "CTO")
    hr_head = TreeNode("Gels", "HR Head")

    ceo = TreeNode("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)
    cto.add_child(infra_head)
    cto.add_child(app_head)

    infra_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))

    hr_head.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    return ceo






