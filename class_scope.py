#global
class fullName():
    fName = "sujitha"
    lName = "swami"
fn = fullName()
print(fn.fName)
#partally priavate scope
class fullName():
    _fName = "sujitha"
    _lName = "swami"
fn = fullName()
print(fn._lName)

#strictly private
class fullName():
    __fName = "sujitha"
    __lName = "swami"
fn = fullName()
print(fn.__lName)

#global variable
def fullName():
    global= fn
    ln = "swami"
    fn = "sujitha"
fullName()
print(fn)
#functional

def fullName():
    global=fn
    ln = "swami"
    fn = "sujitha"
fullName()
print(fn)



#ex of abstraction
class Employee():
    __fName = "sujitha"
    __lName = "swami"
    def fullName(self):
        return self.__fName + " " + self.__lName
emp = Employee()
fullName()
emp.__fName = "as"

print(emp.fullName())
print(emp.__fName)






