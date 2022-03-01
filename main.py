####################################################
# Exceptions and Errors
####################################################
class ThisLTHCLangException:
    def __init__(self, exception_name: str, details: str):
        self.exception_name: str = exception_name
        self.details: str = details
    
    def __str__(self) -> str:
        return f'{self.exception_name}: {self.details}'

class ThisLTHCLangIllegalException(ThisLTHCLangException):
    def __init__(self, details: str):
        super().__init__("Illegal Exception", details)

class ThisLTHCLangError(ThisLTHCLangException):
    def __init__(self, error_name: str, details: str):
        super().__init__(error_name, details)

####################################################
# Var Types
####################################################
class ThisLTHCLangVarType:
    def __init__(self, name: str, value):
        self.name: str = name
        self.value = value
    
    def __str__(self) -> str:
        return f'{self.value}'
    
    def copy(self):
        return ThisLTHCLangError("Excution Error",'Internal op not defined')
    
    def add(self, other):
        "Add"
        return ThisLTHCLangError("Excution Error",'Internal op not defined')
    
    def sub(self, other):
        "Substract"
        return ThisLTHCLangError("Excution Error",'Internal op not defined')
    
    def mult(self, other):
        "Multiply"
        return ThisLTHCLangError("Excution Error",'Internal op not defined')
    
    def div(self, other):
        "Divide"
        return ThisLTHCLangError("Excution Error",'Internal op not defined')
    
    def ediv(self, other):
        "Euclidean Divide"
        return ThisLTHCLangError("Excution Error",'Internal op not defined')
    
    def mod(self, other):
        "modulo"
        return ThisLTHCLangError("Excution Error",'Internal op not defined')
    
    def pow(self, other):
        "power"
        return ThisLTHCLangError("Excution Error",'Internal op not defined')
    
    def eq(self, other):
        "equals"
        return ThisLTHCLangError("Excution Error",'Internal op not defined')
    
    def ne(self, other):
        "not equals"
        return ThisLTHCLangError("Excution Error",'Internal op not defined')
    
    def gt(self, other):
        "greater than"
        return ThisLTHCLangError("Excution Error",'Internal op not defined')
    
    def lt(self, other):
        "lesser than"
        return ThisLTHCLangError("Excution Error",'Internal op not defined')
    
    def ge(self, other):
        "greater than or equals"
        return ThisLTHCLangError("Excution Error",'Internal op not defined')
    
    def le(self, other):
        "lesser than or equals"
        return ThisLTHCLangError("Excution Error",'Internal op not defined')

PYNUMTYPES = int | float

class ThisLTHCLangNumVarType(ThisLTHCLangVarType):
    def __init__(self, name: str, value: PYNUMTYPES):
        super().__init__(name, value)
    
    def copy(self):
        return ThisLTHCLangNumVarType(self.name + '->copy', self.value)

    def add(self, other):
        if isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                copy.value += other.value
                return copy
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')
    
    def sub(self, other):
        if isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                copy.value -= other.value
                return copy
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')
    
    def mult(self, other):
        if isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                copy.value *= other.value
                return copy
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')

    def div(self, other):
        if isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                copy.value /= other.value
                return copy
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')
    
    def ediv(self, other):
        if isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                copy.value //= other.value
                return copy
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')
    
    def mod(self, other):
        if isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                copy.value %= other.value
                return copy
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')

    def pow(self, other):
        if isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                copy.value **= other.value
                return copy
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')
    
    def eq(self, other):
        if isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", copy.value == other.value)
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')
    
    def ne(self, other):
        if isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", copy.value != other.value)
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')
    
    def gt(self, other):
        if isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", copy.value > other.value)
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')
    
    def lt(self, other):
        if isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", copy.value < other.value)
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')
    
    def ge(self, other):
        if isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", copy.value >= other.value)
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')
    
    def le(self, other):
        if isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", copy.value <= other.value)
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')

class ThisLTHCLangBoolVarType(ThisLTHCLangVarType):
    def __init__(self, name: str, value: bool):
        super().__init__(name, value)
    
    def copy(self):
        return ThisLTHCLangBoolVarType(self.name + '->copy', self.value)
    
    def __str__(self) -> str:
        return f'{self.value}'.lower()
    
    def eq(self, other):
        if isinstance(other, ThisLTHCLangBoolVarType):
            try:
                copy = self.copy()
                copy.value = copy.value == other.value
                return copy
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')
    
    def ne(self, other):
        if isinstance(other, ThisLTHCLangBoolVarType):
            try:
                copy = self.copy()
                copy.value = not (copy.value == other.value)
                return copy
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')
    
    def add(self, other):
        if isinstance(other, ThisLTHCLangBoolVarType):
            try:
                copy = self.copy()
                copy.value = copy.value or other.value
                return copy
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')
    
    def mult(self, other):
        if isinstance(other, ThisLTHCLangBoolVarType):
            try:
                copy = self.copy()
                copy.value = copy.value and other.value
                return copy
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')

class ThisLTHCLangStrVarType(ThisLTHCLangVarType):
    def __init__(self, name: str, value: str):
        super().__init__(name, value)
    
    def copy(self):
        return ThisLTHCLangStrVarType(self.name + '->copy', self.value)
    
    def __str__(self) -> str:
        return self.value
    
    def add(self, other):
        if isinstance(other, ThisLTHCLangStrVarType):
            try:
                copy = self.copy()
                copy.value += other.value
                return copy
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')
    
    def div(self, other):
        if isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                copy.value = copy.value[other.value]
                return copy
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')

    def mult(self, other):
        if isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                copy.value = copy.value * other.value
                return copy
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')

    def eq(self, other):
        if isinstance(other, ThisLTHCLangStrVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", copy.value == other.value)
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        elif isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", copy.value == str(other.value))
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')

    def ne(self, other):
        if isinstance(other, ThisLTHCLangStrVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", copy.value != other.value)
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        elif isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", copy.value != str(other.value))
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')

    def gt(self, other):
        if isinstance(other, ThisLTHCLangStrVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", len(copy.value) > len(other.value))
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        elif isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", float(copy.value) > other.value)
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')

    def lt(self, other):
        if isinstance(other, ThisLTHCLangStrVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", len(copy.value) < len(other.value))
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        elif isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", float(copy.value) < other.value)
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')
    
    def ge(self, other):
        if isinstance(other, ThisLTHCLangStrVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", len(copy.value) > len(other.value) or copy.value == other.value)
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        elif isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", float(copy.value) > other.value or copy.value == str(other.value))
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')
    
    def le(self, other):
        if isinstance(other, ThisLTHCLangStrVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", len(copy.value) < len(other.value) or copy.value == other.value)
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        elif isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", float(copy.value) < other.value or copy.value == str(other.value))
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')

LOCATEDTYPES = ThisLTHCLangNumVarType | ThisLTHCLangBoolVarType | ThisLTHCLangStrVarType

class ThisLTHCLangListVarType(ThisLTHCLangVarType):
    def __init__(self, name: str, value: list[LOCATEDTYPES]):
        super().__init__(name, value)

    def copy(self):
        return ThisLTHCLangListVarType(self.name + '->copy', self.value.copy())

    def add(self, other):
        if isinstance(other, ThisLTHCLangListVarType):
            try:
                copy = self.copy()
                copy.value.extend(other.value.copy())
                return copy
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        elif isinstance(other, LOCATEDTYPES):
            try:
                copy = self.copy()
                copy.value.append(other.value)
                return copy
            except:
              return ThisLTHCLangError("Runtime Error", 'An undefined error occured')  
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')

    def div(self, other):
        if isinstance(other, ThisLTHCLangNumVarType):
            try:
                temp = [self.value[other.value]]
                if isinstance(temp, ThisLTHCLangNumVarType):
                    out = ThisLTHCLangNumVarType(self.name + ">>list->num-out", temp[0])
                if isinstance(temp, ThisLTHCLangBoolVarType):
                    out = ThisLTHCLangBoolVarType(self.name + ">>list->bool-out", temp[0])
                if isinstance(temp, ThisLTHCLangStrVarType):
                    out = ThisLTHCLangStrVarType(self.name + ">>list->str-out", temp[0])
                return out
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')

    def mult(self, other):
        if isinstance(other, ThisLTHCLangNumVarType):
            try:
                copy = self.copy()
                copy.value = copy.value.copy() * other.value
                return copy
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')

    def eq(self, other):
        if isinstance(other, ThisLTHCLangListVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", copy.value == other.value)
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        elif len(self.value) == 1:
            if isinstance(other, LOCATEDTYPES):
                try:
                    copy = self.copy()
                    return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", str(copy.value[0]) == str(other.value))
                except:
                    return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')

    def ne(self, other):
        if isinstance(other, ThisLTHCLangListVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", copy.value != other.value)
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        elif len(self.value) == 1:
            if isinstance(other, LOCATEDTYPES):
                try:
                    copy = self.copy()
                    return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", str(copy.value[0]) != str(other.value))
                except:
                    return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')

    def lt(self, other):
        if isinstance(other, ThisLTHCLangListVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", len(copy.value) < len(other.value))
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        elif len(self.value) == 1:
            if isinstance(other, LOCATEDTYPES):
                try:
                    copy = self.copy()
                    if isinstance(other, ThisLTHCLangNumVarType):
                        v = copy.value[0]
                        if isinstance(v, ThisLTHCLangNumVarType):
                            return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", v < other.value)
                        if isinstance(v, ThisLTHCLangStrVarType):
                            return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", float(v) < other.value)
                    if isinstance(other, ThisLTHCLangStrVarType):
                        v = copy.value[0]
                        if isinstance(v, ThisLTHCLangNumVarType):
                            return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", v < float(other.value))
                        if isinstance(v, ThisLTHCLangStrVarType):
                            return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", len(v) < len(other.value))
                except:
                    return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')

    def gt(self, other):
        if isinstance(other, ThisLTHCLangListVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", len(copy.value) > len(other.value))
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        elif len(self.value) == 1:
            if isinstance(other, LOCATEDTYPES):
                try:
                    copy = self.copy()
                    if isinstance(other, ThisLTHCLangNumVarType):
                        v = copy.value[0]
                        if isinstance(v, ThisLTHCLangNumVarType):
                            return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", v > other.value)
                        if isinstance(v, ThisLTHCLangStrVarType):
                            return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", float(v) > other.value)
                    if isinstance(other, ThisLTHCLangStrVarType):
                        v = copy.value[0]
                        if isinstance(v, ThisLTHCLangNumVarType):
                            return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", v > float(other.value))
                        if isinstance(v, ThisLTHCLangStrVarType):
                            return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", len(v) > len(other.value))
                except:
                    return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')

    def le(self, other):
        if isinstance(other, ThisLTHCLangListVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", len(copy.value) < len(other.value) or copy.value == other.value)
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        elif len(self.value) == 1:
            if isinstance(other, LOCATEDTYPES):
                try:
                    copy = self.copy()
                    result = str(copy.value[0]) == str(other.value)
                    if isinstance(other, ThisLTHCLangNumVarType):
                        v = copy.value[0]
                        if isinstance(v, ThisLTHCLangNumVarType):
                            return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", v < other.value or result)
                        if isinstance(v, ThisLTHCLangStrVarType):
                            return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", float(v) < other.value or result)
                    elif isinstance(other, ThisLTHCLangStrVarType):
                        v = copy.value[0]
                        if isinstance(v, ThisLTHCLangNumVarType):
                            return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", v < float(other.value) or result)
                        if isinstance(v, ThisLTHCLangStrVarType):
                            return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", len(v) < len(other.value) or result)
                    else:
                        return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", result)
                except:
                    return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')

    def ge(self, other):
        if isinstance(other, ThisLTHCLangListVarType):
            try:
                copy = self.copy()
                return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", len(copy.value) > len(other.value) or copy.value == other.value)
            except:
                return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        elif len(self.value) == 1:
            if isinstance(other, LOCATEDTYPES):
                try:
                    copy = self.copy()
                    result = str(copy.value[0]) == str(other.value)
                    if isinstance(other, ThisLTHCLangNumVarType):
                        v = copy.value[0]
                        if isinstance(v, ThisLTHCLangNumVarType):
                            return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", v > other.value or result)
                        if isinstance(v, ThisLTHCLangStrVarType):
                            return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", float(v) > other.value or result)
                    elif isinstance(other, ThisLTHCLangStrVarType):
                        v = copy.value[0]
                        if isinstance(v, ThisLTHCLangNumVarType):
                            return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", v > float(other.value) or result)
                        if isinstance(v, ThisLTHCLangStrVarType):
                            return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", len(v) > len(other.value) or result)
                    else:
                        return ThisLTHCLangBoolVarType(copy.name + ">> bool-out", result)
                except:
                    return ThisLTHCLangError("Runtime Error", 'An undefined error occured')
        else:
            return ThisLTHCLangIllegalException(f'Cannot execute specified op between {type(self)} and {type(other)}')
