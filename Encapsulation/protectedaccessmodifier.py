class student:
    _name=None
    _roll=None
    _branch=None
    def __init__(self,name,roll, branch):
        self._name=name
        self._roll=roll
        self._branch=branch
    def _displayrollandbranch(self):
        print("Roll: ",self._roll)
        print("Branch: ",self._branch)
class potato(student):
    def __init__(self, name, roll, branch):
        student.__init__(self,name, roll, branch)
    def displaydetails(self):
        print("Name: ",self._name)
        self._displayrollandbranch()

m=student("Saajan",12345,"Computer Science")
print(m._displayrollandbranch())