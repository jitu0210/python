# ==========================================================
# __contains__
# ==========================================================
# __contains__ defines how the `in` operator works for your object.

class Team:
    def __init__(self, members):
        self.members = members

    def __contains__(self, name):
        return name.lower() in (m.lower() for m in self.members)

team = Team(["Emil", "Tobias", "Linus"])
print("tobias" in team)        # True (case-insensitive, our own rule)
print("Ravi" in team)          # False
print("Ravi" not in team)      # True
