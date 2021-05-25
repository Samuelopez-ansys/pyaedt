from .Analysis import Analysis
from ..modeler.Model2D import Modeler2D
from ..modules.Mesh import Mesh
from ..generic.general_methods import aedt_exception_handler, generate_unique_name


class FieldAnalysis2D(Analysis):
    """ **AEDT_2D_FieldAnalysis**

    Class for 2D Field Analysis Setup (Maxwell2D, Q2D)

    It is automatically initialized by Application call. Refer to Application function for inputs definition

    """
    def __init__(self, application, projectname, designname, solution_type, setup_name=None):


        Analysis.__init__(self, application, projectname, designname, solution_type, setup_name)
        self._modeler = Modeler2D(self)
        self._mesh = Mesh(self)
        # self._post = PostProcessor(self)

    @property
    def modeler(self):
        return self._modeler

    @property
    def mesh(self):
        return self._mesh

    # @property
    # def post(self):
    #     return self._post

    @aedt_exception_handler
    def assignmaterial(self, obj, mat):
        """ The function assigns Material mat to object obj. If material mat is not present it will be created


        :param obj: list of objects to which assign materials
        :type obj: str, list
        :param mat: material to assign
        :type mat: str
        :return: True if succeded | False if failed
        """
        mat = mat.lower()
        selections = self.modeler.convert_to_selections(obj)
        arg1 = ["NAME:Selections"]
        arg1.append("Selections:="), arg1.append(selections)
        arg2 = ["NAME:Attributes"]
        arg2.append("MaterialValue:="), arg2.append(chr(34) + mat + chr(34))
        if mat in self.materials.material_keys:
            Mat = self.materials.material_keys[mat]
            Mat.update()
            if Mat.is_dielectric():
                arg2.append("SolveInside:="), arg2.append(True)
            else:
                arg2.append("SolveInside:="), arg2.append(False)
            self.modeler.oeditor.AssignMaterial(arg1, arg2)
            self._messenger.add_info_message('Assign Material ' + mat + ' to object ' + selections)
            if type(obj) is list:
                for el in obj:
                    self.modeler.primitives[el].material_name = mat
            else:
                self.modeler.primitives[obj].material_name = mat
            return True
        elif self.materials.checkifmaterialexists(mat):
            self.materials._aedmattolibrary(mat)
            Mat = self.materials.material_keys[mat]
            if Mat.is_dielectric():
                arg2.append("SolveInside:="), arg2.append(True)
            else:
                arg2.append("SolveInside:="), arg2.append(False)
            self.modeler.oeditor.AssignMaterial(arg1, arg2)
            self._messenger.add_info_message('Assign Material ' + mat + ' to object ' + selections)
            if type(obj) is list:
                for el in obj:
                    self.modeler.primitives[el].material_name = mat
            else:
                self.modeler.primitives[obj].material_name = mat

            return True
        else:
            self._messenger.add_error_message("Material Does Not Exists")
            return False