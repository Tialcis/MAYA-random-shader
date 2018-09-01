import maya.cmds as cmds
import random as random
import math as math


class RandomShader():

    def __init__(self):
        self.objects_to_shade = []
        self.shaders_to_apply = []

    def bake_objects(self):
        """
        Saves the selected objects random shading
        """

        selected_objects = cmds.ls(sl=True)
        del self.objects_to_shade[:]
        for obj in selected_objects:
            self.objects_to_shade.append(obj)
        print self.objects_to_shade

    def bake_shaders(self):
        """
        Saves the selected shaders to apply to objects
        """

        selected_shaders = cmds.ls(sl=True)
        del self.shaders_to_apply[:]
        for shdr in selected_shaders:
            self.shaders_to_apply.append(shdr)
        print self.shaders_to_apply

    def assign_randomly(self):
        number_of_shaders = len(self.shaders_to_apply)
        for obj in self.objects_to_shade:
            rand_number = random.rand_int(0, number_of_shaders)
            cmds.select(obj)
            shader_name = self.shaders_to_apply[rand_number]
            self.assign_selection_to_shader(shader_name)
        cmds.select(clear=True)

    def assign_distribution(self):
        number_of_shaders = 7
        for obj in self.objects_to_shade:
            rand_number = random.rand_int(0, number_of_shaders)


    def _get_SG_from_shader(self, shader=None):
        if shader:
            if cmds.objExists(shader):
                shading_group_query = cmds.listConnections(shader, destination=True, exactType=True, type='shadingEngine')
                if shading_group_query:
                    return shading_group_query[0]

        return None

    def _assign_obj_list_to_shader(self, obj_list=None, shader=None):
        """
        Assign the shader to the object list
        arguments:
            obj_list: list of objects or faces
        """
        shader_SG = self._get_SG_from_shader(shader)
        if obj_list:
            if shader_SG:
                cmds.sets(obj_list, e=True, forceElement=shader_SG)
            else:
                print 'The provided shader %s didn\'t return a shader_SG' % shader
        else:
            print 'Please select one or more objects'

    def _assign_selection_to_shader(self, shader=None):
        sel = cmds.ls(sl=True, long=True)
        if sel:
            self._assign_obj_list_to_shader(sel, shader)
